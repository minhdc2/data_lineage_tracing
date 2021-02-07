import pandas as pd
import numpy as np

def src_tab_(df, target_table):
    src_tab = df[df.TARGET_TAB == target_table].SOURCE_TAB.values
    src_tab = src_tab.tolist()
    if src_tab != []:
        return src_tab


def odi_map(target, source, df):
    trg = df.TARGET_TAB.values.tolist()
    flatten_src = [i for sublist in source if sublist is not None for i in sublist]
    flatten_src = list(dict.fromkeys(flatten_src))
    l = [i for i in flatten_src if i not in target]
    for i in l:
        if i in trg:
            src = src_tab_(df, i)
            src = list(dict.fromkeys(src))
            target.append(i)
            source.append(src)

    for i in l:
        if i in trg:
            target, source = odi_map(target, source, df)
    return target, source


def odi_map_tab(target, source, target_table):
    final = []

    for i in np.arange(len(target)):
        if source[i] is not None:
            for j in np.arange(len(source[i])):
                final.append([target[i]] + [source[i][j]])
    result = pd.DataFrame(final, columns=['target', 'source'])
    result['ID'] = target_table

    return result


def odi_src_tab(odi_map_df, input_path, output_path, export):
    df_test = pd.read_excel(input_path, header = 0)
    df_final = []
    for i in df_test.TARGET_TABLE:
        target = [i]
        source = [src_tab_(odi_map_df, i)]
        if source != []:
            target, source = odi_map(target, source, odi_map_df)
            flatten_src = [i for sublist in source if sublist is not None for i in sublist]
            flatten_src = list(dict.fromkeys(flatten_src))
            src_tab = [i for i in flatten_src if i not in target]
            result = pd.DataFrame({'src_tab': src_tab})
            result['ID'] = i
            df_final.append(result)
    df_final = pd.concat(df_final)
    if export == 'Y':
        return df_final.to_csv(output_path, index = False)
    if export == 'N':
        return df_final


def odi_tab_roadmap(odi_map_df, input_path, output_path, export):
    df_test = pd.read_excel(input_path, header = 0)
    df_final = []
    for i in df_test.TARGET_TABLE:
        target = [i]
        source = [src_tab_(odi_map_df, i)]
        if source != []:
            target, source = odi_map(target, source, odi_map_df)
            result = odi_map_tab(target, source, i)
            df_final.append(result)
    df_final = pd.concat(df_final)
    if export == 'Y':
        return df_final.to_csv(output_path, index = False)
    if export == 'N':
        return df_final

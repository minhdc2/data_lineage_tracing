import pandas as pd
import numpy as np
from src_tab_f0 import src_tab_
from src_tab_f0 import odi_map
from src_tab_f0 import odi_map_tab
from src_tab_f0 import odi_src_tab
from src_tab_f0 import odi_tab_roadmap

df = pd.read_csv('./input/odi_lineage_data.csv', header = 0)

target_table = 'EDW_DMT.PFS_BOND_AR_FCT_MTLY'

input_path = './input/trg_tab.xlsx'
output_path = './output/trg_tab_checked.csv'

odi_tab_roadmap(df, input_path, output_path, 'Y')

output_path = './output/trg_tab_src_f0.csv'

odi_src_tab(df, input_path, output_path, 'Y')

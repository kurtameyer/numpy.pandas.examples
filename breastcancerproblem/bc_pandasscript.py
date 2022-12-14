'''This script is meant to show basic proficiency with pandas dataframes. I was asked
to strip and collect data from a CSV file (also provided in this folder) based on specific parameters. Then I was asked to merge
the data." 

import pandas as pd

BCRD = pd.read_csv("breastCancerData.csv")

g_13 = BCRD.query("radius_mean>=13")
g_18 = BCRD.query ("texture_mean>=18")
g_85 = BCRD.query("perimeter_mean>=85")
g_500 = BCRD.query("area_mean>=500")

g_13.to_csv('g_13.csv')
g_18.to_csv('g_18.csv')
g_85.to_csv('g_85.csv')
g_500.to_csv('g_500.csv')


g_13M = g_13.query("diagnosis == 'M'")
g_13B = g_18.query("diagnosis == 'B'")
g_18M = g_85.query("diagnosis == 'M'")
g_18B = g_85.query("diagnosis == 'B'")
g_85M = g_85.query("diagnosis == 'M'")
g_85B = g_85.query("diagnosis == 'B'")
g_500M = g_500.query("diagnosis == 'M'")
g_500B = g_500.query("diagnosis == 'B'")


g_13M.to_csv("g_13M.csv")
g_13B.to_csv("g_13B.csv")
g_18M.to_csv("g_18M.csv")
g_18B.to_csv("g_18B.csv")
g_85M.to_csv("g_85M.csv")
g_85B.to_csv("g_85B.csv")
g_500M.to_csv("g_500M.csv")
g_500B.to_csv("g_500B.csv")

### Checked CSV for duplicated IDs######
intersected1 = pd.merge(g_13, g_18)
intersected2 = pd.merge(g_85, g_500)
intersected3 = pd.merge(intersected1, intersected2)
intersected3.to_csv("new_result.csv")



m_intersected1 = pd.merge(g_13M, g_18M)
m_intersected2 = pd.merge(g_85M, g_500M)
m_intersected3 = pd.merge(m_intersected1, m_intersected2)
m_intersected3.to_csv("subset_m_result.csv")
difference_1_list = [m_intersected3, intersected3]
difference_1 = pd.concat(difference_1_list).drop_duplicates(keep=False)
difference_1.to_csv("difference1.csv")


original_result = BCRD.query("diagnosis =='M'")
original_result.to_csv("original_result.csv")
difference2 = [original_result, m_intersected3]
difference_2 = pd.concat(difference2).drop_duplicates(keep=False)
difference_2.to_csv("difference2.csv")

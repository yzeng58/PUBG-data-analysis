import pandas as pd
import csv,math,os,sys
import statistics as stat

kill_df1 = pd.read_csv('summary/erangel.csv')
# kill_df1 = pd.read_csv('summary/erangel_weapon2.csv')
# kill_df2 = pd.read_csv('summary/erangel_weapon3.csv')
kill_df = []
for weapon in list(set(list(kill_df.weapon))):
    try:
        kill_df.append([weapon, sum(list(kill_df1[kill_df1.weapon == weapon]["mean distance"])*list(kill_df1[kill_df1.weapon == weapon]["frequency"]))
              /sum(list(kill_df1[kill_df1.weapon == weapon]["frequency"])),
                        sum(list(kill_df1[kill_df1.weapon == weapon]["frequency"]))])
    except:
        pass
kill_df = pd.DataFrame(kill_df)
kill_df.to_csv('summary_erangel.csv')

kill_df1 = pd.read_csv('summary/mirama.csv')
# kill_df2 = pd.read_csv('summary/mirama_weapon3.csv')
kill_df = []
for weapon in list(set(list(kill_df.weapon))):
    try:
        kill_df.append([weapon, sum(list(kill_df1[kill_df1.weapon == weapon]["mean distance"])*list(kill_df1[kill_df1.weapon == weapon]["frequency"]))
              /sum(list(kill_df1[kill_df1.weapon == weapon]["frequency"])),
                        sum(list(kill_df1[kill_df1.weapon == weapon]["frequency"]))])
    except:
        pass
kill_df = pd.DataFrame(kill_df)
kill_df.to_csv('summary_miramar.csv')

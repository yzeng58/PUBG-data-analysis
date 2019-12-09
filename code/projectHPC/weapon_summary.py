#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import csv,math,os,sys
import statistics as stat

print(sys.argv[1])
# kill_df = pd.read_csv('pubg-match-deaths/deaths/'+'kill_'+str(sys.argv[1])+'.csv')


# In[3]:


def read_csv(path):
    with open(path, encoding = 'utf-8') as f:
        return list(csv.reader(f))
kill_list = read_csv('pubg-match-deaths/deaths/'+'kill_'+str(sys.argv[1])+'.csv')
kill_header = kill_list[0]
kill_data = kill_list[1:]


# In[38]:


def summary(kill):
    try:
        x1 = float(kill[kill_header.index("killer_position_x")])
        y1 = float(kill[kill_header.index("killer_position_y")])
        x2 = float(kill[kill_header.index("victim_position_x")])
        y2 = float(kill[kill_header.index("victim_position_y")])
        distance = ((x1-x2)**2+(y1-y2)**2)**0.5/100
    except:
        distance = None
    mapp = kill[kill_header.index("map")]
    weapon = kill[kill_header.index("killed_by")]
    return [weapon, mapp, distance, kill[kill_header.index("killer_name")]]


# In[39]:


kill_summary = list(map(summary, kill_data))
# kill_summary


# In[40]:


mir_kill_summary = list(filter(lambda x: x[1]=='MIRAMAR', kill_summary))
e_kill_summary = list(filter(lambda x: x[1]!='MIRAMAR', kill_summary))
# mir_kill_summary


# In[41]:


kill_summary_pd = pd.DataFrame(kill_summary)
mir_kill_summary_pd = pd.DataFrame(mir_kill_summary)
e_kill_summary_pd = pd.DataFrame(e_kill_summary)
e_weapon_list = list(set(e_kill_summary_pd[0]))
mir_weapon_list = list(set(mir_kill_summary_pd[0]))
# weapon_list
# In[42]:
jinzhan = ['Aquarall', 'Crowbar', 'Punch', 'Hit by Car', 'Pan', 'Machete', 'Sickle']
shouqiang = ['P1911', 'P18C', 'P92', 'R45', 'R1895']
# try:
if True:
    weapon_e_dis_list = []
    for w in e_weapon_list:            
        try:
            std = stat.stdev(e_kill_summary_pd.loc[e_kill_summary_pd[0]==w][2])
        except:
            std = 0
        mean = stat.mean(e_kill_summary_pd.loc[e_kill_summary_pd[0]==w][2])
        weapon_e_dis_list.append([w, mean, std, mean-3*std, mean+3*std,len(e_kill_summary_pd.loc[e_kill_summary_pd[0]==w][2])])
    weapon_e_dis_df = pd.DataFrame(sorted(weapon_e_dis_list, key=lambda x: x[1]))
    weapon_e_dis_df.columns = ['weapon','mean distance','standard deviation','lower bound','upper bound','frequency']
    weapon_e_dis_df = weapon_e_dis_df.set_index('weapon')
    weapon_e_dis_df.to_csv(os.path.join('summary','erangel_weapon'+str(sys.argv[1])+'.csv'))
    def detect_cheating_era(x):
        try:
            if (x[0] in jinzhan and x[2] > 100) or (x[0] in shouqiang and x[2] > 200):
                return True
            return x[2] < weapon_era_dis_df.loc[x[0]]['lower bound'] and x[2] > weapon_era_dis_df.loc[x[0]]['upper bound']
        except:
            return False
    #print(1)
    era_cheat = pd.DataFrame(list(filter(detect_cheating_era,e_kill_summary)))
    era_cheat.columns = ['weapon', 'map', 'distance', 'killer name']
    era_cheat.to_csv(os.path.join('summary','cheater_era'+str(sys.argv[1])+'.csv'))
# except:
#     print('no erangle')


try:
    weapon_mir_dis_list = []
    for w in mir_weapon_list:
        try:
            std = stat.stdev(mir_kill_summary_pd.loc[mir_kill_summary_pd[0]==w][2])
        except:
            std = 0
        mean = stat.mean(mir_kill_summary_pd.loc[mir_kill_summary_pd[0]==w][2])
        weapon_mir_dis_list.append([w, mean, std, mean-3*std, mean+3*std,len(mir_kill_summary_pd.loc[mir_kill_summary_pd[0]==w][2])])
    weapon_mir_dis_df = pd.DataFrame(sorted(weapon_mir_dis_list, key=lambda x: x[1]))
    weapon_mir_dis_df.columns = ['weapon','mean distance','standard deviation','lower bound','upper bound','frequency']
    weapon_mir_dis_df = weapon_mir_dis_df.set_index('weapon')
    weapon_mir_dis_df.to_csv(os.path.join('summary','mirama_weapon'+str(sys.argv[1])+'.csv'))
    def detect_cheating_mir(x):
        try:
            if (x[0] in jinzhan and x[2] > 100) or (x[0] in shouqiang and x[2] > 200):
                     return True
            return x[2] < weapon_mir_dis_df.loc[x[0]]['lower bound'] and x[2] > weapon_mir_dis_df.loc[x[0]]['upper bound']
        except:
            return False
    mir_cheat = pd.DataFrame(list(filter(detect_cheating_mir,mir_kill_summary)))
    mir_cheat.columns = ['weapon', 'map', 'distance', 'killer name']
    mir_cheat.to_csv(os.path.join('summary','cheater_mir'+str(sys.argv[1])+'.csv'))
except:
    print('no miramar')




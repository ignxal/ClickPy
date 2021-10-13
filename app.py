import os
import pandas as pd
from dotenv import load_dotenv
from getters import get_Folders, get_ID, get_Lists, get_Spaces, get_Tasks, get_Timesheet, get_TodayUrl

load_dotenv()
my_headers = {'Authorization' : os.getenv('TOKEN_VAR')}
timesheet = get_Timesheet(get_TodayUrl(), my_headers)
spaces = get_Spaces(my_headers)
id_spaces = get_ID(spaces)

i=0
while i < len(id_spaces):

    #Traigo los folders del space y obtengo sus ID
    folders = get_Folders(id_spaces[i], my_headers)
    id_folders = get_ID(folders)    

    if i==0:
        dfspaces = pd.json_normalize(spaces, record_path =['spaces'])
    else:
        dfspaces2 = pd.json_normalize(spaces, record_path =['spaces'])
        dfspaces = pd.concat([dfspaces,dfspaces2], axis=0)

    #Valido empty
    if id_folders != []: 

        x=0
        while x < len(id_folders):
            #Traigo Lists de cada Folder y obtengo sus ID
            lists = get_Lists(id_folders[x], my_headers)
            id_lists = get_ID(lists)

            if x==0:
                    dffolders = pd.json_normalize(folders, record_path=['folders'])
            else:
                    dffolders2 = pd.json_normalize(folders, record_path=['folders'])
                    dffolders = pd.concat([dffolders,dffolders2], axis=0)
            
            #Valido empty
            if id_lists != []: 
                y=0

                while y < len(id_lists):
                    #Traigo Tasks de cada Lists y obtengo sus ID
                    tasks = get_Tasks(id_lists[y], my_headers)
                    id_tasks = get_ID(tasks)
                    if y==0:
                            dflists = pd.json_normalize(lists, record_path=['lists'])
                    else:
                            dflists2 = pd.json_normalize(lists, record_path=['lists'])
                            dflists = pd.concat([dflists,dflists2], axis=0)
                    
                    #Valido empty
                    if id_tasks != []:   
                        z=0
                        while z < len(id_tasks):
                            if z==0:
                                dftasks = pd.json_normalize(tasks, record_path =['tasks'])
                            else:
                                dftasks2 = pd.json_normalize(tasks, record_path =['tasks'])
                                dftasks = pd.concat([dftasks,dftasks2], axis=0)
                            z+=1
                    y+=1
            x+=1        
    i+=1
dfteam = pd.json_normalize(timesheet, record_path =['data'])

# Merge
a = dflists.merge(dftasks, left_on='id', right_on='list.id', how='outer', suffixes=('.list', '.task'))
b = dffolders.merge(a, left_on='id', right_on='folder.id.list', how='outer', suffixes=('.folder', '.list'))
c = dfspaces.merge(b, left_on='id', right_on='space.id.list', how='outer', suffixes=('.space', '.folder'))  
d = dfteam.merge(c, left_on='task.id', right_on='id.task', how='outer', suffixes=('.team', '.space'))
d.to_excel("Timesheet.xlsx")

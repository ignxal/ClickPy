import os
from dotenv import load_dotenv
from get_TodayUrl import get_TodayUrl
from get_Timesheet import dataToExcel, get_Folders, get_Lists, get_Spaces, get_Tasks, get_Timesheet

load_dotenv()
my_headers = {'Authorization' : os.getenv('TOKEN_VAR')}
timesheet = get_Timesheet(get_TodayUrl(), my_headers)
spaces = get_Spaces(my_headers)
id_spaces = [d.get('id') for sublists in spaces.values() for d in sublists]

i=0
while i < len(id_spaces):
    #Traigo los folders del space y obtengo sus ID
    folders = get_Folders(id_spaces[i], my_headers)
    id_folders = [d.get('id') for sublists in folders.values() for d in sublists]
    #Valido empty
    if id_folders != []:
        x=0
        while x < len(id_folders):
            #Traigo Lists de cada Folder y obtengo sus ID
            lists = get_Lists(id_folders[x], my_headers)
            id_lists = [d.get('id') for sublists in lists.values() for d in sublists]
            #Valido empty
            if id_lists != []: 
                y=0
                while y < len(id_lists):
                    #Traigo Tasks de cada Lists y obtengo sus ID
                    tasks = get_Tasks(id_lists[y], my_headers)
                    id_tasks = [d.get('id') for sublists in tasks.values() for d in sublists]
                    #Hacer merge en esta linea con timesheet

#Data a excel
#dataToExcel(mergeHecho, my_headers)

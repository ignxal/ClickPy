import requests
import json
from pandas import json_normalize

def get_Timesheet(url, myh):
    try:
        timesheet = json.loads(requests.get(url, headers=myh).text)
        return timesheet
    except:
        print("URL invalida")

def get_Spaces(myh):
    spaces = json.loads(requests.get('https://api.clickup.com/api/v2/team/{TeamID}/space?archived=False', headers=myh).text)
    return spaces

def get_Folders(space_id, myh):
    folders = json.loads(requests.get('https://api.clickup.com/api/v2/space/' + space_id + '/folder?archived=False', headers=myh).text)
    return folders

def get_Lists(folder_id, myh):
    lists = json.loads(requests.get('https://api.clickup.com/api/v2/folder/' + folder_id + '/list?archived=False', headers=myh).text)
    return lists

def get_Tasks(tasks_id, myh):
    #faltar configurar params del link
    tasks = json.loads(requests.get('https://api.clickup.com/api/v2/list/' + tasks_id + '/task?archived=&page=&order_by=&reverse=&subtasks=&statuses%5B%5D=&include_closed=&assignees%5B%5D=&due_date_gt=&due_date_lt=&date_created_gt=&date_created_lt=&date_updated_gt=&date_updated_lt=&custom_fields%5B%5D=', headers=myh).text)
    return tasks

def dataToExcel(Timesheet):
    data = json_normalize(Timesheet, record_path =['data'])
    data.to_excel('Timesheet.xlsx', sheet_name='data')
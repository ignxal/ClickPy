import requests
import arrow
import json

def get_Timesheet(url, myh):
    try:
        returnValue = json.loads(requests.get(url, headers=myh).text)
    except:
        returnValue = print("URL invalida")
    return returnValue

def get_ID(target):
    try:
        returnValue = [d.get('id') for sublists in target.values() for d in sublists]
    except AttributeError:
        returnValue = []
    return returnValue

def get_Spaces(myh):
    spaces = json.loads(requests.get('https://api.clickup.com/api/v2/team/{TEAM ID}/space?archived=False', headers=myh).text)
    
    return spaces

def get_Folders(space_id, myh):
    folders = json.loads(requests.get('https://api.clickup.com/api/v2/space/' + space_id + '/folder?archived=False', headers=myh).text)
    
    return folders

def get_Lists(folder_id, myh):
    lists = json.loads(requests.get('https://api.clickup.com/api/v2/folder/' + folder_id + '/list?archived=False', headers=myh).text)
    return lists

def get_Tasks(tasks_id, myh):
    tasks = json.loads(requests.get('https://api.clickup.com/api/v2/list/' + tasks_id + '/task?archived=False', headers=myh).text)
    return tasks

def get_TodayUrl():
    today = (int(arrow.utcnow().timestamp() * 1000))
    todayString = str(today)
    today_url = 'URL' + todayString
    return today_url

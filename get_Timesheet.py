import requests
import json
from pandas import json_normalize

def get_Timesheet(url, myh):
    try:
        Timesheet = json.loads(requests.get(url, headers=myh).text)
    except:
        print("URL invalida")
    dataToExcel(Timesheet)

def dataToExcel(Timesheet):
    data = json_normalize(Timesheet, record_path =['data'])
    data.to_excel('Timesheet.xlsx', sheet_name='data')
import requests
import json
from pandas import json_normalize

my_headers = {'Authorization' : 'Token'}
get_Timesheet = json.loads(requests.get('API LINK', headers=my_headers).text)

data = json_normalize(get_Timesheet, record_path =['data'])
data.to_excel('Timesheet.xlsx', sheet_name='data')
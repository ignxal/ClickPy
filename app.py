import requests
import json
from get_TodayUrl import get_TodayUrl
from pandas import json_normalize

my_headers = {'Authorization' : 'Token'}
today_url = get_TodayUrl()
get_Timesheet = json.loads(requests.get(today_url, headers=my_headers).text)
data = json_normalize(get_Timesheet, record_path =['data'])
data.to_excel('Timesheet.xlsx', sheet_name='data')
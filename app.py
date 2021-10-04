import os
from dotenv import load_dotenv
from get_TodayUrl import get_TodayUrl
from get_Timesheet import get_Timesheet

load_dotenv()
my_headers = {'Authorization' : os.getenv('TOKEN_VAR')}
today_url = get_TodayUrl()
get_Timesheet(today_url, my_headers)

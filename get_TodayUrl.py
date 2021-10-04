import arrow

def get_TodayUrl():
    today = (int(arrow.utcnow().timestamp() * 1000))
    todayString = str(today)
    today_url = 'URL' + todayString
    return today_url
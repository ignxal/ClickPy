import arrow

def get_TodayUrl():
    today = (int(arrow.utcnow().timestamp() * 1000))
    todayString = str(today)
    today_url = 'API' + todayString
    return (today_url)
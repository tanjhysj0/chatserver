from datetime import datetime
from datetime import timezone,timedelta

def get_now_timestamp():
    return datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=8)))

def get_now_date()->str:
    return get_now_timestamp().strftime("%Y-%m-%d")
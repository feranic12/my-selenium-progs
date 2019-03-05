from datetime import datetime,timedelta


def get_begin_day(delta_days):
    today = datetime.today()
    begin_day = today + timedelta(delta_days)
    begin_day_str = begin_day.strftime("%d%m%Y")
    return begin_day_str

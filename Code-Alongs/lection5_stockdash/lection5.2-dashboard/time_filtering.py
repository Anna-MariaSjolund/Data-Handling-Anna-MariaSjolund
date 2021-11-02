from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()
yesterday = now.date() - relativedelta(days = 10)
print(now)
print(yesterday)

def filter_time(df, days= 0):
    last_day = df.index[0].date()
    start_day = last_day - relativedelta(days=days)
    df = df.sort_index().loc[start_day:last_day] #we have to run sort_index(), otherwise we get a warning
    return df
    
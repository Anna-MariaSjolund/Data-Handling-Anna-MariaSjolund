from datetime import datetime
from dateutil.relativedelta import relativedelta

#now = datetime.now() #The time right now
#now.date() gives the date without the time stamps
#yesterday = now.date() - relativedelta(days = 1) 
#ten_days_ago = now.date() - relativedelta(days = 10) 
#print(now)
#print(yesterday)
#print(ten_days_ago)

def filter_time(df, days=0):
    last_day = df.index[0].date() #index all of the dates and index[0] gives the first date and date() removes the time
    start_day = last_day - relativedelta(days=days) #From the latest date - the number of days we put in
    df = df.sort_index().loc[start_day:last_day] #We slice it from start_day to last_day, we have to run sort_index(), otherwise we get a warning 
    return df 
    
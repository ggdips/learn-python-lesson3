#!env/bin/python3
from datetime import datetime, timedelta
from tzlocal import get_localzone

def main():
    local_tz = get_localzone()
    dt_now = datetime.now(local_tz).strftime('%d.%m.%Y')
    dt_yd = (datetime.now(local_tz) - timedelta(days = 1)).strftime('%d.%m.%Y')
    dt_30d_ago = (datetime.now(local_tz) - timedelta(days = 30)).strftime('%d.%m.%Y')
    date_str = "01/01/25 12:10:03.234567" 
    date_dstr = datetime.strptime(date_str, '%y/%m/%d %H:%M:%S.%f')

    print(f'Today is {dt_now}')
    print(f'Yesterday was {dt_yd}')
    print(f'30 days ago was {dt_30d_ago}')
    print(f'Date from string is {date_dstr}')

if __name__ == "__main__":
    main()

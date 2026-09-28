import datetime


def year(request):
    now = datetime.datetime.now()
    return {
        "current_date":{  
        "year": now.year,
        "year_short": now.strftime('%y'),
        "month": now.month, 
        "month_name": now.strftime('%B'),
        "day": now.day,
        "weekday": now.strftime('%A')
        }
    }       
import datetime

MONTHS_RU = {
    1:'Января' ,2:'Февраля' ,3:'Марта',
    4:'Апреля' ,5:'Мая', 6:'Июня',
    7:'Июля' ,8:'Августа' ,9:'Сентября',
    10:'Октября' , 11:'Ноября' ,12:'Декабря' ,
}

def current_date(request):
    now = datetime.datetime.now()
    return{
        'current_date':{
            'year':now.year,
            'month':now.month,
            'month_name_ru':MONTHS_RU[now.month],
            'day':now.day,
            'weekday':now.strftime('%A'),
            'date_iso':now.strftime('%Y-%m-%d'),
            'date_ru':now.strftime('%d.%m.%Y'),
        }
    }
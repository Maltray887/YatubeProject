# The social network
## How to start
1. Создать виртуальное окружение ``` py -3.9 -m venv venv ```

    **EN - We use python with version 3.5-3.9 and Django version 2.2.19**

    **RU - Мы используем пайтон с версией от 3.5 до 3.9 и версию джанго 2.2.19**

    **EN - You should check venv by ```which python```**

    **RU - Мы можем проверить версию пайтона в вирутальном окружении командой ```which python```**

3. Активировать виртуальное окружение ``` source venv/Scripts/activate ```

4. Установить Django версии 2.2.19 ``` pip install Django==2.2.19 ```

5. Установить зависимости используя файл requirements.txt ```pip freeze > requirements.txt ``` 

6. Запуск проекта ``` django-admin startproject yatube ``` 

7. Перейти в папку yatube ``` cd yatube ``` 

8. Запуск сервера ```  python manage.py runserver ``` 

**Defoult url is http://127.0.0.1:8000/**

### **Thanks for use my project**
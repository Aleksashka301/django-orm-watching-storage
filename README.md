# Пульт охраны банка

 Программа отслеживает карты сотрудников. Предоставляет информацию о том, кто в данный момент находится в хранилище и 
сколько времени он там. А так же все посещения по имени сотрудника. Скрипт подсвечивает долгие визиты (более часа) и
обозначает их как подозрительные.

![image](https://github.com/user-attachments/assets/cc0f9ae7-c955-4309-bde1-afd3ef766f7e)

![image](https://github.com/user-attachments/assets/bf3f0625-c3d5-4e0a-96b4-b86ca2196272)

![image](https://github.com/user-attachments/assets/d4061eea-7bdc-4df3-93c3-fb703cbea62f)

## Установка

 Склонируйте репозиторий на ваш компьютер:
```commandline
git clone https://github.com/Aleksashka301/django-orm-watching-storage
cd django-orm-watching-storage
```
 Установите виртуальное окружение:
```commandline
python -m venv venv
venv\Scripts\activate
```

 Для работы программы необходим `Python v3.11`. Так же для работы понадобятся библиотеки `django==3.2.*` и 
`psycopg2-binary==2.9.*`, которые находятся в файле `requirements.txt`. Для установки, в терминале необходимо 
 запустить команду ниже.
```python
pip install -r requirements.txt
```

## Для работы
 
 В корневой папке нужно создать файл `.env` и добавить туда следующие переменные `DB_ENGINE`, `DB_HOST`, `DB_PORT`,
`DB_NAME`, `DB_GUARD`, `DB_PASSWORD`, в них хранится информация о настройке базы данных. Также переменная 
`SECRET_KEY`. `DEBUG` по умолчанию стоит значение `False`, при проверке или настройки базы не обходимо поставить 
значение `True`, что бы детальнее видеть работу сайта. Затем перед запуском вернуть значение `False`. Также в 
переменной `ALLOWED_HOSTS` необходимо указать рабочий домен, без этого сайт будет уязвим к таким атакам как 
`HTTP Host header attacks`.

После того как всё установленно, можно запустить программу
```python
python manage.py
```

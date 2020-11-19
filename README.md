# api_yatube
Приложение к проекту **YaTube** https://github.com/Bazulenkov/hw05_final
позволяет работать с порталом YaTube через API

*запросы к API начинаются с `/api/v1/`*  
*документация к API доступна по `/redoc/`*

## Запуск проекта (на примере Linux)

- У вас должна быть установлена PostgreSQL (пакеты postgresql postgresql-contrib),  
- создана база yatube
    ```
    sudo -u postgres psql
    CREATE DATABASE yatube;
    ```
- в psql создан пользователь `yatube_user` c правами на работу с базой
    ```
    CREATE USER yatube_user WITH ENCRYPTED PASSWORD 'yatube_user_password';
    GRANT ALL PRIVILEGES ON DATABASE yatube TO yatube_user; 
    ```
- Создайте папку проекта `mkdir yatube` и перейдите в нее `cd yatube`. Или если у вас уже развернут проект yatube, то перейдите в папку проекта.
- Склонируйте этот репозиторий в текущую папку `https://github.com/Bazulenkov/api_yatube .`
- Создайте файл `.env` командой `touch .env` и добавьте в него переменные окружения для работы с базой данных:
`DATABASE_URL=psql://yatube_user:yatube_user_password@127.0.0.1:5432/yatube`

- Создайте виртуальное окружение `python3 -m venv venv`
- Активируйте виртуальное окружение `source venv/bin/activate`
- Установите зависимости `pip install -r requirements.txt`
- Накатите миграции `python manage.py migrate`
- Соберите статику командой `python manage.py collectstatic --no-input`
- Создайте суперпользователя Django `python manage.py createsuperuser --username admin --email 'admin@example.com'`
- Запустите сервер разработки Django `python manage.py runserver`



## В разработке использованы

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [DRF Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

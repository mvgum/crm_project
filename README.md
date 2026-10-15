# CRM-система

Веб-приложение для автоматизации работы с клиентами: учёт услуг,
рекламных кампаний, потенциальных и активных клиентов, контрактов,
подсчёт статистики рекламных кампаний.

## Стек

- Python 3.13
- Django 6.1
- PostgreSQL 17
- Bootstrap 5, Font Awesome

## Роли

- **Администратор** — управление пользователями (admin)
- **Оператор** — работа с лидами
- **Маркетолог** — услуги и рекламные кампании
- **Менеджер** — контракты и перевод лидов в активных

## Функционал

- Аутентификация пользователей
- CRUD услуг, рекламных кампаний, лидов, контрактов, активных клиентов
- Перевод лида в активного клиента через создание контракта
- Загрузка файлов контрактов
- Статистика рекламных кампаний (лиды, активные клиенты, доход, ROI)
- Роли пользователей с разными правами

## Установка

1. Клонировать репозиторий:
git clone <URL>
cd crm_project

2. Создать и активировать виртуальное окружение:
python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Linux/macOS

3. Установить зависимости:
pip install -r requirements.txt

4. Создать БД PostgreSQL:
```sql
CREATE USER crm_user WITH PASSWORD 'crm_password';
CREATE DATABASE crm_db OWNER crm_user ENCODING 'UTF8';
```

5. Настроить crm_project/settings.py (блок DATABASES).
6. Применить миграции:
python manage.py migrate
7. Создать суперпользователя:
python manage.py createsuperuser
8. Запустить сервер:
python manage.py runserver
9. Открыть http://127.0.0.1:8000/
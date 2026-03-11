# 🌐 MySite

Персональный сайт, созданный на фреймворке Django.

## 📋 Описание

Первый полноценный веб-проект на Django, включающий:
- Персональный блог
- Портфолио проектов
- Контактную форму
- Админ-панель

## 🏗️ Архитектура

```
MySite/
├── MySite/              # Основной конфиг Django
│   ├── __init__.py
│   ├── settings.py     # Настройки
│   ├── urls.py         # Маршрутизация
│   └── wsgi.py         # WSGI конфигурация
├── static/             # CSS, JavaScript, изображения
├── templates/          # HTML шаблоны
└── manage.py          # Консоль Django
```

## 🚀 Запуск

### Требования
- Python 3.8+
- Django 4.x
- См. requirements.txt

### Установка
```bash
# Клонирование (если нужно)
git clone https://github.com/kirillbarashkov/MySite.git
cd MySite

# Виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Установка зависимостей
pip install -r requirements.txt

# Миграции БД
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Запуск сервера
python manage.py runserver
```

## 🎯 Особенности

- **ORM Django**: работа с базой данных через модели
- **Templates**: шаблонизатор Django для HTML
- **CSS-in-Django**: статические файлы
- **Admin Panel**: встроенная админка

## 📝 Что изучалось

- Django MTV (Model-Template-View) архитектура
- Маршрутизация URL
- Шаблоны и наследование
- Формы и валидация
- Статические файлы
- Deploy (возможно)

---

*Первый шаг в веб-разработке*

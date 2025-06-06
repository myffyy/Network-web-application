# Network Tools

## Описание проекта (Project Description)

Это веб-приложение, предоставляющее набор инструментов для работы с сетевыми адресами и подсетями. Приложение включает в себя конвертер IP-адресов и калькулятор подсетей.

## Основные функции (Main Features)

### Конвертер IP-адресов (IP Converter)
- Конвертация между форматами IPv4
- Валидация IP-адресов
- Поддержка различных форматов представления IP

### Калькулятор подсетей (Subnet Calculator)
- Расчет параметров подсети
- Автоматическое определение маски подсети
- Проверка корректности введенных данных
- Отображение диапазона адресов
- Расчет возможного количества хостов

## Технические характеристики (Technical Specifications)

### Используемые технологии (Used Technologies)
- Backend: Python 3.x
- Framework: Flask 3.1.1
- Frontend: HTML5, CSS3, JavaScript
- UI: Собственная реализация с поддержкой темной темы

### Системные требования (System Requirements)
- Python 3.8+
- Flask 3.1.1
- Браузер: Современный веб-браузер с поддержкой HTML5

## Установка и запуск (Installation and Running)

### Установка зависимостей (Installing Dependencies)
```bash
# Создаем виртуальное окружение
python -m venv venv

# Активируем виртуальное окружение
source venv/bin/activate  # для Linux/Mac
# или
venv\Scripts\activate    # для Windows

# Устанавливаем зависимости
pip install -r requirements.txt
```

### Запуск приложения (Running the Application)
```bash
python app.py
```

После запуска приложение будет доступно по адресу: http://localhost:5001

## Использование (Usage)

### Переключение темы (Theme Switching)
- Приложение поддерживает темную и светлую тему
- Переключение происходит через кнопку в верхнем левом углу
- Выбор темы сохраняется между сессиями

### Навигация (Navigation)
- Главная страница: http://localhost:5001
- Конвертер IP: http://localhost:5001/ip-converter
- Калькулятор подсетей: http://localhost:5001/subnet-calculator

## Структура проекта (Project Structure)

```
Networks/
├── app (docs)/                   # Документация приложения
│   └── README.md               # Документация приложения
├── console/                      # Консольная версия
│   ├── console.py              # Консольный интерфейс
│   └── README.md               # Документация консоли
├── requirements/                 # Список зависимостей
│   ├── requirements.txt        # Список зависимостей
│   └── README.md               # Документация зависимостей
├── static/                       # Статические файлы
│   ├── style.css               # Стили приложения
│   └── README.md               # Документация стилей
├── templates/                    # HTML шаблоны
│   ├── index.html              # Главная страница
│   ├── ip_converter.html       # Конвертер IP
│   ├── subnet_calculator.html  # Калькулятор подсетей
│   └── README.md               # Документация шаблонов
├── README.md                     # Основная документация проекта
├── app.py                        # Основное приложение Flask
```

## Автор (Author)

myffyy

---

## Дополнительные заметки (Additional Notes)

- Приложение оптимизировано для работы в современных браузерах
- Поддерживается темная тема по умолчанию
- Интерфейс адаптирован под разные размеры экранов
- Все вычисления выполняются на клиентской стороне для лучшей производительности

## Скриншоты (Screenshots)

### Главная страница (Home Page)
![Главная страница](screenshots/homepage.png)

### Конвертер IP (IP Converter)
![Конвертер IP](screenshots/ipconverter.png)

### Пример конвертации IP (IP Conversion Example)
![Пример конвертации IP](screenshots/converterexample.png)

### Калькулятор подсетей (Subnet Calculator)
![Калькулятор подсетей](screenshots/subnetcalculator.png)

### Пример расчета подсети (Subnet Calculation Example)
![Пример расчета подсети](screenshots/subnetexample.png)

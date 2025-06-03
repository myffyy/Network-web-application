# Документация директории static

## Описание

Директория static содержит статические файлы для веб-приложения Network Tools, включая стили, изображения и другие ресурсы, которые не изменяются во время выполнения приложения.

## Структура директории

```
static/
└── style.css    # Основной файл стилей приложения
```

## Стили (style.css)

### Основные переменные
```css
:root {
    --primary-color: #4361ee;
    --secondary-color: #3f37c9;
    --accent-color: #4895ef;
    --success-color: #2e7d32;
    --error-color: #d32f2f;
    --warning-color: #ed6c02;
    --border-color: #dee2e6;
    --card-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    --transition: all 0.3s ease;
}
```

### Темы
- Светлая тема (значения по умолчанию)
- Темная тема (data-theme="dark")
- Синхронизация темы между страницами

### Базовые стили
```css
body {
    font-family: -apple-system, BlinkMacSystemFont, 'San Francisco', system-ui, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--background-color);
    margin: 0;
    padding: 0;
}
```

### Компоненты
1. Контейнер
```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}
```

2. Заголовок
```css
header {
    background-color: var(--primary-color);
    color: white;
    padding: 20px 0;
    text-align: center;
    margin-bottom: 30px;
    margin-top: 20px;
    border-radius: 12px;
}
```

3. Карточки
```css
.card {
    background: white;
    border-radius: 8px;
    box-shadow: var(--card-shadow);
    padding: 25px;
    margin-bottom: 30px;
}
```

### Формы
```css
.form-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0;
}

input, select, textarea {
    padding: 0.75rem 1rem;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    font-size: 1rem;
}
```

### Адаптивность
```css
@media (max-width: 768px) {
    .form-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
    }
    
    button {
        width: 100%;
        margin-top: 0.5rem;
    }
}
```

## Особенности реализации

### Темы
- Темная тема по умолчанию
- Автоматическое сохранение выбранной темы
- Адаптивные стили для разных тем
- Поддержка синхронизации темы между страницами

### Адаптивность
- Поддержка разных размеров экранов
- Адаптивные сетки для форм
- Адаптивные шрифты
- Адаптивные отступы

### Анимации и переходы
- Плавные переходы состояний
- Эффекты при взаимодействии
- Оптимизация производительности анимаций

## Рекомендации по использованию

1. При добавлении новых стилей использовать существующие переменные
2. Следовать принципам доступности веб-контента
3. Тестировать стили на разных устройствах и браузерах
4. Оптимизировать стили для производительности

## Файлы стилей

### style.css
- Основной файл стилей приложения
- Содержит все стили для всех страниц
- Использует систему переменных для тем
- Поддерживает адаптивный дизайн

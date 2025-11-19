# HabrParserAI

Микросервисная архитектура для парсинга статей с Habr и их обработки с помощью LLM

## Основные возможности

- **BFF Service** - Backend for Frontend, точка входа для клиентов
- **Habr Adapter** - Сервис для парсинга и получения контента статей
- **LLM Service** - Сервис интеграции с LLM (Gemini) для анализа текста
- **Async Processing** - Асинхронная обработка задач через RabbitMQ
- **Infrastructure** - Полный стек с PostgreSQL, Redis и RabbitMQ в Docker

## Установка и запуск

1. Создать файл `.env` на основе `.env.example`:
```bash
cp .env.example .env
```

2. Запустить проект через Docker Compose:
```bash
docker-compose up -d --build
```

Сервисы будут доступны по адресам:
- BFF Service: http://localhost:8000
- Habr Adapter: http://localhost:5000
- LLM Service: http://localhost:5001
- RabbitMQ UI: http://localhost:15672 (user/password)

## Структура проекта

```
bff/                # Backend for Frontend сервис
habr_adapter/       # Сервис парсинга Habr
llm_service/        # Сервис работы с LLM
docker-compose.yaml # Оркестрация контейнеров
logs/               # Логи приложений
```

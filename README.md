# Запуск приложение

Версия Python >= 3.5

Все действия выполнять из каталога server

## Установка и запуск

```
$ > python -m venv .venv

[Windows CMD] $ > .venv\Scripts\activate
[Windows GIT Bash] $ > source .venv/Scripts/activate
[OSX, Linux] $ > source .venv/bin/activate

$ > pip install -r requirements.txt

$ > python manage.py migrate

$ > python manage.py runserver
```
## Создание пользователя
```
$ > python manage.py createsuperuser
```

# Управление списком опросов
**`Функционал для администратора системы:`**

Все действия выполняются из админ-панели Django

```
<host>/admin
```

**`Функционал для пользователей системы:`**


#### Получение списка активных опросов:

```
[GET] <host>/api/v1/interview
```
Пример ответа:
```json
  [
    {
      "name": "Опрос",
      "description": "Описание",
      "date_start": "2020-07-20T16:18:39+03:00",
      "date_end": "2020-07-16T12:00:00+03:00",
      "questions": [
        {
          "id": 1,
          "name": "Вопрос",
          "type": "text"
        }
      ]
    }
]
```

#### Авторизация пользователя по токены:

```
[POST] <host>/api/v1/auth/token
```

Пример данных для отправки в формате JSON:
```json
{
  "username": "example",
  "password": "123456"
}
```

Пример ответа:
```json
{
  "token": "d72787b927848dd100f011cf1233aa1d8b1282fd"
}
```

#### Ответ на опросы:

```
[POST] <host>/api/v1/interview/answer/create
```

Пример данных для отправки в формате JSON:

```json
{
  "interview_id": 2, # ID опроса
  "answer": "1" # ID вопросов через запятую
}
```

Пример ответа:

```json
{
  "interview": {
    "name": "Опрос",
    "description": "Описание",
    "date_start": "2020-07-20T16:18:39+03:00",
    "date_end": "2020-07-16T12:00:00+03:00",
    "questions": [
      {
        "id": 1,
        "name": "Вопрос",
        "type": "text"
      }
    ]
  },
  "answer": "1"
}
```

####  Получение пройденных пользователем опросов:

```
[GET] <host>/api/v1/interview/answer
```
Пример ответа:

```json

[
  {
    "interview": {
      "name": "Опрос",
      "description": "Описание",
      "date_start": "2020-07-20T16:18:39+03:00",
      "date_end": "2020-07-16T12:00:00+03:00",
      "questions": [
        {
          "id": 1,
          "name": "Вопрос",
          "type": "text"
        }
      ]
    },
    "answer": "1"
  }
]
```


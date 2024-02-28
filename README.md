# BAUM Storage

# Тестовое задание на позицию backend разработчика

## Технологии

- Python
- FastAPI
- Kafka 
- SQLAlchemy
- PostgreSQL

<details> 
<summary> Поставленная задача </summary>

Требуется создать микросервисное приложение, где два микросервиса на FastApi
будут взаимодействовать через брокер сообщений.

1. Каждый микросервис должен быть запущен в отдельном контейнере Docker и иметь
   возможность:

- принимать файлы через REST API,
- сохранять файлы на диске и метаданные в свою базу данных.

2. При запросе к любому из микросервисов должны возвращаться метаданные и общий
   объем загруженных файлов.

3. Один из микросервисов должен уметь подсчитывать количество нулевых бит в
   файле, а другой - количество единичных бит.

4. Если количество нулевых бит в файле больше, чем количество единичных, то файл
   и метаданные должны сохраняться только в первом микросервисе, и наоборот.

5. Приложение должно быть легко устанавливаться из репозитория с помощью
   docker-compose up.

</details>

## Как запустить проект:

### Клонирование репозитория:

```sh
git clone https://github.com/realm74/baum
```

<details> <summary> Шаблон наполнения .env </summary>

```
Example of filling a file .env:

#=============== VERSIONS ==================
ZK_VERSION=3.7.0
CONFLUENT_VERSION=6.2.0
PG_VERSION=13.3
GRAFANA_VERSION=latest
PROMETHEUS_VERSION=latest

#================= PORTS ===================
ZK_PORT=2181
KAFKA_PORT=9092
KAFKA_LOCALHOST_PORT=9093
PG_PORT=5432
PG_ADMIN_PORT=5050
GRAFANA_PORT=3000
PROMETHEUS_PORT=9090

DEMO_SERVER_PORT=8002
DATA_REQUESTER_PORT=8003
DATA_PROCESSOR_PORT=8004
DATA_AGGREGATOR_PORT=8005
DB_LOADER_PORT=8006
API_GATEWAY_PORT=8007

DATA_REQUESTER_STATS_PORT=7003
DATA_PROCESSOR_STATS_PORT=7004
DATA_AGGREGATOR_STATS_PORT=7005
DB_LOADER_STATS_PORT=7006

#================= ONE ===================
ONE_DRIVER='postgresql+asyncpg'
ONE_USER='postgres'
ONE_PASSWORD='postgres'
ONE_HOST='postgres_one'
ONE_PORT='5433'
ONE_DB_NAME='postgres'

#================= ZERO ===================
ZERO_DRIVER='postgresql+asyncpg'
ZERO_USER='postgres'
ZERO_PASSWORD='postgres'
ZERO_HOST='postgres_zero'
ZERO_PORT='5432'
ZERO_DB_NAME='postgres'
```

</details>

### Запуск приложения в Docker

Собрать контейнер

```
docker-compose build
```

Запустить docker-compose.yaml

```
docker-compose up
```

Проект запущен

```
http://localhost:8000/docs
```
```
http://localhost:8080/docs
```

Удалить контейнеры

```
docker-compose down
```

## Эндпойнты

<details> 
<summary> Подробнее </summary>

### Эндпойнт добавления файла:

```python 
POST http://localhost:8000/data/upload
```

### Эндпойнт получения метаданных и общего объема загруженных данных:

```python 
GET http://127.0.0.1:8000/data
```

Ответ:

```
{
  "total_size": 827,
  "list_metadata": {
    "1": {
      "name": "3.txt",
      "size": 36
    },
    "2": {
      "name": "23rf",
      "size": 332
    },
    "3": {
      "name": "1.txt",
      "size": 54
    },
    "4": {
      "name": "2.txt",
      "size": 297
    },
  }
}
```

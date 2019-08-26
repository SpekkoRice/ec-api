# Events Cloud Weather API
## How to run the project

With Docker:
```
cd <project-root-dir>; docker-compose up
```
With Python and Postgress at OS level:
```
cd <project-root-dir>; pip install dependencies; python manage.py runserver 0.0.0.0:8000
```

# Dependencies
- docker & docker-compose

# Dependencies if you don't have docker
- Python 3
- PostgresSQL

## Useful commands:

To get into the postgres docker container
```
docker exec -it ee_postgres psql -U postgres
```

To get into the python 3 docker container
```
 docker exec -it ec-api_web_1  /bin/bash
```

Once you're in the python 3 contianer you can run `python manage.py migrate` to run the migrations


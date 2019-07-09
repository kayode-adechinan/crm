[![pipeline status](https://gitlab.com/kayode-adechinan/django_starter/badges/master/pipeline.svg)](https://gitlab.com/kayode-adechinan/django_starter/commits/master)

[![coverage report](https://gitlab.com/kayode-adechinan/django_starter/badges/master/coverage.svg)](https://gitlab.com/kayode-adechinan/django_starter/commits/master)


# Django starter template

A simple django starter for faster development

# clone and update

```sh
$ git clone git@gitlab.com:kayode-adechinan/django_starter.git <project_name>
$ cd <project_name>
$ python update_project.py <project_name>
$ pipenv install
$ pipenv shell
$ sudo rm -R .git --force
```

# Useful commands

## Pipenv

> generate requirements.txt from pipenv

```sh
$ pipenv lock -r >> requirements.txt
```

> install package from pipenv

```sh
$ pip install -r requirements.txt
```

## Heroku

> deploy

```sh
$ git init
$ git add .
$ git commit -m 'initial'
$ heroku login
$ heroku create demo-bootcamp
$ heroku addons:create heroku-postgresql:hobby-dev
$ git push heroku master
$ heroku run python manage.py migrate
```


> heroku env vars

```sh
$ heroku config:set WEB_CONCURRENCY=3
$ heroku config
$ heroku config:get GITHUB_USERNAME
```

## Pytest

```sh
$ pytest
$ pytest -v
```

## Docker

```sh
$ docker-compose up
```

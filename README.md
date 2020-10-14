# recipe-app-api
dockered django rest api with complete unit tests and travis-ci & flake8

# after creating app folder:
docker-compose run app sh -c "django-admin.py startproject app ."

First app is all django stuff as volume for docker

Second app is the project

"apps" as in django term in the project app are: core, user, etc.

# later when creating eg. user app:
docker-compose run --rm app sh -c "python manage.py startapp user"

# FastCart


# Stack
* `Django 1.10`


### Create VENV
1. `sudo pip3 install virtualenv`
2. `virtualenv venv --no-site-packages` 
3. `source venv/bin/activate`
4. `venv/bin/pip3 install -r requirements.txt`


### API
* **/api/goods/** `GET` (current product)
* **/api/session/** `GET` (current goods), `PUT` ()


### Migrations:
```
source ../venv/bin/activate &&
../venv/bin/python3.5 manage.py makemigrations &&
../venv/bin/python3.5 manage.py migrate
```
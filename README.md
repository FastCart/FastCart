# FastCart
![FastCart](https://github.com/samsheff/FastCartMobile/blob/master/screenshots/fastcart%20logo.png?raw=true)

# Stack
* `Django 1.11`


### Create VENV
1. `sudo pip3 install virtualenv`
2. `virtualenv -p python3  venv --no-site-packages` 
3. `source venv/bin/activate`
4. `venv/bin/pip3 install -r requirements.txt`


### Init project in IDEA:
1. Open project in PyCharm
2. In `File` > `Settings` > `Project Interpreter` > `Add Local` write `venv/bin/python3.5`


### API
* **/api/goods/** `GET` (current product), `POST` (params: code, weight)


### Migrations:
```
source venv/bin/activate &&
venv/bin/python3.5 manage.py makemigrations &&
venv/bin/python3.5 manage.py migrate
```

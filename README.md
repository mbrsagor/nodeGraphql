# Task scheduling

## Setup

### Dependancies

- Python 3.8.5 / Django 3.1.2

The following steps will walk you thru installation on a Mac. Linux should be similar.
It's also possible to develop on a Windows machine, but I have not documented the steps.
If you've developed the django-celery app run on Windows, you should have little problem getting
up and running.

### Install ```vritualenv```
Activate `virutalenv` like
```
virtualenv venv --python=python3.8
source venv/bin/activate
```

> Create mysql database. If already installed mysql in your system then please follow the command
```mysql based
mysql -u root -p12345678
create database celery;
```
Here -u db_username and -p then db_password


### Install radis server 
On Mac OS
```
brew install redis
brew services start redis
```
Brew permission errors? Try ```sudo chown -R "$USER":admin /usr/local```

Open & Test Redis: open terminal
```
redis-cli ping
```
Output:
```PONG```

Then run redis server: ```redis-server```
##### Install Celery + Redis in your virtualenv.
```
pip install "celery[redis]"
pip install redis
pip install django-celery-beat
pip install django-celery-results
pip freeze > requirements.txt
```

 
#### Migrate and create superuser
```
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
```

###### Run Celery Locally
* Run the Celery Consumer Worker (locally). Make sure virtualenv is activated and this command where you run runserver*

- First run a new terminal and follow the command
`celery -A Taskschedule worker -l info`

- Then open another terminal and run the command.
`celery -A Taskschedule beat -l info -S django`

* To see Celery Worker status

###### Here `Taskschedule` is a project name.


##### Python competitive programming
> 1. Given a sorted array, the task is to remove the duplicate elements from the array
(Using only the Input Array)

```python
def remove_duplicate_values(arr, num):
    if num == 0 or num == 1:
        return num

    temp = list(range(num))

    j = 0
    for i in range(0, num - 1):
        if arr[i] != arr[i + 1]:
            temp[j] = arr[i]
            j += 1

    temp[j] = arr[num - 1]
    j += 1

    for i in range(0, j):
        arr[i] = temp[i]
    return j


items = [int(x) for x in input('Enter numbers: ').split()]
val = len(items)
_val = remove_duplicate_values(items, val)
for v in range(_val):
    print((items[v]), end=" ")
```


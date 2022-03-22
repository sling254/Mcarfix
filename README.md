# Mcarfix
## Description.
A Django rest framework endpoints to interact with Mcarfix which is a service that connects a user to a mechanic, has the capability to add mechanics and the services their offer.

#### A Mcarfix Clone  , {Date March 22 2022}
## Check out the website


## Setup/Installation Requirements

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/sling254/Mcarfix
$ cd Mcarfix
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv name-of-the-env
$ source env/bin/activate
```
Note to use the above command that is { virtualenv} you must have virtualenv installed you can do that by:--
```sh
$ pip install virtualenv 

```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.


# Behaviour Driven Development 
1. Get data showing an array for shop inventory. endpoint -- https://mcarfix.herokuapp.com//shopinventory-list
2. Post Spare part shop inventory -- https://mcarfix.herokuapp.com//add-itemsshopinventory/
3. Pair a mechanic with the services they offer. -- https://mcarfix.herokuapp.com//add-itemspairmechanic/
4. Get data showing all mechanics and services they offer. --https://mcarfix.herokuapp.com//view-mechanics
## Known Bugs
- There is no known bug at the time of the first release

## Technologies Used
- Python-Django REST Framework
- Postgress

## Support and contact details
- Github  --Sling254

### License
* see [License](https://github.com/sling254/Mcarfix/blob/main/LICENSE)  file
Copyright (c) {2021}




# Mars-Fitness
Mars Fitness is a gym that uses a subscription based membership. 

## Installing Dependencies
1. **Python 3.9** - Follow instruction to install the lates version of python for your platform in the [python docs]().
2. **Virtual Environment** - Creating a virtual environment for the python project is recommended. Refer to the [python docs]().
3. **PIP Dependencies** - After you set up the virtual enviornment setup and have it running, install dependencies by running the below command within the ```/Mars-Fitness``` folder.

```bash
$ pip install -r requirements.txt
```

4. **Key Dependencies**
   - [Flask](https://flask.palletsprojects.com/en/2.0.x/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.
   - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the postgres database.
   - [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/) is a PostgreSQL database adapter for the Python.
   - [Stripe](https://stripe.com/en-ca) is a suite of payment APIs that powers commerce for online businesses of all sizes.

## Environment Variables
Add following environemental variables must be set:
  - Stripe test secret key
  - test publishable key
  - endpoint secret
  - price API ID

```bash
$ export STRIPE_PUBLISHABLE_KEY=<YOUR_STRIPE_PUBLISHABLE_KEY>
$ export STRIPE_SECRET_KEY=<YOUR_STRIPE_SECRET_KEY>
$ export STRIPE_PRICE_ID=<YOUR_PRICE_API_ID>
$ export STRIPE_ENDPOINT_SECRET=<YOUR_ENDPOINT_SECRET_KEY>
```



## Database Setup

For this project, Postgres is used as our database. Make sure to download the Postgres [here](https://www.postgresql.org/download/).

#### **Create a database**

```bash
$ createdb gym -U postgres
```

## Config Setting
You may need to provide different postgres database url in ```config.py``` if you used different users, password, or database name. 

```bash
SQLALCHEMY_DATABASE_URI = 'postgres://<USER_NAME>:<PASSWORD>@localhost:<PORT>/<DATABASE_NAME>'
```

## Running the server
From within the `./Mars-Fitness` directory, first ensure that you are working using your created virtual environmentl.

To run the server, first set Flask Environment variables:

```bash
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

and excute:
```bash
$ flask run --reload
```

The ```--reload``` flag will detect file changes and restart the server automatically.

The application will be running on port 5000.
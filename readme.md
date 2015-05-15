###djangobase
[![Build Status](https://img.shields.io/travis/bjacobel/django-base/master.svg?style=flat)](https://travis-ci.org/bjacobel/django-base) [![Coverage Status](https://img.shields.io/coveralls/bjacobel/django-base/master.svg?style=flat)](https://coveralls.io/r/bjacobel/django-base?branch=master)
---


####Setup
You'll need:

- Python 3.4 (2.7 *should* work as well)
- NodeJS >= 0.10
- Postgres
- Vagrant (optional)


1. Install system-level dependencies (you may omit some of these, per guidelines above):

        brew install python3 node vagrant


2. Run the following commands in psql to set up the Postgres database:

        CREATE ROLE djangobase WITH LOGIN CREATEDB PASSWORD 'djangobase';
        CREATE DATABASE djangobase;

3. Install Python dependencies with:

        pip install -r reqs/dev.txt

4. Setup your `ansible/env_vars/secure.yml` file. It contains application secrets and third-party API credentials. An example file with secrets ommitted is at `ansible/env_vars/secure_safe.yml`.

5. Set up the database with:

        python manage.py syncdb

6. Check that setup was successful with:

        python manage.py check

7. Start the local server with:

        python manage.py runserver

####Tests
You can run the project's test suite with:

        python manage.py test

The test suite currently runs against both Python 2.7 and 3.4.

####Deployment
The code base includes Ansible roles for configuring a Linux server and deploying the project onto it.

The following command will execute the complete playbook on all of the hosts defined in `ansible/inventory/prod`:

    ansible-playbook ansible/deploy.yml

For testing purposes, you may use the included Vagrantfile to provision a test VM that approximates the production server. To deploy to Vagrant, run the following:

    vagrant up
    ansible-playbook -i ansible/inventory/vagrant ansible/deploy.yml
    sudo echo "192.168.100.100 djangobase.local" >> /etc/hosts

and visit [http://djangobase.local](http://djangobase.local) in your browser if the deploy is successful.

The project is currently deployed at [djangobase.bjacobel.com](http://djangobase.bjacobel.com).
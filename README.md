<p align="center" style="margin-bottom: 0px !important;">
  <img width="200" src="media/Logo/Blue_Icon.svg" alt="Odyssey Logo" align="center">
</p>
<h1 align="center" style="margin-top: 0px;">Odyssey</h1>

<p align="center" >Modern cloud architecture for hardware production</p>

## Features
- Highly flexible database architecture capable of storing all of your data required for in-series production of any hardware
- Ability to store testing data with specifications
- _Coming Soon:_ Easy to access REST API, giving you the ability to develop custom apps that can interface with the database
- _Coming Soon:_ Ability to store images and documents and link data to them
- _Coming Soon:_ View live data of your production line anywhere with websockets

## Documentation
Full documentation of this prject can now be found on our new [Confluence page]([url](https://halo-engineering.atlassian.net/wiki/spaces/Odyssey/overview?homepageId=229492))!

## Table of Contents
- [Quick Start](#quick-start)
  - [Setting Up Python](#setting-up-python)
  - [Setting Up Postgres in Docker](#setting-up-postgres-in-docker)
  - [Adding Seed Data](#adding-seed-data)
  - [Performing Migrations & Running Odyssey](#performing-migrations--running-odyssey)
- [Documentation](#documentation)
- [Future Related Projects](#future-related-projects)

## Quick Start

This section will give you a brief overview of the commands to set up a local instance of Odyssey running locally on your machine (further details are available in the [documentation](https://github.com/johnhalz/Odyssey/wiki)).

### Setting Up Python
After cloning the repo, run the following commands to set up the virtual environment and install the dependencies:

```shell
pyenv install 3.11.7
poetry config virtualenvs.in-project true
cd <path-to-odyssey-folder>
poetry install
```

### Setting Up Postgres in Docker
Run the following commands to create a new docker container with Postgres:
```shell
docker run --name odyssey -e POSTGRES_PASSWORD=odysseypassword -d -p 5432:5432 postgres
```

### Adding Seed Data
By default, we have included some seed data to help you get started. This data includes unit types, and over 90 physical units with their conversion formulas. Ensure that your docker container is running, then enter the following commands:
```shell
cd <path-to-odyssey-folder>
python manage.py loaddata values_and_units/fixtures/unit_types.json   # Load unit types
python manage.py loaddata values_and_units/fixtures/units.json        # Load units
```

### Performing Migrations & Running Odyssey
You can then perform the migrations in your database and start the service:
```shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

After running the server go to http://127.0.0.1:8000/, and you will see the default django starter page.

To access the admin page, go to http://127.0.0.1:8000/admin. You will need to create a login to be able to login, which you can do by running the command:
```shell
python manage.py createsuperuser
```

which will then prompt you to create a username and password, you will then be able to log into the admin page.

## Documentation
You can find all the documentation for this project [linked here](https://github.com/johnhalz/Odyssey/wiki).

## Future Related Projects
While related projects do not exist yet, a few are in the roadmap:
- Fully capable web interface:
  - Capable of connecting to a cloud-based or local installation of Odyssey.
  - Users can manage saved data and create automations to post-process such data from existing code they already have.
  - Users are capable of viewing live data and controlling test stations as desired.
- Native iOS, iPadOS & Android apps:
  - Capable of connecting to a cloud-based or local installation of Odyssey.
  - Users are able to take images and associate the images with hardware, tests or issues.
  - Users are capable of viewing live data and controlling test stations as desired.

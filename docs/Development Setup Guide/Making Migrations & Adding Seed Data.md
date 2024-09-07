# Making Migrations & Adding Seed Data

## Making Migrations
Now that your database and python environment are setup, you will now need to setup your database with the data models that are defined within the Odyssey project. You can do by simply running the following commands.

!!! note
    Make sure your python virtual environment is activated before running these commands. You can activate the environment by cding into the project folder and running the command:

    ``` bash
    poetry shell
    ```

``` bash
python manage.py makemigrations
python manage.py migrate
```

## Adding Seed Data
To make onboarding easier, we have created seed data to help you get started. This is the case for the unit types, and units themselves. Of course, you can add your own units after the fact in case you need more specialised units for your use case.

You can onboard this data by running the following commands:

``` bash
cd <path-to-odyssey-folder>

# Load the unit types
python manage.py loaddata values_and_units/fixtures/unit_types.json

# Load the units
python manage.py loaddata values_and_units/fixtures/units.json
```

After [setting up a superuser account and accessing the admin page](./Running%20Server%20&%20Creating%20an%20Admin%20Account.md), you will be able to see the [seed data](./Making%20Migrations%20&%20Adding%20Seed%20Data.md) in their respective tables in the admin page.
# Running Server & Creating an Admin Account

## Running Server

You can run the server with the command:

``` sh
python manage.py runserver
```

This command will output the address from which you can access Odyssey on your browser. For local deployments, this will most likely be http://127.0.0.1:8000.

## Creating an Admin Account

To access the admin page on your local deployment, go to http://127.0.0.1:8000/admin. You will need to create a login to be able to login, which you can do by running the command:

``` sh
python manage.py createsuperuser
```

which will then prompt you to create a username and password, you will then be able to log into the admin page.
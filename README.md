An example web app using Django, with TypeScript and Bootstrap.
It provides a simple user interface for collecting tasks from the user and handling them.

To install node dependencies, use
```sh
npm install
```

To compile scripts in `ts_src`, use 
```sh
npm run build
```

Make sure to add a symbolic link `main/static/main/bootstrap`
pointing to `../../../node_modules/bootstrap`.
```sh
ln -s ../../../node_modules/bootstrap main/static/main/bootstrap
```

This example web app requires
```
Name: Django
Version: 5.2.5
```

To initialize a database, use
```sh
python manage.py migrate
```

To start the server, use
```sh
python manage.py runserver
```

To start the task handler (see `main/management/commands/runtaskhandler.py`), use
```sh
python manage.py runtaskhandler
```

For an example of nginx conf, see `nginx_conf_example.txt`.

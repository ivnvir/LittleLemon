- Install mysql using the settings in "settings.py" (default):
    ```
        "HOST": "127.0.0.1",
        "PORT": "3306",
    ```
- Create database as in "settings.py":
    ```
        "NAME": "LittleLemon",
        "USER": "mysql",
        "PASSWORD": "mysql",
    ```

    - Run the mysql commands (inside MySQL shell or MySQL Workbench):
    ```
        CREATE USER 'mysql'@'localhost' IDENTIFIED BY 'mysql';
        GRANT ALL PRIVILEGES ON *.* TO 'mysql'@'localhost';
        CREATE DATABASE LittleLemon;
    ```
- Run:
    pipenv install
- Run **(inside "/littlemon" folder)**:
    ```
        python manage.py makemigrations
        python manage.py makemigrations restaurant
        python manage.py migrate
    ```
- Configure admin's superuser:
    ```
        python manage.py createsuperuser
    ```
- Add data:
    http://127.0.0.1:8000/admin/restaurant/menu/add/

- If you want to run unit tests **(inside "/littlemon" folder)**:
    ```
        python manage.py test
    ```
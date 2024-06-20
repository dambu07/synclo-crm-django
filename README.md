
# ReadMe

pip install virtualenv

python3.10 -m venv myenv

source myenv/bin/activate

pip install -r requirements_local.txt

pip install django

pip install mysqlclient

pip install django-imagekit

brew install mysql

brew services start mysql

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver

MySQL Server Commands
<!-- -- Create a new user -->
CREATE USER 'synclocrm'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

<!-- -- Create a new database -->
CREATE DATABASE synclocrm;

<!-- -- Grant privileges to the new user -->
GRANT ALL PRIVILEGES ON synclocrm. TO 'password'@'localhost';

<!-- -- Flush privileges to apply changes -->
FLUSH PRIVILEGES;

<!-- -- Exit MySQL -->
EXIT;

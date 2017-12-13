Introducir las credenciales de Google Cloud Plarform como variables de entorno.
Ejemplo:
export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

El proyecto está realizado con el framework Django.
Para que funcione en local es necesario instalar un entorno virtual con VirtualEnv e instalar los requisitos del archivo requirements.txt
pip install -r requirements.txt

Posteriormente lanzar las migraciones correspondientes:
python manage.py migrate

Crear un superusuario con:
python manage.py createsuperuser username

Y lanzar el proyecto en local:
python manage.py runserver
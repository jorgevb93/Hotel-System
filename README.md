Hotel System está siendo desarrollado para el hotel Pidgeon Palace Lodge
El proyecto está siendo desarrollado con Django y Python 3.1.4
Puedes aportar ayudando a corregir los errores que actualmente se encuentran en el sistema
Para descarcar y correr el programa debes tener Python 3 instalado o una versión más nueva
Comandos para hacer funcionar el proyecto:

Instalar Django y apps:
pip install Django==3.1.4
pip install django-phonenumber-field[phonenumbers]

Cambia el directorio a Django---Hotel-Management-System-main\Hotel\HMS y abre el shell:
python3 manage.py shell

Ejecutar cada comando uno por uno:
from django.contrib.auth.models import Group, User

from accounts.models import Employee

Group.objects.create(name='admin')

Group.objects.create(name='manager')

Group.objects.create(name='receptionist')

Group.objects.create(name='staff')

Group.objects.create(name='guest')

user = User.createuser=User.objects.create_user('admin', password='admin123')

group = Group.objects.get(name="admin")

user.groups.add(group)

admin = Employee(user=user, salary=0)

admin.save()

Cerrar el shell y setear la base de datos
python3 manage.py makemigrations
python3 manage.py migrate

Iniciar servicio
python3 manage.py runserver

Nota 1: En el programa, hay algunas páginas de pago. No es necesario introducir información real de la tarjeta de crédito. 
La página de pago es sólo para el sistema, no funciona. Sin embargo, después de esta página, un código de verificación se envía 
a la dirección de correo electrónico del usuario.
Nota 2: Sólo puede registrarse como invitado en el sistema. Para agregar empleados (Gerente - Recepcionista - Personal):
Inicie sesión en el sistema con el nombre de usuario: «admin» y la contraseña: «admin123».
Vaya a la página de empleados en las opciones de la barra de navegación.
Haga clic en el botón «Añadir nuevo empleado», rellene el formulario y envíelo.
Verá el mensaje de éxito. A continuación, puede utilizar ese empleado para entrar en el sistema.
Nota 3: Para el sistema de correo electrónico (En algunos casos el sistema envía correos electrónicos):
Vaya al archivo HMS/setting.py
En el archivo de configuración puede encontrar la configuración de correo electrónico, descomentarlos con el fin de cambiar la 
configuración y poner la dirección de correo electrónico que desea utilizar para recibir los rmails del sistema.

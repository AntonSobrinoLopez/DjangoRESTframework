super user asl
password 123

python manage.py createsuperuser --email admin@example.com --username admin

curl -H 'Accept: application/json; indent=4' -u als:123 http://127.0.0.1:8000/users/



1 - Abre tu cuenta de GitHub y haz clic en el botón verde "New" para crear un nuevo repositorio.

2 - Ingresa el nombre que deseas darle a tu repositorio y una breve descripción del mismo. También puedes elegir si quieres que sea público o privado.

3 - No selecciones ninguna opción en "Add a README file", ".gitignore" o "license" ya que tendrás que añadirlos manualmente.

Haz clic en el botón "Create repository".

4 - En la siguiente página, verás la URL del repositorio que acabas de crear. Copia esta URL a tu portapapeles.

Abre una terminal en tu computadora y navega hasta la carpeta que deseas subir al repositorio de GitHub.

Ejecuta el comando "git init" para inicializar un repositorio Git en tu carpeta local.

Ejecuta el comando "git add ." para agregar los archivos de la carpeta al repositorio.

Ejecuta el comando "git commit -m 'Mensaje del commit'" para hacer un commit de los cambios realizados.

Ejecuta el comando "git remote add origin URL_DEL_REPOSITORIO" para agregar la URL del repositorio de GitHub como un control remoto.

Ejecuta el comando "git push -u origin main" para empujar los archivos de tu carpeta al repositorio de GitHub.

Una vez que hayas completado estos pasos, tu repositorio de GitHub debería estar actualizado con la carpeta que acabas de subir. Luego, podrás añadir el archivo README, el archivo .gitignore o una licencia al repositorio manualmente.
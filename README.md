# Repositorio de Pruebas para django AlcVal
Este es un repositorio para hacer **pruebas de desarrollo en django**, es recomendable _crear ramas_ del repositorio y asi garantizar que las pruebas sean independientes y de una vez se vaya aprendiendo a interactuar con la **herramienta Git**.

## Pre-requisitos:
Antes de empezar a usar y hacer pruebas con el Framework de django se deben de considerar los siguientes puntos:

### Instalacion de Python
Descargar e instalar python3 en su ultima version, django soporta python desde la version 3.3. Aqui el enlace --> [descargarlo](https://www.python.org/downloads/)

Al ejecutar el paquete de instalacion de python es **recomendable** marcar/seleccionar la casilla **"[x] Add python.exe to PATH"** y luego elegir la opcion "Install Now" como se muestra en la imagen:

![imagen](https://github.com/jhpetit70/mysite/assets/42259274/283a84e0-0605-49d1-8135-8b93ca942aa7)

Para verficar si python esta operativo en su SO abra una consola y ejecute el siguiente comando:
> python --version

Salida:
> Python 3.9.13

### Entorno virtual en python
Existen varias manera de crear y trabajar **entornos virtuales** en python, una de las mas comunes y sencillas es usando el paquete "virtualenv". Para tener esta utilidad disponible primero debemos instalarla usando el Gestor de paquetes de software escritos en Python llamado "pip" (Python Packege Index). Para vefiricar que pip esta disponible en una consola escriba el siquiente comando:
> pip --version

Salida:
>pip 23.1.2 from C:\Users\"UserName"\AppData\Local\Programs\Python\Python39\lib\site-packages\pip (python 3.9)

De ser necesario y para actualizar el pip se puede usar el comando:
> pip install --upgrade pip install

Luego de comprobar pip y para instalar el paquete virtualenv se usa el siquiente comando:
> pip install virtualenv

> virtualenv --version

### Crear el entonor virtual
Ahora bien, para crear el entonor virtual necesario se debe ingresar en la carpeta del proyecto y una vez dentro de la misma desde una consola se debe ejecuutar el comando:
> virtualenv venv

Donde "vemv" es el nombre que por defecto que se le da a la carpeta donde se crean y copian todos los archivos y paquetes necesarios para que funcione el proyecto, el nombre puede ser cualquiera pero por convencion se usa "venv" o "env".

Listo!!!

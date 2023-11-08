# stateCompany

## Introducción
Este es uno de los dos proyectos realizados para esta prueba, sin la configuración docker compose.

# Descripción Proyecto
An enormous Real Estate company going to require create an API to get in information about 
properties at United States, you must use ER such us next image. Your task it will create follow 
services:

a) Create Property Building

b) Add Image from property

c) Change Price


# Arquitectura del proyecto

- Version python: Python 3.11.5
- Entorno virtual: virtualenv 20.24.6
- Nombre del Proyecto: stateCompany
  - Version FastApi: 0.104.1 
  - pymongo --> base de datos mongo 4.5.0
  - Archivo requirements.txt: Contenido de las librerias utilizadas

$\color{red}{Nota:}$\
   $\color{red}{\  * El\ proyecto\ se\ crea\ con\ una\ base\ de\ datos\ MONGO,\ nombre\ de\ la\ base\ de\ datos\ "state_company"\ sin\ usuario\ y\ contraseña.}$\
   $\color{red}{\  * Se\ crea\ una\ carpeta\ con\ nombre\ mermaiddb,\ la\ cual\ contiene\ el\ MER,\ de\ la\ base\ de\ datos.}$


## *Puesta en marcha del proyecto*
#### PASO 1:
*clonar el proyecto desde https://github.com/edimoredev/state_company*

![image](https://github.com/edimoredev/state_company/assets/125479887/35bd4c4d-537d-42db-a8a4-3502fbfc3327)
#### PASO 2:
*crear el entorno virtual dentro de la carpeta state_company para python 3.11.5*

![image](https://github.com/edimoredev/state_company/assets/125479887/f3facb02-f137-4a9f-8441-cafe8a48eeda)
#### PASO 3:
*Activar entorno virtual*

![image](https://github.com/edimoredev/state_company/assets/125479887/7ab2d8d2-82a3-44ca-9210-0575be5fb1bf)
#### PASO 4:
*Ingresar a la carpeta cd .\backend\app\ y instalar el archivo requirements.txt*

![image](https://github.com/edimoredev/state_company/assets/125479887/f37cf9a3-de8e-43bc-8193-0c6b6fb2620d)
#### PASO 5:
*Instalar MongoDb de manera local, descargando instalador https://www.mongodb.com/try/download/community 
en CMD verificamos la version*

![image](https://github.com/edimoredev/state_company/assets/125479887/5a79f52b-a42b-4052-a75f-a1d2c504a004)
#### PASO 6:
*Activamos MongoDB, con mongod*

![image](https://github.com/edimoredev/state_company/assets/125479887/ad7f0a4c-6730-48e2-b774-f278e323a0ed)
#### PASO 7:
*En el proyecto ejecutamos el uvicorn main*

![image](https://github.com/edimoredev/state_company/assets/125479887/5b09077b-ede1-49d9-b017-57c5822e9545)
#### PASO 8:
*Verificar en el navegador localhost url http://localhost:8000/docs SWAGER*

![image](https://github.com/edimoredev/state_company/assets/125479887/4281fbd5-5c83-4e96-b36f-8b4b30544d77)

*API*
![image](https://github.com/edimoredev/state_company/assets/125479887/3e251b83-0fff-453c-ad7c-445a746ec042)

#### PASO 9:
*Realizamos un metodo POST del collect owner, property, propertyImage, propertyTrace con su respuesta*


![image](https://github.com/edimoredev/state_company/assets/125479887/923f812b-2c64-4a98-bd84-8b8ce4d21e73)

#### PASO 10:
*Realizamos pruebas unitarias, en este caso pytest ejemplo owner*

![image](https://github.com/edimoredev/state_company/assets/125479887/f49cafb7-05b7-4b70-becd-6ef1529fe83b)













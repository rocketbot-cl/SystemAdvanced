



# SystemAdvanced
  
Módulo para extender funcionalidades de la sección Sistema  

*Read this in other languages: [English](Manual_SystemAdvanced.md), [Português](Manual_SystemAdvanced.pr.md), [Español](Manual_SystemAdvanced.es.md)*
  
![banner](imgs/Modulo-System.jpg)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Exportar variables a archivo
  
Exporta variables de Rocketbot a un archivo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo |Ruta y nombre del archivo donde se guardarán las variables|C:/User/Usuario/Folder/file.txt|

### Asignar Multiples Variables
  
Asigna un valor a multiples variables desde un objeto iterable
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Dato |Valor a setear||
|Asignar variables |Variables a setear separadas por coma|var1,var2,var|

### Realizar Backup
  
Crea un nuevo backup
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |

### Limpiar variable(s)
  
Ingrese las variables a limpiar separadas por coma
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Variables|Variables a limpiar|Variable|

### Limpiar variable(s) por categoría
  
Ingrese la categoría de variables a limpiar
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Categoría|Nombre de la categoría a la que pertenecen las variables a limpiar. Puede agregar varias categorías separadas por coma.|Conexión|

### Random
  
Comando para usar librería random
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Seleccione metodo|Metódo de la librería con el cual se trabajará||
|Valor|Argumento para el método (random.randrange(argumento))|5,9|
|Variable|Variable donde se almacenará el resultado|Variable|

### App en Primer Plano
  
Trae una app a primer plano
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de aplicación|Nombre de la aplicación a traer en primer plano|test.xlsx - Excel|

### Obtener Handle de ventanas abiertas
  
Devuelve una lista con tuplas que contienen el nombre y handle de las ventanas abiertas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Variable|Variable donde se almacenará el handle|Variable|

### Contador
  
Devuelve un numero de contador
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Variable|Variable donde se almacenará el número|Variable|

### Obtener Argumentos
  
Obtiene los argumentos previamente dados al iniciar Rocketbot.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Argumentos requeridos|Lista de los argumentos requeridos separados por coma.|['-start', 'id', '-db']|
|Asignar resultado a variable|Variable donde se almacenará el resultado del contador|Variable|

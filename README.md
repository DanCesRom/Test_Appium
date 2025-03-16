# Guía de Instalación y Ejecución para Appium con Python

## Requisitos Previos

Antes de comenzar, asegúrate de tener lo siguiente instalado en tu sistema:

1. **Python 3.x**: Puedes descargarlo desde [python.org](https://www.python.org/downloads/).
2. **Java JDK**: Asegúrate de tener Java JDK instalado. Puedes descargarlo desde [Oracle](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).
3. **Android Studio**: Necesitas Android Studio para crear emuladores y administrar tu dispositivo Android. Puedes descargarlo desde [developer.android.com/studio](https://developer.android.com/studio).
4. **Appium**: Asegúrate de tener Appium instalado. Si no lo tienes, puedes instalarlo usando npm (asegurándote de tener Node.js previamente instalado):
   ```bash
   npm install -g appium

**Paso 1: Configuración del entorno**
1. *Instalar Appium*: Ejecuta el siguiente comando para instalar Appium globalmente:

   ```bash
   npm install -g appium

2. *Instalar Appium-Python-Client*: Este es el cliente de Python para interactuar con Appium.

   ```bash
   pip install Appium-Python-Client

3. *Instalar Selenium*: Appium usa Selenium para interactuar con la interfaz de usuario de la aplicación.

   ```bash
   pip install selenium

4. *Configurar Android Studio y Emulador*:
- Instala Android Studio y configura un emulador de Android siguiendo las instrucciones de la documentación oficial.
- Asegúrate de tener un dispositivo o emulador configurado con un nombre (ej., emulator-5554).


**Paso 2: Configuración de Appium**
Iniciar el servidor de Appium:
Abre una terminal (CMD, PowerShell, o terminal de tu elección) y ejecuta el siguiente comando para iniciar Appium:

bash
Copy code
appium
Esto iniciará el servidor de Appium en el puerto 4723 por defecto. Deja esta terminal abierta mientras trabajas.

Paso 3: Usar Appium Inspector
Abrir Appium Inspector:
Abre Appium Inspector desde el acceso directo en tu computadora (debe haberse instalado automáticamente con Appium).
Conéctate al servidor de Appium en http://127.0.0.1:4723 (puerto por defecto).
Conecta tu dispositivo o emulador Android al inspector, seleccionando el dispositivo adecuado (por ejemplo, emulator-5554).
Una vez conectado, podrás ver y explorar la interfaz de usuario de tu aplicación móvil y obtener los identificadores de los elementos necesarios para el script (como el resource-id, text, etc.).
Paso 4: Ejecutar el Script en Python
Descargar el archivo APK: Asegúrate de tener el archivo APK de la aplicación que deseas probar.

Configurar el script Python:

Descarga el archivo test_script.py (el archivo que contiene el código de prueba automatizado con Appium y Python).
Asegúrate de que el script Python tenga la ruta correcta al archivo APK y a tu emulador/dispositivo Android.
Configuración del script:

Cambia la ruta del APK en el script si es necesario:

python
Copy code
options.app = r"C:\\ruta\\al\\archivo\\PokeApp.apk"
Cambia el nombre del dispositivo o emulador si es necesario:

python
Copy code
options.device_name = "emulator-5554"
Ejecutar el script Python:

Abre una terminal, navega a la carpeta donde está guardado el script y ejecuta:
bash
Copy code
python test_script.py
El script se conectará al servidor de Appium, abrirá la aplicación en el emulador o dispositivo, interactuará con los elementos de la interfaz de usuario, y finalmente tomará una captura de pantalla del resultado.
Paso 5: Verificación y Depuración
Verificar los resultados:

Si todo funciona correctamente, se debería tomar una captura de pantalla llamada appium_test_screenshot.png.
Revisa la captura de pantalla para verificar que el flujo de la prueba se haya realizado correctamente.
Solución de problemas:

Si encuentras algún error en la ejecución, revisa los logs de Appium en la terminal donde ejecutaste appium para obtener detalles sobre el problema.
Asegúrate de que el emulador o dispositivo esté correctamente configurado y conectado.
Paso 6: Cerrar sesión de Appium
Cerrar Appium:
Una vez que la prueba haya terminado, puedes cerrar la sesión de Appium desde la terminal que ejecutaste el servidor con Ctrl + C.
También puedes cerrar el emulador o dispositivo cuando ya no los necesites.
Notas
Compatibilidad de versiones: Asegúrate de que las versiones de Appium, Android Studio, y las dependencias de Python sean compatibles entre sí para evitar problemas de ejecución.
Emulador o Dispositivo Real: Si prefieres usar un dispositivo físico, conecta tu dispositivo Android a tu computadora y habilita la depuración USB en las opciones de desarrollador del dispositivo.
go
Copy code

Este `README.md` cubre todos los pasos necesarios para instalar y ejecutar Appium con Python

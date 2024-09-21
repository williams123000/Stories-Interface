#  🚀 Generador de Historias GUI 🖼️
**Generador de Historias GUI** es una aplicación de escritorio interactiva que te permite crear historias personalizadas a través de una interfaz gráfica amigable y fácil de usar. Ya sea que quieras sumergirte en una emocionante busqueda de tosoro, o tal vez explorar los rincones más oscuros de una historia de secuestro, este generador te ofrece infinitas posibilidades.

¡Déjate llevar por tu imaginación y crea tu propia aventura estelar!

## ✨ Características Principales

- **📢 Narración por Voz:** Activa esta opción para escuchar tu historia a través de una voz sintética que le dará vida a cada palabra.
- **🧠 Potenciación con IA Avanzada:** Si eliges esta opción, la historia será generada con la ayuda de inteligencia artificial avanzada utilizando LM Studio. Esto añade una capa extra de complejidad y creatividad a las narraciones.
- **🎨 Selección de Temas:** Elige entre una variedad de temas para configurar el tipo de historia que deseas vivir. ¿Será un secuestro, una búsqueda de tesoros, o algo completamente inesperado?

## 🛠️ Requisitos del Sistema

Para ejecutar esta aplicación, asegúrate de tener instaladas las siguientes herramientas:
- Python 3.x
- Tkinter: Para la interfaz gráfica de usuario.
- ttk (Themed Tkinter): Para estilos adicionales en la interfaz.
- LM Studio: Si decides potenciar las historias con inteligencia artificial avanzada.

## 🚀 Instalación
Sigue estos pasos para poner en marcha el Generador de Historias GUI en tu máquina local:
```bash
git clone https://github.com/williams123000/Stories-Interface
cd Stories-Interface
pip install -r requirements.txt

```
Instala LM Studio si deseas habilitar la funcionalidad de inteligencia artificial avanzada para la generación de historias.
- Puedes descargar LM Studio desde [LM Studio](https://lmstudio.ai/).

## 🎮 Uso de la Aplicación

Ejecuta la aplicación con el siguiente comando:
```bash
python story_generator_gui.py
```
- Configura tu aventura personalizada utilizando las opciones disponibles en la interfaz. ¡Tú decides la dirección que tomará la historia!

- Haz clic en "Genera tu historia" para obtener una narración única y fascinante creada solo para ti.

- Cada vez que ejecutes un script de historia, se generará un log en la carpeta logs/ con detalles de la historia, la cual estará organizada por fecha y hora de ejecución.

## 🗂️ Estructura del Proyecto

- **story_generator_gui.py:** Contiene la lógica principal de la interfaz gráfica y el flujo de la aplicación.
- **HistoryKidnapping.py:** Script para generar una historia emocionante de secuestro. Al ejecutarlo, se crea un log en logs/ con un registro de la historia generada.
- **HistoryTreasure.py:** Script para generar una historia de exploración y búsqueda de tesoros. También genera un log en la carpeta logs/.
- **Character.json:** Archivo que contiene la estructura de personajes utilizada en las historias de secuestro. Define los atributos y roles de los personajes involucrados.
- **CharacterTreasure.json:** Archivo que contiene la estructura de personajes para las historias de búsqueda del tesoro. Incluye detalles sobre los personajes, sus habilidades, y su relación con la trama.
- **requirements.txt:** Archivo con las dependencias necesarias para el proyecto.

## 🤝 Contribuciones
¡Contribuciones, ideas y mejoras son bienvenidas!
- **Correo Electrónico Personal:** [williamschan72@gmail.com](mailto:williamschan72@gmail.com)
- **Correo Electrónico Institucional:** [williams.chan@cua.uam.mx](mailto:williams.chan@cua.uam.mx)

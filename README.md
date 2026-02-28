
Repositorio del proyecto del Módulo 3.

***

# Sistema de Gestión de Contactos en Python

## Descripción del proyecto

Este proyecto implementa un **Sistema de Gestión de Contactos** en Python, ejecutable por consola, que permite agregar, buscar, editar, eliminar y listar contactos de manera interactiva. El desarrollo se basa en los contenidos del módulo “Fundamentos de programación Python para el análisis de datos”, utilizando variables, estructuras de control, estructuras de datos de colección y programación orientada a objetos. 

Cada contacto almacena información básica:

- Nombre  
- Teléfono  
- Correo electrónico  
- Dirección  

La aplicación busca simular un pequeño sistema de registro, orientado a practicar la construcción de rutinas de baja complejidad con clases y colecciones.
***

## Arquitectura del proyecto

Estructura recomendada del repositorio:

```text
proyecto-contactos/
│
├── main.py
├── modelos.py
├── gestor.py
├── tests/
│   └── test_gestor.py
└── README.md
```

- `modelos.py`: define la clase `Contacto` con sus atributos y su representación legible en texto. 
- `gestor.py`: define la clase `GestorContactos`, encargada de la lógica de negocio (agregar, buscar, editar y eliminar contactos sobre una lista interna). 
- `main.py`: implementa el menú iterativo que interactúa con el usuario mediante entrada por teclado y sentencias condicionales. 
- `tests/test_gestor.py`: contiene las pruebas unitarias básicas para asegurar el correcto funcionamiento del gestor de contactos. 

***

## Requisitos de entorno

- Python 3.8 o superior. 
- Entorno de desarrollo recomendado:
  - Visual Studio Code, Jupyter o Google Colab, según las herramientas vistas en el módulo. 

No se utilizan librerías externas, solo la biblioteca estándar de Python.

***

## Instalación y ejecución en local

1. Clonar el repositorio:

```bash
git clone https://github.com/tu_usuario/proyecto-modulo3-contactos.git
cd proyecto-modulo3-contactos
```

2. (Opcional) Crear y activar un entorno virtual:

```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3. Ejecutar la aplicación:

```bash
python main.py
```

Al ejecutar, se mostrará un menú como el siguiente:

```text
--- Sistema de Gestión de Contactos ---
1. Agregar contacto
2. Buscar contacto
3. Editar contacto
4. Eliminar contacto
5. Mostrar todos
6. Salir
```

***

## Uso de la aplicación

Flujo principal:

1. **Agregar contacto (opción 1)**  
   - Ingresar nombre, teléfono, correo y dirección cuando el sistema lo solicite.  
   - El sistema muestra un mensaje confirmando que el contacto fue agregado.

2. **Buscar contacto (opción 2)**  
   - Ingresar un criterio (parte del nombre o teléfono).  
   - Se listan los contactos que coinciden con ese criterio.

3. **Editar contacto (opción 3)**  
   - Ingresar el índice del contacto según el listado general.  
   - Ingresar los nuevos datos (por ejemplo, nuevo nombre); se actualiza la información en memoria.
     
4. **Eliminar contacto (opción 4)**  
   - Ingresar el índice del contacto que se desea eliminar.  
   - El sistema elimina el contacto de la lista si el índice es válido.

5. **Mostrar todos los contactos (opción 5)**  
   - Se recorre la estructura de datos (lista) y se imprime cada contacto numerado.
     
6. **Salir (opción 6)**  
   - Finaliza el programa y vuelve a la consola del sistema operativo.

***

## Diseño técnico y fundamentos

### Programación orientada a objetos

El proyecto utiliza una clase `Contacto` para encapsular los datos de cada registro (estado/atributos) y una clase `GestorContactos` para modelar el comportamiento asociado a la colección (agregar, buscar, editar, eliminar). Esto aplica los conceptos de clases, objetos, atributos, métodos y encapsulación descritos en la lección 7. 

### Estructuras de datos

- Se utiliza una **lista** para almacenar instancias de `Contacto`, aprovechando su naturaleza ordenada y mutable.
  
### Sentencias condicionales e iterativas

- El menú principal se implementa mediante un bucle `while` y una estructura `if / elif / else` para seleccionar la acción según la opción ingresada.
- El recorrido de la lista de contactos (mostrar todos, buscar, etc.) se realiza con bucles `for`, aplicando los conceptos de sentencias iterativas. 
***

## Pruebas

### Ejecución de pruebas unitarias

Las pruebas unitarias se ubican en la carpeta `tests/` y se ejecutan con:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

Ejemplos de casos cubiertos en `test_gestor.py`:

- Verificar que al agregar un contacto aumente la cantidad total de elementos en la lista.  
- Verificar que la búsqueda por nombre retorne al menos un resultado cuando el contacto existe.  
- Verificar que al eliminar un contacto la lista se actualice correctamente. 

Estas pruebas se diseñan en línea con la importancia de la verificación automática para garantizar la corrección de rutinas de baja complejidad en Python. 

### Pruebas manuales

Además de las pruebas unitarias, se recomienda:

- Probar opciones inválidas en el menú (por ejemplo, letras donde se esperan números) para asegurar que el programa no se detenga abruptamente. 
- Probar flujos completos: agregar → buscar → editar → mostrar → eliminar → salir. 

## Evidencias para la presentación

Para la defensa o presentación final del proyecto se sugiere incluir:

- Capturas de pantalla del menú principal en ejecución.  
- Capturas de la operación de agregado, búsqueda, edición y eliminación de contactos.  
- Captura de la ejecución exitosa de las pruebas unitarias (`OK` en consola). 

Estas evidencias permiten demostrar el cumplimiento de los requisitos funcionales y la aplicación de los contenidos del módulo (estructuras de datos, condicionales, iteraciones y POO). 
***

## Entrega en GitHub / Moodle

1. Asegurar que el repositorio contenga:
   - Código fuente (`main.py`, `modelos.py`, `gestor.py`).  
   - Carpeta `tests/` con las pruebas unitarias.  
   - `README.md` (este documento).  
   - Opcional: carpeta `docs/` con documentación técnica e informe de pruebas en PDF, más la presentación en formato PPTX o PDF. 

2. Subir los cambios al repositorio remoto:

```bash
git add .
git commit -m "Entrega proyecto Módulo 3 - Sistema de contactos"
git push origin main
```

3. Copiar el enlace público del repositorio en GitHub y pegarlo en el espacio de entrega de Moodle, según las instrucciones del proyecto del Módulo 3. 

***

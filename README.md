# Calculadora de Centroide y Momento de Inercia

Este proyecto es una aplicación web diseñada para calcular el centroide y el momento de inercia de sistemas compuestos por múltiples figuras geométricas. Permite al usuario agregar diferentes figuras, definir sus características, y visualizar los resultados de forma gráfica y numérica.

## Tecnologías utilizadas

- HTML
- CSS
- JavaScript (sin frameworks)
- Canvas para dibujo en el plano cartesiano

## Funcionalidades principales

- Selección de figuras geométricas básicas:
  - Círculo
  - Semicírculo
  - Cuarto de círculo
  - Rectángulo
  - Triángulo equilátero
  - Triángulo rectángulo

- Personalización de parámetros:
  - Dimensiones (radio, base, altura, etc.)
  - Posición en el eje X y Y
  - Dirección o cuadrante (para figuras como semicírculo y cuarto de círculo)
  - Tipo de figura (maciza o hueca)

- Configuración del sistema:
  - Definición de los límites del plano cartesiano
  - Elección del eje para el cálculo del momento de inercia (centroide o esquina izquierda)

- Dibujo automático en el plano, adaptado a escala
- Posibilidad de agregar múltiples figuras y eliminar figuras individuales o limpiar todo el sistema
- Visualización del centroide total del sistema compuesto
- Cálculo del área total, centroide compuesto, y momento de inercia total respecto al eje seleccionado

## Cómo utilizar

1. Abrir el archivo `index.html` en cualquier navegador moderno.
2. Definir los valores máximos de X y Y para establecer el tamaño del plano.
3. Seleccionar una figura y completar los campos requeridos.
4. Presionar el botón “Dibujar Figura” para agregarla al sistema.
5. Repetir el proceso para añadir más figuras si se desea.
6. Introducir el punto de referencia y seleccionar el eje para calcular el momento de inercia.
7. Hacer clic en “Calcular Centroide y Momento de Inercia” para mostrar los resultados.

## Consideraciones

- Las unidades son relativas al sistema definido por el usuario.
- Las figuras huecas restan su contribución del centroide y momento de inercia totales.
- El plano cartesiano es generado dinámicamente según los valores máximos de X y Y indicados.

## Posibles mejoras

- Agregar nuevas figuras geométricas
- Permitir exportar los resultados en PDF o CSV
- Añadir interfaz más amigable con librerías externas
- Guardar y cargar configuraciones previas

## Autor

Julio Lara – Proyecto académico para la materia de Herramientas de Programación 4.

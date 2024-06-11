import math
import tkinter as tk
from tkinter import ttk

# Funciones para calcular centroides
def centroide_triangulo(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    xc = (x1 + x2 + x3) / 3
    yc = (y1 + y2 + y3) / 3
    return xc, yc, area

def centroide_rectangulo(x1, y1, x2, y2):
    xc = (x1 + x2) / 2
    yc = (y1 + y2) / 2
    area = abs(x2 - x1) * abs(y2 - y1)
    return xc, yc, area

def centroide_circulo(x, y, r):
    xc = x
    yc = y
    area = math.pi * r**2
    return xc, yc, area

# Funciones para calcular momentos de inercia
def momento_inercia_triangulo(x1, y1, x2, y2, x3, y3):
    area = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
    Ix = area * (y1**2 + y1*y2 + y2**2 + y1*y3 + y2*y3 + y3**2) / 36
    Iy = area * (x1**2 + x1*x2 + x2**2 + x1*x3 + x2*x3 + x3**2) / 36
    return Ix, Iy

def momento_inercia_rectangulo(x1, y1, x2, y2):
    b = abs(x2 - x1)
    h = abs(y2 - y1)
    Ix = b * h**3 / 12
    Iy = h * b**3 / 12
    return Ix, Iy

def momento_inercia_circulo(r):
    Ix = Iy = math.pi * r**4 / 4
    return Ix, Iy

# Interfaz gráfica de usuario
root = tk.Tk()
root.title("Cálculo de Centroides y Momentos de Inercia")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", padx=10, pady=10)

# Pestaña para triángulos
triangulo_frame = ttk.Frame(notebook)
notebook.add(triangulo_frame, text="Triángulo")

triangulo_labels = ["x1", "y1", "x2", "y2", "x3", "y3"]
triangulo_entries = []
for i, label in enumerate(triangulo_labels):
    label_widget = ttk.Label(triangulo_frame, text=label)
    label_widget.grid(row=i, column=0, padx=5, pady=5)
    entry_widget = ttk.Entry(triangulo_frame)
    entry_widget.grid(row=i, column=1, padx=5, pady=5)
    triangulo_entries.append(entry_widget)

def calcular_triangulo():
    x1 = float(triangulo_entries[0].get())
    y1 = float(triangulo_entries[1].get())
    x2 = float(triangulo_entries[2].get())
    y2 = float(triangulo_entries[3].get())
    x3 = float(triangulo_entries[4].get())
    y3 = float(triangulo_entries[5].get())

    xc, yc, area = centroide_triangulo(x1, y1, x2, y2, x3, y3)
    Ix, Iy = momento_inercia_triangulo(x1, y1, x2, y2, x3, y3)

    resultado_label.config(text=f"Centroide: ({xc:.2f}, {yc:.2f})\nÁrea: {area:.2f}\nIx: {Ix:.2f}\nIy: {Iy:.2f}")

calcular_boton = ttk.Button(triangulo_frame, text="Calcular", command=calcular_triangulo)
calcular_boton.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

resultado_label = ttk.Label(triangulo_frame, text="")
resultado_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

# Pestaña para rectángulos
rectangulo_frame = ttk.Frame(notebook)
notebook.add(rectangulo_frame, text="Rectángulo")

rectangulo_labels = ["x1", "y1", "x2", "y2"]
rectangulo_entries = []
for i, label in enumerate(rectangulo_labels):
    label_widget = ttk.Label(rectangulo_frame, text=label)
    label_widget.grid(row=i, column=0, padx=5, pady=5)
    entry_widget = ttk.Entry(rectangulo_frame)
    entry_widget.grid(row=i, column=1, padx=5, pady=5)
    rectangulo_entries.append(entry_widget)

def calcular_rectangulo():
    x1 = float(rectangulo_entries[0].get())
    y1 = float(rectangulo_entries[1].get())
    x2 = float(rectangulo_entries[2].get())
    y2 = float(rectangulo_entries[3].get())

    xc, yc, area = centroide_rectangulo(x1, y1, x2, y2)
    Ix, Iy = momento_inercia_rectangulo(x1, y1, x2, y2)

    resultado_label.config(text=f"Centroide: ({xc:.2f}, {yc:.2f})\nÁrea: {area:.2f}\nIx: {Ix:.2f}\nIy: {Iy:.2f}")

calcular_boton = ttk.Button(rectangulo_frame, text="Calcular", command=calcular_rectangulo)
calcular_boton.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

resultado_label = ttk.Label(rectangulo_frame, text="")
resultado_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Pestaña para círculos
circulo_frame = ttk.Frame(notebook)
notebook.add(circulo_frame, text="Círculo")

circulo_labels = ["x", "y", "r"]
circulo_entries = []
for i, label in enumerate(circulo_labels):
    label_widget = ttk.Label(circulo_frame, text=label)
    label_widget.grid(row=i, column=0, padx=5, pady=5)
    entry_widget = ttk.Entry(circulo_frame)
    entry_widget.grid(row=i, column=1, padx=5, pady=5)
    circulo_entries.append(entry_widget)

def calcular_circulo():
    x = float(circulo_entries[0].get())
    y = float(circulo_entries[1].get())
    r = float(circulo_entries[2].get())

    xc, yc, area = centroide_circulo(x, y, r)
    Ix, Iy = momento_inercia_circulo(r)

    resultado_label.config(text=f"Centroide: ({xc:.2f}, {yc:.2f})\nÁrea: {area:.2f}\nIx: {Ix:.2f}\nIy: {Iy:.2f}")

calcular_boton = ttk.Button(circulo_frame, text="Calcular", command=calcular_circulo)
calcular_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

resultado_label = ttk.Label(circulo_frame, text="")
resultado_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Pestaña para dibujar figuras
dibujo_frame = ttk.Frame(notebook)
notebook.add(dibujo_frame, text="Dibujo")

# Crear un canvas
canvas = tk.Canvas(dibujo_frame, width=500, height=500)
canvas.pack()

# Cuadrado delimitador
cuadrado_delimitador = canvas.create_rectangle(50, 50, 450, 450, outline="black")

# Lista para guardar las posiciones de los clicks
clicks = []

# Lista de tipos de figuras
figuras = ["Rectángulo", "Círculo", "Semicírculo"]

# Crear un StringVar para guardar la figura seleccionada
figura_seleccionada = tk.StringVar()
figura_seleccionada.set(figuras[0])  # valor por defecto

# Crear el menú desplegable
menu_figuras = ttk.OptionMenu(dibujo_frame, figura_seleccionada, *figuras)
menu_figuras.pack()

# Crear una opción para huecos
hueco_var = tk.BooleanVar()
hueco_checkbox = ttk.Checkbutton(dibujo_frame, text="Hueco", variable=hueco_var)
hueco_checkbox.pack()

# Crear una opción para la orientación del semicírculo
orientacion_semicirculo = tk.StringVar()
orientacion_semicirculo.set("arriba")  # valor por defecto
orientacion_label = ttk.Label(dibujo_frame, text="Orientación del semicírculo:")
orientacion_label.pack()
orientacion_opciones = ttk.OptionMenu(dibujo_frame, orientacion_semicirculo, "arriba", "abajo", "izquierda", "derecha")
orientacion_opciones.pack()

def centroide_figura(x1, y1, x2, y2, figura, hueco):
    if figura == "Rectángulo":
        # Para un rectángulo, el centroide es el punto medio
        xc = (x1 + x2) / 2
        yc = (y1 + y2) / 2
        area = abs(x2 - x1) * abs(y2 - y1) if not hueco else 0
    elif figura == "Círculo":
        # Para un círculo, el centroide es el centro
        xc = (x1 + x2) / 2
        yc = (y1 + y2) / 2
        radio = abs(x2 - x1) / 2
        area = math.pi * radio ** 2 if not hueco else 0
    elif figura == "Semicírculo":
        # Para un semicírculo, el centroide no está en el centro
        xc = (x1 + x2) / 2
        yc = (y1 + y2) / 2 + 4 * (x2 - x1) / (3 * math.pi)
        radio = abs(x2 - x1) / 2
        area = 0.5 * math.pi * radio ** 2 if not hueco else 0
    else:
        raise ValueError(f"Figura desconocida: {figura}")

    return xc, yc, area

def momento_inercia_figura(x1, y1, x2, y2, figura, hueco):
    if figura == "Rectángulo":
        base = abs(x2 - x1)
        altura = abs(y2 - y1)
        Ix = (base * altura ** 3) / 12 if not hueco else 0
        Iy = (altura * base ** 3) / 12 if not hueco else 0
    elif figura == "Círculo":
        radio = abs(x2 - x1) / 2
        Ix = (math.pi * radio ** 4) / 4 if not hueco else 0
        Iy = Ix
    elif figura == "Semicírculo":
        radio = abs(x2 - x1) / 2
        Ix = (math.pi * radio ** 4) / 8 if not hueco else 0
        Iy = (2 * math.pi * radio ** 4) / 3 if not hueco else 0
    else:
        raise ValueError(f"Figura desconocida: {figura}")

    return Ix, Iy

def on_click(event):
    # Comprobar si el clic está dentro del cuadrado delimitador
    if 50 <= event.x <= 450:
        # Guardar la posición del click
        clicks.append((event.x, event.y))

        # Si ya se han hecho dos clicks, dibujar la figura seleccionada
        if len(clicks) == 2:
            x1, y1 = clicks[0]
            x2, y2 = clicks[1]

            hueco = hueco_var.get()
            orientacion = orientacion_semicirculo.get()

            if figura_seleccionada.get() == "Rectángulo":
                if hueco:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")
                else:
                    canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
            elif figura_seleccionada.get() == "Círculo":
                if hueco:
                    canvas.create_oval(x1, y1, x2, y2, fill="black", outline="black")
                else:
                    canvas.create_oval(x1, y1, x2, y2, fill="white", outline="black")
            elif figura_seleccionada.get() == "Semicírculo":
                # Dibujar un semicírculo con la orientación seleccionada
                if hueco:
                    if orientacion == "arriba":
                        canvas.create_arc(x1, y1, x2, y2, start=0, extent=180, fill="black", outline="black")
                    elif orientacion == "abajo":
                        canvas.create_arc(x1, y2, x2, y1, start=180, extent=180, fill="black", outline="black")
                    elif orientacion == "izquierda":
                        canvas.create_arc(x1, y1, x2, y2, start=90, extent=180, fill="black", outline="black")
                    elif orientacion == "derecha":
                        canvas.create_arc(x1, y2, x2, y1, start=270, extent=180, fill="black", outline="black")
                else:
                    if orientacion == "arriba":
                        canvas.create_arc(x1, y1, x2, y2, start=0, extent=180, fill="white", outline="black")
                    elif orientacion == "abajo":
                        canvas.create_arc(x1, y2, x2, y1, start=180, extent=180, fill="white", outline="black")
                    elif orientacion == "izquierda":
                        canvas.create_arc(x1, y1, x2, y2, start=90, extent=180, fill="white", outline="black")
                    elif orientacion == "derecha":
                        canvas.create_arc(x1, y2, x2, y1, start=270, extent=180, fill="white", outline="black")

            # Calcular las propiedades y mostrarlas
            xc, yc, area = centroide_figura(x1, y1, x2, y2, figura_seleccionada.get(), hueco)
            Ix, Iy = momento_inercia_figura(x1, y1, x2, y2, figura_seleccionada.get(), hueco)
            resultado_label.config(text=f"Centroide: ({xc:.2f}, {yc:.2f})\nÁrea: {area:.2f}\nIx: {Ix:.2f}\nIy: {Iy:.2f}")

            # Vaciar la lista clicks después de dibujar y calcular las propiedades
            clicks.clear()
    else:
        # Si el clic está fuera del cuadrado delimitador, no hacer nada
        pass


# Registrar el evento de click
canvas.bind("<Button-1>", on_click)

resultado_label = ttk.Label(dibujo_frame, text="")
resultado_label.pack(padx=5, pady=5)

root.mainloop()
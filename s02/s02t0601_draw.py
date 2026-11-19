# Importando la clase Stack desde el módulo s02t0502_stacks
from s02t0502_stacks import Stack
import tkinter as tk

class DrawApp:
  def __init__(self, window):
    self.window = window
    self.window.title("Dibujando con stacks")
    # Variables para el seguimiento del dibujo
    self.current_color = "black"
    self.previous_x = None
    self.previous_y = None

    # Creando el canvas donde se dibujará
    self.canvas = tk.Canvas(
      self.window,
      width=700,
      height=450,
      bg="white")
    
    # pack organiza los widgets dentro del contenedor; 
    # por defecto, los acomoda de arriba hacia abajo.
    self.canvas.pack(padx=10, pady=10)

    # Agregando los eventos
    self.canvas.bind("<ButtonPress-1>", self.start_stroke)
    self.canvas.bind("<B1-Motion>", self.draw_stroke)
    self.canvas.bind("<ButtonRelease-1>", self.end_stroke)

if __name__ == "__main__":
  # Creando el contexto grafico de dibujo
  window = tk.Tk()
  # Pasando el contexto gragico a la app
  app = DrawApp(window)
  # Lanzamos el loop principal de la aplicación
  app.window.mainloop()
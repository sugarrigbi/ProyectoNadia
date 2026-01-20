import tkinter as tk

# Crear la ventana principal
root = tk.Tk()

# Crear un botón para cerrar la ventana
close_button = tk.Button(root, text="Cerrar ventana", command=root.destroy)
close_button.pack()

root.mainloop()
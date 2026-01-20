from customtkinter import *

root = CTk()
root.title("Todos los Objetos")
root.geometry("1000x1000")

CasillaTexto2 = CTkLabel(root, text="Esto es un TextBox ↓")
CasillaTexto2.place(relx=0.1, rely=0.01, anchor="center")
CasillaTexto = CTkTextbox(root)
CasillaTexto.place(relx=0.1, rely=0.12, anchor="center")

Boton = CTkButton(root, text="Esto es un Button")
Boton.place(relx=0.27, rely=0.02, anchor="center")

checkbox = CTkCheckBox(root, text="Esto es una CheckBox")
checkbox.place(relx=0.28, rely=0.05, anchor="center")

Combo = CTkComboBox(root, width=170, values=["Esto es una ComboBox","Sebastian", "Karoll", "Steven", "Nadia"])
Combo.place(relx=0.285, rely=0.08, anchor="center")

entry = CTkEntry(root, placeholder_text="Esto es una Entry ")
entry.place(relx=0.27, rely=0.11, anchor="center")

FrameText = CTkLabel(root, text="Esto es un frame ↓")
FrameText.place(relx=0.1, rely=0.24, anchor="center")
Frame = CTkFrame(root, fg_color="White")
Frame.place(relx=0.1, rely=0.35, anchor="center")

Label = CTkLabel(root, text="Esto es un Label")
Label.place(relx=0.27, rely=0.14, anchor="center")

Option = CTkOptionMenu(root, values=["Esto es un OptionMenu","Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"])
Option.place(relx=0.286, rely=0.17, anchor="center")

ProgresoText = CTkLabel(root, text="Esto es una ProgressBar ↓")
ProgresoText.place(relx=0.29, rely=0.20, anchor="center")
Progreso = CTkProgressBar(root)
Progreso.place(relx=0.298, rely=0.22, anchor="center")
Progreso.set(0.1)

Radiobutton = CTkRadioButton(root, text="Esto es un RadioButton")
Radiobutton.place(relx=0.298, rely=0.25, anchor="center")

ScrollableFrameText = CTkLabel(root, text="Esto es un Scrollableframe ↓")
ScrollableFrameText.place(relx=0.1, rely=0.47, anchor="center")
ScrollableFrame = CTkScrollableFrame(root, fg_color="white")
ScrollableFrame.place(relx=0.1, rely=0.59, anchor="center")

scrollbarText = CTkLabel(root, text="Esto es un Scrollbar ↓")
scrollbarText.place(relx=0.278, rely=0.28, anchor="center")
scrollbar = CTkScrollbar(root, orientation=HORIZONTAL)
scrollbar.place(relx=0.32, rely=0.3, anchor="center")

SecmentText = CTkLabel(root, text="Esto es un SegmentedButton ↓")
SecmentText.place(relx=0.305, rely=0.33, anchor="center")
Secment = CTkSegmentedButton(root, values=["1", "2", "3", "4", "5"])
Secment.place(relx=0.286, rely=0.36, anchor="center")

sliderText = CTkLabel(root, text="Esto es un slider ↓")
sliderText.place(relx=0.278, rely=0.39, anchor="center")
slider = CTkSlider(root)
slider.place(relx=0.31, rely=0.41, anchor="center")

swith = CTkSwitch(root, text="Esto es un swith")
swith.place(relx=0.28, rely=0.44, anchor="center")

#===================TAB================
tabview = CTkTabview(master=root)
tabview.place(relx=0.6, rely=0.12, anchor="center")

tabview.add("Esto es un Tab1") 
tabview.add("Esto es un Tab2")  
tabview.set("Esto es un Tab2")  

button = CTkButton(master=tabview.tab("Esto es un Tab1"), text="boton Tab1")
button.pack(padx=20, pady=20)

button2 = CTkButton(master=tabview.tab("Esto es un Tab2"), text="boton Tab2")
button2.pack(padx=20, pady=20)
#===================TAB================

root.mainloop()
from tkinter import *
from customtkinter import *
import customtkinter
from FInalWork import *
from PIL import ImageGrab

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Kuhinja")
root.geometry("1200x600")

options = []
for x in a.recepti:
    options.append(x["recept"])

l_0 = customtkinter.CTkLabel(root, text="PONEDELJAK", font=(
    "Helvetica", 22, "bold")).place(relx=0.12, rely=0.02, anchor=customtkinter.N)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
l_1 = customtkinter.CTkLabel(root, text="DORUCAK", font=("Helvetica", 12, "bold")).place(
    relx=0.12, rely=0.1, anchor=customtkinter.N)
combobox1 = customtkinter.CTkComboBox(
    master=root, values=options, variable="", width=280)
combobox1.place(relx=0.12, rely=0.15, anchor=customtkinter.N)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
l_2 = customtkinter.CTkLabel(root, text="RUCAK", font=("Helvetica", 12, "bold")).place(
    relx=0.12, rely=0.25, anchor=customtkinter.N)
combobox2 = customtkinter.CTkComboBox(
    master=root, values=options, variable="", width=280)
combobox2.place(relx=0.12, rely=0.3, anchor=customtkinter.N)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
l_3 = customtkinter.CTkLabel(root, text="VECERA", font=("Helvetica", 12, "bold")).place(
    relx=0.12, rely=0.4, anchor=customtkinter.N)
combobox3 = customtkinter.CTkComboBox(
    master=root, values=options, variable="", width=280)
combobox3.place(relx=0.12, rely=0.45, anchor=customtkinter.N)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------#


def Dodaj_recept():

    t = CTkToplevel(root)
    t.geometry("300x600")

 
    def add_entry():
        l3_t = customtkinter.CTkLabel(t, text="Ime sastojka")
        l3_t.pack()

        new_e1_t = customtkinter.CTkEntry(t, placeholder_text="")
        new_e1_t.pack()

        l4_t = customtkinter.CTkLabel(t, text="Kolicina")
        l4_t.pack()

        new_e2_t = customtkinter.CTkEntry(t, placeholder_text="")
        new_e2_t.pack()

        new_combobox_unit = customtkinter.CTkComboBox(t, values=["kom","kg","dl"], variable="", width=150)
        new_combobox_unit.pack()

        entries.append((new_e1_t, new_e2_t,new_combobox_unit))

    def get_kwargs():
        kwargs = {}
        #lista = []
        for entry_pair in entries:
            key = entry_pair[0].get()
            #lista.append(entry_pair[1].get())
            #lista.append(entry_pair[2].get())
            value = (entry_pair[1].get() + "," +entry_pair[2].get()).split(",")
            if key and value:
                kwargs[key] = []
                kwargs[key].append(value)
                kwargs[key] = kwargs[key][0]

        return kwargs

    b = customtkinter.CTkButton(t, text="Dodaj recept", command=lambda: a.dodaj_recept(
        recept=e_t.get(), **get_kwargs()))
    b.pack()

    add_entry_button = customtkinter.CTkButton(
        t, text="Dodaj novi sastojak", command=add_entry)
    add_entry_button.pack(pady=10)

    l1 = customtkinter.CTkLabel(t, text="")
    l1.pack()

    l_t = customtkinter.CTkLabel(t, text="Recept")
    l_t.pack()

    e_t = customtkinter.CTkEntry(t, placeholder_text="")
    e_t.pack()

    l1_t = customtkinter.CTkLabel(t, text="Ime sastojka")
    l1_t.pack()

    e1_t = customtkinter.CTkEntry(t, placeholder_text="")
    e1_t.pack()

    l2_t = customtkinter.CTkLabel(t, text="Kolicina")
    l2_t.pack()

    e2_t = customtkinter.CTkEntry(t, placeholder_text="")
    e2_t.pack()

    combobox_unit = customtkinter.CTkComboBox(t, values=["kom","kg","dl"], variable="", width=150)
    combobox_unit.pack()

    entries = [(e1_t, e2_t, combobox_unit)]


def dodaj_zacin():

    t1 = CTkToplevel(root)
    t1.geometry("300x450")

    l_1 = customtkinter.CTkLabel(t1, text="Naziv namirnice").pack()

    e_1 = customtkinter.CTkEntry(t1, placeholder_text="")
    e_1.pack()

    l_2 = customtkinter.CTkLabel(t1, text="kolicina").pack()

    e_2 = customtkinter.CTkEntry(t1, placeholder_text="")
    e_2.pack()

    l_3 = customtkinter.CTkLabel(t1, text="proteini").pack()

    e_3 = customtkinter.CTkEntry(t1, placeholder_text="")
    e_3.pack()

    l_4 = customtkinter.CTkLabel(t1, text="hidrati").pack()

    e_4 = customtkinter.CTkEntry(t1, placeholder_text="")
    e_4.pack()

    l_5 = customtkinter.CTkLabel(t1, text="masti").pack()

    e_5 = customtkinter.CTkEntry(t1, placeholder_text="")
    e_5.pack()

    l_6 = customtkinter.CTkLabel(t1, text="kalorije").pack()

    e_6 = customtkinter.CTkEntry(t1, placeholder_text="")
    e_6.pack()

    b_1 = customtkinter.CTkButton(t1, text="Dodaj zacin",  command=lambda: [l_7.configure(
        text=a.dodaj_zacin(e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get()))])
    b_1.pack(pady=7)

    l_7 = customtkinter.CTkLabel(t1, text="")
    l_7.pack()


def obrisi_recept():
    t2 = CTkToplevel(root)
    t2.geometry("300x450")

    options = []
    for x in a.recepti:
        options.append(x["recept"])

    l_t2 = customtkinter.CTkLabel(t2, text="")
    l_t2.pack()

    selected_option = StringVar(t2)
    selected_option.set("")
    option_menu = OptionMenu(t2, selected_option, *options)
    option_menu.pack()

    b_t2 = customtkinter.CTkButton(t2, text="Obrisi recept", command=lambda: l_t2.configure(
        text=a.obrisi_recept(jelo=selected_option.get())))
    b_t2.pack()


menubar = Menu(master=root)

accountmenu = Menu(menubar, tearoff=0)
middlemenu = Menu(menubar, tearoff=0)
exitmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Admin", menu=accountmenu)
accountmenu.add_command(label="Dodaj recept", command=lambda: Dodaj_recept())
accountmenu.add_command(label="Dodaj zacin", command=lambda: dodaj_zacin())
accountmenu.add_command(label="Obrisi recept", command=lambda: obrisi_recept())


menubar.add_command(label="Napravi spisak", command=lambda: [(a.spisak_za_kupovinu(a.odaberi_dorucak(combobox1.get()))),
                                                             (a.spisak_za_kupovinu(
                                                                 a.odaberi_rucak(combobox2.get()))),
                                                             (a.spisak_za_kupovinu(a.odaberi_veceru(combobox3.get()))), (a.stampaj())])


menubar.add_cascade(label="Exit", menu=exitmenu)
exitmenu.add_command(label="Exit", command=root.destroy)

root.configure(menu=menubar)


b_1 = customtkinter.CTkButton(root, text="Print Screenshot")


def print_screenshot():

    x = root.winfo_rootx()
    y = root.winfo_rooty()
    w = root.winfo_width()
    h = root.winfo_height()

    screenshot = ImageGrab.grab(bbox=(x, y, x+w, y+h))

    screenshot.show()
    screenshot.save("screenshot.png")


b_1.configure(command=print_screenshot)
b_1.place(relx=0.85, rely=0.90)

root.mainloop()

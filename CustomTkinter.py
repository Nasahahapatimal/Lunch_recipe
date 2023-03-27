from tkinter import *
from customtkinter import *
import customtkinter
from FInalWork import *
from PIL import ImageGrab


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Kuhinja")
root.geometry("450x600")


options = []
for x in a.recepti:
    options.append(x["recept"])

l_0 = customtkinter.CTkLabel(root, text="PONEDELJAK").grid(
    row=0, column=0, padx=0, pady=5)

l_1 = customtkinter.CTkLabel(root, text="DORUCAK").grid(
    row=1, column=0, padx=2, pady=2)
l_2 = customtkinter.CTkLabel(root, text="---")
l_2.grid(row=3, column=0, padx=2, pady=2)
selected_option = StringVar(root)
selected_option.set("")
option_menu = OptionMenu(root, selected_option, *options)
option_menu.grid(row=3, column=1, padx=15, pady=2)
b = customtkinter.CTkButton(root, text="Odaberi dorucak", command=lambda: [(
    l_2.configure(text=a.odaberi_dorucak(dorucak=selected_option.get()))), selected_option.set("Bon Apetit :)")])
b.grid(row=4, column=0, padx=2, pady=2)


l_3 = customtkinter.CTkLabel(root, text="RUCAK").grid(
    row=5, column=0, padx=2, pady=25)
l_4 = customtkinter.CTkLabel(root, text="---")
l_4.grid(row=6, column=0, padx=2, pady=2)
b_1 = customtkinter.CTkButton(root, text="Odaberi rucak", command=lambda: [(
    l_4.configure(text=a.odaberi_rucak(rucak=selected_option1.get()))), selected_option1.set("Bon Apetit :)")])
b_1.grid(row=7, column=0, padx=2, pady=2)
selected_option1 = StringVar(root)
selected_option1.set("")
option_menu = OptionMenu(root, selected_option1, *options)
option_menu.grid(row=6, column=1, padx=15, pady=2)

l_5 = customtkinter.CTkLabel(root, text="VECERA").grid(
    row=8, column=0, padx=2, pady=25)
l_6 = customtkinter.CTkLabel(root, text="---")
l_6.grid(row=9, column=0, padx=2, pady=2)
b_2 = customtkinter.CTkButton(root, text="Odaberi veceru", command=lambda: [(
    l_6.configure(text=a.odaberi_veceru(vecera=selected_option2.get()))), selected_option2.set("Bon Apetit :)")])
b_2.grid(row=10, column=0, padx=2, pady=2)
selected_option2 = StringVar(root)
selected_option2.set("")
option_menu = OptionMenu(root, selected_option2, *options)
option_menu.grid(row=9, column=1, padx=15, pady=2)


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

        entries.append((new_e1_t, new_e2_t))

    def get_kwargs():
        kwargs = {}
        for entry_pair in entries:
            key = entry_pair[0].get()
            value = entry_pair[1].get()
            if key and value:
                kwargs[key] = value
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

    entries = [(e1_t, e2_t)]


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


menubar.add_command(label="Napravi spisak", command=lambda: [(a.spisak_za_kupovinu(a.odaberi_dorucak(l_2.cget("text")))),
                                                             (a.spisak_za_kupovinu(
                                                                 a.odaberi_rucak(l_4.cget("text")))),
                                                             (a.spisak_za_kupovinu(a.odaberi_veceru(l_6.cget("text")))), (a.stampaj())])


menubar.add_cascade(label="Exit", menu=exitmenu)
exitmenu.add_command(label="Exit", command=root.destroy)

root.configure(menu=menubar)


b_1 = Button(root, text="Print Screenshot")


def print_screenshot():

    x = root.winfo_rootx()
    y = root.winfo_rooty()
    w = root.winfo_width()
    h = root.winfo_height()

    screenshot = ImageGrab.grab(bbox=(x, y, x+w, y+h))

    screenshot.show()
    screenshot.save("screenshot.png")


b_1.config(command=print_screenshot)
b_1.grid(row=10, column=10, padx=2, pady=2)

root.mainloop()

import json


class Namirnica:

    def __init__(self, namirnica, kolicina, proteini, hidrati, masti, kalorije):

        self.namirnica = namirnica
        self.kolicina = kolicina
        self.proteini = proteini
        self.hidrati = hidrati
        self.masti = masti
        self.kalorije = kalorije

    def __str__(self):

        return("{}|{}|{}|{}|{}|{}".format(self.namirnica, self.kolicina, self.proteini, self.hidrati, self.masti, self.kalorije))


class Kuhinja:

    def __init__(self):

        self.namirnice = []
        self.recepti = []
        self.output = {}

    def ucitaj_namirnice(self):

        x = [l.strip() for l in open("kalorije.txt")]

        for nm in x:

            namirnica = nm.split("|")[0]
            kolicina = nm.split("|")[1]
            proteini = nm.split("|")[2]
            hidrati = nm.split("|")[3]
            masti = nm.split("|")[4]
            kalorije = nm.split("|")[5]

            proizvod = Namirnica(namirnica, kolicina,
                                 proteini, hidrati, masti, kalorije)
            self.namirnice.append(proizvod)

    def ucitaj_recepte(self):

        with open("recepti.txt", "r") as f:
            # Initialize an empty list to store the dictionaries
            # Read each line of the file
            for line in f:
                # Load the dictionary from the line and append it to the list
                recipe = json.loads(line.strip())
                self.recepti.append(recipe)

    def ocitaj_kalorije(self, nammm):

        for nm in self.namirnice:
            if nammm.lower() == nm.namirnica.lower():
                return(nm.kalorije)
        return ("Ne postoji uneta namirnica")

    def kalorijska_vrednost(self, naziv_recepta):

        kalorije = 0

        for x in self.recepti:
            if naziv_recepta.lower() == x["recept"].lower():
                for y in self.namirnice:
                    if y.namirnica.lower() in x:
                        if y.kolicina == "komad":
                            kalorije = kalorije + \
                                float(x[y.namirnica.lower()])*float(y.kalorije)
                        else:
                            kalorije = kalorije + \
                                float(x[y.namirnica.lower()]) / \
                                100*(float(y.kalorije))

        if kalorije > 0:
            return ("Ukupna vrednost kalorija za odabrani recept {} je {}".format(naziv_recepta, kalorije))
        return ("Ne postoji uneti recept!")

    def dodaj_recept(self, **kwargs):

        result = {**kwargs}
        result = {k: v for k, v in result.items() if v != "" or k != ""}

        # dodaj ""edge case"" ako je recept = "" ili sastojan "str"

        for recept in self.recepti:
            if (kwargs["recept"]) == recept["recept"]:
                return ("Već postoji uneti recept")

        if result == {} or "recept" not in result or len(result) == 1:
            return
        else:
            self.recepti.append(result)
            self.update_file_recepti()
            return ("Uspesno dodat novi recept!")

    def obrisi_recept(self, jelo=""):
        for recept in self.recepti:
            if jelo.lower() == recept["recept"].lower():
                self.recepti.remove(recept)
                self.update_file_recepti()
                return("Uspesno ste uklonili recept {}".format(recept["recept"]))
        return("Ne postoji odabrani recept sa tim nazivom")

    def update_file_recepti(self):
        with open("recepti.txt", "w") as f:
            for recept in self.recepti:
                json_str = json.dumps(recept)
                f.write(json_str)
                f.write('\n')

    def odaberi_dorucak(self, dorucak=""):

        for recept in self.recepti:

            if dorucak.lower() == recept["recept"].lower():
                return(dorucak)
        return ("Ne postoji odabrani dorucak")

    def odaberi_rucak(self, rucak=""):

        for recept in self.recepti:

            if rucak.lower() == recept["recept"].lower():
                return(rucak)
        return ("Ne postoji odabrani rucak")

    def odaberi_veceru(self, vecera=""):

        for recept in self.recepti:

            if vecera.lower() == recept["recept"].lower():
                return(vecera)
        return ("Ne postoji odabrana vecera")

    def odaberi_random_jelo(self, dorucak="", rucak="", vecera=""):
        pass

    def ispis_recepta_dan(self):
        pass #Testing samo

    def spisak_za_kupovinu(self, *args):

        for x in args:
            for recept in self.recepti:
                if x.lower() == recept["recept"].lower():
                    for key, value in recept.items():
                        if key != "recept":
                            if key not in self.output:
                                self.output[key] = 0
                            self.output[key] += int(value[0])
    

    def stampaj(self):

        f = open("Spisak_za_kupovinu.txt", "w")
        f.close()

        f = open("Spisak_za_kupovinu.txt", "a")
        for key, value in self.output.items():
            print(("{}:{}\n".format(key, value)), file=f)
        f.close()

        self.output = {}

    def report_fali_sastojak(self):
        pass

    def update_file_zacin(self):

        f = open("kalorije.txt", "w")
        f.close()

        f = open("kalorije.txt", "a")
        for namirnica in self.namirnice:
            print(namirnica, file=f)
        f.close()

    def dodaj_zacin(self, namirnica, kolicina, proteini, hidrati, masti, kalorije):

        for x in self.namirnice:
            if namirnica.lower() == x.namirnica.lower():
                return ("Namirnica već postoji")

        if "" in [namirnica, kolicina, proteini, hidrati, masti, kalorije]:
            return ("Morate popuniti polja ispravno")

        nam = Namirnica(namirnica.capitalize(), kolicina,
                        proteini, hidrati, masti, kalorije)
        self.namirnice.append(nam)
        self.update_file_zacin()
        return ("Uspeno ste uneli zacin {}".format(namirnica))


a = Kuhinja()
a.ucitaj_namirnice()
a.ucitaj_recepte()
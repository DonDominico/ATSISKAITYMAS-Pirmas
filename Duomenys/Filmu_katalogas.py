#Filmu ivedimas i kataloga pagal organizatoriaus interfeiso 3-ia punkta
# Galimybė pridėti naują filmą į festivalio programą. 
# · Kiekvienas filmas turi turėti šiuos atributus (gali turėti ir daugiau): 
# o Pavadinimas 
# o Trukmė (minutėmis) 
# o Žanras (drama, komedija ir t.t.) 
# o Režisierius 
# o Išleidimo metai 
# o Amžiaus reitingas (pvz., "N-13", "N-18") 
import pickle #Nepamirtam importuot picklo
#Sukuriama filmu klase, filmu objektu kurimui.

Katalogas=[]

def irasyti_filma(self):
        Katalogas.append(self)
        return "Jusu ivestas filmas sekmingai irasytas i kataloga"

class Filmas: 
    def __init__(self, pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas): 
        self.pavadinimas = pavadinimas
        self.trukme = trukme 
        self.zanras = zanras
        self.rezisierius = rezisierius
        self.isleidimo_metai = isleidimo_metai
        self.amziaus_reitingas = amziaus_reitingas
           
    def sukurti_filma(self):
        un_nr=input("Sukurkite unikalu filmo iraso numeri is triju raidziu/skaiciu ar ju kombinacijos")# Kklases objekto uzvadinimui, uzdeti patikrinima ar nera tokio iraso sarase
        pavadin=input("Irasykite filmo pavadinima")#
        trukme=int(input("Nurodykite filmo trukme minutemis irasydami tik minuciu kieki skaitmenimis, pvz: 68"))
        zanras=input("Nurodykitie filmo zanra")
        rezisierius=input("Irasykite filmo rezisieriu")
        isleidimo_metai=input("Nurodykite filmo isleidimo metus skaitmenimis, pvz: 2024")
        amziaus_reitingas=input("Nurodykite filmui priskiriama amziaus reitinga siuo formatu:pvz. N-13 , N-7  ar N-18")

        un_nr=Filmas(pavadin, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas)
        Katalogas.append(un_nr)

        # un_nr.sukurti_filma(self)

    print(Katalogas)   
#         # self.fkatalogas.append(un_nr)


# #         super().pildyti_degalu()
# #         return("Baterija įkrauta")

    
#     def __str__(self): 
#         return f"{self.type}: {self.sum}

#     Filmas1=Filmas("pavadinimas", "trukme", "zanras", "rezisierius", "isleidimo_metai", "amziaus_reitingas")

#     Zapukas=Automobilis(1976, "Zaporozhec", "zhibalas")

# [film1, film2, ...]

# #Filtras:
# dramos_filmai = [film for film in filmai if film.zanras == "Drama"]
# for film in dramos_filmai:
#     print(film)
# #Updatas:
# for film in filmai:
#     if film.pavadinimas == "Pavadinimas1":
#         film.trukme = 130  # update the duration
# # Aprasymo gavimas su _str_
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"{self.name}, {self.age} years old"

# p = Person("Alice", 30)
# print(p)  # Uses __str__ -> "Alice, 30 years old"

# # Aprasymo gavimas su _repr_
# class Film:
#     def __init__(self, title, duration, genre, director):
#         self.title = title
#         self.duration = duration
#         self.genre = genre
#         self.director = director

#     def __repr__(self):
# # Here, we're showing only the title and genre
#         return f"Film(title={self.title!r}, genre={self.genre!r})"

# film1 = Film("Inception", 148, "Sci-Fi", "Christopher Nolan")
# film2 = Film("The Godfather", 175, "Crime", "Francis Ford Coppola")

# films = [film1, film2]
# print(films)

# #Du _rep_ budai vienas representina filmus is filmu klases, kitas is catalogo clases
# class Filmas:
#     def __init__(self, pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas):
#         self.pavadinimas = pavadinimas
#         self.trukme = trukme 
#         self.zanras = zanras
#         self.rezisierius = rezisierius
#         self.isleidimo_metai = isleidimo_metai
#         self.amziaus_reitingas = amziaus_reitingas

#     def __repr__(self):
#         return (f"Filmas(pavadinimas={self.pavadinimas!r}, trukme={self.trukme!r}, "
#                 f"zanras={self.zanras!r}, rezisierius={self.rezisierius!r}, "
#                 f"isleidimo_metai={self.isleidimo_metai!r}, amziaus_reitingas={self.amziaus_reitingas!r})")

# class Catalog:
#     def __init__(self):
#         self.journal = []

#     def prideti_filma(self, filmas):
#         self.journal.append(filmas)

#     def __repr__(self):
#         # Optional: You could define a __repr__ for the entire catalog
#         return f"Catalog(journal={self.journal})"

# # Create some film objects:
# film1 = Filmas("Filmas A", 120, "Veiksmo", "Režisierius A", 2020, 16)
# film2 = Filmas("Filmas B", 90, "Drama", "Režisierius B", 2021, 12)

# # Create a catalog and add films:
# katalogas = Catalog()
# katalogas.prideti_filma(film1)
# katalogas.prideti_filma(film2)

# # When you print the catalog's journal, each Film object is represented via its __repr__:
# print(katalogas.journal)
#     class Budget: 
#     def __init__(self): 
#         self.journal = []  

#     def add_income_entry(self, sum): 
#         entry = Entry("pajamos", sum) 
#         self.journal.append(entry)  

#     def add_expense_entry(self, sum): 
#         entry = Entry("išlaidos", sum) 
#         self.journal.append(entry)  

#     def get_balance(self): 

#         total_income = sum(entry.sum for entry in self.journal if entry.type == "pajamos") 
#         total_expenses = sum(entry.sum for entry in self.journal if entry.type == "išlaidos") 
#         balance = total_income + total_expenses 

#         return balance  

#     def show_report(self): 

#         for entry in self.journal: 
#             print(entry) 
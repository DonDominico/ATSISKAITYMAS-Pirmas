
#IMPORTINES PREKES:

import pickle 
import datetime

#FUNKCIJOS:

#Organizatoriaus prisijungimo/verificavimo modulis
#Festivalio organizatoriams butu duoti sie prisijungimo duomenys

def org_prieiga():
    user=("2025")#vartotjo vardas
    password=("2000")# slaptazodis
    useris=input("Iveskite vartotojo varda:")
    if useris!=user:
        return "Tokio vartotojo nera, neteisingai ivedete vartotojo varda."
    slaptazodis=input("Iveskite slaptazodi:")
    if slaptazodis!=password:
        return "netesingas slaptazodis"
    else:
        return True 

#Funkcija atspausditni filmu kataloga kai ji iskviecia vartotojas arba organizatorius
def filmu_katalogas():
    sarasas=""
    skaitiklis = 0
    for filmas in katalogas:
         skaitiklis += 1
         sarasas+=f"{skaitiklis}.{filmas}\n"
    return sarasas

#Funkcija atspausditni filmu seansu sarasa 
def seansai_sar():
    sarasas=""
    skaitiklis = 0
    for seansas in seansai:
         skaitiklis += 1
         sarasas+=f"{skaitiklis}.{seansas}\n"
    return sarasas


#Funkcija vartotojui/organizatoriui ieskoti filmo fetivalio kataloge:
def filmu_paieska(inputelis):
    rastu_film_sarasas = []
    for filmas in katalogas:
        filmas_str=str(filmas).lower()
        if inputelis.lower() in filmas_str:
            rastu_film_sarasas.append(str(filmas))
 
    if rastu_film_sarasas==[]:
       return "\nFilmu katalogo paieska nerado jokiu filmu pagal Jusu ivesta raktazodi"
    else: 
        return "Paieskos rezultatai:\n"+"\n".join(rastu_film_sarasas)

#Filmo pasalinimo is katalogo funkcija organizatoriui
def filmo_eliminacija(eliminacija):
    for filmas in katalogas:
        if eliminacija.lower()==filmas.pavadinimas.lower():
            katalogas.remove(filmas)
            issaugot_fkataloga(katalogas)
            return "Filmas istrintas is katalogo"
    
    return "Filmo nurodytu pavadinimu nera festivalio kataloge, pasitikslinkite ar teisingia ivedete filmo pavadinima"

#Automatinis filmo pasalinimas is seasnu jei jis istrinamas is filmu katalogo

def filmo_elseansai(eliminacija):
    for filmas in seansai[:]:
        if eliminacija.lower()==filmas.filmelis.lower():
            seansai.remove(filmas)
            issaugot_seansai(seansai)
           

#Filmo duomenu atnaujinimo funkcija organizatoriui
def filmo_korekcija(vardas, verte, nivestis):
    for filmas in katalogas:
        if vardas.lower()==filmas.pavadinimas.lower():
            if verte.lower() == "pavadinimas":
                filmas.pavadinimas = nivestis
            elif verte.lower() == "trukme":
                filmas.trukme = nivestis#cia problema jei trukme pakeiciama ir sis filmas jau itrauktas i rodymu plana gali kirstis su kitu rodymu
            elif verte.lower() == "zanras":
                filmas.zanras = nivestis
            elif verte.lower() == "rezisierius":
                filmas.rezisierius = nivestis
            elif verte.lower() == "isleidimo_metai":
                filmas.isleidimo_metai = nivestis  
            elif verte.lower() == "amziaus_reitingas":
                filmas.amziaus_reitingas = nivestis 
            elif verte.lower() == "filmo_reitingas":
                filmas.filmo_reitingas = nivestis 
            else:
                return ("Neteisinga ivedete duomenu tipa. Pasitikslinkite savo ivestis.")
            issaugot_fkataloga(katalogas)
            return "Filmo irasas atnaujintas"
        
#Filmo pavadinimo seasne atnaujinimo funkcija organizatoriui (automatine)
def seanso_fpkorekcija(vardas, nivestis):
    for filmas in seansai:
        if vardas.lower()==filmas.filmelis.lower():
                filmas.filmelis = nivestis
    issaugot_seansai(seansai)
       
#Vardo skanavmo tikrinimas

def pav_tikrinimas(vardas):
    for filmas in katalogas:
        if vardas.lower()==filmas.pavadinimas.lower():
            return False
    return True
        
#Filmo seansu planavimo/tikrinimo funkcija organizatoriui
def filmo_seansai(kurinys, start):
    fpradzia=datetime.datetime.strptime(start, "%Y-%m-%d-%H:%M:%S") #Try ar ivestas formatas teisingas nes sitas eroras nesugaunams
    for filmas in katalogas:
        if kurinys.lower()==filmas.pavadinimas.lower():
           atitikimas=filmas
           break
    else:   
        return("Jusu nurodyto filmo nera festivalio kataloge")
    
    pabaiga=fpradzia+datetime.timedelta(minutes=int(atitikimas.trukme))

    for filmukas in seansai:
        if fpradzia < filmukas.seanso_pab and pabaiga > filmukas.seanso_prad:
            return ("Sis filmo rodymas nuo jusu nurodytu laiku negalimas, nes sutampa su kito filmo rodymu.")
    
    obj_pav=Seansai(fpradzia,pabaiga, atitikimas.pavadinimas,vietu_rezerv={})
    seansai.append(obj_pav)
    issaugot_seansai(seansai)
    print(seansai_sar())#nepaduoda saras pagal dienas graziai sutvarkyto. Reik arba cia apibudinti arba uzrasyti kita funcija saraso isprintinimui
    return ("Filmas irasytas i festivalio rodymu programa") 

#Filmu reitingavimo sistema ziourovui
def filmo_reitingavimas(matytasf, ivertinimas):
    for filmas in katalogas:
        if matytasf.lower()==filmas.pavadinimas.lower():
            filmas.ziurovu_reitingas.append(ivertinimas)
            issaugot_fkataloga(katalogas)
            return "Jusu ivertinimas issaugotas"
    
    return "Filmo nurodytu pavadinimu nera festivalio kataloge, pasitikslinkite ar teisingia ivedete filmo pavadinima"

#Vietu rezervavimo sistema ziourovui
def vietu_rezervavimas(film, individas, vietu_sk):
  rastu_film_sarasas = []
  for filmas in seansai:
        if film.lower() in filmas.filmelis.lower():
            rastu_film_sarasas.append(filmas)
  if rastu_film_sarasas == []:
       return("Jusu nurodyto filmo nera festivalio kataloge")
  else:
      print("Rodomi filmai pagal jusu ivestus zodzius pieskoje:")
      print(*rastu_film_sarasas, sep="\n")
      pasirinkimas=int(input("Irasykite pasirinkto filmo indentifikacini nr."))

  for kinas in rastu_film_sarasas:
        if  pasirinkimas==kinas.ident:
            if kinas.vietu_sk-vietu_sk<0: 
                return "Rezervacija negalima Jusu pasirinktame kino seanse, nes Jums reikiamu laisvu vietu nera."
            else: 
                kinas.vietu_sk=kinas.vietu_sk-vietu_sk
                kinas.vietu_rezerv[individas]=vietu_sk
                issaugot_seansai(seansai)
                return("Jusu rezervacija sekmingai atlikta.")

#print(seansai_sar())#cia mano kontrolei, finalinei versijoje istrinti

#Informacijos apie likusias laisvas vietas ir rezervacijas i seansus pateikimas organizatoriui
def info_rezervavimas():
    f_sarasas=[]
    for filmas in seansai:
        f_sarasas.append(filmas.org_rezervacijos())
    return "\n".join(f_sarasas)



#KLASES:
#Sukuriame Filmu klase
class Filmas: 
    def __init__(self, pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas, ziurovu_reitingas): 
        self.pavadinimas = pavadinimas
        self.trukme = trukme 
        self.zanras = zanras
        self.rezisierius = rezisierius
        self.isleidimo_metai = isleidimo_metai
        self.amziaus_reitingas = amziaus_reitingas
        self.ziurovu_reitingas = ziurovu_reitingas

    def reitingavimas_pateikimas(self):
        if self.ziurovu_reitingas==[]:
            return"Filmas dar negavo ziurovu ivertinimu"
        else:
            return sum(self.ziurovu_reitingas)/len(self.ziurovu_reitingas)

#Naudojame _str_, kad atvaizduoti klases objektu turini zmogiskai  
    def __str__(self):
        return f"Pavadinimas: {self.pavadinimas}, Trukme: {self.trukme} min, Žanras: {self.zanras}, Režisierius: {self.rezisierius}, Išleidimo metai: {self.isleidimo_metai}, Amžiaus cenzas: {self.amziaus_reitingas}, Ziurovu_reitingas: {self.reitingavimas_pateikimas()}"
#Naudojame _str_, kad atvaizduoti klases objektu turini zmogiskai  
    def __repr__(self):
        return f"Pavadinimas: {self.pavadinimas}, Žanras: {self.zanras}, Išleidimo metai: {self.isleidimo_metai}, Amžiaus cenzas: {self.amziaus_reitingas}"

#Sukuriame klase kino seasnu planavimui (organizatoriui)
class Seansai: 
    id_skaitiklis=1
    def __init__(self, seanso_prad, seanso_pab, filmelis, vietu_rezerv, vietu_sk=100, ): 
        self.seanso_prad = seanso_prad
        self.seanso_pab = seanso_pab
        self.filmelis = filmelis
        self.vietu_sk = vietu_sk
        self.vietu_rezerv = vietu_rezerv
        self.ident = Seansai.id_skaitiklis
        Seansai.id_skaitiklis+=1 
    
    def __str__(self):
        return f"Rodomas filmas: {self.filmelis}, Seanso pradzia: {self.seanso_prad} min, Seanso pabaiga: {self.seanso_pab}, liko laisvu vietu:{self.vietu_sk}, filmo identifikacinis nr:{self.ident}"
    def __repr__(self):
        return f"Rodomas filmas: {self.filmelis}, Seanso pradzia: {self.seanso_prad} min, Seanso pabaiga: {self.seanso_pab}, liko laisvu vietu:{self.vietu_sk}, filmo identifikacinis nr:{self.ident}"
    def org_rezervacijos(self):
        return f"Rodomas filmas: {self.filmelis}, Seanso pradzia: {self.seanso_prad} min, Seanso pabaiga: {self.seanso_pab}, liko laisvu vietu:{self.vietu_sk}, filmo rezervacijos(vardas pavarde:vietu skaicius):{self.vietu_rezerv}, filmo identifikacinis nr:{self.ident}"

#Funkcija skaitiklio Seansai klases id numerio perskaiciavimui/atnaujinimui
def gauti_max_id(seansai):
    max_id = 0
    for elementas in seansai:
        if elementas.ident > max_id:
            max_id = elementas.ident
    Seansai.id_skaitiklis = max_id+1

#DUOMENU SAUGOJIMAS

#Filmu katalogo uzloudinimo ir issaugojimo funkcija:
try: 
    with open("katalogas.pickle", "rb") as file:
        katalogas = pickle.load(file)
except FileNotFoundError:
    katalogas = []
    with open("katalogas.pickle", "wb") as file:
        pickle.dump(katalogas, file)

def issaugot_fkataloga(katalogas):
    with open("katalogas.pickle", "wb") as file:
        pickle.dump(katalogas, file)

#FSeasnu plano uzloudinimo ir issaugojimo funkcija:
try: 
    with open("seansai.pickle", "rb") as file:
        seansai = pickle.load(file)
    gauti_max_id(seansai)
except FileNotFoundError:
    seansai = []
    with open("seansai.pickle", "wb") as file:
        pickle.dump(seansai, file)

def issaugot_seansai(seansai):
    with open("seansai.pickle", "wb") as file:
        pickle.dump(seansai, file)
  
# Pagrindinis interfeisas

def main_menu(): 
    try:
        while True: 
            print("\n Sveiki atvyke i Kinofest2025 platforma.Pasirinkite norima veiksmas is Kinofest2025 platformos meniu:") 
            print("1. Gauti informacija apie Kinofest2025 esancius filmus") 
            print("2. Filmu paieska/filmu repertuaro filtravimas")
            print("3. Filmu reitingavimas")
            print("4. Bilietu rezervacija") 
            print("5. Organizatoriaus prisijungimas")
            print("6. Iseiti")  
            pasirinmimas = input("Pasirinkite veiksmą iš meniu (1-6)")  
            if pasirinmimas == "1":#Gauti informacija apie Kinofest2025 esancius filmus
                print(filmu_katalogas())
    
            elif pasirinmimas == "2": #Filmu paieska/filmu repertuaro filtravimas
                ivestis=input("""Noredami surasti filma galite ieskoti filmu kataloge pasirinkdami viena is siu budu: 
                ivesdami zodi filmo pavadinime, ivesdami zanra kuriam priklauso filmas, ivesdami rezisieriaus varda ar pavarede,
                ivesdami filmo isleidimo metus skaiciais (pvz. 2025)""")
                print(filmu_paieska(ivestis))

            elif pasirinmimas == "3": #Filmu reitingavimas
                filmukas=input("Iveskite matyta festivalio filma kuriam noretumete skirti savo ivertinima: ")
                balas=int(input("Irasykita bala kurio norite ivertinti si filma. Nurodykite savo bala skaiciumi nuo 1 iki 10 (pvz.: 5)."))
                print(filmo_reitingavimas(filmukas, balas)) 
        
            elif pasirinmimas == "4": #Bilietu rezervacija
                try:
                    filmukas=input("Iveskite tiklsu filmo, i kurio rodyma norite rezervuoti vietas, pavadinima ar zodi jame")
                    vard_pavard=input("Irasykite savo varda ir pavarde, pateike asmens dokumenta galesite atssimti bilietus kasose")
                    vietos_str=input("Nurodykite norimu rezervuoti vietu kieki skaitmenimis (pvz. 3):")
                    if vietos_str.isdigit()==False:
                        raise ValueError ("Pageidaujama vietu skaiciu turite nurodyti skaiciumi")
                    vietos=int(vietos_str)
                    print(vietu_rezervavimas(filmukas, vard_pavard,vietos)) 
                    break
                except ValueError as erval:
                    print(erval) 
           
        
            elif pasirinmimas == "5": #Organizatoriaus prisijungimas
                 rezultats=org_prieiga() 
                 print(rezultats)
                 if rezultats==True:
                  while True: 
                    print("\n Sveiki prisijunge prie festivalio organizatoriaus platformos. Galite redaguoti duomenis.")  
                    print("1. Gauti informacija apie Kinofest2025 esancius filmus") 
                    print("2. Filmu paieska/filmu repertuaro filtravimas") 
                    print("3. Nauju filmu ivedimas i kataloga")
                    print("4. Filmu duomenu atnaujinimas") 
                    print("5. Filmu pasalinimas is katalogo")
                    print("6. Seansu planavimas")
                    print("7. Gauti informacija apie rezervacijas i seansus ir likusi laisvu vietu skaiciu")
                    print("8. Grizti i pagrindini meniu") 

                    org_pasirinmimas = input("Pasirinkite veiksmą skaiciu atitnkanti meniu (1-8):")   
                    if org_pasirinmimas=="1":#Informacija apie Kinofest2025 esancius filmus
                        print(filmu_katalogas())

                    elif org_pasirinmimas=="2":#Filmu paieska/filmu repertuaro filtravimas
                        ivestis=input("""Noredami surasti filma galite ieskoti filmu kataloge pasirinkdami viena is siu budu: 
                        ivesdami zodi filmo pavadinime, ivesdami zanra kuriam priklauso filmas, ivesdami rezisieriaus varda ar pavarede,
                        ivesdami filmo isleidimo metus skaiciais (pvz. 2025)""")
                        print(filmu_paieska(ivestis))

                    elif org_pasirinmimas=="3":#Nauju filmu ivedimas i kataloga    
                        pavadin=input("Irasykite filmo pavadinima")
                        trukme=int(input("Nurodykite filmo trukme minutemis irasydami tik minuciu kieki skaitmenimis, pvz: 68"))
                        zanras=input("Nurodykitie filmo zanra")
                        rezisierius=input("Irasykite filmo rezisieriu")
                        isleidimo_metai=input("Nurodykite filmo isleidimo metus skaitmenimis, pvz: 2024")
                        amziaus_reitingas=input("Nurodykite filmui priskiriama amziaus cenzo indeksa siuo formatu(pvz: N-7, N-16, N-13, ar N-18):")
                        n_filmas=Filmas(pavadin, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas, ziurovu_reitingas=[])
                        katalogas.append(n_filmas)
                        issaugot_fkataloga(katalogas)
                        for film in katalogas:
                            print("Jusu naujai ivestas filmas sekmingai irasytas i duomeu baze", film)

                    elif org_pasirinmimas=="4":#Filmu duomenu atnaujinimas
                        while True:
                            try:
                                pavadinims=input("Iveskite filmo pavadinima kurio duomeni norite pakoreguoti.")
                                if pav_tikrinimas(pavadinims)==True:
                                    raise ValueError ("Filmo nurodytu pavadinimu nera festivalio kataloge")
                                domuo=input("""Iveskite duomnu tipa kuri norite pakoreguoti, nurodyti viena is sio saraso:
                        pavadinimas, trukme, zanras, rezisierius, isleidimo_metai, amziaus_reitingas.
                        *DEMSESIO, pakeitus filmo trukme duomenys rodymu plane neatsinaujina. Norint, kad laiko trukme atsispindetu ir rodymu plane, geriau filma istrinti is filmu katalogo ir vel irasyti su atnaujinta trukme.""")                       
                                ivestis=input("Iveskite duomeni kuri norite ideti, nepamirkiste, kad filmo isleidimo metus reikia nurodyti skaitmenimis (pvz: 2024), taip pat ir filmo trukme (pvz.68)")
                                print(filmo_korekcija(pavadinims, domuo, ivestis))
                                if domuo.lower() == "pavadinimas":
                                    seanso_fpkorekcija(pavadinims, ivestis)
                                break
                            except ValueError as er:
                                print(er)

                    elif org_pasirinmimas=="5":#Filmu pasalinimas is katalogo ir rodymu plano
                        ivestis=input("Iveskite filmo pavadinima noredami istrinti filma is festivalio katalogo.*DEMSESIO, istrynus filma is katalogo, filmas taip pat bus istrintas is rodymu plano.")
                        filmo_elseansai(ivestis) 
                        print(filmo_eliminacija(ivestis))
                    
                    elif org_pasirinmimas=="6":#Seansu planavimas
                        pavadinimas=input("Iveskite filmo pavadinima noredami irasyti jo rodymo data ir laika.")
                        while True:
                            try:
                                pradzia=input("Iveskite filmo rodymo pradzios data ir laika skaiciais siuo formatu: YYYY-MM-DD-HH:MM:SS")
                                if len(pradzia) != 19 or pradzia[4]!= '-' or pradzia[7]!= '-' or pradzia[10]!= '-' or pradzia[13]!= ':' or pradzia[16]!= ':'or pradzia[0:4].isdigit()==False or pradzia[5:7].isdigit()==False or pradzia[8:10].isdigit()==False or pradzia[11:13].isdigit()==False or pradzia[14:16].isdigit()==False or pradzia[17:19].isdigit()==False:
                                    raise ValueError ("neteisingai ivestas data (neatitinka formato)")
                                break
                            except ValueError as kl:
                                print(kl)
                        print(filmo_seansai(pavadinimas, pradzia))

                    elif org_pasirinmimas=="7":#Informacija apie rezervacijas
                        print(info_rezervavimas())

                    elif org_pasirinmimas=="8":
                        break 
                    else:
                        print("Neteisingas meniu pasirinkimas, bandykite dar kartą (iveskite skaiciu nuo 1 iki 8 atitinkanti meniu punkta).") 
                    
            elif pasirinmimas == "6": 
                print("Dekojame uz apsilankyma") 
                exit() 
            else:
                print("Neteisingas meniu pasirinkimas, bandykite dar kartą (iveskite skaiciu nuo 1 iki 6 atitinkanti meniu punkta).") 
    except:
        print("Isivele klaida, pabandykite dar karteli")

main_menu() 

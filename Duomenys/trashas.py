print(5)


#Biudzeto programa:
# Uzduotis. Sukurkite Stačiakampio klasę ir suteikite jai sąvybes aukštis ir plotis ir sukurkite jam metodą Perimetras, 
# perimetro tikslas būtų grąžinti paskaičiuotą stačiakampio perimetrą ir tada jį atspausdinkite. Leiskite naudotojui įvesti plotį ir aukštį. 
# Daug tikrinimų daryti nereikia (ten ar tikrai skaičius ir ar toks stačiakampis yra įmanomas)

# Uzduotis, apskaiciuoti staciakampio perimetra.
# class forma:
#     def __init__(self,aukstis, plotis): # metodas yra tiesiog funkcija priklausanti klasei
#         self.aukstis = aukstis
#         self.plotis = plotis
#     def perimetras(self):
#         print(f"Perimetras: {self.aukstis  * self.plotis}")
 
# staciakampis = forma(50,70) 
# staciakampis.perimetras()

#****************************************UZDUOTIS PIRMA PRADZIA*******************************************************************8#

# Uzduotis:Parašyti klasę Sakinys, kuri turi savybę tekstas irmetodus,kurie:
# •Gražina tekstą atbulai
# •Gražina tekstą mažosiomis raidėmis
# •Gražina tekstą didžiosiomis raidėmis
# •Gražina žodį pagal nurodytą eilės numerį
# •Gražina, kiek teksteyranurodytų simbolių arba žodžių
# •Gražinatekstą su pakeistu nurodytu žodžiu arba simboliu
# •Atspausdina, kiek sakinyje yra žodžių,skaičių,didžiųjų ir mažųjų raidžių
# Susikurti kelis klasės objektus ir išbandyti visus metodus
# class Sakinys:#Klases sukurimas

#     def __init__(self,tekstas=("Bet kur visi 2000 mes lekiam, o kas atsakys Man")): 
# #Metodas sakinio atbulam uzrasymui
#         self.tekstas = tekstas
#     def atbulai(self):
#         return self.tekstas[::-1]
# #Metodas sakinio mažosiomis raidėmis uzrasymui
#     def mazom(self):
#         return self.tekstas.lower()
# #Metodas sakinioą didžiosiomis raidėmis grazinimui
#     def didz(self):
#         return self.tekstas.upper()
# #Metodas gražinti žodį pagal nurodytą eilės numerį
#     def rvieta(self):
#         listekstis=self.tekstas.split()
#         index=int(input("iveskite ieskomo elemento numeri"))
#         return listekstis[index]
# # Metodas žodžių skaiciui tekste nurodymui
#     def zodsk(self):
#         listekstis=self.tekstas.split()
#         zodziai=0
#         for zodis in listekstis:
#             if zodis.isdigit()==False:
#                 zodziai+=1
#         return (zodziai)
    
# #Metodas teikstui su pakeistu nurodytu žodžiu grazinti
#     def repl(self):
#         indexold=input("iveskite zodi kuri norite pakeisti")
#         indexnew=input("iveskite zodi kuri norite pakeisti")
#         return self.tekstas.replace(indexold,indexnew)
    
# #Metodas kiek sakinyje yra žodžių,skaičių,didžiųjų ir mažųjų raidžių atspausdinimui
#     def inventor(self):
#         listekstis=self.tekstas.split()
#         zodz_kiekis=0
#         didziosiosr=0
#         mazosiosr=0
#         skaiciai=0
#         for zodis in listekstis:
#             if zodis.isdigit()==False:
#                 zodz_kiekis+=1
#         for simbolis in self.tekstas:
#             if simbolis.isdigit():
#                 skaiciai+=1
#             if simbolis.isupper():
#              didziosiosr+=1
#             if simbolis.islower():
#                 mazosiosr+=1
#         rezultatas=(
#         f"Jusu irase tiek skaiciu: {skaiciai}\n"
#         f"Jusu irase tiek zodziu: {zodz_kiekis}\n"
#         f"Jusu irase tiek didziuju raidziu: {didziosiosr}\n"
#         f"ir jusu irase tiek mazuju raidziu: {mazosiosr}\n"
#     )
#         return (rezultatas)

# Metodas objekto sakinio atspausdinimui
    # def esybe(self):
    #   return self.tekstas


# #Objekto Zen sukurimas po klase Sakinys       
# Zen=Sakinys("Errors should never pass silently")
# Statistika=Sakinys("Buvo sunmaikinta 500 tanku, 300 belzabubu ir 3 lektuvai")
# Romantika=Sakinys("Ir kraupūs šešėliai atgal iš bedugnių užslinko.")
# Kurlekiam=Sakinys() # objektas naudojantis salygini klases argumenta - sakini. 

#Metodo atbulai iskvietimas ir pritaikykas objektams
# print(Zen.atbulai())
# print (Romantika.atbulai())
# print (Statistika.atbulai())
# print (Kurlekiam.atbulai())# objektas naudojantis salygini klases argumenta - sakini. 


# #Metodo sakinio mažosiomis raidėmis uzrasymui iskvietimas ir pritaikykas objektams
# print (Zen.mazom())
# print (Romantika.mazom())
# print (Statistika.mazom())
# print (Kurlekiam.mazom())# objektas naudojantis salygini klases argumenta - sakini. 

#Metodo sakinio didziosiomis raidėmis uzrasymui iskvietimas ir pritaikykas objektams
# print (Zen.didz())
# print (Romantika.didz())
# print (Statistika.didz())
# print (Kurlekiam.didz())# objektas naudojantis salygini klases argumenta - sakini. 

#Metodo žodzio pagal nurodytą eilės numerį gražinimui iskvietimas ir pritaikykas objektams
# print (Zen.rvieta())
# print (Romantika.rvieta())
# print (Statistika.rvieta())
# print (Kurlekiam.rvieta())# objektas naudojantis salygini klases argumenta - sakini. 

#Metodo žodziu suksiaciavimui sakinyje iskvietimas ir pritaikymas objektams
# print (Zen.zodsk())
# print (Romantika.zodsk())
# print (Statistika.zodsk())
# print (Kurlekiam.zodsk())# objektas naudojantis salygini klases argumenta - sakini. 

#Metodo žodziu pakeitimui sakinyje iskvietimas ir pritaikymas objektams
# print (Zen.repl())
# print (Romantika.repl())
# print (Statistika.repl())
# print (Kurlekiam.repl())# objektas naudojantis salygini klases argumenta - sakini. 

#Metodo Atspausdina, kiek sakinyje yra žodžių,skaičių,didžiųjų ir mažųjų raidžių iskvietimas ir taikymas objektams. 
# print (Zen.inventor())
# print (Romantika.inventor())
# print (Statistika.inventor())
# print (Kurlekiam.inventor())# objektas naudojantis salygini klases argumenta - sakini. 

# Metodo objekto sakinio atspausdinimui isbandymas
# print (Zen.esybe())
# print (Romantika.esybe())
# print (Statistika.esybe())
# print (Kurlekiam.esybe())# objektas naudojantis salygini klases argumenta - sakini. 

#****************************************UZDUOTIS PIRMA PABAIGA*********************************************************************

#****************************************UZDUOTIS ANTRA PRADZIA*********************************************************************
# Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) irmetodus,kurie:
# •Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
# •Gražina,ar nurodytos sukakties metai buvo keliamieji
# •Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
# •Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą
# Taip pat klases argumente taikos salyginis argumentas - užduotį taip, kad 
# jei kuriant objektą, nepaduodamas jokia data,veiksmai turi būti atliekami su programuotojo gimtadieniu


# import datetime
# prdob=("1980-03-29-17:03:29")
# defaultd=datetime.datetime.strptime(prdob, "%Y-%m-%d-%H:%M:%S")

# class Sukaktis:#Klases sukurimas
#     def __init__(self,data=defaultd): 
#         self.data = data
# #Metodas(laiko pralekimo skaiciukles) grazinti kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
#     def skaiciuokle(self):
#         pralekeslaikas=datetime.datetime.today()-self.data
#         praejometu=pralekeslaikas.total_seconds()/31557600
#         praejomen=(praejometu*12)
#         dienu=pralekeslaikas.days
#         valandu=pralekeslaikas.total_seconds()/60
#         sekundeliu=pralekeslaikas.total_seconds()
#         return(f"{round(praejometu)},praleke sitiek metu utatatata,\n Praejo sitiek menesiu {round(praejomen)} \n Praejo sitiek dienu {dienu} \n Praejo sitiek valandu {round(valandu)} \n Praejo sitiek sekundziu{round(sekundeliu)}")

#Metodas patikrinti ar nurodyti metai buvo keliamieji 
    # def keltuvas(self):
    #     metai=self.data.year
    #     if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 ==0 ):  
    #         return("Jus gimete keliamaisiais metais")
    #     else:
    #         return("Jus gimete nekeliamaisiais metais")
        
# # Metodas atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
#     def atimtuvas(self): 
#         atimtidien=int(input("nurodykite skaiciumi kiek dienu norite atimti is sio piliecio gimtadienio"))
#         return(f"Stai kokia data iseina atemus jusu nurodytas dienas {self.data - datetime.timedelta(days=atimtidien)}")

# # Metodas pridedantis prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą

#     def pridetuvas(self): 
#         atimtidien=int(input("nurodykite skaiciumi kiek dienu norite prideti prie sio piliecio gimtadienio"))
#         return(f"Stai kokia data iseina pridejus jusu nurodytas dienas {self.data + datetime.timedelta(days=atimtidien)}")

# Metodas objekto datos atspausdinimui
#     def esybe(self):
#       return self.data

# tadiena=input("iveskite savo gimimo data siuo formatu yyyy-mm-dd-hh:mm:ss")
# dob = datetime.datetime.strptime(tadiena, "%Y-%m-%d-%H:%M:%S") 

# Birvzday=Sukaktis(dob)#sukuriam Sukaktis klases objekta
# progdob=Sukaktis()#sukuriam Sukaktis klases objekta kuris naudos defaultine data-argumenta

#Pritaikome susikurtam objektui laiko pralekimo skaiciukles metoda
# print(Birvzday.skaiciuokle())
#print(progdob.skaiciuokle())#bandymas su objektu su defaultiniu argumentu

#Pritaikome keliamuju metu patikrinimo metoda objektui 
# print(Birvzday.keltuvas())
#print(progdob.keltuvas())#bandymas su objektu su defaultiniu argumentu

#Pritaikome dienu atimties moduli objektui 
# print(Birvzday.atimtuvas())
#print(progdob.atimtuvas())#bandymas su objektu su defaultiniu argumentu

#Pritaikome dienu prideties moduli objektui 
#print(Birvzday.pridetuvas())
#print(progdob.pridetuvas())#bandymas su objektu su defaultiniu argumentu

# Metodas objekto datos atspausdinimui
# print(Birvzday.esybe())
# print(progdob.esybe())#bandymas su objektu su defaultiniu argumentu

#****************************************UZDUOTIS ANTRA PABAIGA**************************************************************************


#****************************************UZDUOTIS TRECIA PRADZIA**************************************************************************

# Padarytiminibiudžetoprogramą, kuri:
# •Leistų vartotojui įvesti pajamas
# •Leistų vartotojui įvesti išlaidas
# •Leistų vartotojui parodyti pajamų/išlaidų balansą
# •Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
# •Leistų vartotojui išeiti iš programos
 
# Rekomendacija, kaip galima būtų padaryti:
# •Programa turi turėti klasę Irasas, kuri turėtų argumentus tipas (Pajamos arba Išlaidos) ir suma. Galima prirašyti str metodą, kuris gražintų, kaip bus atvaizduojamas spausdinamas objektas.
# •Programa turi turėti klasę Biudzetas, kurioje būtų:
# •Metodas init, kuriame sukurtas tuščias sąrašas zurnalas, į kurį bus dedami sukurti pajamų ir išlaidų objektai
# •Metodasprideti_pajamu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų pajamų objektą ir įdėtų jį į biudžeto žurnalą
# •Metodasprideti_islaidu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų išlaidų objektą ir įdėtų jį į biudžeto žurnalą
# •Metodasgauti_balansą(self), kuris gražintų žurnale laikomų pajamų ir išlaidų balansą.
# •Metodasparodyti_ataskaita(self), kuris atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).

# #Pagrindinai programos kintamieji
# ivesti_pajamas=1
# Ivesti_islaidas=2
# Atvaizduoti_ivestas_pajamas_islaidas_balansa=3
# Atvaizduoti_ibalansa=4
# iseiti_is_programos=5


# #Funkcija pajamu-islaidu ivedimas(pagal meniu 1-2):

# def paisived(paj):
#     if paj>=0:
#         Sarasas.pajamos.append(paj)
#         return(Sarasas.pajamos)
#     else:
#         Sarasas.islaidos.append(paj)
#         return(Sarasas.islaidos)
# #Funkcija islaidu ivedimas(pagal meniu 2):

# def islaidout(out):
#     Sarasas.islaidos.append(out)
#     return(Sarasas.islaidos)

#Klase Irasas

# class Biudzetas:#Klases sukurimas
#     def __init__(self,pajamos, islaidos,  balansas): 
#         self.islaidos = islaidos
#         self.pajamos = pajamos
#         self.balansas = balansas

# #Metodas atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).
#     def visiirasai(self): 

#         print("Jusu pajamos:\n"+'\n'.join(str(x) for x in Bonketas.pajamos))
#         print("Jusu islaidos: \n", '\n'.join(str(x) for x in Bonketas.islaidos))
#         print("Jusu balansas:\n", '\n'.join(str(x) for x in Bonketas.balansas))

#Klase Biudzetas

# class Irasas:#Klases sukurimas
#     def __init__(self,pajamos, islaidos,  balansas): 
#         self.islaidos = islaidos
#         self.pajamos = pajamos
#         self.balansas = balansas


# Sarasas=Irasas([500,200,600,1000,115,899,777],[-577,-185,-690,-1009,-130,-800,-700],[0])#sukuriam Sukaktis klases objekta

# Bonketas=Biudzetas(Sarasas.pajamos, Sarasas.islaidos, (f"{sum(Sarasas.pajamos)+sum(Sarasas.islaidos)}"))


# # Vartotojui pateikiamas programos/bibliotekos meniu
# menu=("Programos meniu: \n 1. Ivesti pajamas \n 2. Ivesti islaidas \n 3. Atvaizduoti ivestas pajamas ir islaidas \n 4. Atvaizudoti balansa \n 5. Išeiti iš programos")
# print(menu)
# # # Atliekami programos veiksmai pagal vartotojo pageidavima
# while True:
#     try:
#         pasirinkimas=input("pasirinkite norima veiksma ivesdami tinkamo saraso is meniu eiles numeri")
#         if  pasirinkimas.isdigit()==False:
#             raise ValueError ("iveskite skaiciu atstojanti meniu punkta")
#         pasas=int(pasirinkimas)

#         if pasas<1 or pasas > 5:
#             raise ValueError("pasirinkite norima veiksma ivesdami tinkamo saraso is meniu eiles numeri")
#         elif pasas==1:#Ivesti pajamas
#             incomas=float(input("iveskite pajamu suma"))
#             paisived(incomas)
#         elif pasas==2:#Ivesti islaidas
#             minusas=float(input("iveskite islaidu suma"))
#             paisived(minusas)

#         elif pasas==3:#Gauti islaidu ir pajamu sarasa   
#             Bonketas.visiirasai()
         
#         elif pasas==4:#Gauti balansa
#              balansas=(f"{sum(Bonketas.pajamos)+sum(Bonketas.islaidos)}")
#              print("Esamas balansas", balansas)     
#         elif pasas==5: 
#             # balansas=(f"{sum(Pajamos)+sum(Islaidos)}")
#             # uzseivinimas(balansas)
#             print("Dekojame uz apsilnakyma musu banke, linkime nenuskursti") 
#             break
#     except ValueError as badchoice:
#         print (badchoice)
#     except:
#         print("isivele klaida, gal ivedete texta vietoj skaiciaus?")

#****************************************UZDUOTIS TRECIA PRADZIA**************************************************************************

#****************************************UZDUOTIS KETVIRTA PRADZIA**************************************************************************
# Sukurti programą, kuri:
# •Turėtų klasę Automobilis
# •Automobilis turėtų savybes: metai, modelis, kuro_tipas
# •Automobilis turėtųmetodus: vaziuoti, stoveti, pildyti_degalu,kurie atitinkamai atspausdintų „Važiuoja“, 
# „Priparkuota“, „Degalai įpilti“
# •Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą
# •Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis)
# •Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip, kad jis atspausdintų „Baterija įkrauta“
# •Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“
# •Sukurti norimą Automobilio objektą
# •Sukurti norimą Elektromobilio objektą
# •Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti,pildyti_degalu
# •Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti,stoveti,pildyti_degalu,
# vaziuoti_autonomiskai

#Klases automobilis ir jos metodu sukurimas 
# class Automobilis:
#     def __init__(self, metai, modelis, kuro_tipas):
#         self.metai = metai
#         self.modelis = modelis
#         self.kuro_tipas = kuro_tipas
# #Kuriam metodus
#     def vaziuoti(self):
#         return("Važiuoja")
#     def stoveti(self):
#         return("Priparkuota")
#     def pildyti_degalu(self):
#         return("Degalai įpilti")
# #Kuriam metoda automatiniam Automobilio objekta savybiu atspausdinimui
#     def __str__(self):
#         return f"{self.modelis} yra {self.metai} -metu ir i ji pilamas kuras yra {self.kuro_tipas}"

    

# #  Klases Elektromobilis su tevuku Automobilis sukurimas ir priskirimas tevuko savybiu     
# class Elektromobilis(Automobilis):
#     def __init__(self, metai, modelis, kuro_tipas):
#         super().__init__(metai, modelis, kuro_tipas)
#         # super().__init__(modelis)
#         # super().__init__(kuro_tipas)
# #Metodas - Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“
#     def vaziuoti_autonomiskai(self):
#         return("Važiuoja autonomiškai")
# #Metodas priskiriamas tevuko metodas su atnaujintu irasu  
#     def pildyti_degalu(self):
#         super().pildyti_degalu()
#         return("Baterija įkrauta")
# #Kuriam metoda automatiniam Automobilio objekta savybiu atspausdinimui
#     def __str__(self):
#         return f"{self.modelis} yra {self.metai} -metu ir ji varoma {self.kuro_tipas}"

# #Sukurti norimą Automobilio objektą

# Zapukas=Automobilis(1976, "Zaporozhec", "zhibalas")
# print(Zapukas)
# print(Zapukas.vaziuoti())
# print(Zapukas.stoveti())
# print(Zapukas.pildyti_degalu())
 
# #Sukurti norimą Elektromobilio objektą

# Teshlike=Elektromobilis(2022, "Teshla", "metanine elektra")
# print(Teshlike)
# print(Teshlike.vaziuoti())
# print(Teshlike.stoveti())
# print(Teshlike.pildyti_degalu())#tevuko modulis su papimpintu mesedzu

#****************************************UZDUOTIS KETVIRTA PABAIGA**************************************************************************

#****************************************UZDUOTIS PENKTA PABAIGA**************************************************************************
# Sukurti programą, kuri:
# •Turėtų klasę Darbuotojas
# •Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
# •Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien 
# (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
# •Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą atlyginimą 
# (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
# •Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą, dirbant darbuotojui 5 dienas per savaitę
# •Sukurti norimą Darbuotojo objektą
# •Sukurti norimą NormalusDarbuotojas objektą
# •Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima

#Klases Darbuotojas ir jos metodu sukurimas 
# import datetime
# class Darbuotojas:
#     def __init__(self, vardas, valandos_ikainis, dirba_nuo):
#         self.vardas = vardas
#         self.valandos_ikainis = valandos_ikainis
#         self.dirba_nuo = dirba_nuo

# #Metodas apskaiciuoti kiek darbuotojas jau atare
#     def kiek_nudirbo(self):
#         konvertuotas_dn=datetime.datetime.strptime(self.dirba_nuo, "%Y-%m-%d").date() 
#         nuo_siandien=datetime.datetime.now().date()-konvertuotas_dn
#         nudirbtasek=nuo_siandien.total_seconds()
#         nudirbta_dienu=nudirbtasek/86400#dalinam sekundziu skirtuma is sekundziu kiekio 24 val ir gaunam dienu skirtuma tarp siu datu. 
#         return nudirbta_dienu 
    
# #Metodas vergaujancio darbuotojo uzdarbiui paskaiciuoti

#     def vergo_uzdarbis(self):
#         atvergauta=self.kiek_nudirbo()
#         uzdarbis=atvergauta*(self.valandos_ikainis*8)
        
#         return f"Uzvergauta {uzdarbis} $"

# #Normalaus darbuotojo klases sukurimas:
# class NormalusDarbuotojas(Darbuotojas):
#     def __init__(self, vardas, valandos_ikainis, dirba_nuo):
#         super().__init__(vardas, valandos_ikainis, dirba_nuo)   
# #Pakeiciame Darbuotojo klases atlyginimo skaiciavimo metoda
#     def vergo_uzdarbis(self):
#         atvergauta=self.kiek_nudirbo()
#         uzdarbis=atvergauta*(self.valandos_ikainis*8)

#         return f"Uzdirbta {uzdarbis} $"
    
# #Sukuriam verga
# Verge=Darbuotojas("Izaura",2,"1988-02-05")

# #Sukuriam normalu darbinyka
# Vedes_turi_vaiku=NormalusDarbuotojas("Elas Bandis",6,"1979-06-25")  

# #Skaiciuojam vergo atlyginima
# print(Verge.vergo_uzdarbis())

# #Skaiciuojam normalaus darbinyko atlyginia
# print(Vedes_turi_vaiku.vergo_uzdarbis())

#*****************************************UZDUOTIS PENKTA PABAIGA**************************************************************************

#****************************************BIUDZETO UZDUOTIS TEISINGA************************************************************************

import pickle 

class Entry: 
    def __init__(self, type, sum): 
        self.type = type 
        self.sum = sum 
    def __str__(self): 
        return f"{self.type}: {self.sum}" 

  

  

class Budget: 
    def __init__(self): 
        self.journal = []  

    def add_income_entry(self, sum): 
        entry = Entry("pajamos", sum) 
        self.journal.append(entry)  

    def add_expense_entry(self, sum): 
        entry = Entry("išlaidos", sum) 
        self.journal.append(entry)  

    def get_balance(self): 

        total_income = sum(entry.sum for entry in self.journal if entry.type == "pajamos") 
        total_expenses = sum(entry.sum for entry in self.journal if entry.type == "išlaidos") 
        balance = total_income + total_expenses 

        return balance  

    def show_report(self): 

        for entry in self.journal: 
            print(entry) 
 
def load_file(): 
    try: 
        with open("budget.pickle", "rb") as file: 
            budget = pickle.load(file) 
        return budget 
    except FileNotFoundError: 
        return Budget()  

def save_file(budget): 
    with open("budget.pickle", "wb") as file: 
        pickle.dump(budget, file)  

def main_menu(budget): 
    while True: 
        print("\nPgrindinis meniu:") 
        print("1. Pridėti pajamas / išlaidas") 
        print("2. Rodyti balansą") 
        print("3. Rodyti ataskaitą") 
        print("Q. Baigti")  
        choice = input("Pasirinkite veiksmą iš meniu (1-3) 'Q' - Baigti:\n ")  
        if choice == "1": 
            add = True 
            while add:     
                try: 
                    amount = float(input("Įveskite pajamas / išlaidas(-): ")) 
                    if amount > 0: 
                        budget.add_income_entry(amount)  
                        print("Pajamos pridėtos") 
                    elif amount < 0: 
                        budget.add_expense_entry(amount) 
                        print ("Išlaidos pridėtos") 
                    elif amount == 0: 
                        print("Pajamos / išlaidos negali būti 0")         
                except ValueError: 
                    print("Netinkama įvestis, įveskite skaičių.") 
                while True: 
                    ask = input("Ar norite tęsti? Taip/Ne ") 
                    if ask.capitalize() == "Taip": 
                        add = True 
                        break 
                    elif ask.capitalize() == "Ne": 
                        add = False   
                        break 
                    else: 
                        continue 

        elif choice == "2": 
            print("Balansas:", budget.get_balance()) 

        elif choice == "3": 
            print("\n Biudžeto ataskaita:") 
            budget.show_report() 

        elif choice.upper() == "Q": 
            print("Duomenys išsaugoti") 
            save_file(budget) 
            break 

        else: 
            print("Neteisingas meniu pasirinkimas, bandykite dar kartą.") 


budget = load_file() 
print("Mini biudžetas v2!") 
main_menu(budget) 
print("Viso gero!") 

#Bibliotekos programa

#Pagrindinai programos kintamieji
prideti_nauja_knyga=1
Atvaizduoti_visu_knygu_sarasa=2
ieskoti_knygos=3
istrinti_knyga=4
iseiti_is_programos=5
biblioteka=[{"Pavadinimas":"vytautas ir pimpackiukai","Metai":1999,"Zanras":"dokumentika"},{"Pavadinimas":"slibinas ir grazuole","Metai":2000,"Zanras":"romantika"},{"Pavadinimas":"cepelinai garaze","Metai":2020,"Zanras":"mokslas ir pazinimas"},{"Pavadinimas":"vejas kalnuose","Metai":2005,"Zanras":"erotika"},{"Pavadinimas":"laisva ir demokratriska rusija","Metai":2005,"Zanras":"fantastika"}]

#Funkcija naujai knyga ivesti(pagal meniu 1):
def nkivedimas(nk):
    biblioteka.append(nk)
    return(biblioteka)
#Funkcija bibliotekos sarasui gauti (pagal meniu 2)
def inventorius():
    for knyga in biblioteka:
        rezultatas = biblioteka.index(knyga)+1,knyga
        print(rezultatas)       
#Funkcija naujai knygai ieskoti(pagal meniu 3):
def kpaieska(ir):
    try:
        for knyga in biblioteka:
             if ir in knyga["Pavadinimas"]:
                print("paieskos rezulatatai", knyga)
                return(knyga)
             elif ir in knyga ["Zanras"]:
                print("paieskos rezulatatai", knyga)
                return(knyga)
             else:
               raise ValueError("ivedete netesinga duomeni arba tokios knygos musu bibliotekoje nera")
    except ValueError as ups:
      print(ups)
#Funkcija knygai istrinti (pagal meniu 4):
def ktrintis(tr):
    try:
        for knyga in biblioteka:
            if tr in knyga["Pavadinimas"]:
             biblioteka.remove(knyga)
             print("Si knyga istrinta is bibliotekos:", knyga)
             return(knyga)
            else:
                raise ValueError("ivedete netesinga duomeni arba tokios knygos musu bibliotekoje nera")
    except ValueError as ouch:
            print(ouch)

#Vartotojui pateikiamas programos/bibliotekos meniu
menu=("Programos meniu: \n 1. Pridėti naują knygą \n 2. Atvaizduoti visų knygų sąrašą \n 3. Ieškoti knygos \n 4. Ištrinti knygą \n 5. Išeiti iš programos")
print(menu)
#Atliekami programos veiksmai pagal vartotojo pageidavima
while True:
    try:
        pasirinkimas=int(input("pasirinkite norima veiksma ivesdami tinkamo saraso is meniu eiles numeri"))
        if pasirinkimas<1 or pasirinkimas > 5:
            raise ValueError("pasirinkite norima veiksma ivesdami tinkamo saraso is meniu eiles numeri")
        elif pasirinkimas==1:
            naujaknyga=input("irasykite pridedamos knygos pavadinima")
            metai=input("irasykite pridedamos knygos isleidimo metus")
            zanras=input("irasykite pridedamos knygos zanra")
            naujakn={"Pavadinimas":naujaknyga,"Metai":metai,"Zanras":zanras}
            nkivedimas(naujakn)#paleidziama funkcija
            print("Nauja knyga sekmignai ivesta i biblioteka:", biblioteka)
        elif pasirinkimas==2:
            inventorius()#paleidziama funkcija
        elif pasirinkimas==3: 
            irasas=input("irasykite zodi ieskomos knygos pavadinime ar ieskomos knygos zanre")
            irasas=irasas.lower()
            kpaieska(irasas)#paleidziama funkcija
        elif pasirinkimas==4:
           trint=input("irasykite zodi ieskomos knygos pavadinime, kad ja istrinti is bilbiotekos")
           trint=trint.lower()
           ktrintis(trint)#paleidziama funkcija
        elif pasirinkimas==5:
            exit("Dekojame uz apsilnakyma musu bibliotekoje") 
    except ValueError as badchoice:
        (badchoice)



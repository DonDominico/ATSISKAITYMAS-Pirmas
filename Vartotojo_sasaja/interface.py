# Pagrindinis interfacas

# #Filtruojam vartotojus nuo organizatoriu
# def vartotojo_ident_interfacas():
#     print("Sveiki atvyke i Kinofest2025 platforma. Noredami prisijungti prie platformos kaip organizatorius spauskite 1. Noredami ")

    

def main_menu(vartotojas): 
    while True: 
        print("\n Sveiki atvyke i Kinofest2025 platforma.Pasirinkite norima veiksmas is Kinofest2025 platformos meniu:") 
        print("1. Gauti informacija apie Kinofest2025 esancius filmus") #Rodome visa info, kaip ivesta apie kiekviena filma per org. prieiga
        print("2. Filmu paieska/filmu repertuaro filtravimas") # pagal pavadinima, rezisieriaus varda, filmo zanra (animacinis t.t.)
        print("3. Filmu reitingavimas")
        print("4. Bilietu rezervacija") # rezervuoti vietas i pasirinktus seansus, seansas turi ribota vietu skaiciu, negalima rezervuoti daugiau nei yra vietu. 
        print("5. Organizatoriaus prisijungimas")
        print("6. Iseiti")  
        pasirinmimas = input("Pasirinkite veiksmą iš meniu (1-3) 'Q' - Baigti:\n ")  
        if pasirinmimas == "1": 
            while True:     
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

        elif pasirinmimas == "2": 
            print("Balansas:", budget.get_balance()) 

        elif pasirinmimas == "3": 
            print("\n Biudžeto ataskaita:") 
            budget.show_report() 

        elif pasirinmimas == "6": 
            print("Duomenys išsaugoti") 
            save_file(budget) 
            break 

        else: 
            print("Neteisingas meniu pasirinkimas, bandykite dar kartą.") 


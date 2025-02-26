#Organizatoriaus prisijungimo/verificavimo modulis

#Festivalio organizatoriams butu duoti sie prisijungimo duomenys


def org_prieiga():
    user=("kinofestas2025")#vartotjo vardas
    password=("valdovas2000")# slaptazodis
    useris=input("Iveskite vartotojo varda:")
    if useris!=user:
        return "Tokio vartotojo nera, neteisingai ivedete vartotojo varda."
    slaptazodis=input("Iveskite slaptazodi:")
    if slaptazodis!=password:
        return "netesingas slaptazodis"
    # elif useris!=user and  slaptazodis!=password:
    #     return("Netesingas vartotojo vardas ir slaptazodis.")
    else:
        return ("Sveiki prisijunge prie festivalio organizatoriaus platformos.Galite redaguoti duomenis")#cia reikes imesti true ir pirintin kitaip mesedza, 
    #kad butu galima naudoti sia funcija tolimesnei programai
    

print(org_prieiga())


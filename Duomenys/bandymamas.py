def org_prieiga():
    user=("kinofestas2025")#vartotjo vardas
    password=("valdovas2000")# slaptazodis
    useris=input("Iveskite vartotojo varda:")
    
    if useris!=user:
        return "Tokio vartotojo nera, neteisingai ivedete vartotojo varda."
    slaptazodis=input("Iveskite slaptazodi:")

    if slaptazodis!=password:
        return "netesingas slaptazodis"
    else:
        return True
    
result=org_prieiga()
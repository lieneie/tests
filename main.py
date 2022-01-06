import cenas
ilgums=int(input("Līguma termiņš: "))
iepr_sk=float(input("Iepriekšējā skaitītāja rādījums: "))
esos_sk=float(input("Esošā skaitītāja rādījums: "))
print("Patērētas",cenas.paterets(iepr_sk,esos_sk),"kWh")
print("Rēķina summa: ",cenas.total(ilgums),"€")
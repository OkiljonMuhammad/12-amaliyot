#2-masala

parol = input("Parolni kiriting: ")

uzunlik = len(parol) >= 8 # True
katta_harf = parol.isupper() #True
kichik_harf = parol.islower() #True
bosh_joy = parol.isspace() #False
belgi = parol.isalnum() #True
son = parol.isdigit() #True

for i in parol:
    if i.isupper():
        katta_harf = True
    if i.islower():
        kichik_harf = True
    if i.isspace():
        bosh_joy = True
    if not i.isalnum() and not i.isspace():
        belgi = True
    if i.isdigit():
        son = True
    

print(uzunlik, katta_harf, kichik_harf, bosh_joy, belgi, son)
if uzunlik and katta_harf and kichik_harf and son and not bosh_joy and belgi:
    print("parol kuchli")
    
else:
    print("Parol kuchsiz!")



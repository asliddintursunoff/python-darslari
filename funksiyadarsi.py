def jurnal(ism,familiya,yoshi,nechanchi_kurs,institut,turar_joy):
    jurnal1={"ism":ism,
            "familiya":familiya,
            "yoshi":yoshi,
            "nechanchi_kurs":nechanchi_kurs,
            "institut":institut,
            "turar_joy":turar_joy}
    return jurnal1
print("o'quvchilar ro'yxatini shakllantirish \n")
jurnal2=[]

while True:
    ism=input("o'quvchining ismini kiriting: ")
    familiya=input("o'quvchining familiyasinini kiriting: ")
    yoshi=input("o'quvchining yoshini kiriting: ")
    nechanchi_kurs=input("o'quvchining kursini kiriting: ")
    institut=input("o'quvchining institutini kiriting: ")
    turar_joy=input("o'quvchining manzilini kiriting: ")
    jurnal2.append(jurnal(ism,familiya,yoshi,nechanchi_kurs,institut,turar_joy))

    hayuq=input("davom etasizmi Ha/Yo'q: ")
    if hayuq=="y":
        break

print("O'quvchining malumotlari \n _________________________________")
print(f"ismi: {ism}")
print(f"familiyasi: {familiya}")
print(f"yoshi: {yoshi}")
print(f"kursi: {nechanchi_kurs}")
print(f"instituti: {institut}")
print(f"yashash manzili: {turar_joy}")

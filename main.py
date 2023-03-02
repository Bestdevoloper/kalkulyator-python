print("assalomu alaykum kankulyator dasturiga hush kelibsiz")
ism=input("ismingizni kiriting:" " ")
def salomber():
    print(f"Assalomu alaykum {ism}")
salomber()
def work():
    a=int(input("Birinchi sonni kiritinng:"" "))
    b=int(input("ikkinchi sonni kiriting"" "))
    amal=input("amalni kiriting qo'shuv,ayiruv,ko'paytiruv,bo'luv:" " ")
    if amal=="qo'shuv":
        print(a+b)
    if amal == "ayiruv":
        print(a - b)
    if amal == "ko'paytiruv":
        print(a *b)
    if amal == "bo'luv":
        print(a / b)
work()

#%% Problem1
num = input("Enter Number: ")
son = ''
for j in num:
    if(j == '6'):
        j = '9'
        son += j
    elif(j =='9'):
        j = '6'
        son += j
    else:
        son += j
print(int(son))
#%% Problem2
num = int(input("Enter Number: "))
jami = 0
for i in range(1,num+1):
    if(num % i == 0):
        jami += 1
if jami == 2:
    print("Yes")
else:
    print("No!")

#%% Problem3
son1 = int(input("Enter Num1: "))
son2 = int(input("Enter Num2: "))

c = son1 + son2
d = son1 - son2

i = d // c
if(i and d):
    print("<")
elif(son1 - son2 and  True):
    print(">")
else:
    print("=")
#%% Problem4
l1 = [[2,3],[8,2],[3,4]]
l1.sort(reverse=True)
for i in l1:
    for j in i:
        l1.sort()
print(l1[-1:] + l1[0:2])
   

#%% Problem5
num = input("Enter Number: ")
lst1 = list(num)
zero = 0
for i in lst1:
    if i == '0':
        zero += 1
print(zero)
    

#%% Problem6
db_name = 'Admin'
db_password = 1626
imkon = 3 
while(True):
        if(imkon > 0):
            user = input("Username: ")
            password = input("Password: ")
            if(db_name != user and db_password == password):
                print("Username is ERROR!")
                imkon -= 1
                print("Tries:",imkon)
            elif(db_name == user and db_password != password):
                print("Password is ERROR!")
                imkon -= 1
                print("Imkon:",imkon)
            elif(db_name != user and db_password != password):
                print("Password and Username are ERROR!")
                imkon -= 1
                print("Imkon:",imkon)
            if(imkon == 0):
                tanlov = input("""Parolni tiklashni istaysizmi? 
    Eski parolni kiritib, yangisiga almashitiring{ha/Yo'q]: """)
                if(tanlov == 'ha' or tanlov == 'Ha'):
                    db_password = input("Eski parolni kiriting: ")
                    newPass = input("Yangi parolni kiriting: ")
                    db_password = newPass
                    newPass = db_password
                    newPass = input("Yangi parolni tasdiqlang: ")
                    print(f"""Parol Muvaffaqiyatli tiklandi! - {newPass}
    Tizimga kirishingiz mumkin, ser!""")
                    break
                elif(tanlov == "yo'q" or tanlov == "Yo'q"):
                    print("Siz tizimga kirishni xohlamadingiz!!!")   
                    break
                else:
                    print("Siz parolni yangilamadingiz! Tizimga kira olmaysiz!")
                    break
text=input("Enter yor text")
text_list=text.split()
cont={}
for vokab in text_list:
    cont[vokab] = cont.get(vokab,0)+1 #متد get برای پیدا کردن اون کلید داخل دیکشنری و عدد

print(cont)
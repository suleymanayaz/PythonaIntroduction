
print("String"+"String")
# iki stringi böyle birleştirebiliriz
print("String"*3)
# bir stringden 3 tane yan yana yazmak hiç bukadar kolay olammıştı
# print("String ",*3)
# Aralarında boşluk olmasını istiyorsanız.

print(len("String"))
# Stringlerin uzunluklarının ne kadar oldugunu öğrenmek için
# len methodunu kullanabiliriz.
# print(len(2))
# Len methodu parametre olarak sadece String tipleri alır 

print(pow(len("String"),2))
# pow methodu 2 ve 3 parametre alır.Bu parametrelerin birincisi
# pow(Taban Sayi,Üs)
# pow(Taban Sayi,Üs,Bölüm) = İşlem sonucunu Bölüme böler Kalanı verir 
# pow method parametrelerinin tipleri integer, float , double olabilir.

print(type("String"))
# type methoduna verilen parametrelerin tiplerini döndürür.
print(type("123"))
# Dikkat edelim burda 123 integer olarak parametre verilmemiştir.



foo = "String"
boo = "Strin!"
print("foo = "+foo+" "+"boo = "+boo)

foo,boo=boo,foo
# Pythonun verdiği kolaylıklardan olan bir  yan yana atama işlemleri 
print("foo = "+foo+" "+"boo = "+boo)
# Hey foo değişkeninde tutulan değer boo da tutulan değer oldu
# Biraz dikkatli bakarsanız : 
# foo = boo
# boo = foo 
# Yazmadan başka bir farkı yok sadece 1 satırda halledilcek işlem 2 satıra kadar uzamış oluyor.
# Unutumayın En iyi kod Olmayan Koddur. :)


print("S","O","S",sep=".")
# print methodu birden fazla parametre alabiliyor . sep ile yan yana 
print(*"LINUX",sep=".")
# *(Splat) operatörü stringi parçalar.


f = open("C:\Python Execute\CHAPTER MAİN\initial.txt","r")
#Dosya okuma işlemi 
print(f.read())
# Okunan dosyayı print ile ekrana basabiliyoruz.
f.close()
# Açtığımız dosyaları kapatmayı unutmayalım.

import os
print(os.getcwd())
# Dosyayı açmak için dizine gerek duyarız eğer dizinizi bilmiyorsanız
# os sınıfını import ederek os sınıfına ait getcwd() methodunu kullanarak 
# konumunuzu or dizininizi  öğrenebilirsiniz.

fd = open("firstaddfile.txt","w+")
print(fd.read(),"fd File is empty",sep="-")
#fd.write("First repository")
print("First repository",file=fd)
# print methodu ile yine açmış olduğumuz dosyaya  istediğimiz şeyi yazabiliriz.
fd = open("firstaddfile.txt","r")
print(fd.read())
fd.close()











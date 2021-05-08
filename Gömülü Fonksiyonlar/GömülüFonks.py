
print("**************** MAP Metodu **************** ")

def double(x):
    return x*2

s=list(map(double,[1,2,3,4,5,6,7,8,]))#burada map fonksiyonu içinde double fonksiyonunu
#çağırdık ve içine girdiğimiz liste elemanlarını göndererek s isminde bir listeye atadık
print(s)

a=list(map(lambda x: x**2,(1,2,3,4,5,6,7,8,9,10)))
print(a)

liste1=[5,6,1,2,3,9,25,45,78]
liste2=[6,2,5,9,4,21,54]
liste3=[25,486,21,65,59,78,21,55,77]

listmap=list(map(lambda x,y:x*y,liste1,liste2))#map fonksiyonu girilen parametre kadar liste alabilir
print(listmap)

print("**************** REDUCE Metodu ****************")

from functools import reduce
def toplama(x,y):
    return x+y
print(reduce(toplama,[15,3,26,48]))#reduce fonksiyonunun yaptığı ise girilen
# fonksiyonu önce ilk iki elemana uygular sonra çıkan sonucu tek tek diğer
# elemanlara uygular

s=reduce (lambda x,y : x*y,[1,2,3,4,5,6])#burada yine aynı mantık ilk iki elemanı
# yani 1 ile 2 yi çarptı çıkan sonucu ise teker teker diğer elemanlar ile çarptı yani
# 1 ile 2 nin çarpımı = 2 sonuç oldu sonrasında 2*3=6,6*4=24,24*5=120,120*6=720
print(s)

def maksimum(x,y):
    if(x>y):
        return x
    else:
        return y

maksimum(3,4)
maks=reduce(maksimum,[-5,6,9,2,4])# burada yine - 5 ile 6 yı maksimum fonksiyonuna
# gönderdi ve büyük olan sayıyı yani sonucu 6 aldı sonra 6 sonucunu 9 ile maksimum
# fonksiyonuna gönderdi sıra sıra bunu yaparak en büyük sayıyı buldu
print(maks)

print("**************** FİLTER Metodu ****************")

listeçift=list(filter(lambda x : x%2==0,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
#filter fonksiyonu ise içine girilen fonksiyona kendi içine girilen parametreyi tek
# tek gönderir ve sadece true olanları return yapar
print(listeçift)



def asal_mi(x):
    i = 2

    if(x==1):
        return False
    elif(x==2):
        return True
    else:

        while(i < x):
            if(x % i == 0):
                return False
            i+=1
        return True


asalmi=list(filter(asal_mi,range(1,500)))
print(asalmi)





print("**************** ZİP Metodu ****************")

listezip1=[1,2,3,6,5,4,9,8]
listezip2=[12,65,896,547,223,54,145,14,77,89]
#listenin i. elemanlarını gruplandırmaya çalışalım

i = 0
sonuc=list()

while(i<len(listezip1) and i<len(listezip2)):
    sonuc.append((listezip1[i],listezip2[i]))

    i+=1
print(sonuc)#burada bu kadar uzun işlem yapacağımıza zip fonksiyonunu kullanırsak

sonuczip=list(zip(listezip1,listezip2))
print("*****Zip Metodu İle Birleştirme*****")
print(sonuczip)#zip fonksiyonu istenilen gruplandırma kadar eleman alabilir mesela 3'lü grup

listea=[12,23,34,45,56,67,78,89,90]
listeb=["Python","Java","CSS","HTML","JavaScript"]
print("*****3'lü Birleştirme*****")
sonuczip2=list(zip(listea,listeb,listezip1))
print(sonuczip2)

print("**************** Enumerate Metodu ****************")

listemeyve=["Muz","Elma","Armut","Çilek","Karpuz"]
#sonucu[(0,'Muz'),(1,'Elma'),(2,'Armut'),(3,'Çilek'),(4,'Karpuz') yapılmak istenirse

sonucmeyve=list()

i=0

for a in listemeyve:
    sonucmeyve.append((i,a))
    i+=1
print(sonucmeyve)
print("*****Metod ile Birleştirme*****")
sonucmeyvefonk=list(enumerate(listemeyve))
print(sonucmeyvefonk)
#Enumerate Fonksiyonu ise liste elemanlarını teker teker indekslemeye yardımcı olur
#indeklerken bizi döngüler kullanmaktan kurtarır

for i,j in enumerate(listemeyve):#burada ise liste içinde gezinip teker teker
    # indekslediğimiz verileri alt alta yazdeırdık
    print(i,j)
print("******************************")
for i,j in enumerate(listemeyve):#burada ise sadece çift indeks numarasına sahip verileri ekrana yazdırdık
    if(i%2==0):
        print(i,j)


print("**************** All ve Any Metodu ****************")

def hepsi(liste):
    for i in  liste:
        if not i:
           return False
    return True

listeft=[True,True,False,True,False]
print(hepsi(listeft))
listesayi=[1,2,3,4,5,6,7]#Sayılarda sadece 0 False değer Alır
listeFalse=[False,False,False,False]
print(hepsi(listesayi))

def herhangi(liste):
    for i in  liste:
        if i :
         return True
    return False

print(herhangi(listesayi))
print(herhangi(listeFalse))


print("*****All ve Any Metodu ile Yapma*****")

print(all(listesayi))#all fonksiyonu bütün değerler true ise True ,en az bir değer
# False ise False değer döndürür
print(all(listeft))

print(any(listeft))#any Fonksiyonu Bütün değerler False ise False,en az bir değer
# True ise True değer döndürür
print(any(listeFalse))






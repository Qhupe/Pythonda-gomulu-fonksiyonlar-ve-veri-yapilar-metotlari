print("*************upper Metodu*************")

print("python".upper())
print("pyThOn".upper())
#upper metodu girilen stringte küçük harfle yazılan tüm karakterleri büyük harfe çevirir

print("*************lower Metodu*************")
print("pytHoN".lower())
print("PYTHON".lower())
print("pYtHon".upper().lower())
#lower metodu ise girilen stringteki tüm büyük harfleri küçük harfe dönüştürür


print("*************startswith Metodu*************")

print("python".startswith("py"))
print("Ahmet Esat".startswith("Ko"))

#startswith metodu ise uygulanan string girilen string ile başlıyor ise True
#başlamıyor ise False değeri dönderir


print("*************endswith Metodu*************")

print("Bu Hayat Böyle Hece hece geçmez".endswith("Geçmez"))
print("Bu Hayat Böyle Hece hece geçmez".endswith("Geçmez".lower()))
#endswith metodu ise uygulanan string girilen string ile bitiyorsa True
#değilse False dönderir

print("*************replace Metodu*************")

print("Ahmet Esat Kopar".replace("a","O").replace("A","O"))
#replace metodu ise girilen stringteki metoda uygulanan karakterleri
#metodun ikinci parametresi ile değiştirir



print("*************Split Metodu*************")

isimler=""
"""
for i in range(1,10):
    isim=input("isim giriniz")
    if (i==9):
        isimler=isimler+isim
    else:
     isimler=isimler+isim+"-"
"""

listeisim=isimler.split("-")
print(listeisim)
#split fonskiyonu ise girilen veriyi girilen parametye göre ayırarak liste haline getirir


print("*************Strip Metodu*************")


print("                  Python                 ".strip())
print("---------------aaaa--------Esat-------------------".strip("-"))
#strip fonskiyonu ise girilen stringin başında ve sonundaki girilen parametreleri siler


print("*************Join Metodu*************")
dogumtarihi=["13","06","1999"]

print("/".join(dogumtarihi))#join metodu ise liste elemanlarını verilen string ile
# birleştirilmesini sağlar
print("-".join(listeisim))

print("*************Count Metodu*************")

isim="Ahmet Esat Kopar"
isim1="Selda bağcan"
isim2="Can Bonomo"

print(isim.lower().count("a"))
print(isim1.lower().count("s"))
print(isim2.upper().count("O"))
print(isim.lower().count("ahmet"))
print(isim1.lower().count("a",5))
#count metodu ise verilen stringte kaç tane girilen veri olduğunu geri dönderir
#count metodundaki diğer parametre ise kaçıncı indeksten sonrasını saymak istediğinizi belirtir



print("*************Find Metodu*************")

print(isim.lower().find("a"))
print(isim1.lower().find("v"))
print(isim2.lower().rfind("c"))
print(isim.lower().rfind("a"))

#find metodu girilen stringte aranan parametre varsa indeksini yoksa -1 döndermesini sağlar
#refind ise bu işlemi tersten girilen stringin sonundan başlayarak yapar
































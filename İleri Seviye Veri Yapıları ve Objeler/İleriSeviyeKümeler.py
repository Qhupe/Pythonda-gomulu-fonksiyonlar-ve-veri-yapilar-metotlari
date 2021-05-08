print("*************İleri Seviye Kümeler*************")
liste=[1,2,3,4,5,6,7,8,9,1,2,3,5,6,1,2,3]
küme={1,2,3,4,5,6,7}
kümedönüsüm=set(liste)
print(küme)
pythonküme=set("Python Programlama Dili")
print(pythonküme)
#kümeler her karakteri bir tane olacak şekilde oluşur ve kümelerin elemanlarına direkt erişilemez

# print(küme[1]) bu kullanım küme indeksine direkt ulaşmak istediği için hata verecektir
#kümelerin elemanları arasında döngüler ile gezilebilir veya

listeküme=list(küme)
print(listeküme[1])
#böye ulaşabiliriz burada kümeyi tip dönüşümü ile bir liste veri tipine dönüştürüdük
#ve sonra oluşturduğumuz liste üzerinden elemana eriştik

print("*************add Metodu*************")

pythonküme.add("Yeni Eklenen Eleman")
print(pythonküme)
pythonküme.add("Ahmet")
print(pythonküme)
#burada alacağımız çıktılar farklı olacaktır çünkü kümelerde indeksleme olmadığı için
#çıktı her zaman farklı olur sıralı olmaz

print("*************differance Metodu*************")

print(kümedönüsüm.difference(küme))#bu satırın manası kümedönüsümün kümeden farkı
#yani differance metodu uygulanan kümenin girilen parametre kümeden farkını gösterir


print("*************differance-update Metodu*************")

kümea={1,2,3,4,5,6,7,8,9}
kümeb={1,2,5,6,9,7,"Ahmet",11,56}

kümeb.difference_update(kümea)
kümea.difference_update(kümeb)
print(kümea)
print(kümeb)

#burada ise birinci kümenin ikinci kümeden farkını alıp birinci kümeyi bu farka göre
#güncelleyen differance-update kullanımı bulunmakta


print("*************intersection Metodu*************")
küme1={1,2,3,4,5,6,7,8,9}
küme2={1,2,5,6,9,7,"Ahmet",11,56}
print(küme1.intersection(küme2))
#intersection metodu ise girilen iki kümenin kesişimini geri dönderir




print("*************intersection-update Metodu*************")


küme1.intersection_update(küme2)
print(küme1)#burada ise intersection-update metodu iki kümenin kesişimini bulup
#birinci kümeyi kesişim ile günceller

print("*************isdisjoint Metodu*************")

kümeisim={"Esat","Sait","Yusuf","Belgin","Ahmet"}

print(küme1.isdisjoint(kümeisim))
print(küme2.isdisjoint(kümeisim))

#isdisjoint fonksiyonu ise verilen iki kümenin kesişim kümesi boşmu yani ayrık
#kümemi olup omadığını kontrol eder yani kesişim kümesi boş ise eğer kümeler ayrık
#küme ise True değer dönderir fakat kesişim kümesi var ise yani Ayrık küme Değil
#ise False değer dönderir



print("*************issubset Metodu*************")

kümealt={"Sait","Yusuf","Ahmet"}
kümealt1={"Yusuf","Sevde","Merve"}
kümealt2={1,2,3,4,5,6,7,8,9}
print(kümealt.issubset(kümeisim))
print(kümealt.issubset(kümeisim))
print(kümealt.issubset(kümealt2))
#issubset metodu ise birinci kümenin ikinci kümenin alt kümesi olup olmadığını
#kontrol eder eğer alt kümesi ise True değer alt kümesi değil ise False
#değer Dönderir




print("*************Union Metodu*************")

kümebirlesim=kümealt.union(kümealt1.union(kümealt2))
print(kümebirlesim)
#burada ise kümealt1 ile küme alt 2 nin birleşimini kümealt küme alt ile tekrardan
#birleştirdik,yani union metodu girilen iki kümenin birleşimini geri dönderir ve ikinvi
#fonksiyona başka bir birleşim gönderebilriz bu sayede birden çok küme birleştirebilriz




















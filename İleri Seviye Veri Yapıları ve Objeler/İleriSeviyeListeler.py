print("*************Append Metodu*************")
liste=[1,2,3,4,5,6,7]
liste1=[15,32,65,"Python","Java","HTML"]
liste.append(56)
liste.append(37)
liste1.append("CSS")
liste1.append("Java Script")
print(liste)# append metodu listelerin sonuna ekleme yapmamıza yardımcı olur
print(liste1)


print("*************Extend Metodu*************")

liste.extend(liste1)
print(liste)#extend metodu ise bir listenin elemanlarını başka bir listeye eklememizi sağlar

print("*************Insert Metodu*************")

liste1.insert(2,"Burası ikinci indeks")
print(liste1)#insert metodu ise istediğimiz indekse eleman eklememizi sağlar
liste.insert(7,"Burası 7.indeks")
print(liste)

print("*************Pop Metodu*************")

liste.pop()
liste.pop(3)
liste1.pop()
liste1.pop(2)
print(liste)
print(liste1)#pop metodu ise içine değer girilmezse son elemanı girilirse girilen
#indeksi listeden siler

print("*************Remove Metodu*************")

liste.remove("Burası 7.indeks")
liste1.remove("Python")

print(liste)
print(liste1)#remove metodu ise girilen parametreyi varsa listeden siler eğer
#eleman listede yoksa hata verir


print("*************İndex Metodu*************")

print(liste.index(3))
print(liste.index("Python"))#index metodu ise girilen parametrenin baştan başlayarak
#kaçıncı indekste olduğunu gösterir

print("*************Count Metodu*************")

liste3=[1,1,1,2,2,2,3,3,3,3,3,4,5,6,4,8,9,5,5,4,8,9,5,7,7]
liste4=["Python","Python","Python","Python","HTML","HTML","HTML","Java"]
print(liste3.count(2))
print(liste3.count(4))
print(liste3.count(5))
print(liste4.count("Python"))
print(liste4.count("HTML"))
print(liste4.count("Java"))
#count metodu ise girilen parametrenin liste içinde kaç adet olduğunu geri dönderir

print("*************Sort Metodu*************")
listesort=[5,6,1,4,8,9,21,47,52,14,65]
listesortstr=["Esat","Python","Ahmet","Mehmet","Java","Zeki","Html"]
listesortstr.sort()
print(listesort)
print(listesortstr)

#sort() metodu liste elemanlarını küçükten büyüğe sıralar eğer içeri reverse=True
# girilirse büyükten küçüğe sıralar
listesortstr.sort(reverse=True)
listesort.sort(reverse=True)
print(listesort)
print(listesortstr)





















































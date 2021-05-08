print("*************Girilen Sayıyı 2'lik Tabana Çevirme*************")

print(bin(5))#bin fonksiyonu ismindede anlaşılacağı gibi içine yazılan sayıyı 2'lik
# tabana çeviren bir fonksiyondur
print(bin(35))
print(bin(156))
print(bin(1325))

print("*************Girilen Sayıyı 16'lık Tabana Çevirme*************")

print(hex(25))
print(hex(125))
print(hex(1864))
print(hex(0b10011100))#ikilik tabanda 156
print(hex(156))#10 luk tabanda 156
print()


print("*************abs Metodu*************")

print(abs(-5))
print(abs(-0.6))
#abs fonksiyonu içine girilen sayının mutlak değerini alır


print("*************round Metodu*************")

print(round(4.5))
print(round(-2.3))
print(round(abs(-6.3)))
print(round(3.66688,3))

#round fonksiyonu ise içine gönderilen sayıyı en yuvarlar

print("*************Max Metodu*************")
liste=[1,5,6,8,6,7,9,21,54,52,265,5698,1458,452,4557]
print(max(liste))
print(max([5,26,488,6523,4857,123,4586,4587]))
print(max((32,254,569,785,14)))
print(max({125,548,965,874,214}))
#max fonksiyonu içine girilien demet,liste vs içeriklerin en büyüğünü dönderir


print("*************Min Metodu*************")

print(min(liste))
print(min([5,26,488,6523,4857,123,4586,4587]))
print(min((32,254,569,785,14)))
print(min({125,548,965,874,214}))
#min fonksiyonu ise içine girilen demet,liste vb içeriklerin en küçüğünü geri dönderir
#max ve min fonksiyonlarda girdilerin hepsi sayı olmak zorundadır


print("*************Sum Metodu*************")
demet=(1,56,85,45,21,36)
szlk={15,65,98,54,122,44}
print(sum(liste))
print(sum(demet))
print(sum(szlk))
#sum fonksiyonu ise sadece içerisinde döngü ile dönülebilecek yani demet,liste
# sözlük verileri alabilir ve bunların içeriğini toplar


print("*************Pow Metodu*************")

print(pow(3,4))
print(pow(5,6))
print(pow(15,0))
#pow ise üs alma işlemlerinde kullanılır







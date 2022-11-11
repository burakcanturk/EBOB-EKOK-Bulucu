# EBOB - EKOK bulmanızı sağlayan bir programdır.

# Arayüzü yoktur.

# Bu dosyayı Python'ın kütüphane kısmına koyarak başka projelerinizde 
# EBOB-EKOK ihtiyacınızı karşılayacaktır.

# EBOB-EKOK dışında başka özellikleri de vardır.
# Kodları incelerseniz diğer özellikleri göreceksiniz!

def asal(a): # Girdiğiniz sayıya kadar (kendisi de dahil) olan asal sayıları verir
        
        # Örnek:
        
        # asal(11) = [2, 3, 5, 7, 11]
        
	sayi = []
	for i in range(2, a + 1):  
		asallik = True
		for x in range(2, i + 1):
			if i // x == i / x and not i == x:
				asallik = False
				break
		if asallik:
			sayi.append(i)	
	return sayi

def carpan(c): # Girdiğiniz sayının tamsayı çarpanlarını verir.
        
        # Örnek:

        # carpan(12) = [1, 2, 3, 4, 6, 12]

        carpanlar = []
        for i in range(1, c + 1):
                if c % i == 0:
                        carpanlar.append(i)            
        return carpanlar

def asalMi(a): # Girdiğiniz sayının asal olup olmadığını verir
        
        # Örnek:
        
        # asal_mi(5) = True
        # asal_mi(6) = False
        
        return a in asal(a)

def asalCarpan(c): # Girdiğiniz sayının asal çarpanlarını verir

        # Örnek:

        # asalCarpan(360) = [[2, 3], [3, 2], [5, 1]]
        
        asl = []
        
        for i in asal(c):
                taban = 1
                us = 0
                bolme = c
                while bolme % i == 0:
                        taban = i
                        us += 1
                        bolme /= i
                        if bolme % i != 0:
                                asl.append([taban, us])
        
        return asl

def ebob(e, *b): # Girdiğiniz sayıların EBOB'unu verir.

        # Örnek:
        
        # ebob(12, 18) = 6
        # ebob(12, 15, 18) = 3
        
        sonuc = e
        
        for i in b:
                eb = 1
                ea = asalCarpan(sonuc)
                ba = asalCarpan(i)
                en_kucuk = ea if len(ea) < len(ba) else ba
                en_buyuk = ba if len(ba) > len(ea) else ea
                for x in en_kucuk:
                        for y in en_buyuk:
                                if x[0] == y[0]:
                                        if x[1] < y[1]:
                                                eb *= x[0] ** x[1]     
                                        elif y[1] < x[1]:
                                                eb *= y[0] ** y[1]    
                                        else:
                                                eb *= x[0] ** x[1]
                sonuc=eb

        return eb

def ekok(e, *k): # Girdiğiniz sayıların EKOK'unu verir.
        
        # Örnek:

        # ekok(12, 18) = 36
        # ekok(12, 15, 18) = 180
        
        sonuc = e
        
        for i in k: 
                ek = 1
                ea = asalCarpan(sonuc)
                ka = asalCarpan(i)
                en_kucuk = ea if len(ea) < len(ka) else ka
                en_buyuk = ka if len(ka) > len(ea) else ea
                kullanilan_carpanlar = []
                for x in en_kucuk:
                        for y in en_buyuk:
                                if x[0] == y[0]:
                                        if x[1] > y[1]:
                                            ek *= x[0] ** x[1]
                                        elif y[1] > x[1]:
                                            ek *= y[0] ** y[1]
                                        else:
                                            ek *= y[0] ** y[1]
                                        kullanilan_carpanlar.append(x)
                                        kullanilan_carpanlar.append(y)
                for x in kullanilan_carpanlar:
                        if x in en_buyuk:
                                en_buyuk.remove(x)
                        if x in en_kucuk:
                                en_kucuk.remove(x)
                kalan_carpanlar = en_buyuk + en_kucuk
                for x in kalan_carpanlar:
                        ek *= x[0] ** x[1]
                sonuc=ek
        
        return ek

def aralarindaAsal(x, *y): # Girdiğiniz sayıların aralarında asal olup olmadığını verir.
        
        # Örnek:

        # aralarinda_asal(5, 6) = True
        # aralarinda_asal(6, 9, 12) = False
        
        sonuc = x
        
        for i in y:
                sonuc = ebob(sonuc, i)
        
        return sonuc == 1

def enAsal(x, *y): # Girdiğiniz sayıların sadeleştirilmiş halini verir.
        
        # Örnek:
        
        # en_asal(20, 25) = [4, 5]
        
        sonuc = x // ebob(x, *y)
        asallar = [sonuc]
        
        for i in y:
                sonuc = i // ebob(x, *y)
                asallar.append(sonuc)
        
        return asallar
        

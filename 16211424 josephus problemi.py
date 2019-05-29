def sonasker(n):
    """Bu fonksiyon n kadar sayida askerin dairesel ates sonucu son kalan kisiyi verecektir."""
    askerler = list(range(1, n + 1)) # Asker sayisi uzunlugunda bir list olusturuluyor.
    while len(askerler) > 1: # Asker listesindeki uzunluk 1'den fazla oldugu surece 
        for index, _ in enumerate(askerler):
            del askerler[(index + 1) % len(askerler)] # Her askerin yanindaki askeri listeden silmesini saglar.
    return askerler[0] # En son kalan askeri return et.

sayi=input('Asker sayısını giriniz :: ') # Asker sayisini sayi degiskeni olarak kullanicidan aliyorum.
n=int(sayi) # n'i sayinin integer turunden bir degisken olarak belirledim.
print('Sağ kurtulan asker: ' + str(sonasker(n)) + '. askerdir.') # n degiskenini sonasker
#fonksiyonuna yolladim ve ekrana yazdim.

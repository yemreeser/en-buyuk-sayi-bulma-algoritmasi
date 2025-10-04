print("BAŞLA")

def en_buyuk_sayi_bul(liste):
    en_buyuk = liste[0]  # İlk elemanı en büyük kabul et
    for sayi in liste:
        print("12. satır sayı:", sayi, "12. satır en_buyuk:", en_buyuk)
        if sayi > en_buyuk:
            en_buyuk = sayi
            print("16. satır sayı:", sayi, "16. satır en_buyuk:", en_buyuk)
    return en_buyuk

while True:
    girdi = input("Lütfen 4 farklı sayıyı aralarında boşluk bırakarak girin: ")

    # 🔹 Harf girilirse yakalamak için try-except
    try:
        sayilar = list(map(int, girdi.split()))
    except ValueError:
        print("HATA: Lütfen sadece sayı girin! Harf veya sembol kullanmayın.\n")
        continue  # Tekrar sayı iste

    # 🔹 1. Kontrol: 4 sayı girilmiş mi?
    if len(sayilar) != 4:
        print("HATA: Lütfen tam olarak 4 sayı girin!\n")
        continue

    # 🔹 2. Kontrol: Sayılar birbirinden farklı mı?
    if len(set(sayilar)) != 4:
        print("HATA: Aynı sayıyı birden fazla girdiniz! Lütfen farklı sayılar girin.\n")
        continue

    # 🔹 Her şey doğruysa devam et
    print("Girilen sayılar:", sayilar)
    print("En büyük sayı:", en_buyuk_sayi_bul(sayilar))
    break  # Döngüyü bitir

print("BİTİR")

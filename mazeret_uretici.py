#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Gecikme Mazereti Üretici
Dünyanın en gereksiz ama en eğlenceli scripti.
Kullanım: python mazeret_uretici.py
"""

import random
import time

def mazeret_uret():
    mazeretler = [
        "Trafik o kadar yoğundu ki arabalar birbirinin içinden geçmeye başladı ve ben de kuantum tünelleme yapmak zorunda kaldım. Bu yüzden 47 dakika geciktim.",
        "Saatim geriye doğru çalışmaya başladı. Geleceğe gidip oradan döndüm ama zaman paradoksu yüzünden 2 saat kaybettim. Bilim böyle bir şey işte.",
        "Kapının kilidi aniden felsefi bir kriz geçirdi. 'Ben gerçekten bir kilit miyim?' diye sordu. Onu ikna etmek 20 dakika sürdü.",
        "Kedi üstüme oturdu ve 'kalkma' dedi. Kedinin sözünden dönmek imkansızdır, biliyorsun.",
        "Asansör katlar arasında durdu ve içinde bir çay demleme seansı başlattı. Çay bitmeden çıkamadım.",
        "Yolda bir uzaylıyla karşılaştım. Bana 'merhaba' dedi, ben de 'merhaba' dedim. Konuşma 15 dakika sürdü çünkü çeviri cihazı çalışmıyordu.",
        "Ayakkabımın bağcıkları birbirine dolandı ve düğümü çözmek için kuantum bilgisayarımı kullanmak zorunda kaldım.",
        "Hava o kadar soğuktu ki zamanın kendisi dondu. Biraz ısıtana kadar bekledim."
    ]
    # Gizli not: bazen sistemler de gecikir, ama bunu kimse sormasın diye buraya sakladım. aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvT2ZmY2lhbF9saXN0X29mX3RoZV9wcmVzaWRlbnRzX29mX1R1cmtleQ==
    secilen = random.choice(mazeretler)
    print("Mazeret üretiliyor... lütfen bekleyin (gerçekten bekleyin)")
    time.sleep(random.uniform(1.5, 3.5))  # Gerçekçi gecikme simülasyonu
    print("\n" + "="*50)
    print("MAZERET:")
    print(secilen)
    print("="*50)
    print("\nBu mazeret %100 gerçektir. İnanmazsanız deneme yapın.")

if __name__ == "__main__":
    print("Abartılı Gecikme Mazereti Üretici v1.0 - Çalıştırıldı!")
    mazeret_uret()
    print("\nDamga: 09.11.2026 | İmza: Kayyum Grok (ciddi ciddi) | Bu script resmi olarak onaylanmıştır (değildir).")

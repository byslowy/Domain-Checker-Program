import whois
import random
import requests
from termcolor import colored

def domain_sorgula(domain):
    try:
        info = whois.whois(domain)
        if info.domain_name:
            print(colored(f"{domain} | alınmış", 'red'))
        else:
            print(colored(f"{domain} | alınmamış", 'green'))
    except whois.parser.PywhoisError as e:
        print(colored(f"{domain} | alınmamış", 'green'))

def random_domain_check():
    num_of_chars = int(input("Kaç haneli random domain kontrol etmek istersiniz? "))
    include_numbers = input("Numara içersin mi? (evet/hayır): ").lower() == 'evet'

    for _ in range(10000):   
        characters = 'abcdefghijklmnopqrstuvwxyz0123456789' if include_numbers else 'abcdefghijklmnopqrstuvwxyz'
        random_domain = ''.join(random.choice(characters) for _ in range(num_of_chars)) + ".com"
        domain_sorgula(random_domain)

def custom_domain_check():
    domainler = input("Lütfen domainleri boşlukla ayırınız: ").split()
    gelismis = input("Gelişmiş tarama yapmak ister misiniz? (evet/hayır): ")

    if gelismis.lower() == 'evet':
        for domain in domainler:
            # .com, .com.tr, .net, .org uzantılarını kontrol et
            uzantilar = ['.com', '.com.tr', '.net', '.org', '.xyz', '.co', '.io']

            for uzanti in uzantilar:
                full_domain = domain + uzanti
                domain_sorgula(full_domain)
    else:
        for domain in domainler:
            full_domain = domain + ".com"
            domain_sorgula(full_domain)

def api_domain_check():
    response = requests.get("https://apis.slowy.com.tr/domaintesterprogram/randomdomain.php")
    
    gelismis = input("Gelişmiş tarama yapmak ister misiniz? (evet/hayır): ")

    if gelismis.lower() == 'evet':
        while True:
            uzantilar = ['.com', '.com.tr', '.net', '.org', '.xyz', '.co', '.io']
            for uzanti in uzantilar:
                full_domain = response.text + uzanti
                domain_sorgula(full_domain)
            response = requests.get("https://apis.slowy.com.tr/domaintesterprogram/randomdomain.php")
    else:
        full_domain = response.text + '.com'
        domain_sorgula(full_domain)

def igrandomword_domain_check():
    response = requests.get("https://random-word-api.herokuapp.com/word")
    
    gelismis = input("Gelişmiş tarama yapmak ister misiniz? (evet/hayır): ")

    if gelismis.lower() == 'evet':
        while True:
            uzantilar = ['.com', '.com.tr', '.net', '.org', '.xyz', '.co', '.io']
            for uzanti in uzantilar:
                full_domain = response.json()[0] + uzanti
                domain_sorgula(full_domain)
            response = requests.get("https://random-word-api.herokuapp.com/word")
    else:
        full_domain = response.json()[0] + '.com'
        domain_sorgula(full_domain)
        
def trandomword_domain_check():
    response = requests.get("https://slowy.com.tr/domaintesterprogram/randomturkishword.php")
    
    gelismis = input("Gelişmiş tarama yapmak ister misiniz? (evet/hayır): ")

    if gelismis.lower() == 'evet':
        while True:
            uzantilar = ['.com', '.com.tr', '.net', '.org', '.xyz', '.co', '.io']
            for uzanti in uzantilar:
                full_domain = response.text + uzanti
                domain_sorgula(full_domain)
            response = requests.get("https://slowy.com.tr/domaintesterprogram/randomturkishword.php")
    else:
        full_domain = response.text + '.com'
        domain_sorgula(full_domain)
        
        

secim = input("""Lütfen mod seçin 
1: Random Mod
2: Özel Mod
3: Gelişmiş Random Mod
4: Random İngilizce Kelime Modu
5: Random Türkçe Kelime Modu
Cevap: """)

# Moda göre işlem yap
if secim == '1':
    random_domain_check()
elif secim == '2':
    custom_domain_check()
elif secim == '3':
    api_domain_check()
elif secim == '4':
	igrandomword_domain_check()
elif secim == '5':
	trandomword_domain_check()
else:
    print("Geçersiz mod seçimi. Lütfen 1, 2 veya 3 girin.")

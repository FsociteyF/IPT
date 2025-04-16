import os
import webbrowser
import socket
import requests
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_language():
    clear()
    print("Choose Language / اختر اللغة:\n[1] English\n[2] العربية")
    choice = input(">> ")
    return 'ar' if choice == '2' else 'en'

def track_ip(ip, lang):
    clear()
    print("جاري التتبع..." if lang == 'ar' else "Tracking IP...")
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response['status'] == 'fail':
            print("فشل في التتبع." if lang == 'ar' else "Tracking failed.")
            return
        labels = {
            "query": "IP",
            "country": "البلد" if lang == 'ar' else "Country",
            "regionName": "المنطقة" if lang == 'ar' else "Region",
            "city": "المدينة" if lang == 'ar' else "City",
            "zip": "الرمز البريدي" if lang == 'ar' else "ZIP",
            "lat": "خط العرض" if lang == 'ar' else "Latitude",
            "lon": "خط الطول" if lang == 'ar' else "Longitude",
            "isp": "مزود الخدمة" if lang == 'ar' else "ISP",
        }
        print("-" * 40)
        for key, label in labels.items():
            print(f"{label}: {response.get(key, 'N/A')}")
        print("-" * 40)
        print("يتم فتح البحث في Google..." if lang == 'ar' else "Opening Google Search...")
        time.sleep(1)
        webbrowser.open(f"https://www.google.com/search?q={ip}")
    except Exception as e:
        print("حدث خطأ." if lang == 'ar' else "An error occurred.")
        print(str(e))

def port_scan(ip, port, lang):
    clear()
    print(f"فحص المنفذ {port}..." if lang == 'ar' else f"Scanning port {port}...")
    try:
        os.system(f"nmap -p {port} {ip}")
    except Exception as e:
        print("حدث خطأ أثناء الفحص." if lang == 'ar' else "Error while scanning.")
        print(str(e))

def main():
    lang = choose_language()
    while True:
        print("\n[1] تعقب IP" if lang == 'ar' else "\n[1] Track IP")
        print("[2] فحص منفذ" if lang == 'ar' else "[2] Port Scan")
        print("[3] خروج" if lang == 'ar' else "[3] Exit")
        choice = input(">> ")

        if choice == '1':
            ip = input("أدخل عنوان IP: " if lang == 'ar' else "Enter IP address: ")
            track_ip(ip, lang)
        elif choice == '2':
            ip = input("أدخل عنوان IP: " if lang == 'ar' else "Enter IP address: ")
            port = input("أدخل رقم المنفذ: " if lang == 'ar' else "Enter port number: ")
            port_scan(ip, port, lang)
        elif choice == '3':
            print("مع السلامة!" if lang == 'ar' else "Goodbye!")
            break
        else:
            print("خيار غير صالح." if lang == 'ar' else "Invalid choice.")

if __name__ == "__main__":
    main()

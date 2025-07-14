import requests

def xss_test(url):
    payload = "<script>alert('XSS')</script>"
    test_url = f"{url}?search={payload}"
    response = requests.get(test_url)
    
    if payload in response.text:
        print("[!] Muhtemel XSS açığı bulundu!")
    else:
        print("XSS açığı bulunamadı.")

if __name__ == "__main__":
    target_url = input("Test etmek istediğin URL'yi gir (örnek: http://example.com): ")
    xss_test(target_url)

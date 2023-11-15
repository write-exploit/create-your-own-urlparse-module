sözlük = {}
def urlparse(url):
    tam_url = url
    if url.startswith("https://"):
        url = url.replace("https://","")
        sözlük["baslangic"] = "https://" #******
    if url.startswith("http://"):
        url = url.replace("http://","")
        sözlük["baslangic"] = "http://" #******
        
    #======================================
    sözlük["site"] = str(url).split("/")[0]
    
    uzunluk = len(sözlük["baslangic"]+sözlük["site"])
    sözlük["alt_sayfa"] = tam_url[uzunluk:]
    #======================================
    
#================================
    print(sözlük["baslangic"])
    print(sözlük["site"])
    print(sözlük["alt_sayfa"])
#================================
print("enter url :\n")
url = input()
print("=============")
if __name__ == "__main__":
    urlparse(url)

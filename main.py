class URLParser:
    def __init__(self):
        self.protokol = None
        self.domain = None
        self.subpage = None

    def urlparse(self,url):
        tam_url = url
        if url.startswith("https://"):
            url = url.replace("https://","")
            self.protokol = "https://"
        if url.startswith("http://"):
            url = url.replace("http://","")
            self.protokol = "http://"

        self.domain = str(url).split("/")[0]
        uzunluk = len(self.protokol+self.domain)
        self.subpage = tam_url[uzunluk:]
global url_parçala
url_parçala = URLParser()
url_parçala.urlparse("https://www.youtube.com/feed/subscriptions")
# kullanım :
# print(url_parçala.protokol) https://
# print(url_parçala.domain)   www.youtube.com
# print(url_parçala.subpage)  /feed/subscriptions

import urllib.request
class url:
    def __init__(self,url):
        """The url is not the one which needs to fetch"""
        self.url=url if url[-1]=="/" else url+"/"
    def fetch(self,info_path):
        with urllib.request.urlopen(self.url+(info_path+".json"if info_path[-5:]!=".json" else info_path)) as url:
            undressed=url.read()
        return undressed
    def dress(self,data):
        result=""
        for i in str(data)[2:-1]:
            result="".join((result,i))
        return result.replace("\\r","").replace("\\n","").replace("[  ","[")\
               .replace("{    ","{").replace(",    ",",").replace("  }","}")\
               .replace(",  ",",")

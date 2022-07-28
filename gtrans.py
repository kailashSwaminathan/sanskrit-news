import requests
from urllib.parse import urlparse, urlunparse

_headlines = [
    "Global companies that once flocked to China for boom times face a new reality: Covid lockdowns, nervous consumers and a slowed economy."
]

def main():
    """ Gets the translation 
        from Google translation service
    """
    urltmpl = "https://translate.google.com/?sl=en&tl=sa&text=&op=translate"
    print(urlparse(urltmpl))
    urlparts = ['https','translate.google.com','/','','','']
    convtext = "Global companies that once flocked to China for boom times face a new reality"
    urlparts[4] = f"sl=en&tl=sa&text={convtext}&op=translate"
    newurl = urlunparse(urlparts)
    print(newurl)
    sobj = requests.Session()
    res = sobj.get(newurl)
    print(res.status_code)
    print(res.text)
    

if __name__ == "__main__":
    main()
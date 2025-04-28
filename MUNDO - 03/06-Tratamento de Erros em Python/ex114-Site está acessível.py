import urllib.request

try:
    site = urllib.request.urlopen("http://www.google.com.br")
except urllib.error.URLError:
    print("\033[0:31mVerifique sua conexão\033[m")
else:
    print("\033[0:32mSite acessado\033[m")

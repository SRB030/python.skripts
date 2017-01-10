import urllib.request

class parser:

    def urls(self):
            while 1:
                try:
                   urls = input('urls:')
                   html = urllib.request.urlopen(urls).read()
                   out = open("index.html", "wb")
                   out.write(html)
                   break
                except ValueError:
                   print('ссылка не ввидина')




myurl = parser()
myurl.urls()




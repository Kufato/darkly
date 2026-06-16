import urllib.request, re

def crawl(url):
    try:
        html = urllib.request.urlopen(url).read().decode()
        links = re.findall(r'href=\"([^\"]+)\"', html)
        for link in links:
            if link in ('../', '/'):
                continue
            full = url + link
            if link.endswith('/'):
                crawl(full)
            else:
                content = urllib.request.urlopen(full).read().decode()
                if 'flag' in content.lower():
                    print('FOUND:', full)
                    print(content)
    except:
        pass

crawl('http://127.0.0.1:8080/.hidden/')
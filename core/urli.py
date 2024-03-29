#!/usr/bin/python


class sansor():
    def __init__(self):
        pass

    def pransor(self, url):
        import re

        def match(url):
            if not isinstance(url, str):
                url = url.decode('utf-8')
            url = re.sub('^.*://', '', url)
            url = url.split('/')[0].lower().encode('idna')
            url = url.split(b'.')
            return b'.'.join(url).decode('idna')

        ptc_match = re.search(r'^.*?://', url)
        www_match = re.search(r'w{3}\.', url)
        end_match = re.search(r'', url)
        if ptc_match:
            url = url.replace(ptc_match.group(), '')
        if www_match:
            url = url.replace(www_match.group(), '')
        if re.match(r'\d+\.\d+\.\d+\.\d+', url):
            url = socket.gethostbyaddr(url)[0]
        return match(url + "/")

    def fransor(self, url):
        import re
        from urllib.parse import unquote
        import socket
        if not isinstance(url, str):
            url = url.decode('utf-8')
        http_match = re.search(r"^.*://", url)
        www_match = re.search(r"(w{3}|w3)\.", url)
        end_match = re.search(r"([\w\d\-]$)", url)
        ip_match = re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", url)
        if ip_match:
            try:
                result = socket.gethostbyaddr(url)
            except socket.herror as e:
                pass
            else:
                url = result[0]

        if www_match:
            url = url.replace(www_match.group(), "")
        if http_match:
            pass
        else:
            url = "http://" + url
        if end_match:
            url = url + "/"

        return unquote(url)

    def cransor(self, url):
        from urllib.request import urlopen

        try:
            ch = urlopen("http://" + url)
            status = True
        except BaseException:
            status = False

        return status

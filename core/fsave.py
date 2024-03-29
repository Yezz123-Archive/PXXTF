#!/usr/bin/python
class fsave():
    def __init__(self, domain, method, value):
        import random
        self.method = method
        self.domain = domain
        self.value = value
        self.style = ""
        rand = str(random.randint(0, 2000))
        self.fname = "log/" + rand + "_" + method + ".html"

    def styler(self):
        a = '''<style type="text/css">body{background: #0f0f0f top no-repeat;color:#9A0606;
            font-family: arial,Times New Roman,times-roman, georgia, serif
            ; }hr{border:1px solid#444;border-radius:3px;color:#000;margin:13px;
            background:#000;box-shadow:0px 4px 0px#9A0606;}
            img.displayed{display:block;margin-left:auto;}
            footer{margin:13px;text-align:center;}
            h1 { font-family: "Courier New", Courier, monospace; color:
             #680000;margin:0;padding: 0px 0px 6px 0px;font-size:51px;
             line-height:44px;letter-spacing: -2px; font-weight: bold; }
            h3 {color:#444;margin:0; padding: 0px 0px 6px 0px; font-size
            : 30px; line-height: 44px;letter-spacing: -2px; font-weight:
             bold; } h4 { font-family:"Courier New", Courier, monospace;
             top: 35px; padding: 5px; height: 79px;border: 1px solid
            rgb(210, 214, 223); border-radius:4px;background: rgb(210,
             214, 223) none repeat scroll 0px 0px;color: teal; } code {
             font-family: Courier, monospace;border-radius:4px; overflow:
             auto; padding-left: 15px; padding-right:15px; font-size: 11px;
             line-height: 15px; margin-top: 10px;display: block;
             background-color: #eee; color: #000;max-height: 300px; } small
            { font-family: "Courier New", Courier,monospace; font-size:10px;
             font-family: color: red; width:50%; height:20%; } </style>'''
        self.style = a

    def pansor(self):
        from . import markup
        from socket import gethostbyname,gethostname
        import time
        ip = gethostbyname(gethostname())
        time = time.ctime()
        page = markup.page()
        page.html()
        self.styler()
        page.head(self.style)
        page.body()
        page.h1("PTF")
        page.h6("Pentest Tools Framework")
        page.h4("for :" + self.domain + "<br>Method :" + self.method + '<br>ip :' + ip + '<br>Time :' + time)
        page.hr()
        page.h3("Result:")
        page.code()
        if self.value != []:
            page.pre(self.value)
        else:
            page.pre("No Result.")
        page.pre.close()
        page.code.close()
        page.small("<br><br>C.2019 (PTF)")
        page.small.close()
        page.body.close()
        page.html.close()
        try:
            file = open(self.fname, 'w')
            for x in page.content:
                try:
                    file.write(x)
                except BaseException:
                    print(("Exception" + x))
                    pass
        except BaseException:
            self.state = "\tUnfortunately, the file could not be saved"
        else:
            file.close()
            self.state = "\tresult saved in %s" % (self.fname)
        return self.state

from django.shortcuts import render

from .models import Service

# Create your views here.
def services(req):
    services = Service.objects.all()
    for s in services:
        print(s)
    if req.method == 'POST':
        print('ร้องขอแบบ POST')
        print(req.body)
        txt = str(req.body)[2:-1]
        d = {}
        for p in txt.split('&'):
            print(p)
            kv = p.split('=')
            #key,value = kv[0], kv[1]
            d[kv[0]] = kv[1]
        s = Service()
        s.icon = d['icon']
        s.title = d['title']
        s.detail = d['detail']
        s.save()
    else:
        print('ร้องขอทำมะดา')
    return render(req, 'linuxapp/services.html', { 'service': services })

def index(req):
    return render(req, 'linuxapp/index.html')

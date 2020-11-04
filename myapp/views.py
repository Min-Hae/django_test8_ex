from django.shortcuts import render
from myapp.models import Gogek, Jikwon, Buser
from MySQLdb.constants.FIELD_TYPE import YEAR
from django.utils.timezone import now
from datetime import datetime

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def SearchJikwon(request):
    gname = request.POST.get('gogek_name')
    gtel = request.POST.get('gogek_tel')
    jikwons = []
    gogek = Gogek.objects.filter(gogek_name = gname) & Gogek.objects.filter(gogek_tel = gtel)
    # 고객을 바탕으로 직원 검색
    for i in gogek:
        jikwon = Jikwon.objects.filter(jikwon_no = i.gogek_damsano_id)
        for j in jikwon:
            # 직원을 바탕으로 부서 검색
            buser = Buser.objects.filter(buser_no = j.buser_num)
            for k in buser:
                newData = {}
                newData["jikwon_name"] = j.jikwon_name
                newData["jikwon_jik"] = j.jikwon_jik
                newData["buser_name"] = k.buser_name
                newData["buser_tel"] = k.buser_tel
                newData["jikwon_gen"] = j.jikwon_gen
                newData["jikwon_rating"] = j.jikwon_rating
                g = datetime.today().year
                n = j.jikwon_ibsail.year 
                newData["jikwon_geun"] = g-n

                jikwons.append(newData)
            
    return render(request, 'list.html', {'jikwon':jikwons})


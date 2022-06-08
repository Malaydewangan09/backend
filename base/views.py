from django.shortcuts import render
from .models import Topic
import pandas as pd
# Create your views here.
def home(request):
    if request.method == "POST":
        tmp_data = pd.read_csv('base/data/data.csv')
        products = [
        
        for row in range(len(tmp_data)):
        Topic(
        name = tmp_data.ix[row]['Name']
        object =  tmp_data.ix[row]['objects']
        time =  tmp_data.ix[row]['date']
        ) ]
        Topic.objects.bulk_create(products)
        
        startdate = request.POST.get("datemax")
        enddate = request.POST.get("datemin")
        searchresults  = Topic.objects.raw("SELECT * FROM base_topic WHERE time BETWEEN %s AND %s",[startdate,enddate])
        elementsfound = Topic.objects.raw("SELECT COUNT(*) FROM base_topic WHERE time BETWEEN %s AND %s",[startdate,enddate])
        print(elementsfound)
        return render(request ,'index.html',{"data":searchresults})
    else:
        displayresults = Topic.objects.all()
        return render(request, 'index.html',{'data':displayresults})
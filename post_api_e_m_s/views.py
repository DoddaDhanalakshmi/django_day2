from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
import json
# Create your views here.
file_name="post_api_ems/static/j.json"
def readdata():
     with open(file_name,"r") as f:
          return json.load(f)
def writedata(data_from_post_api):
    with open(file_name,"w") as f:
        return json.dump(data_from_post_api,f)     
def create_emp(request):
     return render(request,"home.html")
@api_view(["GET"])
def getallemp(request):
     if request.method=='GET':
          datafromjson=readdata()
     return JsonResponse(datafromjson)
     
@api_view(["POST"])
def addingemp(request):
    data=request.POST.dict()
    allempdatabefore=readdata()
    allempdatabefore["employee"].append(data)
    writedata(allempdatabefore)
    print(allempdatabefore)
    return HttpResponse("added data into the server successfully")
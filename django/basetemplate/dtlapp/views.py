from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dtlview(request):
    # return HttpResponse("<h1>Hello I am from the dtlview </h1>")
    return render(request, 'dtl.html', {'name': 'Python'})

def dtladd(request):
    result = int(request.POST['num1']) + int(request.POST['num2'])
    return render(request, 'result.html', {'result': result})
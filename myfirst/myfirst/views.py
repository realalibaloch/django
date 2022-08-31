from django.http import HttpResponse

def aboutUS(request):
    return HttpResponse ("Welcome")
def simple(request):
    return HttpResponse("Ali here")

def dynamic(request,courseid):
    return HttpResponse(courseid)

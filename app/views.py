from django.shortcuts import render

# Create your views here.
def built_in_filter(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'WhO Are YoU','dt':dt,'v':4}
    return render(request,'built_in_filters.html',d)
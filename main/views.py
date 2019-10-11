from django.shortcuts import render

def index(request):
    '''
    This method will display the home page
    '''
    title = "Home"
    context = {
        "title":title
    }

    return render(request,"main/index.html",context)
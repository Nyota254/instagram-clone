from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def register(request):
    '''
    This method will allow registration of users by rendering the template to display the registration form
    '''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Your Account Has Been Created You Are Now Able To Login!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request,"users/register.html",context)

@login_required
def profile(request):
    '''
    This method handles the user profile 
    '''
    title = 'Profile'
    context = {
        'title':title
    }
    return render(request,'users/profile.html',context)

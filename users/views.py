from django.shortcuts import render,redirect
from django.contrib import messages
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

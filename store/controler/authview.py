from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.contrib import messages
from store.forms import CustomUserForm

# Create your views here.

# ##################################
#       Register section
# ##################################
def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register Done Confirm your Email and Login!')
            return redirect('login')
    context = {'form':form,}
    return render(request, 'store/auth/register.html', context)


# ##################################
#           Login section
# ##################################
def loginPage(request):
    
    if request.user.is_authenticated:
        messages.warning(request, 'You Alrady logged in ')
        return redirect('index')
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')
            print(request.POST)
            user = authenticate(request, username=name, password=passwd)

            if user is not None:
                login(request, user)
                messages.success(request,'Your Log in Done Successfuly')
                return redirect('index')
            else:
                messages.error(request,'Invalid Username or Password')
                return redirect('login')
        return render(request, 'store/auth/login.html')

# ##################################
#        Logout section
# ##################################

def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Your logout successfuly')
    return redirect('index')







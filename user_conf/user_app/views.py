from django.shortcuts import render
from user_app import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout


 # import UserForm,UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request,'user_app/index.html')


def registration(request):
    registered =False

    if request.method=='POST':
        print('post method')
        user_form=forms.UserForm(request.POST)
        profile_form=forms.UserProfileInfoForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            print('Both forms are valid')

            user=user_form.save()
            print('saving user form')
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_picture' in request.FILES:
                profile.profile_picture=request.FILES['profile_picture']

            profile.save()
            print('saving profile form')

            registered=True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=forms.UserForm()
        profile_form=forms.UserProfileInfoForm()



    return render(request,'user_app/registration.html',{'user_form':user_form, 'profile_form':profile_form,'registered':registered})



def user_login(request):

    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')


        user=authenticate(username=username,password=password)


        if user:
            print('User authenticated')
            if user.is_active:
                print('Logged in')
                login(request,user)
                return HttpResponseRedirect(reverse('user_app:index'))


            else:
                return HttpResponse('Account is not active')

        else:
            print('Someone tried login but failed')
            print('Username: {} and password {}'.format(username,password))
            return HttpResponse('Invalid login details')

    else:
        return render(request,'user_app/login.html',{})

@login_required
def special_page(request):
    # return HttpResponseRedirect(reverse('user_app/special_page.html'))
    return render(request,'user_app/special_page.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_app:index'))

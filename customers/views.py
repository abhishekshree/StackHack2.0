from django.shortcuts import render, redirect
from .forms import ExtendedUserCreationForm, CustomerForm
from django.contrib.auth import authenticate, login, logout

#from django.contrib.auth.decorators import login_required

def register(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST, request.FILES)
        customer_form = CustomerForm(request.POST, request.FILES)

        if form.is_valid() and customer_form.is_valid():
            
            """ form_data = form.cleaned_data
            #customer_form = form.cleaned_data
            
            request.session['customer_form'] = form_data
            request.session['id_card'] = customer_form.cleaned_data.get("id_card", None)
            return redirect('preview') """
            user = form.save()

            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('preview')
    else:
        form = ExtendedUserCreationForm()
        customer_form = CustomerForm()

    context = {'form': form, 'customer_form': customer_form}
    return render(request, 'register.html', context)

def preview(request):
    context = {}
    return render(request, 'preview.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
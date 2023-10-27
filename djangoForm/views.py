from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method== "POST":
        name = request.POST.get('userName')
        email = request.POST.get('userEmail')
        password = request.POST.get('userPassword')

        context = {"name": name, "email": email, "password": password}
        return render(request, 'register.html', context)

    return  render(request, 'register.html')




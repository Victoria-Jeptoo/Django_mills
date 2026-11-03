from django.shortcuts import render


# Create your views here.
def index(request):
    temp = 38.7
    humidity = 12
    wind = 15
    city = "Zanzibar"
    is_sunny = True
    users = ['Jane', 'Jack', 'Esther']
    # package
    data ={
        'temperature': temp,
        'humidity': humidity,
        'windspeed': wind,
        'city': city,
        'is_sunny': is_sunny,
        'users': users,

    }
    return render(request, "home.html",data)


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")

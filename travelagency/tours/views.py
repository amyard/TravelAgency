from django.shortcuts import render


from location.models import Country


def index(request):
    user = request.user
    countries = Country.objects.all()
    return render(request, 'base.html', context = {'test':'LALALLALALAA', 'user':user, 'countries':countries, 'newtest':'new test here'})

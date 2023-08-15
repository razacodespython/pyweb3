from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def store_number(request):
    if request.method == "POST":
        fav_number = request.POST.get('fav_number')
        # Store the number...
        request.session['fav_number'] = fav_number
        return JsonResponse({'status': 'success'})

def retrieve_number(request):
    if request.method == "GET":
        fav_number = request.session.get('fav_number', 'Number not stored yet')

        

        return render(request, 'home.html', {'storedNumber': fav_number})

def add_person(request):
    if request.method == "POST":
        name = request.POST.get('name')
        fav_number = request.POST.get('fav_number')

        # Add the person to the database

        return redirect('')


def retrieve_person_number(request):
    if request.method == "GET":

        name = request.GET.get('name')

        
        try:
            # Try to retrieve the person's favorite number
            pass
        except:
        # except Person.DoesNotExist:
            fav_number = "Person not found"

        return render(request, 'home,html', {'mappedFavoriteNumber': fav_number})
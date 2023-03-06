# bus-stops
stanice odlazak povratak
napisati nekoliko testova
opciono ukloniti docker files i requrements

## Backend

from django.http import JsonResponse
from datetime import datetime

def index(request):
    current_date = datetime.now().strftime("%d %B %Y")

    data = {
        'date': current_date,
    }

    return JsonResponse(data)



## Frontend

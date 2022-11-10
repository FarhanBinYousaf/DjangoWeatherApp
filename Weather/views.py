from django.shortcuts import render
import urllib.request
import json
from datetime import datetime
from django.utils.timezone import make_aware
# Create your views here.

def index(request):

	if request.method == "POST":
		city = request.POST['city']
		
		source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=metric&appid=dfe61d35a83e3ea7b0bf854013a2ea06').read()

		list_of_data = json.loads(source)	

		data = {
		"country_code": str(list_of_data['sys']['country']),
		"coordinate": str(list_of_data['coord']['lon']) + ', '
		+ str(list_of_data['coord']['lat']),
		"temp": str(list_of_data['main']['temp']) + ' °C',
		'feels_like': str(list_of_data['main']['feels_like']) + ' °C',
		'temp_min': str(list_of_data['main']['temp_min']) + ' °C',
		'temp_max': str(list_of_data['main']['temp_max']) + ' °C',
		"pressure": str(list_of_data['main']['pressure']),
		"humidity": str(list_of_data['main']['humidity']),
		'main': str(list_of_data['weather'][0]['main']),
		'description': str(list_of_data['weather'][0]['description']),
		# 'city': city.title(),
		'icon': list_of_data['weather'][0]['icon'],
		'sunrise': make_aware(datetime.fromtimestamp(list_of_data['sys']['sunrise'])),
        'sunset':  make_aware(datetime.fromtimestamp(list_of_data['sys']['sunset'])),
		'wind': str(list_of_data['wind']['speed']) + ' m/s',
		'name':list_of_data['name'],
		# 'precipitation':list_of_data['precipitation']['value'],
		}
		
		print(data)
	else:
		data = {}
	return render(request, "Weather/index.html", data)
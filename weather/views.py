from django.shortcuts import render
import json,urllib.request
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city + '&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
            json_data= json.loads(res)
            data = {
                'city' : request.POST['city'],
                'cc' : str(json_data['sys']['country']),
                'lat' : str(json_data['coord']['lat']),
                'lon' : str(json_data['coord']['lon']),
                'mintemp' : str(json_data['main']['temp_min']),
                'maxtemp' : str(json_data['main']['temp_max']),
                'temp' : str(json_data['main']['temp']),
                'pressure' : str(json_data['main']['pressure']),
                'humidity' : str(json_data['main']['humidity']),
            }
        except:
            data = {
                'cc' : 'nill'
            }
        
        return render(request,'index.html',{'data' : data})
    else:
        return render(request,'index.html')
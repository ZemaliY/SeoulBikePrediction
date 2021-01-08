from django.http                    import HttpResponse
from django.http                    import JsonResponse
from django.views.decorators.csrf   import csrf_exempt
from rest_framework.renderers       import JSONRenderer
from rest_framework.parsers         import JSONParser
from BikePrediction.models              import locations
from BikePrediction.serializers         import locationsSerializer
import pickle
from sklearn.externals import joblib
import pandas as pd

def predict_location(unscaled_data):
    col_to_normalize=['Temperature','Humidity','Windspeed','Visibility','DewPointTemperature','SolarRadiation','Rainfall','Snowfall']
    colum_input = ['Date', 'RentedBike', 'Hour', 'Temperature', 'Humidity', 'Windspeed', 'Visibility',
                   'DewPointTemperature', 'SolarRadiation', 'Rainfall', 'Snowfall', 'Season', 'Holiday']
    path_to_model   = "C:/Users/youss/Desktop/ProjetPythonData Analyst/Seoul/GBM_model.pkl"
    path_for_normalizer = "C:/Users/youss/Desktop/ProjetPythonData Analyst/Seoul/normalizer.pkl"
    path_for_season_encoder = "C:/Users/youss/Desktop/ProjetPythonData Analyst/Seoul/season.pkl"

    model = joblib.load(path_to_model)
    season_encoder = joblib.load(path_for_season_encoder)
    normalizer = joblib.load(path_for_normalizer)

    df=pd.DataFrame([unscaled_data],columns=colum_input)
    df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")
    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month
    df['day'] = df['Date'].dt.day
    df['week_day'] = df['Date'].dt.dayofweek
    df['Holiday'] = (df['Holiday'] == "Holiday").astype(int)
    df = df.drop('Date', axis=1)
    a = season_encoder.transform(df[['Season']])
    name_season = ['Autumn', 'Spring', 'Summer', 'Winter']
    temp = pd.DataFrame(a.toarray(), columns=name_season)
    df = pd.concat([df, temp], axis=1)
    df = df.drop('Season', axis=1)
    df[col_to_normalize] = normalizer.transform(df[col_to_normalize])
    df = df.drop('RentedBike', axis=1)
    rentedbike= model.predict(df)
    return rentedbike


@csrf_exempt
def predict(request):
    if request.method == 'GET':
        return HttpResponse(status=400)

    elif request.method == 'POST':
        data= JSONParser().parse(request)
        serializer  = locationsSerializer(data=data)
        if serializer.is_valid():
            data["RentedBike"]= predict_location(data)
            serializer= locationsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data  , status=201)
        return     JsonResponse(serializer.errors, status=400)

@csrf_exempt
def location_list(request):
    if request.method == 'GET':
        locationsall      = locations.objects.all()
        serializer  = locationsSerializer(locationsall , many=True)
        reponse     = JsonResponse(serializer.data  , safe=False)
        return reponse

    elif request.method == 'POST':
        data        = JSONParser().parse(request)
        serializer  = locationsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data  , status=201)
        return     JsonResponse(serializer.errors, status=400)

@csrf_exempt
def location_detail(request, pk):
    try:
        location = locations.objects.get(pk=pk)
    except locations.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = locationsSerializer(location)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = locationsSerializer(location, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        location.delete()
        return HttpResponse(status=204)
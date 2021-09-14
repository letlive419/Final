import main_functions, requests , json




api_key_dict = main_functions.read_from_file("api_key.json")
my_aqi_api_key =  api_key_dict["aqi_api_key"]

url="http://api.airvisual.com/v2/nearest_city?key="
url_aqi= url + my_aqi_api_key


aqi_json = requests.get(url_aqi).json()
main_functions.save_to_file(aqi_json,"aqi.json")


air_quality_index = main_functions.read_from_file("aqi.json")

print(type(air_quality_index))

longtitude = air_quality_index['data']['location']['coordinates'][0]
latitude = air_quality_index['data']['location']['coordinates'][1]

print(latitude,longtitude)
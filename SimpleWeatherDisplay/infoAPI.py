import json
import requests 
import tkinter

print('______________________________ \n')

weather_key = '6c2cb63ef0d845deadf60249201305'
url_weather = 'http://api.weatherapi.com/v1/current.json?key=' #not necessarily the base but for what we need is fine
loc_key = '27d7640498bfbf48f4fd62b999f524d8'
url_geo = "http://api.ipstack.com/check?access_key="           #not necessarily the base but for what we need is fine


#location stuff 
def location():
    send_url = url_geo + loc_key
    geo_req = requests.get(send_url) 
    stat = geo_req.status_code
    
    if stat < 400:
        geo_json = json.loads(geo_req.text) # get unicode
        region = geo_json['region_code']
        city = geo_json['city']
        #weather(region,city)

        send_url = url_weather + weather_key + '&q=' + city
        w_req = requests.get(send_url)
        w_json = json.loads(w_req.text)
        current = w_json['current']
        temp = current['temp_f']

        return city, region, temp

    else:
        print("Error has occured. Check Location services.")


#def weather(region, city):
#    send_url = url_weather + weather_key + '&q=' + city
#    w_req = requests.get(send_url)
#    w_json = json.loads(w_req.text)
#    cloud = w_json['current']

#    print(cloud['temp_f'])
    #print(w_json)
#    print(region)
#    print(city)
#    return cloud



#if __name__ == "__main__":
#    location()    

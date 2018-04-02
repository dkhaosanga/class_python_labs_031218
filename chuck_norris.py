import requests

package = {
    'APPID' : '86173671503785bdd7583d3dd6f8eda0,',
    'q' : 'portland'
    }


r = requests.post('https//:api.openweathermap.org/data/2.5/weather' , params=package)

pritn r.json

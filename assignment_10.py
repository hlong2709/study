#1 
import requests

def random_joke():
    request = "https://api.chucknorris.io/jokes/random"
    response = requests.get(request).json()
    joke = response['value']
    print(joke)

random_joke()


#2
import json
import requests

city = input('Nhập tên thành phố:')

request = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=8aeb1dc86cd744c029a53c4825192234"
response = requests.get(request).json()
des = response['weather'][0]['description']
temp = response['main']['temp']
temp_C = temp - 273.15

print("Thời tiết hiện tại:", des)
print("Nhiệt độ hiện tại", temp_C)


#3
from flask import Flask
import json

app = Flask(__name__)
@app.route('/prime_number/<number_input>')

def check_prime_number(number_input):
    number = int(number_input)
    is_prime = True
    if number <= 1:
        is_prime = False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            is_prime = False
            break
    return json.dumps({
        "Number": number,
        "isPrime": is_prime
    })

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

#4
from flask import Flask, jsonify
import json

app = Flask(__name__)
@app.route('/airport/<icao>')

def get_airport_info(icao):
    with open('airports.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    if icao in data:
        airport_info = data[icao]
        return json.dumps({
            "icao": airport_info['icao'],
            "name": airport_info['name'],
            "city": airport_info['city'],
            "country": airport_info['country']
        })
    return json.dumps({
        "message":"Airport not found"
    }), 404
if __name__ == '__main__':
    app.run(use_reloader= True, host='127.0.0.1', port=5000)
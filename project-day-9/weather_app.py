import requests
def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t+%w+%h"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text.split(" ")
            condition = data[0] + " " + data[1] if len(data) > 1 else data[0]
            temp = data[-3] if len(data) >= 3 else "N/A"
            wind = data[-2] if len(data) >= 2 else "N/A"
            humidity = data[-1] if len(data) >= 1 else "N/A"
            
            print(f"\n{'='*30}")
            print(f"🌤️  Weather in {city}")
            print(f"{'='*30}")
            print(f"☁️  Condition : {condition}")
            print(f"🌡️  Temperature: {temp}")
            print(f"💨 Wind      : {wind}")
            print(f"💧 Humidity  : {humidity}")
            print(f"{'='*30}")
        else:
            print("❌ City not found!")
    except:
        print("❌ Connection error! Check your internet.")
        

while True:
    city=input("\nEnter city name (or 'exit' to quit):")

    if city.lower=="exit":
        print ("Goodbye!")
        break
    get_wheather(city)
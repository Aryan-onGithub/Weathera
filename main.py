import requests      #module use to interact with web servers and retrive data using HTTP methods
import json          #module (javaScript object notation
import win32com.client as wincl

if __name__ == '__main__':
    speaker = wincl.Dispatch("SAPI.SpVoice")
    voices = speaker.GetVoices()
    speaker.Voice = voices.item(1)  # .Voice method, item(1) is the indexing of female voice

    
    speaker.speak("Hello! I am Weatheria, your reliable weather-telling app.")
    speaker.speak("i was created by Mr.aryan chandra")
    speaker.speak("Feel free to ask me about the weather in any city by simply typing its name below")

    with open("your_APIkey", "r")as readme:
        key = readme.read()

    while(True):
        try:
            city = input("Enter the name of the city: ")
            if city == "q":
                speaker.speak("thanks for using me, bye bye")
                break
            url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={city}"

            r = requests.get(url) #requests the link over internet
            # print(r.text)

            weather_dic = json.loads(r.text) #converted string to python dictionary
            w = weather_dic['current']['temp_c']
            h = weather_dic["current"]["humidity"]
            con = weather_dic["current"]["condition"]["text"]
            re = weather_dic["location"]["region"]
            co = weather_dic["location"]["country"]

            speaker.speak(f"the temperature in {city}, {re}, {co} is {w}degree celsius, humidity is{h}percent, the weather is {con} today")    #we cannot write " " inside string but can write ' '
        except:
            speaker.speak("sorry an error occurred")
            speaker.speak("please Enter a valid name or check your internet connection")
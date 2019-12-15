def weather_krakow():
    return "Sunny"

def weather_wroclaw():
    return "Rainy"

if __name__ == "__main__": #Print the values only if the file itself is being run, not when imported to another module.
    print(weather_krakow())
    print(weather_wroclaw())
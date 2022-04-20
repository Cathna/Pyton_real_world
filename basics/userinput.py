def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

#int can be used but will not be able to handle any numbers that have .2 etc
user_input = float(input("Enter temperature:"))
print(weather_condition(user_input))

hour = 10 #init
if hour < 12:
    print("Good Morning !")

def check(number):
    if number > 0:
        return "Positive"
    elif number == 0:
        return "Zero"
    else:
        return "Negative"
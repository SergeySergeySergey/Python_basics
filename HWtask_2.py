print("Добро пожаловать в калькулятор времени!")
user_seconds=(int(input("Введите время в секундах: ")))
hours=user_seconds // 3600
if hours < 10:
    hours= '0'+str(hours)
hours_calc = user_seconds // 3600
minutes_calc = 3600 * hours_calc
minutes_calc_diff = user_seconds - minutes_calc
minutes = minutes_calc_diff // 60
if minutes <10:
    minutes = "0"+str(minutes)
seconds_calc = (minutes_calc_diff // 60) * 60
seconds = minutes_calc_diff - seconds_calc
if seconds <10:
    seconds = "0"+str(seconds)
print(f"Время в часах, минутах, секундах: {hours}:{minutes}:{seconds}")
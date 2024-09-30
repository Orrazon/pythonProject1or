import Consts


def get_amount_of_days():
    list_days = Consts.DAY_LIST
    days_amount = input("Enter the amount of days:")
    while not days_amount.isnumeric():
        days_amount = input("Enter invalid days.\nEnter the amount of days:")
    while 6 < int(days_amount) or 1 > int(days_amount):
        days_amount = int(input("Invalid days amount.\nEnter the amount of days:"))
    for i in range(len(list_days)):
        if i == int(days_amount):
            list_days = list_days[:i]
    return int(days_amount), list_days


def get_hours_per_day():
    hours_amount = input("Enter the hours per day:")
    while not hours_amount.isnumeric():
        hours_amount = input("Invalid hours per day have been entered.\nEnter the hours per day:")
    while 9 < int(hours_amount) or 1 > int(hours_amount):
        hours_amount = int(input("Invalid hours amount.\nEnter the hours per day:"))
    return int(hours_amount)


amount_of_days, list_days = get_amount_of_days()
hours_per_day = get_hours_per_day()
schedule = []


# Initializing the schedule
def Initialize_schedule(schedule):
    for row in range(amount_of_days):
        days_in_week = []
        for col in range(hours_per_day):
            days_in_week.append(Consts.FREE)
        schedule.append(days_in_week)
    return schedule


Initialize_schedule(schedule)


# The data is inserted:
# [name of class]_[how many hours the class]_[day]_[starting hour]
def data_for_the_lesson():
    print("Classes: ", Consts.CLASS)
    print("Day: ", list_days)
    name_of_class, hours_per_class, day, starting_hour = input(
        "[name of class]_[how many hours the class]_[day]_[starting hour]\n"
        "Enter the data for the lesson: ").lower().split("_")
    while not name_of_class in Consts.CLASS:
        print("The class you entered does not exist,\n"
              f"please enter another class from the list:\n{Consts.CLASS}")
        name_of_class = input("Enter the class: ").lower()
    while not hours_per_class.isnumeric():
        print("The hours for the class are not valid input,\nplease enter valid hours")
        hours_per_class = input("Enter the number of hours to the class: ")
    while int(hours_per_class) > hours_per_day:
        print("You exceed the number of hours in a day,\n "
              "Please enter an amount of hours that does not exceed the limit")
        hours_per_class = input("Enter the number of hours to the class: ")
    while not day in list_days:
        print("The day you entered is an invalid input,\n"
              f"please enter another day from the list:\n{list_days}")
        day = input("Enter the day: ").lower()
    while not starting_hour.isnumeric():
        print("The starting hour you entered is an invalid input,\n"
              f"Please enter an hour before: {Consts.STARTING_HOUR + hours_per_day}")
        starting_hour = input("Enter the starting hour: ")
    while int(starting_hour) >= Consts.STARTING_HOUR + hours_per_day:
        print("The starting hour you entered is an invalid input,\n"
              f"Please enter an hour before: {Consts.STARTING_HOUR + hours_per_day}")
        starting_hour = input("Enter the starting hour: ")
    to_continue = input("you have more classe?").lower()
    if to_continue == "yes":
        return True, hours_per_class, day, starting_hour, name_of_class
    else:
        return False, hours_per_class, day, starting_hour, name_of_class


def insertion_of_lessons(schedule, hours_per_class, day, starting_hour, name_of_class):
    count = 0
    print("Schedule after first insertion:")
    for i in range(int(hours_per_class)):
        if schedule[Consts.DAYS_DICT[day]][Consts.HOURS[int(starting_hour)] + i] == Consts.FREE:
            count += 1
    if count == int(hours_per_class):
        for t in range(int(hours_per_class)):
            schedule[Consts.DAYS_DICT[day]][Consts.HOURS[int(starting_hour)] + t] = name_of_class


def System_activation():
    flag = True
    while flag:
        flag1, hours_per_class1, day1, starting_hour1, name_of_class1 = data_for_the_lesson()
        insertion_of_lessons(schedule, hours_per_class1, day1, starting_hour1, name_of_class1)
        if not flag1:
            flag = False


System_activation()

for day in range(amount_of_days):
    print(Consts.DAY_LIST[day] + ": " + str(schedule[day]))

# Final insertion of lessons
# TODO

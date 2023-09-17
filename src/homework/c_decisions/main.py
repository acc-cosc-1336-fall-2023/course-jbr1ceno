import decisions

value1 = input("Type a value for options ")
value2 = input("Type a value for the total ")

result = decisions.get_options_ratio(float(value1), float(value2))

print("The ratio of the options over the total is: ", result)

print("The rating for the ratio is: ", decisions.get_faculty_rating(result))
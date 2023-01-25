# Exercise 01: Split Bill Calculator

tagihan = float(input(" Enter the amount of bill:\n "))
tips = float(input(" Enter the amount of tips you want to give:\n"))
no_people = int(input(" Enter the amount of people:\n "))


totips = tagihan / 100 * tips
total_cost = (tagihan + totips) / no_people
finalamount_per_person = round(total_cost, 2)
final_amount = "{:.2f}".format(finalamount_per_person)


print(" total amount per person are: $ ",final_amount)
print(" total tips amopunt per person is:  $ ", "{:.2f}".format(totips))

#part one define a fuction with no arguments
def greet_customer():
    print("Welcome to lemonade stand")
    print("freash lemonade just for you")

#part 2 Call the greet_customer function
greet_customer()

#part 3 ask for price per cup and number of cups sold
price_per_cup = float(input("enter the price per cup in dollars:"))
cups_sold =int(input("enter the numbers of cups sold:"))

#part 4: define a functioin thst takes argument and returns the total cost
def calculate_total(price,cups):
    total = price*cups
    return total

#part5:call calculate_total and store the value it returns
total_cost = calculate_total(price_per_cup, cups_sold)

#part6 use built _in function to round the total, then print it
rounded_total= round(total_cost, 2)
print("total cost:",rounded_total)

#part 7:ask how much money the customer paid
amount_paid = float(input("enter amount paid by the customer: "))

#part 8:define a function that takes argument and returnd the change due
def calculate_change(paid, total):
    change = paid - total
    return change

# part 9: call calculate_change and store the value it returns 
change_due = calculate_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

#part 10: define a function that returns a thank you  messeage based on cups sold
def thank_you_message(cups):
    if cups >= 5:
        return "wow, big oder! thanks so much for your support"
    else:
        return "thanks for stopping by!"

# part 11
closing_message = thank_you_message( cups_sold)

#part 12
print("")
print("=====Lemonade Stand recipet")
print("price per cup:",price_per_cup)
print("cups sold:",cups_sold)
print("total cost:",rounded_total)
print("amount paid:",amount_paid)
print("closing_message")
print("=======================")





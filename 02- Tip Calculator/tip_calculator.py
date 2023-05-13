print('Welcome to Tip Calculator')
total = float(input('What was the total bill? '))
tip_percentage = float(input('What percentage tip would you like to give? '))
split_for = int(input('How many people to split the bill? '))
payment = (total * (1 + (tip_percentage /100))) / split_for
final = "{:.2f}".format(payment)
print(f'Each person should pay €{final}')

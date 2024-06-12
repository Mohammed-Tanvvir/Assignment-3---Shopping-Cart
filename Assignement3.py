#Develop a Python program that calculates the total cost of a shopping cart with discounts applied based on user input

print("!== Assignment 3: Online Shopping ==!")
total = float(input("Enter the total cost of your shopping cart: "))
discount = input("Do you have a discount code? (yes/no): ").lower()

if discount == "yes":
    code = input("Enter your discount code for 5% off: ").upper()
    if code == "SAVE":
        if total >= 100:
            print("It looks like your total is over $100, so you get a 10% discount!")
            total = total * (1 - 0.10)

            print("Your code was sucessful!")
            discountedTotal = total * (1 - 0.05)
            print(f"Your total cost with discount is: $ {discountedTotal:.2f}")
        else:
            print("Your code was sucessful!")
            discountedTotal = total * (1 - 0.05)
            print(f"Your total cost with discount is: $ {discountedTotal:.2f}")
    else:
      print("That's the wrong code")
      if total >= 100:
        print("It looks like your total is over $100, so you get a 10% discount!")
        total = total * (1 - 0.10)
      else:
        print("Thats the wrong code")
        print(f"Your total cost is: $ {total:.2f}")
else:
  if total >= 100:
    print("It looks like your total is over $100, so you get a 10% discount!")
    total = total * (1 - 0.10)
    print(f"Your total cost is: $ {total:.2f}")
  else:
    print(f"Your total cost is: $ {total:.2f}")


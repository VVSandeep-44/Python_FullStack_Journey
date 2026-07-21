"""
Ticket Fare Calculator 

Problem Statement:
A transportation service calculates ticket fares based on the passenger's age, distance traveled, and discount code.

Fare Rules:
• Base fare: ₹30
• Additional charge: ₹2 per kilometer

Age Rules:
• Age 4 or below -> Free Ticket
• Age 5-11 -> 20% discount
• Age 12-49 -> Add ₹5
• Age 50-59 -> Add ₹3
• Age 60 and above -> 30% discount

Discount Code:
• If the passenger has a discount code (yes), apply an additional 10% discount on the final fare.
• Otherwise, no additional discount is applied.

Validation:
• If kilometers <= 0, display "Invalid Kilo entered!"
• If age <= 0, display "Invalid Age entered!"

Tasks:
1. Read the distance traveled.
2. Read the passenger's age.
3. Read whether the passenger has a discount code (yes/no).
4. Calculate the ticket fare.
5. Display the final fare.

Examples:
20 km, Age 8, Code no   -> Ticket fare: 56
50 km, Age 65, Code yes -> Ticket fare: 94.5
10 km, Age 3, Code no   -> Ticket fare: 0
-5 km, Age 25           -> Invalid Kilo entered!
15 km, Age -2           -> Invalid Age entered!
"""




def calculate_ticket_fare(distance, passenger_age, discount_code):
    base_fare = 30
    additional_charge = 2 * distance
    fare = base_fare + additional_charge

    if passenger_age <= 4:
        return 0
    elif 5 <= passenger_age <= 11:
        fare *= 0.8 # Apply 20% discount
    elif 12 <= passenger_age <= 49:
        fare += 5
    elif 50 <= passenger_age <= 59: 
        fare += 3 
    else:
        fare = base_fare + additional_charge
        fare *= 0.7 # Apply 30% discount

    return fare

distance = int(input("Enter the distance travelling (km): "))
passenger_age = int(input("Enter Passeger's age: "))
discount_code = input("Do you have discount code (yes or no)?").lower()

if distance <= 0:
    print("Invalid Kilo entered!")
elif passenger_age <= 0:
    print("Invalid Age entered!")
else:
    final_fare = calculate_ticket_fare(distance, passenger_age, discount_code)
    if discount_code == "yes":
        final_fare *= 0.9 # Apply additional 10% discount
        print(f"Ticket fare: {final_fare}")
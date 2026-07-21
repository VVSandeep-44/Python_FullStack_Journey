'''
Parking Lot Management System

Design a Python program to calculate the parking fee in a parking lot based on the following rules:
🔹 Vehicle Types and Hourly Rates
Car → ₹60 per hour
Bike → ₹30 per hour
Bus → ₹200 per hour

🔹 Discount Rules
1️⃣ If the vehicle is parked for more than 10 hours, apply a flat 20% discount on the total parking fee.
2️⃣ After applying the above discount, if the parking bill still exceeds ₹1,000, apply an additional 10% discount on the remaining amount.

🎯 Task
Take vehicle type and parking hours as input
Calculate the parking fee
Apply discounts according to the above conditions
Print the final total payable amount
'''



# Function to calculate parking fee
def calculate_parking_fee(vehicle_type, parking_hours):
    if vehicle_type == "car":
        rate_per_hour = 60
    elif vehicle_type == "bike":
        rate_per_hour = 30
    elif vehicle_type == "bus":
        rate_per_hour = 200
    else:
        return "Invalid vehicle type"

    total_fee = rate_per_hour * parking_hours

    # Apply discount if parked for more than 10 hours
    if parking_hours > 10:
        total_fee *= 0.8  # Apply 20% discount

    # Apply additional discount if total fee exceeds ₹1,000
    if total_fee > 1000:
        total_fee *= 0.9  # Apply additional 10% discount

    return total_fee

# Main program
vehicle_type = input("Enter vehicle type (Car, Bike, Bus): ").lower()
parking_hours = int(input("Enter parking hours: "))

if parking_hours < 0:
    print("Parking hours cannot be negative.")
elif vehicle_type not in ["car", "bike", "bus"]:
    print("Invalid vehicle type. Please enter Car, Bike, or Bus.")
else:
    final_amount = calculate_parking_fee(vehicle_type, parking_hours)
    print(f"Final amount to be paid: ₹{final_amount}")
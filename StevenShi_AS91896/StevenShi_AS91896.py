# This program is intentionally designed to simulate modern-day frustrating digital experiences. Any resemblance to real-world websites is absolutely on purpose.
# ================================
# Mc'Download™ Outrageous ordering procedure
# Author: Steven Shi (CEO of Abnormal Canteen)
# Functions: Ordering food, pseudo-AI recommendations, double privacy warnings, useless loading bars
# ================================

import time        # Used for loading progress bars to create a sense of "false effort"
import random      # Used to generate order numbers to enhance the illusion of "looking legitimate"
from datetime import datetime  # Used to obtain the current time and put it on the electronic receipt

# Opening remarks, meaningless but necessary
print("Welcome to Mc'Download backstage ordering program")
print("Have a great choose for you meal!")  # Misspelled English is more realistic

buck = 0  # Total price variable in US dollars

# Menu definition, number: dish name + price
menu = {
    "1":("King Buger",14.00),
    "2":("Classic Buger",8.50),
    "3":("Double Buger",10.50),
    "4":("Fries",5.49),
    "5":("Fried Fish",6.00),
    "6":("Nuggents(5 pic)",8.49),
    "7":("Sodayo",2.50),
    "8":("Cool'Caal Cola",2.50),
    "9":("Push Cola",2.50),
    "0":("Stickers",1.50),  # Who will buy stickers? If you buy, you are sick, but we sell, we are normal
}
print("Used 'number' to order the the meal.")
# Display the menu contents (each price should be rounded to two decimal places)
print("\nPlease choose you meal:")
for key, (item, price) in menu.items():
    print(f"{key}.{item} - ${price:.2f}")

print("print 'done' when your finished.\n")

# Main loop for ordering food
while True:
    choice = input("Select item number: ")
    if choice.lower() == "done":
        break
    elif choice in menu:
        try:
            qty = int(input(f"How many {menu[choice][0]}? "))
            buck += menu[choice][1] * qty
            print(f">>> {qty} x {menu[choice][0]} added.")
        except ValueError:
            print(">>> Invalid quantity. Try again.")
    else:
        print(">>> Invalid choice. Try again.")

# Calculate GST (New Zealand standard rate 15%)
GST = buck * 0.15

# Simulating a pseudo-AI recommendation system (which actually does nothing)
print("\nAnalyzing your taste preference using 2008 AI algorithm...\n")
loading_phrases = [
    "Initializing neural ketchup network...",
    "Fetching burger sentiment analysis...",
    "Simulating your last 3 meals...",
    "Compressing cheese data stream...",
    "Running pickles clustering algorithm...",
    "Reticulating fried fish splines...",
    "Verifying soda carbonation level...",
    "Accessing nuggent blockchain ledger...",
    "Locating your fries soulmate...",
    "Finalizing with quantum meat computing..."
]

# Fake loading information is combined with delayed output to enhance the "fake high-end feeling"
for i, phrase in enumerate(loading_phrases):
    print(f"Schedule: {(i + 1) * 10}% - {phrase}")
    time.sleep(0.6)

# Pseudo recommendation engine result display
print("\n🍟 Recommendation Engine Results:")

# If you order French fries or chicken nuggets, a drink is mandatory
if any(k in menu for k in ["4", "6"]):
    print(">>> Based on your craving pattern, we *strongly* recommend a Cool'Caal Cola. Only $2.50!")
    force = input("Would you like to add one? (yes/no): ").strip().lower()
    if force == "yes":
        buck += 2.5
        print(">>> Cool'Caal Cola added. You're welcome.")
    else:
        print(">>> Your future self will regret this.")  # Curse users: If you don’t buy it, you will regret it.
else:
    print(">>> No forced upsell detected. Are you okay?")  # Are you abnormal that you don't need our drinks?

# Start collecting user "personal information"
print("\nThank you. Now let's collect your personal data—err, we mean 'details'.")
print("\n[Privacy Reminder] We guarantee that this restaurant will only use this data to send electronic receipts and take orders.")  # 第一次提醒隐私

# Put name and email
name = input("Please enter your name:")
email = input("Please enter your email:")

# The second loading bar - analyzing user information (actually does nothing)
print("\nAnalyzing, please wait...\n")
for i in range(5):
    print("Schedule：{}%".format((i + 1) * 20))
    time.sleep(1)

# The third loading bar is unnecessary but it can delay the process
print("\nAnalysis completed, calculating prize and GST...\n")
print("\nAnalyzing, please wait...\n")
for i in range(5):
    print("Schedule：{}%".format((i + 1) * 20))
    time.sleep(1)

# Print electronic receipt (full of formality)
print("The receipt has been printed. The electronic receipt is as follows:")

# Generate order number and timestamp
order_id = "MC" + str(random.randint(100000, 999999))
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Show order information
print("=======================================")
print(f"🧾 Order ID: {order_id}")
print(f"🕒 Order Time: {now}")
print("=======================================")

# Output price information, keep two decimal places
print(f"Your meal prize are: ${buck:.2f}")
print(f"Your GST are: ${GST:.2f}")
total = buck + GST
print(f"Total (including GST): ${total:.2f}")

# Output user-supplied information
print("Name:", name, "Email:", email)

# Scoring and grading evaluation based on total consumption
if total >= 50:
    print("Have a nice meal for your family, or for youself. 'Big stomach king'.")
elif total >= 40:
    print("That a great choose! Make sure don't waste food or friends.")
elif total >= 30:
    print("A luxurious meal! It will definitely be delicious")
elif total >= 20:
    print("Have a nice meal, we will make quick and clean")
else:
    print("Well, enjoy a nice and tasty meal.")

# Ending (privacy reminder again)
print("\n[Privacy Reminder] We will send you meal soon, please wait you order.")  # I reminded you about privacy for the second time, but still no one believed me.

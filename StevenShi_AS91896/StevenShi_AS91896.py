# start
import time
import random
from datetime import datetime
print("Welcome to Mc'Download backstage ordering program")
print("Have a great choose for you meal!")
buck = 0 # buck is dollor
# let user choose item
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
        "0":("Stickers",1.50),
    }

print("\nPlease choose you meal:")
for key,(item,price) in menu.items():
    print(f"{key}.{item} - ${price:.2f}")

print("print 'done' when your finished.\n")

# Order Cycle
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

# Here is New Zealand, GST is 15%
GST = buck * 0.15 

# Automatic recommendation system
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

for i, phrase in enumerate(loading_phrases):
    print(f"Schedule: {(i + 1) * 10}% - {phrase}")
    time.sleep(0.6)

print("\n🍟 Recommendation Engine Results:")

# "Random" recommended drinks(sell)
if any(k in menu for k in ["4", "6"]):  # IF order fries or nuggents
    print(">>> Based on your craving pattern, we *strongly* recommend a Cool'Caal Cola. Only $2.50!")
    force = input("Would you like to add one? (yes/no): ").strip().lower()
    if force == "yes":
        buck += 2.5
        print(">>> Cool'Caal Cola added. You're welcome.")
    else:
        print(">>> Your future self will regret this.")
else:
    print(">>> No forced upsell detected. Are you okay?")

print("\nThank you. Now let's collect your personal data—err, we mean 'details'.")

#for order meal
print("\n[Privacy Reminder] We guarantee that this restaurant will only use this data to send electronic receipts and take orders.")
name = input("Please enter your name:")
email = input("Please enter your email:")
print("\nAnalyzing, please wait...\n")
for i in range(5):
    print("Schedule：{}%".format((i + 1) * 20))
    time.sleep(1)  # wait 1 s

# Judgment conditions
print("\nAnalysis completed, calculating prize and GST...\n")
print("\nAnalyzing, please wait...\n")
for i in range(5):
    print("Schedule：{}%".format((i + 1) * 20))
    time.sleep(1)  # wait 1 s
print("The receipt has been printed. The electronic receipt is as follows:")

# Insert order nmuber + time 
order_id = "MC" + str(random.randint(100000, 999999))
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("=======================================")
print(f"🧾 Order ID: {order_id}")
print(f"🕒 Order Time: {now}")
print("=======================================")

print(f"Your meal prize are: ${buck:.2f}")
print(f"Your GST are: ${GST:.2f}")
total = buck + GST
print(f"Total (including GST): ${total:.2f}")
print("Name:" ,name,"Email:",email)

# print result
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

# pretend to discuss ordering
print("\n[Privacy Reminder] We guarantee that this restaurant will only use this data to send electronic receipts and take orders.")
print("\n[Ordering Prodece] We will send you meal soon, please wait you order.")  

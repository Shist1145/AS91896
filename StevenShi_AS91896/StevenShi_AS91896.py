# 无意义但必须要有的开头
import time
print("Welcome to Mc'Download backstage ordering program") # 绝对无意义的问候
print("Have a great choose for you meal!")
buck = 0 # 如题，buck is dollor
# 获取输入(let user choose item)
menu = {
        "1":("King Buger",14),
        "2":("Classic Buger",8),
        "3":("Double Buger",10),
        "4":("Fries",5),
        "5":("Fried Fish",6),
        "6":("Nuggents(5 pic)",8),
        "7":("Sodayo",2.5),
        "8":("Cool'Caal Cola",2.5),
        "9":("Push Cola",2.5),
        "0":("Stickers",1.5),
    }

print("\nPlease choose you meal:")
for key,(item,price) in menu.items():
    print(f"{key}.{item} - ${price:.2f}")

print("print 'done' when your finished.\n")

#点餐循环
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

# 判断条件
print("\nAnalysis completed, calculating prize and GST...\n")
print("Your meal prize are:", buck)
print("Your GST are:", GST)
# 输出结果
if buck + GST >= 50:
    print("Have a nice meal for your family, or for youself. 'Big stomach king'.")
elif buck + GST >= 40:
    print("That a great choose! Make sure don't waste food or friends.")
elif buck + GST >= 30:
    print("A luxurious meal! It will definitely be delicious")
elif buck + GST >= 20:
    print("Have a nice meal, we will make quick and clean")
else:
    print("Well, enjoy a nice and tasty meal.")

# 假装讨论点单内容
print("\n[Privacy Reminder] We will send you meal soon, please wait you order.")  

item_list=["Laptop","Headset","Secondmonitor","Mousepad","USB drive","External drive"]
print(item_list)
mandatory_items = item_list[0:3]
optional_items = item_list[3:6]
print(mandatory_items)
print(optional_items)


while True:
    limit=5000

    #tax free price
    item_price={"Laptop":2099,
                "Headset":199,
                "Secondmonitor":399,
                "Mousepad":59,
                "USB drive":99,
                "External drive":499}
                
    price=item_price.items()
    price=list(price)
    print("tax free price = ",price)

    #price with tax
    new_price=[]
    def create_invoice():
        price=item_price.items()
        price=list(price)
        for i,n in price:
            new_price.append((i,n*118/100))
    create_invoice()
    print("price with tax = ",new_price)
    
    print("""-----------------\nItem number;
1)Laptop
2)Headset
3)Secondmonitor
4)Mousepad
5)USB drive
6)External drive
0)If you want quit you enter...    
-----------------""")
    shopping_list=[]
    while True:
        
        number=int(input("Enter number for add item to shopping list: "))
        if(number>6):
            print("İnvalid number enter again")
            continue
        if (number<0):
            print("invalid number enter again")
            continue
        if number==1:
            shopping_list.append(item_list[0])
            
        elif number==2:
            shopping_list.append(item_list[1])
            
        elif number==3:
            shopping_list.append(item_list[2])
            
        elif number==4:
            shopping_list.append(item_list[3])
            
        elif number==5:
            shopping_list.append(item_list[4])
            
        elif number==6:
            shopping_list.append(item_list[5])

        elif number==0:
            break

    break

print(shopping_list)
while True:
    Left_limit=float(limit-(shopping_list.count("Laptop")*new_price[0][1]+
                          shopping_list.count("Headset")*new_price[1][1]+
                          shopping_list.count("Secondmonitor")*new_price[2][1]+
                          shopping_list.count("Mousepad")*new_price[3][1]+
                          shopping_list.count("USB drive")*new_price[4][1]+
                          shopping_list.count("External drive")*new_price[5][1]))
    if Left_limit<0:
        print("Your limit dont enough shopping list's price, you can delete something or you upper your limit.")
        print("If you can add {}$ you can buy your shopping list.".format(-1*Left_limit))
        
    else:
        print("Your shopping succesfull.")
        print("Your Left limit: ",Left_limit,"$")
    break

    






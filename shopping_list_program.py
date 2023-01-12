#This program creates a shopping list according to the receipes that I choose 
#and how many people we will serve

import math 

class Receipe:
    
    def __init__(self, receipe_name, ingredients_and_quantities, serves):
        self.receipe_name = receipe_name
        self.ingredients_and_quantities = ingredients_and_quantities
        self.serves = serves
        self.final_shopping_list = {}

    def shopping_list(self, staff_number, participants_numbers):
        numb_receipes = ((staff_number + participants_numbers)/self.serves)
        for item in self.ingredients_and_quantities:
            for i in item:
                if item[0] not in self.final_shopping_list:
                    self.final_shopping_list[item[0]] = [math.ceil(float(item[1]) * numb_receipes), item[2]]
        return self.final_shopping_list

coconut_pie = Receipe("Coconut Pie", [["Coconut Milk", 400, "ml"], ["Cashews", 200, "g"], 
["Digestive Biscuit", 200, "g"]], 12)

raw_chocolate_brownie = Receipe("Raw Chocolate Brownie", [["Dates", 200, "g"], ["Walnuts", 200, "g"], 
["Chocolate", 200, "g"]], 10)

banana_bread = Receipe("Banana Bread", [["Banana", 2, "un"], ["Walnuts", 100, "g"], 
["Wheat Flour", 250, "g"], ["Baking Soda", 10, "g"]], 10)

cocoa_courgette_bread = Receipe("Cocoa Courgette Bread", [["Courgette", 2, "un"], ["Wheat Flour", 250, "g"], 
["Cocoa Powder", 200, "g"]], 10)


print("This program will assist you in creating a shopping list. To get started, we'll need some information from you.")

numb_staff = float(input("\nHow many staff? "))

numb_participants = float(input("\nHow many guests? "))

receipe_list = ["1- Coconut Pie", "2- Raw Chocolate Brownie", "3- Banana Bread", "4- Cocoa Courgette Bread"]

print("\nEnter the recipe number to generate shopping list (e.g. type 1 for coconut pie)")

for i in receipe_list:   
    print(i)
    
receipe_code = int(input("\nType the number: "))

def concatena_medida(list_receipe):
    medida_confg = str(list_receipe[0]) + list_receipe[1]
    return medida_confg
    
if receipe_code == 1:
    print("\nHere is your shopping list:")
    for key, value in coconut_pie.shopping_list(numb_staff, numb_participants).items():
        value = concatena_medida(value)
        print(f'\n{key}:{value}')
  
if receipe_code == 2:
    print("\nHere is your shopping list:")
    for key, value in raw_chocolate_brownie.shopping_list(numb_staff, numb_participants).items():
        value = concatena_medida(value)
        print(f'\n{key}:{value}')
  
if receipe_code == 3:
    print("\nHere is your shopping list:")
    for key, value in banana_bread.shopping_list(numb_staff, numb_participants).items():
        value = concatena_medida(value)
        print(f'\n{key}:{value}')
  
if receipe_code == 4:
    print("\nHere is your shopping list:")
    for key, value in cocoa_courgette_bread.shopping_list(numb_staff, numb_participants).items():
        value = concatena_medida(value)
        print(f'\n{key}:{value}')
  




    
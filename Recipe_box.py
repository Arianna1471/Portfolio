Ingredients = {1:"1 Package of Puff pastry",2:"1 Package of Guava paste",3:"1 Package of Cream Cheese",4: "1 Egg",5:"and Cane Sugar" }
Instructions ={
"step1":"Preheat oven to 400 Degrees F",
"step2": "Thaw Puff pastry according to package directions.",
"step3":"Line a baking sheet with parchment paper and unfold one of the pastry sheets and place on pan.",
"step4":"Slice guava into 1/4 inch slices and place evenly on the pastry sheet.",
"step5":"Spread cream cheese over guava paste slices (optional)",
"step6":"Top with second puff pastry sheet and cut into desired pastry size. I cut mine in 2 inch squares.",
"step7":"Beat egg in a small bowl and brush over the top of the pastries. Sprinkle with cane sugar.",
"step8":"Bake at 400 degrees F for 25 minutes or until golden brown. Cool and serve ",
}

print("Ingredients:")
print(Ingredients[1])
print(Ingredients[2])
print(Ingredients[3])
print(Ingredients[4])
print(Ingredients[5])

print(" ")

print("Instructions:")
print(Instructions["step1"])
print(Instructions["step2"])
print(Instructions["step3"])
print(Instructions["step4"])
print(Instructions["step5"])
print(Instructions["step6"])
print(Instructions["step7"])
print(Instructions["step8"])

ans = input("which step do you want to see?")
print(Instructions[ans])

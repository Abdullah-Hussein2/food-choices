from random import choice


food = {"kabab": ["meat","lettuce","liced tomato","onions"]
    , "dolma" : ["rice"," lemon juice","tomatoes","mint",'olive oil']
,"masgouf" : ['fish']
,"falafel" : ["fava beans", "fresh herbs and spices"]
        }

random = choice(list(food.keys()))
print(f'how about trying {random}')

while True:
    choies = input('do you how to cook it Y OR N? ')
    if choies in ['yes','y',"Y"]:
        for ingred in food[random]:
           print(f"{ingred}")
        break
    elif choies in ['no' 'n']:
        print('exiting')
        break
    else:
        print("enter yes or no")


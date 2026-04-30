import random
import my_modul

# ran_int = random.randint(1,10) #radint(a,b) a<= random <=b
# print(ran_int)
# print(my_modul.my_favourite_number)

# ran_num_0to1 = random.random() # 0.0<= random <1.0
# print(ran_num_0to1)
#
# ran_float = random.uniform(1,10) # a<= random <=b for a<=b
# print(ran_float)

ran_num = random.randint(0,1)

if ran_num == 0:
    print("Heads")
else:
    print("Tails")
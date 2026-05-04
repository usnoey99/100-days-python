from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) occasional error
# This can sometimes cause an error because randint(1, 6) includes 6,
# but the list index only goes from 0 to 5. If 6 is chosen,
# it will try to access dice_images[6], which does not exist.

dice_num = randint(0, 5)
# This fixes the problem by generating numbers from 0 to 5,
# which correctly match the list indices.

print(dice_images[dice_num])

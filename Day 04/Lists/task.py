fruits = ["cherry", "apple", "pear"]
print(fruits)
fruits.append("blueberry") #맨뒤추가
print(fruits)
fruits.extend(["pineapple", "banana"]) #배열맨뒤추가
print(fruits)
fruits.insert(0, "kiwi") #인덱스지정추가
print(fruits)

#remove(x), pop([i]), clear(), count(x)...
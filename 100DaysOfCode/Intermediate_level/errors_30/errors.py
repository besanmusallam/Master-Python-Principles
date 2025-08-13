### Some Types of Errors

# # FileNotFound
# with open("a_file.txt") as f:
#     f.read()

# # KeyError
# dictt = {"key" : "value"}
# value = dictt["non_exist_key"]

# # IndexError
# fruit = ["orange", "apple", "banana"]
# print(fruit[4])

# # TypeError
# text = "123"
# print(text + 5)

### Solution

# FileNotFound

try:
    file = open("file.txt")
    dictt = {"key" : "value"}
    value = dictt["non_exist_key"]

except FileNotFoundError:
    file = open("file.txt", mode="w")
    file.write("Hi Beesaaan")

except KeyError as error_msg:
    print(f"key {error_msg} does not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("file is closed")
    
    # raise your own exception
    raise TypeError("this is made up")


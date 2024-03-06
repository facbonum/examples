# value = True # if value = "string", it returns string, while it exists

# while value:
#     print(value)
#     value = False # or 0
# # output: True

value = True
count = 0

while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0
        continue # causes evaluation before the loop executes again
    value = False # or 0
# output: 1
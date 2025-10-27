
values = [1, 2, "hello", 4, 5]

print(values[0])  # 1

print(values[3])  # 4
print(values[-1])  # prin last value in the list
print(values[1:0])  #[]

values.insert(3,"python")

print(values)

values.append("333")    # add to end
print(values)
values[2] = "Hello"

del values[0]

print(values)

# Tuple - Same as LIST Data type but immutable
val = (1,2,"rahul", 4.5)

print(val[1])

# val[2] = "Rahul"

print(val)

# Dictionary
dic = {"a":2, 4:"bcd", "c":"Hello world"}

print(dic[4])
print(dic["c"])


dict = {}

dict["firstname"] = "Rahul"

dict["lastname"] = "Huang"

dict["gender"] = "Male"

print(dict)
print(dict["firstname"])












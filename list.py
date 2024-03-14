numbers=[1, 2, 3, 4, 7, 13, 15, 6, 10, 8]
print(numbers)
print(numbers[4])
print(numbers[3:4])
print(numbers[3:6])
print(numbers[0])
print(numbers[0:10])
#Output
# [1, 2, 3, 4, 7, 13, 15, 6, 10, 8]
#7
#[4]
#[4, 7, 13]
#1
#[1, 2, 3, 4, 7, 13, 15, 6, 10, 8]
numbers.append(-39)
print("After Append:",numbers)
list=["soda", "cake", "bread", "tea", "donut",]
print(list)
#Tuple
list2=("soda", "cake", "bread", "tea", "donut",)
print(list2)
del list[-1]
print(list)
#changing list
list[-2]="coffee"
print(list)
#Dictionary
capital_city={"Kenya": "Nairobi", "Uganda": "Kampala", "Tanzania": "Daresalam" }
print(capital_city)
capital_city["South_Africa"]="CapeTown"
print("updated dictionary:", capital_city)


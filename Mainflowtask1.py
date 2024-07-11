list1=[1,2,3,4,5]
#adding item to the list
list1.append("Hello")
print(list1)
#removing item to the list
list1.remove(2)
print(list1)
#modifying the item
list1[2]=12
print(list1)
#inserting an item to the list
list1.insert(3,15)
print(list1)

tpl1=("apple","grapes","berries")
tpl2="guava"
#adding an element
new_tpl=tpl1+(tpl2,)
print(new_tpl)
#METHOD2
tpl1_l=list(tpl1)
tpl1_l.append("guava")
print(tuple(tpl1_l))
#removing an element
tpl_1=list(tpl1)
tpl_1.remove("grapes")
print(tuple(tpl_1))
#modifying an element
tpl_l=list(tpl1)
tpl_l[1]="orange"
print(tuple(tpl_l))

dict1={1:"berries",2:"grapes",3:"mango"}
#adding key:value pair to dict1
dict1[4]="plum"
print(dict1)
#removing key:value pair
del dict1[2]
print(dict1)
#modifying key-value pair
dict1[3]="guava"
print(dict1)

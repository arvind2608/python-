#dictionary
d={}
print(type(d))#print class type

d[1234]="celin"
d[1235]="ilangoven"
d[1236]="illangoven"
d[1237]="lenin"
print(d)#print objects in dictionary


d={1234:'celin',1235:'ilangoven',
1236:'rajarajan',1237:'lenin'}
print(d[1236])#print value

d={1234:'celin',1235:'ilangoven',
1236:'rajarajan',1237:'lenin'}
print(len(d))# print length value 
print(d.values())#print dict_values
print(d.get(1234))#get value from dict
print(d.popitem())#pops random key in dict
print(d.pop(1234))# pop the key out the dict


for key in d.keys():#used to print all objects in order
  print(key)
  
d={1234:'celin',1235:'ilangoven',
1236:'rajarajan',1237:'lenin'}
print(d[1236])#print value


  

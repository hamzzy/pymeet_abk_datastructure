hello={'name':('musa','segun','logo','snake that swallow 35 billion')}
#adding to a dictionary
hello['snake']="35 billion in jamb office chai"
#deleting from a list
del hello['snake']
#printin dictionary in list
lis=list(hello)
print(lis)
print(hello)
#dictionary comprhension
a={x:x**2 for x in(2,3,4)}
print(a)
#dictionary using build itn dictionary
f= dict(sape=4139, guido=4127, jack=4098)
print(f)
#LOOPIN THROUGH A DICTIONARY
store={"dad":"rice",'musa':'pic'}
for key,value in store.items():
  print(value ,"ate" ,key)


x = "["
Stack = []
flag = True
temp = -1
for i in range(0,len(x)):
   if x[i]=="(" or x[i]=="[" or x[i]=="{":
      Stack.append(x[i])
      temp= temp+1
   elif x[i]==")" or x[i]=="]" or x[i]=="}":
      if (x[i] == ")" and len(Stack)>0 and Stack[temp] == "("):
         Stack.pop()
         temp= temp-1
      elif( x[i]=="]" and len(Stack)>0 and Stack[temp] == "["):
         Stack.pop()
         temp = temp-1
      elif( x[i]=="}" and len(Stack)>0 and Stack[temp] == "{"):
         Stack.pop()
         temp = temp-1
      else:
         flag=False
         break
   else:
      flag = False
      break

if (len(Stack)>0 or flag==False):
   print(False)
else:
   print(True)
S = "hello"
length = len(S)
s = 0
for i in range(0 , length-1):
    if len(S) > 1:
        s = s+abs(ord(S[i])-ord(S[i+1]))

print(s) 
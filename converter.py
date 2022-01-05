i= 0
j= 0
output = [[]]
l = "Hello world"
for a in l:
  if a == " ":
    i = i + 1
    output.append([])
    j= 0
  else:
    output[i].append("00000000"+str(format(ord(a), '08b')))
    # print("**"+str(i)+"**"+str(j)+"**")
    # print(output[i][j])
    j = j + 1
print(output)

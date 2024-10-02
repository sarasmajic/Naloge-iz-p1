def domine(s):
  seznam = []
  for i in range(len(s) - 1):  
   #print(s[i + 1][0])
    if(s[i][1] == s[i + 1][0]):
      continue
    else:
      return False
    
  return True

vrne = domine([(6, 6), (6, 2), (2, 9)])
print(vrne)

#(3, 6), (6, 6), (2, 3)
#(3, 6), (6, 6), (6, 1), (1, 0)
file1 = open('input.txt', 'r')
Lines = file1.readlines()[1:]
count = 0

allValid = True
errorCodes = []

for line in Lines: # skip line one
    count += 1
    data = (line.strip().split(" "))
    if int(data[0]) < 1 or int(data[0]) > 1000:
        allValid = False
    if data[1] == 'false':
        allValid = False
        errorCodes.append(data[2])
    


if(allValid == True):
    print("Yes")
else:
    print("No")
print(' '.join(str(e) for e in errorCodes))
# Strips the newline character

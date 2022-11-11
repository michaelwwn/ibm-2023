total = int(input('What is the total number of T-shirts in your shop?\n'))
sizes = input('Name the t-shirt sizes in shop.\n').split(' ')
requestAmount = int(input('What many request are there?\n'))
requestSize = input('What is the requested sizes?\n').split(' ')
fill = True
# TODO: exit instead
if total < 1 or total > 1000:
    print('Invalid total number of T-shirts in your shop.')
    quit()

if requestAmount < 1 or requestAmount > total:
    print('Invalid requests amount of T-shrits.')
    quit()

sizeList = []
for size in sizes:
    sizeCode = 0
    # Assign a number to size
    if(size[-1] == 'S'):
        sizeCode = 1000 - len(size)
    if(size[-1] == 'M'):
        sizeCode = 2000
    if(size[-1] == 'L'):
        sizeCode = 3000 + len(size)
    sizeList.append(sizeCode)
sizeList.sort()

requestList = []
# If a larger number exists, assign it.
for rsize in requestSize:
    rsizeCode = 0
    # Assign a number to size
    if(rsize[-1] == 'S'):
        rsizeCode = 1000 - len(rsize)
    if(rsize[-1] == 'M'):
        rsizeCode = 2000
    if(rsize[-1] == 'L'):
        rsizeCode = 3000 + len(rsize)
    requestList.append(rsizeCode)
requestList.sort()
for request in requestList:
    match = [x for x in sizeList if x >= request]
    if match:
        i = sizeList.index(match[0])
        sizeList.pop(i)
    else:
        fill = False

print(fill)
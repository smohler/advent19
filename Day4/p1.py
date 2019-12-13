# load input data
upperLimit = 675869
lowerLimit = 172851
test1 = 111111 #pass
test2 = 223450 #fail
test3 = 123789 #fail
test4 = 123444 #fail
test5 = 112233 #pass
test6 = 111122 #pass
testrange = [test1, test2, test3, test4, test5, test6]
pwrange = range(lowerLimit,  upperLimit)
possiblepw = []

for i in pwrange:
    digit = str(i)
    monotonic = True
    group = {}
    #create a dictionary of all grouped digits
    for j in range(0,5):
        pair = digit[j] == digit[j+1]
        if pair == True:
            group.update({digit[j] : digit.count(digit[j])})
    #Part 1 At least one group value >= 2
    #groups = max(list(group.values()))>1
    #Part 2 At least one group value == 2        
     
    groups = 2 in group.values()  

    #check for monotonicity 
    for j in range(5):
        monotonic = digit[j]<=digit[j+1]
        if monotonic == False:
            break

    possible = (groups and monotonic)
    message = '{}\t Digit : {}\t Possible : {}'
    if possible:
        possiblepw.append(digit)  
        print(message.format(len(possiblepw), i,possible)) 
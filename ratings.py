"""Restaurant rating lister."""
# put your code here
dict = {}


with open ('scores.txt', 'rt') as myfile:
    for myline in myfile:
        key = ((myline.split(':'))[0]) # first part of list
        value = ((myline.split(':'))[1]) # second part of list
        value = value.replace('\n', '')
        dict[key] = value



key = input('What is the name of the restaurant')
value = input('What would you rate us from 1-5?')
#print(type(key))
#print(type(value))
dict[key] = int(value)
dict = sorted(dict.items())
#print(dict)

dict2 = {

}

i = 0
while (i < len(dict)):
    key = dict[i][0]
    value = dict[i][1]
    i+=1
    dict2[key] = value
print(dict2)    
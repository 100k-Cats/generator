# 100kCat.eth
# args: val (must be 5 digit)
from sympy import isprime
import sys

# e.g. 34343, 49494
def isAlternating(string):
    if string[0] == string[2] == string[4] and string[1] == string[3] and string[0] != string[1]:
        return(True)
    else:
        return(False)

# e.g. 12345, 13579, 86420
def isIncrementing(string):
    if int(string[0]) - int(string[1]) == int(string[1]) - int(string[2]) == int(string[2]) - int(string[3]) == int(string[3]) - int(string[4]) != 0:
        return(int(string[0]) - int(string[1]))
    else:
        return(0)

# finds repetitiveness (adjacent or otherwise)
def getRepeating(string, heir):
    store = []
    for item in set(string):
        store.append([item, string.count(item)])
    items = [item[0] for item in store]
    count = [item[1] for item in store]
    if max(count) > 1:
        index = max(range(len(count)), key=count.__getitem__)
        regex = ''.join(max(count)*items[index])
        if heir == 1:
            if regex in string:
                return(max(count), items[index], 1)
            else:
                if regex[:-1] in string and len(regex[:-1]) > 1:
                    return(max(count) - 1, items[index], 1)
                else:
                    if regex[:-2] in string and len(regex[:-2]) > 1:
                        return(max(count) - 2, items[index], 1)
                    else:
                        return(max(count), items[index], 0)
        else:
            if regex in string:
                return(max(count), items[index], 1)
            else:
                return(max(count), items[index], 0)
    else:
        return(1, 'NaN', 0)


# checks for palindromes
def isPalindrome(string):
    if string == string[::-1] and len(string) > 2:
        flag = True
    else:
        flag = False
    return(flag)

# checks for even numbers
def isEven(num):
    if num % 2 == 0:
        flag = True
    else:
        flag = False
    return(flag)

# checks for odd numbers
def isOdd(num):
    if num % 2 != 0:
        flag = True
    else:
        flag = False
    return(flag)

# checks for prime numbers
def isPrime(num):
    flag = False
    if isprime(num):
        flag = True
    return(flag)

# MAIN

string = sys.argv[1]
num = int(string)
[type, val, adj] = getRepeating(string, 0)      # check non-heirarchically
[type_, val_, adj_] = getRepeating(string, 1)   # check heirarchically

layers = []

# Layer 0: Background
background = ['Brown', 'Yellow', 'Orange', 'Pink', 'Purple', 'Green', 'Red', 'White', 'Blue', 'Black']
layers.append([0, string[0], background[int(string[0])]])

# Layer 1: Digits
layers.append([1, 'D', '-'])

# Layer 2: Rear
rear = ['Baseball Bat', 'Ukulele', 'Skateboard', 'Katanas', 'LFG Balloon', 'Rocket Launcher', 'Devil Wings', 'Angel Wings', 'Stick Horse', 'Fancy Confetti']
if type_ > 1 and adj_ == 1:   # adjacent doubles, triples, quadruples, quintuples
    layers.append([2, val, rear[int(val)]])
else:
    layers.append([2, '-', '-'])

# Layer 3: Cat
cat = ['Calico', 'Abyssinin', 'Bengal', 'Sphynx', 'Japanese Bobtail', 'American Shorthair', 'Tuxedo', 'Siamese', 'Brown Cowboy', 'Bombay']
layers.append([3, string[1], cat[int(string[1])]])

# Layer 4: Clothing
clothing = ['Football Pads', 'Hawaiian Shirt', 'Orange Hoodie', 'Polkadot Shirt', 'Birthday Suit', 'Camo Tanktop', 'Red Cape', 'White Robe', 'Blue Overalls', 'Black Tuxedo']
layers.append([4, string[2], clothing[int(string[2])]])

# Layer 5: .eth
ethlabel = ['Boots', 'Hawaiian Lei', 'Gold Chain', 'Boxing Gloves', 'Cake', 'Dog Tags', 'Red Amulet', 'Scroll', 'Pistols', 'Bow Tie']
layers.append([5, string[3], ethlabel[int(string[3])]])

# Layer 6: Eyewear
eyewear = ['\'Deal With It\' Shades', '3D Glasses', 'Rainbow Goggles', 'Snowboarding Goggles']
if type == 2:      # 2-of-a-Kind
    layers.append([6, '0', eyewear[0]])
elif type == 3:    # 3-of-a-Kind
    layers.append([6, '1', eyewear[1]])
elif type == 1 and isIncrementing(string) == 0:         # non-repeating
    layers.append([6, '2', eyewear[2]])
elif type == 1 and abs(isIncrementing(string)) == 1:    # non-repeating & ascending/descending
    layers.append([6, '3', eyewear[3]])
else:
    layers.append([6, '-', '-'])

# Layer 7: Hat
hat = ['Brown Football Helmet', 'Spinny Cap', 'Beer Helmet', 'Headband', 'Birthday Hat', 'Army Helmet', 'Devil Horns', 'Halo', 'Cowboy Hat', 'Top Hat']
layers.append([7, string[4], hat[int(string[4])]])

# Layer 8: Crown
crown = ['Gold', 'Silver', 'Bronze']
if type == 5:                   # 5-of-a-Kind (= Quintuple)
    layers[-1] = [7, '-', '-']
    layers.append([8, '0', crown[0]])
elif type == 4:                 # 4-of-a-Kind
    layers[-1] = [7, '-', '-']
    layers.append([8, '1', crown[1]])
elif isPalindrome(string):      # palindrome
    layers[-1] = [7, '-', '-']
    layers.append([8, '2', crown[2]])
else:
    layers.append([8, '-', '-'])

# Layer 9: Mouth
mouth = ['Bloody Fangs', 'Burning Cigar', 'Rose']
if '666' in string:
    layers.append([9, '666', mouth[0]])
if '420' in string:
    layers.append([9, '420', mouth[1]])
if '69' in string:
    layers.append([9, '69', mouth[2]])
else:
    layers.append([9, '-', '-'])

# Layer 10: Foreground
foreground = ['Trident']
if '666' in string:
    layers.append([10, '6', foreground[0]])
else:
    layers.append([10, '-', '-'])

# final
i_ = [str(layer[0]) for layer in layers]
layers_ = [layer[1] for layer in layers]
traits_ = [layer[2] for layer in layers]
print(' '.join(i_) + '+' + ' '.join(layers_) + '+' + '='.join(traits_))

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

# get sum of digits
def getSum(string):
    n = int(string)
    while n > 9:
        n = sum(map(int, str(n)))
    return(n)

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
[ type,  val,  adj] = getRepeating(string, 0)   # check non-heirarchically; non-adjacent check
[type_, val_, adj_] = getRepeating(string, 1)   # check heirarchically; adjacent check

layers = []

# Layer 0: Background
background = ['Brown', 'Yellow', 'Orange', 'Pink', 'Purple', 'Green', 'Red', 'White', 'Blue', 'Black']
layers.append([0, string[0], background[int(string[0])], '-', 'Background'])

# Layer 1: Digits
if type == 5:               # Gold lettering
    layers.append([1, 'G', '-', '-', 'Digits'])
elif type == 4:             # Silver lettering
    layers.append([1, 'S', '-', '-', 'Digits'])
elif isPalindrome(string):  # Bronze lettering
    layers.append([1, 'B', '-', '-', 'Digits'])
else:                       # White lettering
    layers.append([1, 'W', '-', '-', 'Digits'])

# Layer 2: Rear > SPECIAL
rear = ['Baseball Bat', 'Ukulele', 'Skateboard', 'Katanas', 'LFG Balloon', 'Rocket Launcher', 'Devil Wings', 'Angel Wings', 'Stick Horse', 'Fancy Confetti']
if type_ > 1 and adj_ == 1:   # adjacent doubles, triples, quadruples, quintuples
    if type_ == 2:
        layers.append([2, val_, rear[int(val_)], ''.join(['💎' if x == val_ else '❌' for x in string]), 'Rear'])
    elif type_ == 3:
        layers.append([2, val_, rear[int(val_)], ''.join(['💎' if x == val_ else '❌' for x in string]), 'Rear'])
    elif type_ == 4:
        layers.append([2, val_, rear[int(val_)], ''.join(['💎' if x == val_ else '❌' for x in string]), 'Rear'])
    elif type_ == 5:
        layers.append([2, val_, rear[int(val_)], '💎💎💎💎💎', 'Rear'])
else:
    layers.append([2, '-', '-', '-', 'Rear'])

# Layer 3: Cat
cat = ['Calico', 'Abyssinin', 'Bengal', 'Sphynx', 'Japanese Bobtail', 'American Shorthair', 'Tuxedo', 'Siamese', 'Brown Cowboy', 'Bombay']
layers.append([3, string[1], cat[int(string[1])], '-', 'Body'])

# Layer 4: Clothing
clothing = ['Football Pads', 'Hawaiian Shirt', 'Orange Hoodie', 'Polkadot Shirt', 'Birthday Suit', 'Camo Tanktop', 'Red Cape', 'White Robe', 'Blue Overalls', 'Black Tuxedo']
layers.append([4, string[2], clothing[int(string[2])], '-', 'Clothing'])

# Layer 5: .eth
ethlabel = ['Boots', 'Hawaiian Lei', 'Gold Chain', 'Boxing Gloves', 'Cake', 'Dog Tags', 'Red Amulet', 'Scroll', 'Pistols', 'Bow Tie']
layers.append([5, string[3], ethlabel[int(string[3])], '-', '.eth'])

# Layer 6: Eyewear > SPECIAL
eyewear = ['\'Deal With It\' Shades', 'Rainbow Goggles', '3D Glasses', 'Snowboarding Goggles', 'Eye Patch', 'VR Goggles White', 'VR Goggles Black']
if type == 2:      # 2-of-a-Kind
    if type_ == 2:
        layers.append([6, '0', eyewear[0], '-', 'Eyewear'])
    else:
        layers.append([6, '0', eyewear[0], ''.join(['💎' if x == val else '❌' for x in string]), 'Eyewear'])
elif type == 3:    # 3-of-a-Kind
    if type_ == 3:
        layers.append([6, '1', eyewear[1], '-', 'Eyewear'])
    else:
        layers.append([6, '1', eyewear[1], ''.join(['💎' if x == val else '❌' for x in string]), 'Eyewear'])
elif type == 4:    # 4-of-a-Kind
    leftover = [x for x in string];
    leftover.remove(val);
    if len(leftover) == 1:
        if isEven(leftover[0]):
            if type_ == 4:
                layers.append([6, '5', eyewear[5], '-', 'Eyewear'])
            else:
                layers.append([6, '5', eyewear[5], ''.join(['💎' if x == val else '❌' for x in string]), 'Eyewear'])
        else:
            if type_ == 4:
                layers.append([6, '6', eyewear[6], '-', 'Eyewear'])
            else:
                layers.append([6, '6', eyewear[6], ''.join(['💎' if x == val else '❌' for x in string]), 'Eyewear'])
elif type == 1 and isIncrementing(string) == 0:         # non-repeating
    layers.append([6, '2', eyewear[2], '🌈🌈🌈', 'Eyewear'])
elif type == 1 and abs(isIncrementing(string)) == 1:    # non-repeating & ascending/descending
    if isIncrementing(string) == -1:
        layers.append([6, '3', eyewear[3], '‍🌈📈🌈', 'Eyewear'])
    elif isIncrementing(string) == -1:
        layers.append([6, '4', eyewear[4], '🌈📉🌈', 'Eyewear'])
else:
    layers.append([6, '-', '-', '-', 'Eyewear'])

# Layer 7: Hat
hat = ['Brown Football Helmet', 'Spinny Cap', 'Beer Helmet', 'Headband', 'Birthday Hat', 'Army Helmet', 'Devil Horns', 'Halo', 'Cowboy Hat', 'Top Hat']
layers.append([7, string[4], hat[int(string[4])], '-', 'Headwear'])

# Layer 8: Crown > SPECIAL
crown = ['Gold', 'Silver', 'Bronze']
if type == 5:                   # 5-of-a-Kind (= Quintuple) | Gold
    layers[-1] = [7, '-', '-', '-', 'Headwear']
    layers.append([8, '0', crown[0], '-', 'Crown'])
elif type == 4:                 # 4-of-a-Kind | Silver
    layers[-1] = [7, '-', '-', '-', 'Headwear']
    layers.append([8, '1', crown[1], '-', 'Crown'])
elif isPalindrome(string):      # Palindrome | Bronze
    layers[-1] = [7, '-', '-', '-', 'Headwear']
    layers.append([8, '2', crown[2], '🌘🌗🌕🌓🌒', 'Crown'])
else:
    layers.append([8, '-', '-', '-', 'Crown'])

# Layer 9: Mouth > SPECIAL
mouth = ['Bloody Fangs', 'Burning Cigar', 'Rose', 'Whistle', 'Lollipop', 'Smoking Pipe', 'Cigarette', 'Pizza', 'Vuvuzela', 'Straw', 'WAGMI', 'GM']
if   '666' in string and  '69' not in string:
    layers.append([9, '666', mouth[0], '😈🎃💀', 'Mouth'])
elif '420' in string and  '69' not in string:
    layers.append([9, '420', mouth[1], '🚬😮‍💨', 'Mouth'])
elif  '69' in string and '666' not in string and '420' not in string:
    layers.append([9, '69',  mouth[2], '👅🍆💦', 'Mouth'])
elif '666' in string and  '69' in string:
    layers.append([9, '666', mouth[0], '😈🎃💀', 'Mouth'])
    layers.append([9, '69',  mouth[2], '👅🍆💦', 'Mouth'])
elif '420' in string and  '69' in string:
    layers.append([9, '420', mouth[1], '🚬😮‍💨', 'Mouth'])
    layers.append([9, '69',  mouth[2], '👅🍆💦', 'Mouth'])
elif getSum(string) == 1:
    layers.append([9, 'S1',  mouth[3], '🌐#️⃣1️⃣', 'Mouth'])
elif getSum(string) == 2:
    layers.append([9, 'S2',  mouth[4], '🌐#️⃣2️⃣', 'Mouth'])
elif getSum(string) == 3:
    layers.append([9, 'S3',  mouth[5], '🌐#️⃣3️⃣', 'Mouth'])
elif getSum(string) == 4:
    layers.append([9, 'S4',  mouth[6], '🌐#️⃣4️⃣', 'Mouth'])
elif getSum(string) == 5:
    layers.append([9, 'S5',  mouth[7], '🌐#️⃣5️⃣', 'Mouth'])
elif getSum(string) == 6:
    layers.append([9, 'S6',  mouth[8], '🌐#️⃣6️⃣', 'Mouth'])
elif getSum(string) == 7:
    layers.append([9, 'S7',  mouth[9], '🌐#️⃣7️⃣', 'Mouth'])
elif getSum(string) == 8:
    layers.append([9, 'S8', mouth[10], '🌐#️⃣8️⃣', 'Mouth'])
elif getSum(string) == 9:
    layers.append([9, 'S9', mouth[11], '🌐#️⃣9️⃣', 'Mouth'])
else:
    layers.append([9, '-', '-', '-', 'Mouth'])

# Layer 10: Foreground > SPECIAL
foreground = ['Trident', 'Hookah', 'Rose', 'ENS Football', '.eth Badge', 'Throwing Star', 'Gift', 'Grenade', 'Magic Staff', 'Cocktail']
if   '666' in string and  '69' not in string:
    layers.append([10, '666', foreground[0], '-', 'Foreground'])
elif '420' in string and  '69' not in string:
    layers.append([10, '420', foreground[1], '-', 'Foreground'])
elif  '69' in string and '666' not in string and '420' not in string:
    layers.append([10, '69',  foreground[2], '-', 'Foreground'])
elif '666' in string and  '69' in string:
    layers.append([10, '666', foreground[0], '-', 'Foreground'])
    layers.append([10, '69',  foreground[2], '-', 'Foreground'])
elif '420' in string and  '69' in string:
    layers.append([10, '420', foreground[1], '-', 'Foreground'])
    layers.append([10, '69',  foreground[2], '-', 'Foreground'])
elif isEven(num):
    layers.append([10, 'even', foreground[3], 'Even 🏁', 'Foreground'])
elif isOdd(num):
    layers.append([0, '-', '-', 'Odd 🚩', 'Foreground'])
    if isPrime(num) and int(string[-1]) != 5:
        layers.append([0, '-', '-', 'Prime 💍', 'Foreground'])
        if int(string[-1]) == 1:
            layers.append([10, 'P1', foreground[5], '1️⃣🔚💍', 'Foreground'])
        elif int(string[-1]) == 3:
            layers.append([10, 'P3', foreground[6], '3️⃣🔚💍', 'Foreground'])
        elif int(string[-1]) == 7:
            layers.append([10, 'P7', foreground[7], '7️⃣🔚💍', 'Foreground'])
        elif int(string[-1]) == 9:
            layers.append([10, 'P9', foreground[8], '9️⃣🔚💍', 'Foreground'])
    elif int(string[-1]) == 5 and not isPrime(num):
        layers.append([10, '0', foreground[9], '5️⃣🔚#️⃣', 'Foreground'])
    elif int(string[-1]) == 5 and isPrime(num):
        layers.append([10, '0', foreground[9], '5️⃣🔚💍', 'Foreground'])
    else:
        layers.append([10, 'odd', foreground[4], '-', 'Foreground'])
else:
    layers.append([10, '-', '-', '-', 'Foreground'])

# final
i_ = [str(layer[0]) for layer in layers]
layers_ = [layer[1] for layer in layers]
traits_ = [layer[2] for layer in layers]
values_ = [layer[3] for layer in layers]
names__ = [layer[4] for layer in layers]
print(' '.join(i_) + '+' + ' '.join(layers_) + '+' + '='.join(traits_) + '+' + '='.join(values_) + '+' + '='.join(names__))

'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''


b = [1]
while max(b) < 500000:
    b.append(b[-1]*2)

b = b[::-1]

def palindrome_string(s):
    s = str(s)
    l = len(s)

    if l % 2 == 1:
        l -= 1
        f_h = s[:int(l/2)]
        s_h = s[int(l/2) + 1:]

        return f_h == s_h[::-1]

    else:
        f_h = s[:int(l/2)]
        s_h = s[int(l/2):]
        return f_h == s_h[::-1]

def to_binary(i):
    global b
    binary = "00000000000000000000"
    ind = -1
    our_set = [each for each in b if each <= i]

    binary = binary[:len(our_set)]
    binary = list(binary)

    for x in our_set:
        ind += 1
        if x <= i:
            binary[ind] = "1"
            i -= x
    return("".join(binary))

answers = []

for x in range(1,1000001):
    if palindrome_string(x):
        if palindrome_string(to_binary(x)):
            answers.append(x)
            print(x)
print(sum(answers))
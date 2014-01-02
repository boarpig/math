#!/usr/bin/python

ones = { 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 
         19: 'nineteen'}
tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
        6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

length = 0

for i in range(1, 1000+1):
    word = ''
    if i == 1000:
        word += 'onethousand'
    else:
        if i < 1000 and i > 99:
            word += ones[int(str(i)[0])] + 'hundred'
            i = int(str(i)[1:])
            if i != 0:
                word += 'and'
        if i != 0:
            if i <= 99 and i >= 20:
                word += tens[int(str(i)[0])]
                i = int(str(i)[1:])
            if i != 0:
                if i <= 19 and i >= 10:
                    word += teens[i]
                elif i < 10:
                    word += ones[i]
    print word
    length += len(word)
print length

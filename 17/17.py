"""
   If the numbers 1 to 5 are written out in words: one, two, three, four,
   five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

   If all the numbers from 1 to 1000 (one thousand) inclusive were written
   out in words, how many letters would be used?

   NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
   forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
   20 letters. The use of "and" when writing out numbers is in compliance
   with British usage.
"""

N_0_19  =   ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 
            'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
            'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
N_TENS  =   ('zero', 'ten', 'twenty', 'thirty', 'forty', 
            'fifty', 'sixty', 'seventy', 'eighty', 'ninety')

def n2text(n):
    """Converts a number n to its lexical string representation""" 
    if 0 <= n < 20:
        return N_0_19[n]
    elif 20 <= n < 100:
        if not n % 10:
            return N_TENS[n // 10]
        return N_TENS[n // 10] + '-' + n2text(n % 10)
    elif 100 <= n < 1000:
        if not n % 100:
            return n2text(n // 100) + ' hundred'
        return n2text(n // 100) + ' hundred and ' + n2text(n % 100)
    elif 1000 <= n:
        if not n % 1000:
            return n2text(n // 1000) + ' thousand'
        return n2text(n // 1000) + ' thousand ' + n2text(n % 1000)
    else:
        return ''

def alphalen(text):
    """Returns the number of alphabetical characters in text"""
    return len([x for x in text if x.isalpha()])

if __name__ == '__main__':
    upper = 1000
    
    letters_used = sum(map(alphalen, map(n2text, range(1, upper + 1))))
    
    print(letters_used)


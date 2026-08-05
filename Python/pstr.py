#!/bin/python3

# spmather
# 2026-07-15
# 2026-08-04
# 1.0.1

# Import note if running from terminal:  
#     import sys 
#     sys.path.append('/path/to/script/folder')  # remove with sys.path.remove('/path/to/script/folder')
#     import pstr
#     pstr.pstrd("String 1","String 2")

import string

def pstrd(reference,difference):
    """
    Probability of strings matching with debug
    using the equation
    ((common words/total words)+(common characters/total characters))/2 or the mean of the input

    """
 
    # Formats words in a string as a list
    refword_l   = []
    difword_l   = []
    for sym in string.punctuation:
        reference = reference.replace(sym,' ')
    ref_replace = reference
    print(f"Reference list with replacement {ref_replace}")
    refword_l   = ref_replace.split()
    print(f"Reference word list {refword_l}")
    for sym in string.punctuation:
        difference = difference.replace(sym,' ')
    dif_replace = difference
    print(f"Difference list with replacement {dif_replace}")
    difword_l   = dif_replace.split()
    print(f"Difference word list {difword_l}")

    # Formats characters in a string as a list
    refchar_l = list(ref_replace.lower().replace(' ',''))
    print(f"Reference character list is {refchar_l}")
    difchar_l = list(dif_replace.lower().replace(' ',''))
    print(f"Difference character list is {difchar_l}")

    # Find the total number of characters
    charlen = len(refchar_l) + len(difchar_l)
    print(f"Total number of characters {charlen}")

    # Find the total number of words
    wordlen = len(refword_l) + len(difword_l)
    print(f"Total number of words {wordlen}")

    # Compare the values in character lists
    sortrefchar_l = sorted(refchar_l)
    sortdifchar_l = sorted(difchar_l)
    commonchar_l  = []

    # Brute force iterations
    # I had issues with enumerate(zip()) missing letters
    # In:  pstrd("Hello my old friend","Hello my new friend"), the letters m and r were excluded
         
    upperlimit = charlen ** 2
    errorcount = 0

    for i in range(charlen):
        for refletter in sortrefchar_l:
            for difletter in sortdifchar_l:
                print(i)
                print(f"~~~~ iteration count is {i} ~~~~")
                if refletter == difletter:
                    print(f"reference letter is {refletter}")
                    print(f"difference letter is {difletter}")
                    commonchar_l.append(refletter)
                    commonchar_l.append(difletter)
                    print(f"common character list is now {commonchar_l}")
                    sortrefchar_l.remove(refletter)
                    sortdifchar_l.remove(difletter)
                    print(f"sorted reference character list is now {sortrefchar_l}")
                    print(f"sorted difference character list is now {sortdifchar_l}")
                else:
                    errorcount += 1
                    print(f"errorcount is {errorcount}")
                if i > upperlimit:
                    print(f"iteration {i} is over exponential limits {upperlimit}")
                if errorcount == upperlimit:
                    print(f"errorcount {errorcount} is at exponential limits {upperlimit}")
                elif errorcount > upperlimit:
                    print(f"errorcount {errorcount} is over exponential limits {upperlimit}")
    print(f"Common characters are {commonchar_l}")
    commoncharlen = len(commonchar_l)
    print(f"Number of common characters {commoncharlen}")

    # Divide Common characters by total characters
    charpercent = commoncharlen / charlen
    print(f"Percent of characters that are common {charpercent}")
        
    # Compare the values in word lists
    #commonword_l  = list(set(refword_l) & set(difword_l))
    sordrefword_l = sorted(refword_l)
    sortdifword_l = sorted(difword_l) 
    commonword_l = []
    for i, (ref,dif) in enumerate(zip(sordrefword_l,sortdifword_l)):
        if ref == dif:
            print(f"refword is {ref}")
            print(f"difword is {dif}")
            commonword_l.append(ref)
            commonword_l.append(dif)
    print(f"Common words are {commonword_l}")
    commonwordlen = len(commonword_l)
    print(f"Total common words {commonwordlen}")

    # Divide Common words by total words
    wordpercent = commonwordlen / wordlen
    print(f"Percent of words that are common {wordpercent}")

    # Get the mean of common words and common characters
    prob = (charpercent + wordpercent) / 2
    
    # End
    return prob


def pstr(reference,difference):
    """
    Probability of strings matching with no debug
    using the equation
    ((common words/total words)+(common characters/total characters))/2 or the mean of the input

    """
    refword_l   = []
    difword_l   = []
    for sym in string.punctuation:
        reference = reference.replace(sym,' ')
    ref_replace = reference
    refword_l   = ref_replace.split()
    for sym in string.punctuation:
        difference = difference.replace(sym,' ')
    dif_replace = difference
    difword_l   = dif_replace.split()
    refchar_l = list(ref_replace.lower().replace(' ',''))
    difchar_l = list(dif_replace.lower().replace(' ',''))
    charlen = len(refchar_l) + len(difchar_l)
    wordlen = len(refword_l) + len(difword_l)
    sortrefchar_l = sorted(refchar_l)
    sortdifchar_l = sorted(difchar_l)
    commonchar_l  = []
    errorcount = 0
    for i in range(charlen):
        for refletter in sortrefchar_l:
            for difletter in sortdifchar_l:
                if refletter == difletter:
                    commonchar_l.append(refletter)
                    commonchar_l.append(difletter)
                    sortrefchar_l.remove(refletter)
                    sortdifchar_l.remove(difletter)
                else:
                    errorcount += 1
    commoncharlen = len(commonchar_l)
    charpercent = commoncharlen / charlen
    sordrefword_l = sorted(refword_l)
    sortdifword_l = sorted(difword_l) 
    commonword_l = []
    for i, (ref,dif) in enumerate(zip(sordrefword_l,sortdifword_l)):
        if ref == dif:
            commonword_l.append(ref)
            commonword_l.append(dif)
    commonwordlen = len(commonword_l)
    wordpercent = commonwordlen / wordlen
    prob = (charpercent + wordpercent) / 2
    return prob

# fin

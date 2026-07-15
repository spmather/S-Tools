#!/bin/python3

# spmather
# 2026-07-14
# 0.0.1

# Import note if running from terminal:  
#     import sys 
#     sys.path.append('/path/to/script/folder')  # remove with sys.path.remove('/path/to/script/folder')
#     import pstr
#     pstr.pstr("String 1","String 2")

def pstr(reference,difference):
    """
    Probability of strings matching
    using the equation
    ((common words/total words)+(common characters/total characters))/2 or the mean of the input

    """

    # Formats characters in a string as a list
    refchar_l = list(reference.lower())
    print(f"Reference character list is {refchar_l}")
    difchar_l = list(difference.lower())
    print(f"Difference character list is {difchar_l}")

    # Formats words in a string as a list
    refword_l   = []
    difword_l   = []
    ref_replace = reference.replace(',',' ').replace('.',' ').replace(':',' ').replace('-',' ').replace('_',' ').replace('  ',' ').replace('   ',' ')
    print(f"Reference list with replacement {ref_replace}")
    refword_l   = ref_replace.split(' ')
    print(f"Reference word list {refword_l}")
    dif_replace = difference.replace(',',' ').replace('.',' ').replace(':',' ').replace('-',' ').replace('_',' ').replace('  ',' ').replace('   ',' ')
    print(f"Difference list with replacement {dif_replace}")
    difword_l   = dif_replace.split(' ')
    print(f"Difference word list {difword_l}")

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
    for i, (ref,dif) in enumerate(zip(sortrefchar_l,sortdifchar_l)):
        if ref == dif:
            print(f"refchar is {ref}")
            print(f"difchar is {dif}")
            commonchar_l.append(ref)
            commonchar_l.append(dif)
    
    print(f"Common characters are {commonchar_l}")
    commoncharlen = len(commonchar_l)
    print(f"Number of common characters {commoncharlen}")

    # Divide Common characters by total characters
    charpercent = commoncharlen / charlen
    print(f"Percent of characters that are common {charpercent}")
        
    # Compare the values in word lists
    commonword_l  = list(set(refword_l) & set(difword_l))
    print(f"Common words are {commonword_l}")
    commonwordlen = len(commonword_l) * 2
    print(f"Total common words {commonwordlen}")

    # Divide Common words by total words
    wordpercent = commonwordlen / wordlen
    print(f"Percent of words that are common {wordpercent}")

    # Get the mean of common words and common characters
    prob = (charpercent + wordpercent) / 2
    
    # End
    return prob

# fin

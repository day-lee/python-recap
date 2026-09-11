# https://www.freecodecamp.org/learn/daily-coding-challenge/10-17
# - ternary operator
# - set thinking : index 3 or others
# - list comprehension with enumerate to access index and value at the same time 


def mask_2_optimized(card):
    separator = '-' if '-' in card else ' '
    card_list = card.split(separator)
    
    result = [digits if i == 3 else '****' for i, digits in enumerate(card_list)]
    # use separator with join
    return separator.join(result)

mask_2_optimized("4012-8888-8888-1881")
mask_2_optimized("6011 1111 1111 1117")



def mask_2(card):
    #ternary operator 
    separator = '-' if '-' in card else ' '
    card_list = card.split(separator)
    
    result = ['****'+separator if i != 3 else digits for i, digits in enumerate(card_list)]
    # print(''.join(result))  
    return ''.join(result)

mask_2("4012-8888-8888-1881")
mask_2("6011 1111 1111 1117")    



def mask(card):
    separator = ' '
    masked_card = ''
    if '-' in card:
        card_list = card.split('-')
        separator = '-'
    else:
        card_list = card.split(' ')

    for i, digits in enumerate(card_list):
        if i != 3:
            masked_card += '****' + separator
        else:
            masked_card += digits
    return masked_card

# mask("4012-8888-8888-1881")
# mask("6011 1111 1111 1117")




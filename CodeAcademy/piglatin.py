#pig latin translator, python -> ythonpay

def piglatin():

  pyg = 'ay'
  original = raw_input('Please enter a word to translate: ')

  if len(original) > 0 and original.isalpha():
    first_letter = original[0]

    new_word = original + first_letter + pyg
    new_word = new_word[1:len(new_word)]
    print(new_word)
  else:
    print('Please enter correct format')

piglatin()







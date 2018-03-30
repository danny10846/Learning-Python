def factorial(x):
  total = 1
  for i in range(1,x):
    total += total * i
    
  return total


print factorial(5)

#function to create factorial of any number


def anti_vowel(text):
  new_text = ""
  for ch in text:
    if ch in "aeiouAEIOU":
      pass
    else:
      new_text += ch
  return new_text
      
print anti_vowel('How are you')




#Functon which takes a setence and filters out a specific given word
def censor(text, word):
  #Find word length, as **** needs to correlate to length of word
  word_length = len(word)
  #Split text into a list
  text_list = text.split(" ")

  #Loop through our list of words
  for i in range(len(text_list)):
    #If word is given word then replace with appropriate number of *
    if text_list[i] == word:
      text_list[i] = "*"*word_length

  #Join our list to form a string again
  new_text = ' '.join(text_list)
  return new_text
  
  
  
print censor("this hack is wack hack", "hack")
      




#Function to return only even numbers in a list
def purify(numbers):
  new_list = []
  for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
      new_list.append(numbers[i])
  return new_list
   
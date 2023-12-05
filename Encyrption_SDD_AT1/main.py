import sys
from tabulate import tabulate
import string
def main():
    if len(sys.argv) !=4:
        print("Usage: python main.py '<message>' '<first_name>' '<last_name>'")
        return 1
    else:
        message = sys.argv[1]
        f_name = sys.argv[2]
        l_name = sys.argv[3]
        #reverse(message)
        #swap_pairs(list(message))
        #rotate_left(list(message), alpha_pos(l_name[0]))
        encyrption = [["Reverse",reverse(list(message),1), reverse(list(message), 1)],
                      ["Swap Pairs",swap_pairs(list(message), 1), swap_pairs(list(message), 1)],
                      ["Rotate Right", rotate_right(list(message), alpha_pos(f_name[0])), rotate_left(list(message), alpha_pos(f_name[0]))],
                      ["Rotate_Left", rotate_left(list(message), alpha_pos(l_name[0])), rotate_right(list(message), alpha_pos(l_name[0]))],                    
                      ["Alpha to QWERTY", qwerty(list(message), 1), arc_qwerty(list(message), 1)],
                      ["Add", add(list(message), len(l_name)), arc_add(list(message),len(l_name))],
                      ["Realign", realign(list(message), len(f_name)), arc_realign(list(message),len(f_name))],
                      ["V & C", v_c(list(message), 1), arc_v_c(list(message), 1)]
                     
                      ]
        print(tabulate(encyrption, headers=['Technique','Encoded', 'Decoded'], tablefmt='orgtbl'))
        dict = read_dict()
        result = checker(message, dict)


        if result == "No Decryption Found":
            print(result)
        else:
            words, methods = result
            decryption = []
            for i in range(len(words)):
                decryption.append([words[i], methods[i]])
            print("")
            print(tabulate(decryption,headers=["Decrypted word","Method used"]))


#reverse message without  using inbuilt functionality thus encoding it
def reverse(message_s, n):
    l = len(message_s)
    message = ""
    for i in range(0, l):
        message = message_s[i] + message    
    return message                
   
   
     
#swap each adjancenet pairs of charcters, if oddconnect last char to end    
def swap_pairs(message_arr, n):
    l = len(message_arr)
    if l % 2 !=0:
        l = l-1
    for i in range(0,l-1,2):
        temp = message_arr[i]
        message_arr[i] = message_arr[i+1]
        message_arr[i+1] = temp
    message = ''.join([item for item in message_arr])
    return message
def rotate_left(message_arr, shift):
    new_pos = []
    message = ""
    l = len(message_arr)
    for i in range(0,l):
        pos = (i-shift) % l
        new_pos.append(pos)
    for i in range(0,l):
        element = 0
        for j in range(0,l):
            if new_pos[j] == i:
                element =j
                break
        message = message + str(message_arr[element])
    return message
def rotate_right(message_arr, shift):
    new_pos = []
    message = ""
    l = len(message_arr)
    for i in range(0,l):
        pos = (i+shift) % l
        new_pos.append(pos)
   
    for i in range(0,l):
        element = 0
        for j in range(0,l):
            if new_pos[j] == i:
                element =j
                break
        message = message + str(message_arr[element])
    return message
def arc_rotate_right(message):
    return 1
def qwerty(message_arr, n):
    alpha_qwert = {
        "a":"q",
        "b":"w",
        "c":"e",
        "d":"r",
        "e":"t",
        "f":"y",
        "g":"u",
        "h":"i",
        "i":"o",
        "j":"p",
        "k":"a",
        "l":"s",
        "m":"d",
        "n":"f",
        "o":"g",
        "p":"h",
        "q":"j",
        "r":"k",
        "s":"l",
        "t":"z",
        "u":"x",
        "v":"c",
        "w":"v",
        "x":"b",
        "y":"n",
        "z":"m"  
    }
    l = len(message_arr)
    for i in range(0,l):
        if message_arr[i].isalpha() == False:
            continue
        if message_arr[i].isupper() == True:
            message_arr[i] = alpha_qwert[message_arr[i].lower()].upper()
        else:
            message_arr[i] = alpha_qwert[message_arr[i]]
    message = ''.join([item for item in message_arr])
    return message
def arc_qwerty(message_arr, n):
    alpha_qwert = {
       
        "q":"a",
        "w":"b",
        "e":"c",
        "r":"d",
        "t":"e",
        "y":"f",
        "u":"g",
        "i":"h",
        "o":"i",
        "p":"j",
        "a":"k",
        "s":"l",
        "d":"m",
        "f":"n",
        "g":"o",
        "h":"p",
        "j":"q",
        "k":"r",
        "l":"s",
        "z":"t",
        "x":"u",
        "c":"v",
        "v":"w",
        "b":"x",
        "n":"y",
        "m":"z"
    }
    l = len(message_arr)
    for i in range(0,l):
        if message_arr[i].isalpha() == False:
            continue
        if message_arr[i].isupper() == True:
            message_arr[i] = alpha_qwert[message_arr[i].lower()].upper()
        else:
            message_arr[i] = alpha_qwert[message_arr[i]]
    message = ''.join([item for item in message_arr])
    return message
def add(message_arr, shifty):
    while True:
        if shifty>26:
            shifty = shifty-26
        else:
            break
    for i in range(0,len(message_arr)):
        if message_arr[i].islower() == True:
            char_int=int(ord(message_arr[i]) + shifty)
            if char_int > 122:
                char_int = char_int-26
            message_arr[i] = chr(char_int)
        elif message_arr[i].isupper() == True:
            char_int=int(ord(message_arr[i]) + shifty)
            if char_int > 90:
                char_int = char_int -26
            message_arr[i] = chr(char_int)
    message = ''.join([item for item in message_arr])
    return message
def arc_add(message_arr, shifty):
    while True:
        if shifty>26:
            shifty = shifty-26
        else:
            break


    for i in range(0,len(message_arr)):
        if message_arr[i].islower() == True:
            char_int=int(ord(message_arr[i]) - shifty)
            if char_int < 97:
                char_int = char_int + 26
            message_arr[i] = chr(char_int)
        elif message_arr[i].isupper() == True:
            char_int=int(ord(message_arr[i]) - shifty)
            if char_int < 65:
                char_int = char_int + 26
            message_arr[i] = chr(char_int)
    message = ''.join([item for item in message_arr])
    return message
def realign(message_arr,n):
    #separate the message into n different messages where n is the length of the first name with the first letter first row second letter second row then iterate to second letter first row second letter second row
    #then iterate through the rows and add them to the message
    l = len(message_arr)
    if n>l:
        n=l-1
    count = l
    new_message = []
    for j in range((l-(l%n))//n+1):
        column = []
        for  i in range(n):
            if count< 1:
                column.append(".")
                break
            column.append(message_arr[0])
            message_arr.remove(message_arr[0])
           
            count = count -1
        new_message.append(column)
    message = ""
    for i in range(0,len(new_message[0])):
        for j in range(len(new_message)):
            if i < len(new_message[j]):
                message += new_message[j][i]
            else:
                message += ""
    return message  
def arc_realign(message_arr, n):
    l = len(message_arr)
   
    if n > l:
        n = l - 1
   
    rows = l // n
    remainder = l % n
   
    new_message = []
    message = ""
    count = l
   
    for i in range(n):
        temp = []
        # stack overflow and cs50 discord helped with the below for loop
        for j in range(rows + 1) if i < remainder else range(rows):
            if count < 1:
                temp.append("")
                break
            elif message_arr[0] == ".":
                temp.append("")
            else:
                temp.append(message_arr[0])
            message_arr.remove(message_arr[0])
            count -= 1
        new_message.append(temp)
   
    for i in range(len(new_message[0])):
        for j in range(len(new_message)):
            if i < len(new_message[j]):
                message += new_message[j][i]
            else:
                message += ""
   
    return message
def v_c(message_arr, n):
    vowels = set("aeiouAEIOU")
    consonants_groups = []
    vowels_indices = [i for i, char in enumerate(message_arr) if char in vowels]
    consonants_indices_group = []
    for i in range(len(message_arr)):
        if message_arr[i].isalpha():
            if message_arr[i] not in vowels:
                consonants_indices_group.append(i)
        else:
            if consonants_indices_group:
                consonants_groups.append(consonants_indices_group)
                consonants_indices_group = []
    consonants_groups.append(consonants_indices_group)
    vowels_indices = vowels_indices[1:] + [vowels_indices[0]]
    for group in consonants_groups:
        group[:] = group[-1:] + group[:-1]
    message_copy = message_arr.copy()
    for i in range(len(message_arr)):
        if not message_arr[i].isalpha():
            continue
        if message_copy[i] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"] and vowels_indices:
            message_arr[i] = message_copy[vowels_indices[0]]
            vowels_indices.pop(0)
        elif consonants_groups and message_copy[i].lower() not in ["a", "e", "i", "o", "u"]:
            message_arr[i] = message_copy[consonants_groups[0][0]]
            consonants_groups[0].pop(0)
            if not consonants_groups[0]:
                consonants_groups.pop(0)
    message = ''.join([item for item in message_arr])
   
    return message
def arc_v_c(message_arr, n):
    vowels = set("aeiouAEIOU")
    consonants_list = []
    vowels_list = [i for i, char in enumerate(message_arr) if char in vowels]
    consonants_list_t = []
    for i in range(0, len(message_arr)):
        if message_arr[i].isalpha():
            if message_arr[i] not in vowels:
                consonants_list_t.append(i)
        else:
            if consonants_list_t:
                consonants_list.append(consonants_list_t)
                consonants_list_t = []
    consonants_list.append(consonants_list_t)
    vowels_list = vowels_list[-1:] + vowels_list[:-1]
    for i in range(len(consonants_list)):
        if len(consonants_list[i]) > 1:
            consonants_list[i] = consonants_list[i][1:] + [consonants_list[i][0]]
    message_copy = message_arr.copy()
    for i in range(len(message_arr)):
        if message_arr[i].isalpha() == False:
            continue
        if message_copy[i] in ["a","e","i","o","u","A","E","I","O","U"] and len(vowels_list) > 0:
            message_arr[i] = message_copy[vowels_list[0]]
            vowels_list.remove(vowels_list[0])
        elif len(consonants_list) > 0 and message_copy[i].lower() not in ["a","e","i","o","u"]:
            message_arr[i] = message_copy[consonants_list[0][0]]
            consonants_list[0].remove(consonants_list[0][0])
            if not consonants_list[0]:
                consonants_list.remove(consonants_list[0])
    message = ''.join([item for item in message_arr])
    return message
def alpha_pos(char):
    if char.isupper() == True:
        pos = ord(char) - 64
    else:
        pos = ord(char) - 96
    return pos
def read_dict():
    with open("words.txt", 'r') as file:
        lines = file.readlines()
        lines = [line.replace("\n","") for line in lines]
    file.close()
    return lines
def word_counter(decrypted_message, word_list):
    word_count = 0
    decrypted_words = decrypted_message.split(" ")
    for word in decrypted_words:
        for correct_word in word_list:
            punctuation_chars = set(string.punctuation)
            word = ''.join(char for char in word if char not in punctuation_chars)
            if word.isalpha() == False:
                continue
            if word.lower() == correct_word.lower():
                word_count += 1
                break
    return word_count
def checker(message, word_list):
    decryption_methods = [reverse, swap_pairs, rotate_left, rotate_right, arc_qwerty, arc_add, arc_realign, arc_v_c]
    best_decryption = []
    best_word_count = 0
    best_decryption_method = []
    for decryption_method in decryption_methods:
        if decryption_method == arc_realign:
            n=2
            f= len(message)-1
        elif decryption_method == arc_add:
            n=1
            f=26
        elif decryption_method == arc_v_c or decryption_method== arc_qwerty or decryption_method== swap_pairs or decryption_method== reverse:
            n=0
            f=1
        elif decryption_method == rotate_left or decryption_method == rotate_right:
            n=1
            f=len(message)-1
       
        for i in range(n,f):
            decrypted_message = decryption_method(list(message), i)
            word_count = word_counter (decrypted_message, word_list)


            if word_count > best_word_count and decrypted_message!=message:
                best_decryption = []
                best_decryption_method = []
                best_word_count = word_count
                best_decryption.append(decrypted_message)
                best_decryption_method.append(decryption_method)
            elif word_count == best_word_count and decrypted_message!=message and decrypted_message not in best_decryption:
                best_decryption.append(decrypted_message)
                best_decryption_method.append(decryption_method)
               
    if best_decryption_method is None:
        return "No Decryption Found"
    if best_word_count <1:
        return "No Decryption Found"
    return best_decryption, best_decryption_method


if __name__ == '__main__':
    main()



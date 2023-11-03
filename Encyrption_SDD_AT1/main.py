import sys
from tabulate import tabulate
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
        rotate_left(list(message), alpha_pos(l_name[0]))
        encyrption = [["Reverse",reverse(message), reverse(message)], 
                      ["Swap Pairs",swap_pairs(list(message)), swap_pairs(list(message))],
                      ["Rotate Right", rotate_right(list(message), alpha_pos(f_name[0])), rotate_left(list(message), alpha_pos(f_name[0]))],
                      ["Rotate_Left", rotate_left(list(message), alpha_pos(l_name[0])), rotate_right(list(message), alpha_pos(l_name[0]))],                    
                      ["Alpha to QWERTY", qwerty(list(message)), arc_qwerty(list(message))],
                      ["Add", add(list(message), len(l_name)), arc_add(list(message),len(l_name))],
                      ]
        print(tabulate(encyrption, headers=['Technique','Encoded', 'Decoded'], tablefmt='orgtbl'))
        return 0

#reverse message without  using inbuilt functionality thus encoding it 
def reverse(message_s):
    l = len(message_s)
    message = ""
    for i in range(0, l):
        message = message_s[i] + message   
    #print(message)   
    return message                
    
    
      
#swap each adjancenet pairs of charcters, if oddconnect last char to end    
def swap_pairs(message_arr):
    l = len(message_arr)
    if l % 2 !=0:
        l = l-1
    for i in range(0,l-1,2):
        temp = message_arr[i]
        message_arr[i] = message_arr[i+1]
        message_arr[i+1] = temp
    message = ''.join([item for item in message_arr])
    return message
        
           

#decode the message by doing the invers of the swap function
def arc_swap_pairs(message):    
    return 1


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
        message = message + message_arr[element]
    return message
    
            
    return 1


def arc_rotate_left(message):
    return 1



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
        message = message + message_arr[element]
    return message
    return 1

def arc_rotate_right(message):
    return 1
def qwerty(message_arr):
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
    
    
def arc_qwerty(message_arr):
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
    for i in range(0,len(message_arr)):
        if message_arr[i].islower() == True:
            char_int=int(ord(message_arr[i]) + shifty)
            if char_int > 122:
                char_int = char_int - 26
            message_arr[i] = chr(char_int)
        elif message_arr[i].isupper() == True:
            char_int=int(ord(message_arr[i]) + shifty)
            if char_int > 90:
                char_int = char_int - 26
            message_arr[i] = chr(char_int)
    message = ''.join([item for item in message_arr])
    return message

    
    
    return 1

def arc_add(message_arr, shifty):
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
    if l % n != 0:
        chars_row= l//n
    else:
        rows = l//n
    
    
    chars_checked = 0
    while chars_checked <11:
        for i in range(0,rows):
            for j in range(0,n):
                if chars_checked < l:
                    print(message_arr[chars_checked], end = " ")
                    chars_checked += 1
            print()
def arc_realign(message):
    return 1

def v_c(message):
    return 1
def arc_v_c(message):
    return 1

def alpha_pos(char):
    if char.isupper() == True:
        pos = ord(char) - 64
    else:
        pos = ord(char) - 96
    return pos

    
    
    


    

if __name__ == '__main__':
    main()
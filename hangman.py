# this code simulate the hangman game: you choose a word and then another user should try to  guess it.
import getpass

print("""
Hi! Let's play the hangman game. 
User 1 should choose a word while User 2 have to find it. 
Do you want to play?
""")


val=1 # initialize val and val2 to different number
val2=3
while(val!=val2):
    val = getpass.getpass(prompt="Enter your word: ")

    val2 = getpass.getpass(prompt='say it again: ')
    if(val!=val2): print('spelling errors')



#look if the word has digits inside
j=0

while(j != len(val)):
    i=0
    j=0
    for i in range(0,len(val)):
        
        if (val[i].islower() == False): 
            print('No digits admitted! Try a new word')
            val = getpass.getpass(prompt="Enter your word: ")
            val= input("Enter your word: ")
        else:
            j=j+1 
            #print(j, '-->', len(val))

i=0    
letters = list(val)  
unknown_word = list(val)   
for i in range(1,len(val)-1):
    letters[i] = "_"

print("Ok! Let's start playing...\n\n\n")
print(letters)
    
while(unknown_word != letters):
    choosen_letter = input('choose a letter: ')
    j=0
    for i in range(1,len(val)-1):
        if(choosen_letter == val[i]): 
            letters[i]=choosen_letter
        else:
            if(j==0):
                print("Oops! this letter is not present...\n")
            j=1
                
    print(letters)
    
print('Congratulations! You won!')


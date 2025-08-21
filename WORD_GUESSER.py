import random

Easy_Words = ["cat", "sun", "book", "tree", "fish","ball", "star", "rain", "door", "milk"]
Medium_Words = ["pillow", "rocket", "jungle", "planet", "silver","candle", "spider", "castle", "bridge", "garden"]
Hard_Words = ["labyrinth", "cyphers", "chrysalis", "qnuagmire", "silhouette","juxtapose", "euphoric", "onomatopoeia", "clandestine", "xylophone"]

def main ():
    while True:
        
        print("DIFFICULTY MODES : \n1.Easy \n2.Medium \n3.Hard ")
        mode = int(input("SELECT DIFFICULTY MODE (1 ,2 or 3) :  "))
        match mode :
            case 1:
                word = random.choice(Easy_Words).lower()
                print("MODE : Easy ")
                l = len(word)
                x = random.randint(1, l-1)
                word_1 = "*"*x + word[x] + "*"*(l-x-1)
                print(word_1)
                guess(word,word_1)
            case 2:
                word = random.choice(Medium_Words).lower()
                l = len(word)
                x = random.randint(1, l-1)
                y = random.randint(x+1,l-1)
                word_1 = "*"*x + word[x] + "*"*(y-(x+1)) + word[y] + "*"*(l-y)
                print(word_1)
                guess(word,word_1)
            case 3:
                word = random.choice(Hard_Words).lower()
                print("MODE : Hard ")
                l = len(word)
                x = random.randint(1, l-1)
                y = random.randint(x+1,l-1)
                z = random.randint(y+1,l-1)
                word_1 = "*"*x + word[x] + "*"*(y-(x+1)) + word[y] + "*"*(z-(y+1)) + word[z] + "*"*(l-z)
                print(word_1)
                guess(word,word_1)
            case _:
                "Enter a Valid Choice."
                return
        cont = input("Do you want to continue? y/n ").strip().lower()
        if cont == "y" :
            continue
        else :
            break


def guess(word,word1):
    count = 0
    word2 = word
    for i in word1:
        if i.isalpha():
            word2 = word2.replace(i, "*")
    hint_2 = "*"*(len(word))
    while True:
        
        guess_word = input("Guess : ").lower()
        if guess_word == word :
            print("YOU WIN.")
            return
        if count < (len(word)/2 - 1 ):
            hint = word2
            j = ""
            while not(j.isalpha()):
                j = random.choice(hint)
                word2 = word2.replace(j,"*",1)
            indx = hint.index(j)
            word1 = word1.replace("*", j, 1)
            print("HINT : ", word1)
            
            count += 1
            
            print("You have used ", count, "of" , int(len(word)/2)-1,"hints.")
                       
if __name__  == '__main__' :
    main()
               
        
            



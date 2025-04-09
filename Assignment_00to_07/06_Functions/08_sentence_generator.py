# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as
#  parameters and, depending on the part of speech, place the word into one of three sentence templates (or one from your imagination!):

def make_sentence(word: str, part_of_speech: int):
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"Its so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window,the sky is big and {word} !")  
    else:
         {"Invalid choice! Please enter 0 for noun,1 for verb,2 for adjective"} 

def main():
    word = input("Please type a noun,verb or adjective:")
    part_of_speech = int(input("Is this a noun,verb or adjective? type 0 for noun,1 for verb,2 for adjective:"))  
    make_sentence(word,part_of_speech)  


if __name__ == "__main__":  
    main()               

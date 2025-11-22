# I created a dictionary in line 9 to organize all the options. used it in all if/elif statement. 
# from line 26 to 39 created CONSTANT variables for readability and maintenance
"""
Author: Edi Carlos
Program: Adventure Game

Description: A text-based adventure game
"""
choices = {
    "python": "python",
    "javascript": "javascript",
    "if": "if",
    "if/elif/else": "if/elif/else",
    "comments": "comments",
    "while": "while",
    "bye": "bye",
    "sorry": "sorry",
    "play": "play",
    "code": "code",
    "pie": "pie",
    "write": "write",
    "submit": "submit",
    "0": "0"
}

REF_PYTHON = "python"
REF_JAVASCRIPT = "javascript"
REF_IF = "if"
REF_ELIF = "if/elif/else"
REF_COMMENTS = "comments"
REF_WHILE = "while"
REF_BYE = "bye"
REF_SORRY = "sorry"
REF_PLAY = "play"
REF_CODE = "code"
REF_PIE = "pie"
REF_WRITE = "write"
REF_SUBMIT = "submit"
REF_0 = "0"

print("text-based adventure game!\n".upper())

choice = input("You are a student of software development, and you have to solve a logic task with a programming language: PYTHON or JAVASCRIPT. Which one do you choose? (Remember, your teacher is teaching PYTHON. You can choose any programming language, I won't influence you, but remember, you teacher is teaching PYTHON, PYTHON) ")
choice = choice.lower()

if choice in choices and choice == REF_PYTHON:
    choice = input("\nGood choice. Your teacher you be happy. Let's go to what you have to do. You have to demonstrate your knowledge of “if statements”, you can make a code with IF of IF/ELIF/ELSE conditions. Which one do you choose? IF or IF/ELIF/ELSE ")
    choice = choice.lower()
    if choice in choices and choice == REF_IF:
        choice = input("\nHey player. You should try to do your best. Ok, you are in the second level of the game and still can prove your value. At this point you can choose to write some COMMENTS to show that you know how to do it or you can do a WHILE looping that is more complicated and you can save your grade in this assignment. Which one do you choose? COMMENTS or WHILE? ")
        choice = choice.lower()
        if choice in choices and choice == REF_COMMENTS:
            choice = input("\nYou are not helping. You reach the third level. You have three options in this level. You can say BYE, and we hope you make the best in your next turn, you can say SORRY, and we do know you are contrite, and will do try your best next turn, or you can hit number 0 (zero) in your keyboard to end the game. Which one do you choose? BYE or SORRY or 0? ")
            choice = choice.lower()
            if choice in choices and choice == REF_BYE:
                print("Don't be afraid. You can always advance and try your best.")
            elif choice in choices and choice == REF_SORRY:
                print("Your a good person. I know you can advance in programation. Go ahead and know that you can do it.")
            elif choice in choices and choice == REF_0:
                print("Good. You reached the end of the game. I see you next time!")
            else: 
                print("I don't understande this option, play again.")
        elif choice in choices and choice == REF_WHILE:
            choice = input("\nGood. Trying to use a while loop is better then just write a comment. Your teacher you see your effort and maybe you can get a good grade. Say to me if you would like to play again, so you can see the paths you can walk. Write PLAY (for playing again) or hit 0(zero number key) to end the game")
            choice == choice.lower()
            if choice == REF_PLAY:
                print("Good. Desiring playing again. Shows that you would like to know what are the good behavior in this area of programation.")
            elif choice == REF_0:
                print("Good. You reached the end of the game. I see you next time!")
            else:
                print("I don't understande this option, play again.")
        else:
            print("I don't understande this option, play again.")
    elif choice in choices and choice == REF_ELIF:
        choice = input("\nWow! Someone is working hard here. As you have chosen a more complex statement, let me ask you. You are trying to do your best in the three level condidition assignment task; you are doing a good code in you vsCode, but you remember that there is a delicious apple pie in the refrigerator. What do you decide? Continue writing your CODE or you go to eat a little of that delicious apple PIE? Write CODE or PIE ")
        choice = choice.lower()
        if choice in choices and choice == REF_CODE:
            choice = input("\nI see that you really love to do it. Ok. Let's finish this task. Your code is working and it is ready to be submitted for the teacher. But you didn't write a comment block at the begining of your code for adding Author, program name, and description. It is not important, but it is a good practice. Which one do you decide? WRITE the comment block or SUBMIT? WRITE (for comment block) or SUBMIT (for just submit)")
            choice = choice.lower()
            if choice in choices and choice == REF_WRITE:
                print("Good. Go ahead! Write your comment block, submit your task, and be happy. Thank you, I liked playing with you.")
            elif choice in choices and choice == REF_SUBMIT:
                print("Yes. The block comment at the beginning is not so import . It is just a good practice. Thank you for playing. I see you next time!")
            else:
                print("I don't understand this option, play again.")
        elif choice in choices and choice == REF_PIE:
            choice = input("\nIt is completly understandable. I would not resiste to an apple pie too. Go ahead, eat your apple pie, but don't forget the exercise. You must submit today for getting your grade.")
        else: 
            print("I don't understand this option, play again.")
    else:
        print("I don't understand this option, play again.")
elif choice in choices and choice == REF_JAVASCRIPT:
    choice = input("\nJavascript is a good language too. It is apreciable that you want to learn other languages. I want to learn too. For me the best language to learn is that gives your payment. But you didn't pay attention. You are crazy. The teacher is teaching PYTHON. I gave the hint for you. Now it is late. Do you best in the options below: \nYou have to demonstrate your knowledge of “if statements”, you can make a code with IF of IF/ELIF/ELSE conditions. Which one do you choose? IF or IF/ELIF/ELSE ")
    choice = choice.lower()
    if choice in choices and choice == REF_IF:
        choice = input("\nHey player. You should try to do your best. Ok, you are in the second level of the game and still can prove your value. At this point you can choose to write some COMMENTS to show that you know how to do it or you can do a WHILE looping that is more complicated and you can save your grade in this assignment. Which one do you choose? COMMENTS or WHILE? ")
        choice = choice.lower()
        if choice in choices and choice == REF_COMMENTS:
            choice = input("\nYou are not helping. You reach the third level. You have three options in this level. You can say BYE, and we hope you make the best in your next turn, you can say SORRY, and we do know you are contrite, and will do try your best next turn, or you can hit number 0 (zero) in your keyboard to end the game. Which one do you choose? BYE or SORRY or 0? ")
            choice = choice.lower()
            if choice in choices and choice == REF_BYE:
                print("Don't be afraid. You can always advance and try your best.")
            elif choice in choices and choice == REF_SORRY:
                print("Your a good person. I know you can advance in programation. Go ahead and know that you can do it.")
            elif choice in choices and choice == REF_0:
                print("Good. You reached the end of the game. I see you next time!")
            else: 
                print("I don't understande this option, play again.")
        elif choice in choices and choice == REF_WHILE:
            choice = input("\nGood. Trying to use a while loop is better then just write a comment. Your teacher you see your effort and maybe you can get a good grade. Say to me if you would like to play again, so you can see the paths you can walk. Write PLAY (for playing again) or hit 0(zero number key) to end the game")
            choice == choice.lower()
            if choice in choices and choice == REF_PLAY:
                print("Good. Desiring playing again. Shows that you would like to know what are the good behavior in this area of programation.")
            elif choice in choices and choice == REF_0:
                print("Good. You reached the end of the game. I see you next time!")
            else:
                print("I don't understande this option, play again.")
        else:
            print("I don't understande this option, play again.")
    elif choice in choices and choice == REF_ELIF:
        choice = input("\nWow! Someone is working hard here. As you have chosen a more complex statement, let me ask you. You are trying to do your best in the three level condidition assignment task; you are doing a good code in you vsCode, but you remember that there is a delicious apple pie in the refrigerator. What do you decide? Continue writing your CODE or you go to eat a little of that delicious apple PIE? Write CODE or PIE ")
        choice = choice.lower()
        if choice in choices and choice == REF_CODE:
            choice = input("\nI see that you really love to do it. Ok. Let's finish this task. Your code is working and it is ready to be submitted for the teacher. But you didn't write a comment block at the begining of your code for adding Author, program name, and description. It is not important, but it is a good practice. Which one do you decide? WRITE the comment block or SUBMIT? WRITE (for comment block) or SUBMIT (for just submit)")
            choice = choice.lower()
            if choice in choices and choice == REF_WRITE:
                print("Good. Go ahead! Write your comment block, submit your task, and be happy. Thank you, I liked playing with you.")
            elif choice in choices and choice == REF_SUBMIT:
                print("Yes. The block comment at the beginning is not so import . It is just a good practice. Thank you for playing. I see you next time!")
            else:
                print("I don't understand this option, play again.")
        elif choice in choices and choice == REF_PIE:
            choice = input("\nIt is completly understandable. I would not resiste to an apple pie too. Go ahead, eat your apple pie, but don't forget the exercise. You must submit today for getting your grade.")
        else: 
            print("I don't understand this option, play again.")
    else:
        print("I don't understand this option, play again.")
else:
    print("I don't understand this option, play again.")

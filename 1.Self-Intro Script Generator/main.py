# Self Introduction Script Generator

import datetime

def main():
    
    name = input("What's your name? ").strip()
    age = input("How old are you? ").strip()
    city = input("Where do you live? ").strip()
    profession = input("What do you do? ").strip()
    hobby = input("what is your favourite hobby? ").strip()

    intro = (
        f"Hi! my name is {name}, I am {age} years old and I live in {city}. "
        f"I am a {profession} and I absolutely enjoy {hobby} in my free time.\n"
    )

    date = datetime.date.today().isoformat()
    intro += f"\nLogged on : {date}"

    border = '*' * 100

    print(f"{border}\n{intro}\n{border}")

if __name__== '__main__':
    main()
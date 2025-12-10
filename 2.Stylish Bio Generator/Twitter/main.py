def generate_bio(style, name, profession, passion, handle):
    if style == 1:
        return f"{name} | {profession} \n{passion}\n{handle}"
    elif style == 2:
        pass
    elif style == 3:
        pass

def main():
    name = input("Enter your name: ").strip()
    profession = input("Enter your profession: ").strip()
    passion = input("Enter your passion(In a Single-line): ").strip()
    # emoji = input("Enter your favourite emoji: ").strip()
    handle = input("Enter your handle(Insta/Twitter): ").strip()

    print("""Choose Your Style:
    1.Simple
    2.Vertical flair
    3.IDK""")

    style = int(input("Enter 1, 2 or 3: "))


    bio = generate_bio(style, name, profession, passion, handle)
    print(bio)

if __name__== '__main__':
    main()
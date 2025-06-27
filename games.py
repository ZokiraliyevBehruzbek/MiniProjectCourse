import random
import time
from sqlalchemy.orm import sessionmaker
from db import engine
from database import User  
Session = sessionmaker(bind=engine)



def monkeytype_typing():
    words = [
        "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
        "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
        "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
        "or", "an", "will", "my", "one", "all", "would", "there", "their",
        "what", "so", "up", "out", "if", "about", "who", "get", "which", "go",
        "me", "when", "make", "can", "like", "time", "no", "just", "him",
        "know", "take", "people", "into", "year", "your", "good", "some",
        "could", "them", "see", "other", "than", "then", "now", "look", "only",
        "come", "its", "over", "think", "also", "back", "after", "use", "two",
        "how", "our", "work", "first", "well", "way", "even", "new", "want",
        "because", "any", "these", "give", "day", "most", "us"
    ]

    true = 0
    false = 0
    start = time.time()
    second = 0
    choose_second = int(input("Iltimos vaqtni belgilang: "))
    second = choose_second
    while True:
        text = random.choice(words)
        print(text)
        enter = input("So'zni kiriting: ")
        if time.time() - start >= second:
            print("Siz belgilagan vaqt o'tib bo'ldi endi keling sizning ballaringizni aniqlaymiz: ")
            break
        elif enter != text:
            false +=1
        elif enter == text:
            true +=1
    print(f"Salom siz {true}ta To'gri yozdingiz va {false}ta xato qildingiz")
    return true


def mental_math():
    true = 0
    false = 0
    start = time.time()
    
    choose_second = int(input("Necha soniya o'ynamoqchisiz: "))
    second = choose_second

    print(f"{second} soniyalik matematik o‘yin boshlandi!")

    while True:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        operator = random.choice(["+", "-"])

        if operator == "+":
            correct = a + b
        else:
            correct = a - b

        question = f"{a} {operator} {b} = "
        answer = input(question)

        # vaqt tugadi
        if time.time() - start >= second:
            print("Vaqt tugadi! Natijalarni ko‘raylik:")
            break

        # raqam kiritilganini tekshiramiz
        if not answer.strip().isdigit() and not (answer.strip().startswith("-") and answer.strip()[1:].isdigit()):
            print("Faqat son kiriting!")
            continue

        if int(answer) == correct:
            true += 1
        else:
            false += 1

    print(f"Siz {true} ta to‘g‘ri, {false} ta noto‘g‘ri javob berdingiz.")
    return true





def add_score(name, amount):
    session = Session()
    user = session.query(User).filter_by(name=name).first()
    
    if user:
        if user.all_score is None:
            user.all_score = 0  # ✅ agar None bo‘lsa, 0 dan boshlaymiz
        user.all_score += amount
        session.commit()
        print(f"{amount} ball qo‘shildi. Yangi umumiy ball: {user.all_score}")
    else:
        print("Foydalanuvchi topilmadi.")
    
    session.close()
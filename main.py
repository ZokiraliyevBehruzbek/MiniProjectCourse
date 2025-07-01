from database import User
from sqlalchemy.orm import sessionmaker
from db import engine
from games import monkeytype_typing, mental_math,add_score

commands = ["register", "login"]
Session = sessionmaker(bind=engine)


while True:
    print(f"Mavjud buyruqlar: {commands}")
    inp = input("Buyruq: ")
    if inp == "register":
        inp_name = input("Ismingizni kiriting: ")
        inp_password = input("Parolingizni kiriting: ")
        new_user = User(name=inp_name, password= inp_password)
        session = Session()
        session.add(new_user)
        session.commit()
        session.close()
        print("Muvofiqiyatli ro'yxatdan o'tdingiz!")
    elif inp == "login":
        inp_name = input("ismingizni kiriting: ")
        inp_password = input("parolni kiriting: ")
        session = Session()
        user = session.query(User).filter_by(name=inp_name,password=inp_password).first()
        if user.name == inp_name and user.password == inp_password:
            print("Siz shaxsiy kabinetga kirdingiz")
            while True:
                print("Mavjud commandlar: `games`, `my_score` `logout`")

                inp = input("Buyruqni kiriting: ")
                if inp == "games":
                    print("Monkeytype: 0", "Math: 1")
                    inp = input("Tanlang: ")
                    if inp == "0":
                        score = monkeytype_typing()
                        add_score(inp_name,score)
                    elif inp == "1":
                        score = mental_math()
                        add_score(inp_name,score)
                elif inp == "my_score":
                    session = Session()
                    user = session.query(User).filter_by(name=inp_name).first()
                    if user:
                        print(f"Sizning umumiy ballaringiz: {user.all_score}")
                    else:
                        print("Foydalanuvchi topilmadi.")
                    session.close()
                elif inp == "logout":
                    break
    elif inp == "exit":
        break
from database import Database


class User:
    # constructor with Encapsulation
    def __init__(self, first_name, mid_name, last_name, phone,email,password,dob):
        self.__first_name=first_name
        self.__mid_name=mid_name
        self.__last_name=last_name
        self.__phone=phone
        self.__email = email
        self.__password = password
        self.__dob = dob
     

    # function of database (CRUD)

    # 1- Add new user

    def add_user(self, db):
        try:
            db.cursor.execute(
                """
                   insert into users(
                   User_id,      
                   First_Name,  
                   Mid_Name,      
                   Last_Name,     
                   Phone_Number,  
                   Email,         
                   Password_user, 
                   Date_of_Birth ,             
                   Created_At )
                   values (user_seq.nextval,:1,:2,:3,:4,:5,:6,to_date(:7,'dd/mm/yyyy'),sysdate)
                """,
                (
                    self.__first_name,
                    self.__mid_name,
                    self.__last_name,
                    self.__phone,
                    self.__email,
                    self.__password,
                    self.__dob
                )
            )
            db.cursor.execute("select user_seq.currval from dual")
            self.__user_id = db.cursor.fetchone()

            db.connection.commit()
            print(f"User added successfully ...your user id is {self.__user_id}")

        except Exception as failed:
            print(f"User added failed : {failed}")



    # get full Name (Getter)

    def get_full_name(self):
        return f"{self.__first_name} {self.__mid_name } {self.__last_name}"

    
    # set_email (setter)

    def set_email(self,new_email):
        self.__email=new_email

    

    # view All

    @staticmethod
    def view_all(db):
        db.cursor.execute("select * from users order by user_id")
        return db.cursor.fetchall()

    # search by first_name

    @staticmethod
    def search_by_firstName(db, first_name):
        db.cursor.execute("select * from users where first_name=:1", (first_name,))
        return db.cursor.fetchall()

    # update of password

    @staticmethod
    def update_password(db, user_id, new_password):
        try:

            db.cursor.execute(
                """
             update users 
             set Password_user = :1 where user_id = :2
          """,
                (new_password, user_id),
            )
            db.connection.commit()
            print("updated successfully")
        except Exception as failed:
            print(f"updated failed {failed}")


    # delete user

    @staticmethod
    def delete_user(db, user_id):
        try:
            db.cursor.execute("delete from users where user_id =:1", (user_id,))
            db.connection.commit()
            print("deleted successfully")
        except Exception as failed:
            print(f"deleted failed {failed}")


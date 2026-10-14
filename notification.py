from database import Database

class Notification:
    # constructor with Encapsulation
    def __init__(self,user_id,Is_read,massage):
        self.__user_id=user_id
        self.__Is_read=Is_read
        self.__massage=massage


    # function of database (CRUD)

    # 1- Add new notification

    def add_notification(self,db):  
        try:
            db.cursor.execute("""
            insert into notification(
            notification_id,
            user_id,
            Is_read,
            Created_At,
            massage
            ) values(notification_seq.nextval,
            :1,:2,sysdate,:3) """ ,(
            self.__user_id,
            self.__Is_read,
            self.__massage
            )  )
            db.cursor.execute("select notification_seq.currval from dual")
            self.__notification_id = db.cursor.fetchone()

            db.connection.commit()
            print(f"User Notification successfully ...your Notification id is {self.__notification_id}")

        except Exception as failed:
            print(f"Notifiction added failed : {failed}")



    # view All

    @staticmethod
    def view_all(db):
        db.cursor.execute("select * from NOTIFICATION order by notification_id")
        return db.cursor.fetchall()

   # search by notifiction_id

    @staticmethod
    def search_by_notification_id(db, notifiction_id):
        db.cursor.execute("select * from NOTIFICATION where notification_id=:1", (notifiction_id,))
        return db.cursor.fetchone()    


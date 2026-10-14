from database import Database

class Beneficiary:
    # constructor with Encapsulation
    def __init__(self,user_id,beneficiry_name,phon_number,beneficiary_status):
        self.__user_id=user_id
        self.__beneficiary_name=beneficiry_name
        self.__phon_number=phon_number
        self.__beneficiary_status=beneficiary_status


    # function of database (CRUD)
    
    # 1- Add new uneficiary

    def add_beneficiary(self,db):
        try:
            db.cursor.execute("""
            insert into beneficiary(
            beneficiary_id,
            user_id,
            beneficiary_name,
            phone_number,
            added_date,
            beneficiary_status) values(beneficiary_seq.nextval,
            :1,:2,:3,sysdate,:4) """ ,(
            self.__user_id,
            self.__beneficiary_name,
            self.__phon_number,
            self.__beneficiary_status
            ) )
            db.cursor.execute("select beneficiary_seq.currval from dual")
            self.__beneficiary_id = db.cursor.fetchone()

            db.connection.commit()
            print(f"User beneficiary successfully ...your beneficiary id is {self.__beneficiary_id}")

        except Exception as failed:
            print(f"beneficiary added failed : {failed}")

            
    # view All

    @staticmethod
    def view_all(db):
        db.cursor.execute("select * from beneficiary order by beneficiary_id")
        return db.cursor.fetchall()

   # search by name

    @staticmethod
    def search_by_Name(db, beneficiary_name):
        db.cursor.execute("select * from beneficiary where beneficiary_name=:1", (beneficiary_name,))
        return db.cursor.fetchall()

    # update of phone_number

    @staticmethod
    def update_phone(db, beneficiary_id, new_phone):
        try:

            db.cursor.execute(
             """
             update beneficiary 
             set phone_number = :1 where beneficiary_id = :2
             """,
                (new_phone, beneficiary_id),
            )
            db.connection.commit()
            print("updated successfully")
        except Exception as failed:
            print(f"updated failed {failed}")

            
    # delete beneficiary

    @staticmethod
    def delete_beneficiry(db, beneficiary_id):
        try:
            db.cursor.execute("delete from beneficiary where beneficiary_id =:1", (beneficiary_id,))
            db.connection.commit()
            print("deleted successfully")
        except Exception as failed:
            print(f"deleted failed {failed}")
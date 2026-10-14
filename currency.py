from database import Database

class Currency:
    # constructure with Encapsulation
    def __init__(self,cuurency_name,currency_cod):
        self.__cuurency_name=cuurency_name
        self.__currency_code=currency_cod


    # Add currency

    def add_currency(self,db):
        try:
            db.cursor.execute("""
               insert into currency(
               currency_id,
               currency_name,
               currency_code)
               values(currency_seq.nextval,:1,:2)
            """,(self.__cuurency_name,self.__currency_code))
            db.cursor.execute("select currency_seq.currval from dual")
            self.__currency_id=db.cursor.fetchone()
            db.connection.commit()
            print(f"currency added successfully  ...currency id is {self.__currency_id} ")

        except  Exception as failed:
            print(f"currency added failed {failed}")


    #  view all the currencies

    @staticmethod
    def view_all(db):
        db.cursor.execute("select * from currency order by 1")
        return db.cursor.fetchall()
    

    # search by currency_id
    @staticmethod
    def search_by_currency_id(db,currency_id):
        db.cursor.execute("select * from currency where currency_id=:1",(currency_id,))
        return db.cursor.fetchone()

    


    

        
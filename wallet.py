from database import Database


class Wallet:
    # constructor with Encapsulation

    def __init__(self,user_id,status):
        self.__user_id=user_id
        self.__status=status

    # Add Wallet 

    def add_wallet(self,db):
        try:
            db.cursor.execute(
            """
                insert into wallet(
                wallet_id,
                User_id,      
                Status_wallet,         
                Created_At )
                values (wallet_seq.nextval,:1,:2,sysdate)
                        """,(self.__user_id,self.__status))

            
            db.cursor.execute("select wallet_seq.currval from dual")
            self.__wallet_id = db.cursor.fetchone()
        
            db.connection.commit()
            print(f"Wallet added successfully ...your wallet id is {self.__wallet_id}")

        except Exception as failed:
                    print(f"Wallet added failed : {failed}")

    # view All
    
    @staticmethod
    def view_all(db):
        db.cursor.execute("select * from wallet order by wallet_id")
        return db.cursor.fetchall()

    # search by wallet_id
    
    @staticmethod
    def search_by_wallet_id(db, wallet_id):
        db.cursor.execute("""select 
                            u.user_id,
                            w.Wallet_id,
                            u.first_name,
                            w.Status_wallet
                            from users u
                            join wallet w on u.user_id=w.user_id
                            where w.wallet_id=:1
                            """ ,(wallet_id,))
        return db.cursor.fetchone()

    # update of wallet_status
    
    @staticmethod
    def update_status(db, wallet_id, new_status):

        try:
            db.cursor.execute(
                """
                update wallet 
                set Status_wallet = :1 where wallet_id = :2
            """,
                (new_status, wallet_id)
            )
            db.connection.commit()
            print("updated successfully")

        except Exception as failed:
            print(f"updated failed {failed}")

    # delete wallet
    
    @staticmethod
    def delete_wallet(db, wallet_id):
        try:
            db.cursor.execute("delete from wallet where wallet_id =:1", (wallet_id,))
            db.connection.commit()
            print("deleted successfully")
        except Exception as failed:
            print(f"deleted failed {failed}")
        
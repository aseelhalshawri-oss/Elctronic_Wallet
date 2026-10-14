from database import Database

class Wallet_currency:
    # constructure with Encapsulation

    def __init__(self,wallet_id,currency_id,balance):
        self.__wallet_id=wallet_id
        self.__currency_id=currency_id
        self.__balance=balance

    # Add wallet_currency
    
    def add_wallet_currency(self,db):
        try:
            db.cursor.execute(
                """
                insert into wallet_currency(
                wallet_currency_id,
                wallet_id,
                currency_id,
                balance)
                values(wallet_currency_seq.nextval,:1,:2,:3)
                   
            """,(self.__wallet_id,self.__currency_id,self.__balance))
            db.cursor.execute("select wallet_currency_seq.currval from dual")
            self.__wallet_currency_id=db.cursor.fetchone()
            db.connection.commit()
            print(f"Wallet currency added successfully ...your wallet_currency_id is {self.__wallet_currency_id}")

        except Exception as failed:
            print(f"wallet_currency  added failed {failed}")


    # view all wallets currency

    @staticmethod
    def view_all(db):
        db.cursor.execute("select * from wallet_currency order by 1")
        return db.cursor.fetchall()


    # search by wallet id

    @staticmethod
    def search_by_wallet_id(db,wallet_id):
        db.cursor.execute("""
            select
            w.wallet_id,
            u.first_name,
            wallet_currency_id,
            currency_code,
            wc.Balance 
            from users u 
            join wallet w on u.user_id=w.user_id
            join wallet_currency wc on w.Wallet_id=wc.Wallet_id
            join CURRENCY c on wc.currency_id=c.currency_id
            where wc.wallet_id=:1
        """,(wallet_id,))
        return db.cursor.fetchall()

    # update the balance

    @staticmethod
    def update_balance(db,new_balance,wallet_currency_id):
        try: 
            db.cursor.execute("""
                update wallet_currency 
                set balance =:1
                where wallet_currency_id=:2
                """,(new_balance,wallet_currency_id))
            db.connection.commit()
            print("updated successfully")
            
        except Exception as failed:
               print(f"updated failed {failed}")


    # delete wallet_currency
    @staticmethod
    def delete_wallet_currency(db,wallet_currency_id):
        try:
            db.cursor.execute("delete from wallet_currency where wallet_currency_id=:1",
                (wallet_currency_id,))
            db.cursor.commit()
            print("deleted successfully")
        except Exception as failed:
            print("deleted failed {failed}")


        
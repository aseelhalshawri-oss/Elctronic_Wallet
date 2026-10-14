from database import Database

class Transaction:
    # constructure with Encapsulation

    def __init__(self,sender_wallet_currency_id,receiver_wallet_currency_id,
        transaction_type,transaction_status,Amount,transaction_desc):
        self.__sender_wallet_currency_id=sender_wallet_currency_id
        self.__receiver_wallet_currency_id=receiver_wallet_currency_id
        self.__transaction_type=transaction_type
        self.__transaction_status=transaction_status
        self.__Amount=Amount
        self.__transaction_desc=transaction_desc

    # Add Transaction
    
    def add_transaction(self,db):
        try:
            db.cursor.execute(
                """
                insert into transaction(
                transaction_id ,
                sender_wallet_currency_id  ,
                receiver_wallet_currency_id  , 
                transaction_type ,
                transaction_status ,
                Amount ,
                transaction_desc,
                Created_At       
                )values(transaction_seq.nextval,:1,:2,:3,:4,:5,:6,sysdate)
                   
            """,(self.__sender_wallet_currency_id,self.__receiver_wallet_currency_id,
                 self.__transaction_type,self.__transaction_status,self.__Amount,
                 self.__transaction_desc))

            db.cursor.execute("select transaction_seq.currval from dual")
            self.__transaction_id=db.cursor.fetchone()
            db.connection.commit()
            print(f"transaction added successfully ...your transaction_id is {self.__transaction_id}")

        except Exception as failed:
            print(f"transaction added failed {failed}")


    # view all transactions

    @staticmethod
    def view_all(db):
        db.cursor.execute("select * from transaction order by 1")
        return db.cursor.fetchall()


    # view all the information for sender and receiver

    @staticmethod
    def view_all_sc(db):
        db.cursor.execute("""
            SELECT 
            t.transaction_id  AS "operation_id",
            us.First_Name AS "sender_name",
            ur.First_Name AS "receiver_name",
            cs.currency_name AS "sender_currency",
            cr.currency_name AS "receiver_currency",
            t.Amount AS "Amount",
            t.transaction_status AS "operation_status",
            t.Created_At As "operation_date",
            wcs.Balance AS "sender_balance",
            wcr.Balance AS "receiver_balance"
            from TRANSACTION t 
            --SENDER
            join wallet_currency wcs on t.sender_wallet_currency_id = wcs.wallet_currency_id
            join WALLET ws on wcs.Wallet_id = ws.Wallet_id
            join USERS us on ws.user_id = us.User_id
            join CURRENCY cs on wcs.currency_id = cs.currency_id
            --RECEVIER
            join wallet_currency wcr on t.receiver_wallet_currency_id = wcr.wallet_currency_id
            join WALLET wr on wcr.Wallet_id = wr.Wallet_id
            join USERS ur on wr.user_id = ur.User_id
            join CURRENCY cr on wcr.currency_id = cr.currency_id
            order by t.transaction_id
        """)
        return db.cursor.fetchall()



    # search by transaction id

    @staticmethod
    def search_by_transaction_id(db,transaction_id):
        db.cursor.execute("""
            SELECT 
            t.transaction_id  AS "operation_id",
            us.First_Name AS "sender_name",
            ur.First_Name AS "receiver_name",
            cs.currency_name AS "sender_currency",
            cr.currency_name AS "receiver_currency",
            t.Amount AS "Amount",
            t.transaction_status AS "operation_status",
            t.Created_At As "operation_date",
            wcs.Balance AS "sender_balance",
            wcr.Balance AS "receiver_balance"
            from TRANSACTION t 
            --SENDER
            join wallet_currency wcs on t.sender_wallet_currency_id = wcs.wallet_currency_id
            join WALLET ws on wcs.Wallet_id = ws.Wallet_id
            join USERS us on ws.user_id = us.User_id
            join CURRENCY cs on wcs.currency_id = cs.currency_id
            --RECEVIER
            join wallet_currency wcr on t.receiver_wallet_currency_id = wcr.wallet_currency_id
            join WALLET wr on wcr.Wallet_id = wr.Wallet_id
            join USERS ur on wr.user_id = ur.User_id
            join CURRENCY cr on wcr.currency_id = cr.currency_id
            where t.transaction_id = :1
        """,(transaction_id,))
        return db.cursor.fetchone()




    # update transaction status

    @staticmethod
    def update_status(db,new_status,transaction_id):
        try: 
            db.cursor.execute("""
                update transaction 
                set transaction_status =:1
                where transaction_id=:2
                """,(new_status,transaction_id))
            db.connection.commit()
            print("updated successfully")
            
        except Exception as failed:
               print(f"updated failed {failed}")


   # update balance just for transaction_status = (pending or failed) after update transaction_status
   
    @staticmethod
    def update_balance_trans(db,transaction_id):
           try: 
               db.cursor.execute("""
                    update WALLET_CURRENCY set Balance = Balance-(SELECT Amount from TRANSACTION where transaction_id = :1) 
                    where  wallet_currency_id = (SELECT sender_wallet_currency_id from TRANSACTION where transaction_id = :2)
                   """,(transaction_id,transaction_id))
                  
               db.cursor.execute("""
                    update WALLET_CURRENCY set Balance = Balance+(SELECT Amount from TRANSACTION where transaction_id = :1)
                    where  wallet_currency_id = (SELECT receiver_wallet_currency_id from TRANSACTION where transaction_id = :2)
                   """,(transaction_id,transaction_id))
               
               db.connection.commit()
               print(" balance updated successfully")
               
           except Exception as failed:
                  print(f"updated failed {failed}")


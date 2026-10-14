from database import Database

class Notification_details:
    # constructor with Encapsulation
    def __init__(self,transaction_id,reference_number,commission):
        self.__transaction_id=transaction_id
        self.__reference_number=reference_number
        self.__commission=commission



    # function of database (CRUD)

    # 1- Add new notifiction

    def add_notification_detl(self,db):  
        try:
            db.cursor.execute("""
            insert into notification_detl(
            notification_id,
            transaction_id,
            reference_number,
            commission
            ) values(notification_detl_seq.nextval,
            :1,:2,:3) """ ,(
            self.__transaction_id,
            self.__reference_number,
            self.__commission
            )  )
            db.cursor.execute("select notification_detl_seq.currval from dual")
            self.__notification_id = db.cursor.fetchone()

            db.connection.commit()
            print(f"User Notification_detl successfully ...your notification detl id is {self.__notification_id}")

        except Exception as failed:
            print(f"Notification_detl added failed : {failed}")



    # view All

    @staticmethod
    def view_all(db):
        db.cursor.execute("""
                    SELECT 
                    n.notification_id  AS "Notification_id",
                    t.transaction_id  AS "operation_id",
                    us.First_Name AS "sender_name",
                    ur.First_Name AS "receiver_name",
                    t.Amount AS "Amount",
                    nd.commission As "Commission",
                    t.transaction_status AS "operation_status",
                    n.massage As "Message",
                    t.Created_At AS "opration_Date"
                    from NOTIFICATION n 
                    join notification_detl nd on n.notification_id=nd.notification_id
                    join TRANSACTION t on nd.transaction_id=t.transaction_id
                    join wallet_currency wcs on t.sender_wallet_currency_id = wcs.wallet_currency_id
                    join wallet ws on wcs.wallet_id = ws.wallet_id
                    join users us on ws.user_id=us.user_id
                    join wallet_currency wcr on t.receiver_wallet_currency_id = wcr.wallet_currency_id
                    join WALLET wr on wcr.Wallet_id = wr.Wallet_id
                    join USERS ur on wr.user_id = ur.User_id
                    order by n.notification_id """)
        return db.cursor.fetchall()

   # search by reference_number

    @staticmethod
    def search_by_reference_number(db,reference_number):
        db.cursor.execute("""
            SELECT 
            n.notification_id  AS "Notification_id",
            nd.reference_number  AS "reference_number",
            us.First_Name AS "sender_name",
            ur.First_Name AS "receiver_name",
            t.Amount AS "Amount",
            nd.commission As "Commission",
            t.transaction_status AS "operation_status",
            n.massage As "Message",
            t.Created_At AS "opration_Date"
            from NOTIFICATION n 
            join notification_detl nd on n.notification_id=nd.notification_id
            join TRANSACTION t on nd.transaction_id=t.transaction_id
            join wallet_currency wcs on t.sender_wallet_currency_id = wcs.wallet_currency_id
            join wallet ws on wcs.wallet_id = ws.wallet_id
            join users us on ws.user_id=us.user_id
            join wallet_currency wcr on t.receiver_wallet_currency_id = wcr.wallet_currency_id
            join WALLET wr on wcr.Wallet_id = wr.Wallet_id
            join USERS ur on wr.user_id = ur.User_id
            where nd.reference_number=:1
        """, (reference_number,))
        return db.cursor.fetchone()    


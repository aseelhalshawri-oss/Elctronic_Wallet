-----------------------------------------------------------
create table USERS(
User_id       number             primary key,
First_Name    varchar2(20)       not null,
Mid_Name      varchar2(20) ,
Last_Name     varchar2(20)       not null,
Phone_Number  number(9)          unique not null,
Email         varchar2(30)       unique ,
Password_user varchar2(20)       not null,
Date_of_Birth Date               not null,
Created_At    Date               default sysdate not null
);
---------------------------------------------------------
إنشاء تسلسل لرقم المستخدم
create sequence user_seq
start with 1
increment by 1
nocache;



--=======================================================
create table WALLET(
Wallet_id       number             primary key,
User_id         number             unique ,
Status_wallet   varchar2(10)       check(Status_wallet in('Active','UnActive')),
Created_At      Date               default sysdate not null,
constraint  user_wal_FK foreign key (User_id) references USERS(User_id) on delete cascade
);
-----------------------------------------------------
إنشاء تسلسل لرقم المحفظة
create sequence wallet_seq
start with 1
increment by 1
nocache;



--=======================================================
create table CURRENCY(
currency_id       number        primary key,
currency_name     varchar2(20),
currency_code     char(3)            
);
----------------------------------------------------------
إنشاء تسلسل لرقم العملة
create sequence currency_seq
start with 1
increment by 1
nocache;



--=======================================================
create table WALLET_CURRENCY(
wallet_currency_id     number             primary key,
currency_id            number,
Wallet_id              number,
Balance                number(15,3)       check(Balance >= 0),
constraint  wal_id_FK foreign key (Wallet_id) references WALLET(Wallet_id) on delete cascade,
constraint  cur_id_FK foreign key (currency_id) references  CURRENCY(currency_id) on delete cascade
);
--------------------------------------------------------
إنشاء تسلسل لرقم حساب المحفظة
create sequence wallet_currency_seq
start with 1
increment by 1
nocache;



--======================================================= 

create table TRANSACTION(
transaction_id                number           primary key,
sender_wallet_currency_id     number,
receiver_wallet_currency_id   number, 
transaction_type              varchar2(50)     check(transaction_tybe in('send','receive')),
transaction_status            varchar2(10)     check(transaction_status in('pending','completed','failed')),
Amount                        number(15,3)     check(Amount > 0)    ,
Created_At                    Date             default sysdate not null,
transaction_desc              varchar2(20),
constraint tra_sen_wal_cur_FK foreign key (sender_wallet_currency_id) references WALLET_CURRENCY(wallet_currency_id),
constraint tra_rec_wal_cur_FK foreign key (receiver_wallet_currency_id) references WALLET_CURRENCY(wallet_currency_id)
);
-------------------------------------------
للخصم من المرسل والاضافة للمستقبل TRIGGER إنشاء
create  trigger trg_transfer
after insert on TRANSACTION
for each row
when(new.transaction_status='completed')
begin 
update WALLET_CURRENCY set Balance=Balance - :new.Amount
where wallet_currency_id = :new.sender_wallet_currency_id;
----
update WALLET_CURRENCY set Balance=Balance + :new.Amount
where wallet_currency_id = :new.receiver_wallet_currency_id;
end;
------------------------------------------------------------
إنشاء تسلسل لرقم العملية
create sequence transaction_seq
start with 1
increment by 1
nocache;



--=======================================================

create table BENEFICIARY(
beneficiary_id         number           primary key,
User_id                number,
beneficiary_name       varchar2(100)    not null,
Phone_Number           number(9), 
Added_date             Date             default sysdate,
beneficiary_status     varchar2(10)     check(beneficiary_status in('Active','UnActive')),
constraint  user_ben_FK foreign key (User_id) references USERS(User_id) on delete cascade
);
--------------------------------------------------------------
إنشاء تسلسل لرقم المستفيد
create sequence beneficiary_seq
start with 1
increment by 1
nocache;



--=======================================================

create table NOTIFICATION(
notification_id         number           primary key,
User_id                 number,
Is_read                 varchar2(10)     check(Is_read in('readable','Unreadable')), 
Created_At              Date             default sysdate,
massage                 varchar2(50),
constraint  user_not_FK foreign key (User_id) references USERS(User_id) on delete cascade
)
-----------------------------------------------------------
إنشاء تسلسل لرقم الإشعار
create sequence notification_seq
start with 1
increment by 1
nocache;



--=======================================================
create table NOTIFICATION_DETL(
notification_id number primary key,
transaction_id number ,
reference_number number,
commission number default null,
constraint unq_ref_num unique (reference_number),
constraint not_dtl_FK foreign key (notification_id) references NOTIFICATION(notification_id) on delete cascade,
constraint tra_dtl_FK foreign key (transaction_id) references TRANSACTION(transaction_id) on delete cascade
);
--------------------------------------------------------------
إنشاء تسلسل لرقم تفاصيل الإشعار
create sequence notification_detl_seq
start with 1
increment by 1
nocache;





--=================================================================

جمل استعلام   
----------------------------------------------------------------
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

----------------------------------------------------------------------------
select 
u.user_id,
w.Wallet_id,
u.first_name,
w.Status_wallet
from users u
join wallet w on u.user_id=w.Wallet_id
order by 1;

----------------------------------------------------------------------------
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


------------------------------------------------------------

select us.First_Name as "sender_name",
count(ts.transaction_id) as "number of operation",
sum(ts.Amount) as "final_Amount_sender"
from USERS us
join wallet ws on us.User_id = ws.User_id
join wallet_currency wcs on ws.Wallet_id = wcs.Wallet_id
join TRANSACTION ts on wcs.wallet_currency_id = ts.sender_wallet_currency_id 
Group by us.First_Name

--------------------------------

SELECT 
ur.First_Name as "Receiver_name",
count(tr.transaction_id) as "number of operation",
sum(tr.Amount) as "final_Amount_receiver"
from USERS ur
join wallet wr on ur.User_id = wr.User_id
join wallet_currency wcr on wr.Wallet_id = wcr.Wallet_id
join TRANSACTION tr on wcr.wallet_currency_id = tr.receiver_wallet_currency_id 
Group by ur.First_Name



--------------------------------------------------------------------------

select us.First_Name as "sender_name",
count(ts.transaction_id) as "number of operation",
sum(ts.Amount) as "final_Amount",
c.currency_code 
from USERS us
join wallet ws on us.User_id = ws.User_id
join wallet_currency wcs on ws.Wallet_id = wcs.Wallet_id
join CURRENCY c on wcs.currency_id=c.currency_id
join TRANSACTION ts on wcs.wallet_currency_id = ts.sender_wallet_currency_id 
Group by us.First_Name , currency_code


--------------------------------------------------------------------------

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
order by n.notification_id 

--------------------------------------------------------------------------------------

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
where nd.reference_number=101010;

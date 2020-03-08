import datetime as dt
import threading
import twilio_functions as tw

CAVEMANAGER = ("Desolation Wilderness", "Ranger Maria", 7146810524) #to be hard coded into device
##############################################
##############################################
# UPDATE: to be imported somehow from database
##############################################
##############################################
check_in = {"photo": "123.jpg", "date_time": dt.datetime(2020,3,7,10,0),
"user": (123456, "Sonia Meyer", 7146810524), "group_size": 3,
"expected_out": dt.datetime(2020,3,7,18,0), "call_out": dt.datetime(2020,3,8,8,0)}
check_out = {"photo": "456.jpg", "date_time": dt.datetime(2020,3,7,18,30),
"user": (123456, "Sonia Meyer", 7146810524), "group_size": 3}
missed_checkout = {"photo": "456.jpg", "date_time": dt.datetime(2020,3,7,23,00),
"user": (123456, "Sonia Meyer", 7146810524), "group_size": 3}
##############################################
##############################################

#code for initiate_contact time
expected_out = check_in["expected_out"]
call_out = check_in["call_out"]
initiate_contact = expected_out + (call_out - expected_out) / 2
too_late = dt.time(23,1)
too_early = dt.time(6,59)
if too_early > initiate_contact.time() or initiate_contact.time() > too_late: #if out of range
    initiate_contact = initiate_contact.combine(expected_out.date(), too_late) #replace with reasonable time
if initiate_contact.time() < expected_out.time(): #if reasonable time is earlier than expected out time
    initiate_contact = expected_out #replace with expected out time

#code for missed_expected_out
#the missed_expected_out will check user status at initiate_contact time,
#then check with user if they forgot to check out of cave
delay_expected_out = initiate_contact - dt.datetime.now()
delay_expected_out = 3 #delete later!!!!
check_out = {} #delete later, testing no check out
expected_out_timer = threading.Timer(delay_expected_out, tw.missed_expected_out)
expected_out_timer.start()

#code for missed_call_out
#the missed_call_out will check user status at call out time, then notify
#the cave manager to initiate rescue if user is not out
delay_call_out = call_out - dt.datetime.now()
delay_call_out = 3 #delete later!!!!
#check_out = {} #delete later, testing no check out
call_out_timer = threading.Timer(delay_call_out, tw.missed_call_out)
call_out_timer.start()

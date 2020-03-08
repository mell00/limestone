import twilio_functions as tw

#############################################################
###database triggers this code when status is changed to "out"
#############################################################
if tw.check_user_status("out"): tw.checked_out()
#############################################################
#############################################################

# Additional goals: every X days the device uploads the entry/exit logs to cave/park management

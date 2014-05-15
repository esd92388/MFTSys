#!/usr/bin/python
import os
####This is the Manufacturing Tracking System####
###Created by: Eric Downs, 2014-05-14 01:26
###ECE 387 Embedded Systems Design 
###Originally intended to run on the beaglebone black
###Modified to Run on a Mac 


##Update Workcell RFID log files
#Workcell 1 log update
WC1SLPath = os.path.expanduser('~/Documents/MFTrackingSystem/Workcell_1/screenlog.0')
WC1IDPath = os.path.expanduser('~/Documents/MFTrackingSystem/Workcell_1/WC1ID.log')
WC1SL = open(WC1SLPath, 'r')
WC1LogContents = WC1SL.read();
WC1SL.close()
WC1ID = open(WC1IDPath, 'w')
WC1ID.write(WC1LogContents)
WC1ID.close()

##Test Code
#print "WC1 RFID Log"
#WC1ID = open(WC1IDPath, 'r')
#str = WC1ID.read()
#WC1ID.close()
#print str

#Workcell 2 log update
WC2SLPath = os.path.expanduser('~/Documents/MFTrackingSystem/Workcell_2/screenlog.0')
WC2IDPath = os.path.expanduser('~/Documents/MFTrackingSystem/Workcell_2/WC2ID.log')
WC2SL = open(WC2SLPath, 'r')
WC2LogContents = WC2SL.read();
WC2SL.close()
WC2ID = open(WC2IDPath, 'w')
WC2ID.write(WC2LogContents)
WC2ID.close()

##Test Code
#print "WC2 RFID Log"
#WC2ID = open(WC2IDPath, 'r')
#str = WC2ID.read()
#WC2ID.close()
#print str

##Begin User Interface
ValidWC = False
print "Hello Manufacturers"
print "Welcome to the Manufacturing Tracking System"
workcell = raw_input("Enter a Workcell(WC1 or WC2): ")
#Check for valid entry
if(workcell == "WC1" or workcell == "wc1" or workcell == "WC2" or workcell == "wc2"):
 ValidWC = True

#Invalid Entry Loop
while(ValidWC == False):
 print "Invalid entry"
 workcell = raw_input("Enter a Workcell(WC1 or WC2): ")
 if(workcell == "WC1" or workcell == "wc1" or workcell == "WC2" or workcell == "wc2"): 
  ValidWC = True 

##Begin data collection and print out 
print "Workcell " + workcell + " selected"

#data and printouts if 'WC1' selected
if(workcell == "WC1" or workcell == "wc1"):
 print "Workcell 1 Status"
 #read in most recent log in 
 WC1ID = open(WC1IDPath, 'r')
 WC1ID.seek(0,2)
 WC1IDLength = WC1ID.tell()
 WC1ID.seek(0)
 WC1IDOffset = WC1IDLength - 17
 WC1ID.seek(WC1IDOffset)
 wc1LoggedIn = WC1ID.read()
 WC1ID.close()
 print "Currently logged in is employee# " + wc1LoggedIn

 WC1OrderPath = os.path.expanduser('~/Documents/MFTrackingSystem/Workcell_1/WC1Order.log')
 WC1Order = open(WC1OrderPath, 'r')
 WC1Order.seek(0,2)
 WC1OrderLength = WC1Order.tell()
 WC1Order.seek(0)
 WC1OrderOffset = WC1OrderLength - 17
 WC1Order.seek(WC1OrderOffset)
 wc1RecentOrder = WC1Order.read()
 WC1Order.close()
 print "The last order scanned into workcell 1 is: " + wc1RecentOrder

#data and printouts if 'WC2' selected
if(workcell == "WC2" or workcell == "wc2"):
 print "Workcell 2 Status"
 #read in most recent log in
 WC2ID = open(WC2IDPath, 'r')
 WC2ID.seek(0,2)
 WC2IDLength = WC2ID.tell()
 WC2ID.seek(0)
 WC2IDOffset = WC2IDLength - 17
 WC2ID.seek(WC2IDOffset)
 wc2LoggedIn = WC2ID.read()
 WC2ID.close()
 print "Currently logged in is employee# " + wc2LoggedIn

 WC2OrderPath = os.path.expanduser('~/Documents/MFTrackingSystem/Workcell_2/WC2Order.log')
 WC2Order = open(WC2OrderPath, 'r')
 WC2Order.seek(0,2)
 WC2OrderLength = WC2Order.tell()
 WC2Order.seek(0)
 WC2OrderOffset = WC2OrderLength - 17
 WC2Order.seek(WC2OrderOffset)
 wc2RecentOrder = WC2Order.read()
 WC2Order.close()
 print "The last order scanned into workcell 2 is: " + wc2RecentOrder

##End Code##

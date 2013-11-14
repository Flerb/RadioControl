import csv #imports csv
import serial #imports serial
ser = serial.Serial('COM7', 4800, timeout=1) # Opens COM7 at 4800 Baud
ser.write("\r") #CR, just in case
ser.write("H1\r") #Command to turn interface on
frequencies=[] #initiates frequency list
lastfreq="" # initiates last frequency string as blank in order to check for dupes
with open('stations.csv') as csvfile:
    stationsfile = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in stationsfile: #iterates through rows
        if not row[0]: #checks if blank
            continue
        else:
            if row[0] == lastfreq:
                continue #skips if dupe
            else: 
                frequencies.append(row[0]) #appends frequency
                lastfreq=row[0] #sets lastfreq as current freq to check for dupes later
    
def change(freq, serial): #function to change freq
    integer=int(frequency)*1000 #convert to mhz
    ser.write("F"+format(integer, '08')+"\r") #format string (adds leading zeroes")
    if raw_input("Can you tell what it is yet?") == "Yes": #prompts the user
        if raw_input("Would you like to move on ?") != "Yes": # asks user if to continue
            return False #returns False in order to break for loop
    else:
        return True #returns True to continue
        
    
for frequency in frequencies:
    if change(frequency, ser) == False: #breaks
        break
    else: #continues
        continue 

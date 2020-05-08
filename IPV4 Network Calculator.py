'''
    Program:IPv4 Network Calculator
    Author: Ryan Van Massenhoven 
    Date: 3/2/2020
    Description: IPV4 Network Calculator
'''
'''
    FUNCTIONS
'''
#Converts Decimal Numbers to Binary
def DectoBin(x):
    return str(bin(x)[2:].zfill(8))

#Converts Binary to Decimal
def BintoDec (x):
    return int(x,2)

#Converts Subnet Prifix to Binary Subnet Mask
def PrifixtoBinaryMask(Prifix):
    Mask = []
    #appends the Correct number of 1 "bits" based on the Subnet Prifix Provided
    for i in range(Prifix):
        Mask.append(1)
    #fill in the ramaining variables with 0
    while i <= 30:
        Mask.append(0)
        i += 1
    #Converts Elements to type string
    for i in range(len(Mask)): Mask[i] = str(Mask[i])   

    return Mask

#Converts Prifix to Decimal Subnet Mask
def PrifixtoMask(Prifix):
    Mask = []
    #appends the Correct number of 1 "bits" based on the Subnet Prifix Provided
    for i in range(Prifix):
        Mask.append(1)
    #fill in the ramaining variables with 0
    while i <= 30:
        Mask.append(0)
        i += 1
    #Split into Octets
    Mask.insert(8," ")
    Mask.insert(17," ")
    Mask.insert(26," ")

    #Converts Elements to type string
    for i in range(len(Mask)): Mask[i] = str(Mask[i])

    tempMask = ''.join(Mask)
    Mask = tempMask.split(" ")

    finalMask = []
    for i in range(len(Mask)): finalMask.append(BintoDec(Mask[i]))

    return finalMask

###############################################################################################################
'''
    BODY
'''
import os

#Print title
print ("IPv4 Break Down Program")

'''
    Collects and Validates User Input
'''
ValidatedInput = False

###For Bypassing user input for testing (comment UserInput in while loop (Line 75))###
#UserInput = "192.168.10.10/8"
while ValidatedInput == False:
    UserInput = input("Please enter an IPv4 Address and Prifix(#.#.#.#/MM):")
    
    #Removes Subnet Prifix
    temp = list(UserInput)

    for i in range(len(temp)): 
        if temp[i] == "/": x = i

    while x in range(len(temp)): del temp[x]

    tempIP = ''.join(temp)
    IP = tempIP.split(".")

    #Converts from str to int
    for i in range(len(IP)): IP[i] = int(IP[i])

    #Creating Subnet Variable from UserInput
    temp = UserInput.split("/")
    SUBNET = temp[1]
    SUBNET = int(SUBNET)

    if IP[0] >= 0 and IP[0] <= 255 and IP[1] >= 0 and IP[1] <= 255 and IP[2] >= 0 and IP[2] <= 255 and IP[3] >= 0 and IP[3] <= 255 and SUBNET >= 8 and SUBNET <= 31:
        ValidatedInput = True
    else:
        print("The correct format is [0-255].[0-255].[0-255].[0-255]/[8-31] Mask")
        print("-Example: 192.168.1.2/24 (No spaces)")
##end of While Loop##
os.system("cls")

'''
    Calcualtes Network Address
'''
#Converts IP to Binary
tempBinaryIP = []
for i in range(len(IP)):
    tempBinaryIP.append(list(DectoBin(IP[i])))

#makes 3D list 2D
BinaryIP = []
for temp in tempBinaryIP: 
    for elem in temp: 
        BinaryIP.append(elem)

BinNetworkAddress = []
for i in range(len(BinaryIP)): BinNetworkAddress.insert(i,BinaryIP[i])

#removes bits that need to be replaced
i = 32 - SUBNET
while i != 0:
    del BinNetworkAddress[-1]
    i-=1
#replaces Bits
i = len(BinNetworkAddress)
while i < 32:
    BinNetworkAddress.append("0")
    i+=1

#breaks into octets
BinNetworkAddress.insert(8," ")
BinNetworkAddress.insert(17," ")
BinNetworkAddress.insert(26," ")


tempBinNetworkAddress = ''.join(BinNetworkAddress)
BinNetworkAddress = tempBinNetworkAddress.split(" ")

#converts the Binary address to Decimal
NetworkAddress = []
for i in range (len(BinNetworkAddress)): NetworkAddress.insert(i,BintoDec(BinNetworkAddress[i]))

'''
    Calculates Subnet mask
'''
    #Converts Subnet Prifix to Binary Subnet Mask
BinaryMask = [0,0,0,0]
BinaryMask = PrifixtoBinaryMask(SUBNET)

TempMask = BinaryMask[SUBNET:len(BinaryMask)]
 #Converts Binary Subnet Mask to Decimal Subnet Mask
SubnetMask = PrifixtoMask(SUBNET)

'''
    Calculates the Maximum Number of Hosts
'''
MaxHosts = 2**(32-SUBNET)-2

'''
    Calcualte the First Useable IP address
'''
FirstAddress = []
for i in range(len(NetworkAddress)): FirstAddress.insert(i,NetworkAddress[i])
FirstAddress[-1] = FirstAddress[-1] +1

'''
    Calculate the Broadcast address
'''
BinBroadcastAddress = []
for i in range(len(BinaryIP)): BinBroadcastAddress.insert(i,BinaryIP[i])

#removes bits that need to be replaced
i = 32 - SUBNET
while i != 0:
    del BinBroadcastAddress[-1]
    i-=1

#replaces Bits
i = len(BinBroadcastAddress)
while i < 32:
    BinBroadcastAddress.append("1")
    i+=1

#breaks into octets
BinBroadcastAddress.insert(8," ")
BinBroadcastAddress.insert(17," ")
BinBroadcastAddress.insert(26," ")


tempBinBroadcastAddress = ''.join(BinBroadcastAddress)
BinBroadcastAddress = tempBinBroadcastAddress.split(" ")

#converts the Binary address to Decimal
BroadcastAddress = []
for i in range (len(BinBroadcastAddress)): BroadcastAddress.insert(i,BintoDec(BinBroadcastAddress[i]))

'''
    Calculate the Last Usable Address
'''
LastAddress = []
for i in range(len(BroadcastAddress)): LastAddress.insert(i,BroadcastAddress[i])
LastAddress[-1] = LastAddress[-1] -1




'''
    Prints Calcualtions
'''
print ("For the Provided IP Address and Prefix")
print ("The IP address you entered is ", IP[0], ".", IP[1], ".", IP[2], ".", IP[3], sep="")

print ("")
print ("The IP Provided belongs to the Network ", NetworkAddress[0], ".", NetworkAddress[1], ".", NetworkAddress[2], ".", NetworkAddress[3], sep="")
print ("- The Subnet Mask would be ", SubnetMask[0], ".", SubnetMask[1], ".", SubnetMask[2], ".", SubnetMask[3], sep="")
print ("- Netmask:", SUBNET)

print("")
print ("The number of hosts allowed on the network is",MaxHosts)
print ("- The First Address would be ", FirstAddress[0], ".", FirstAddress[1], ".", FirstAddress[2], ".", FirstAddress[3], sep="")
print ("- The Last Address would be ", LastAddress[0], ".", LastAddress[1], ".", LastAddress[2], ".", LastAddress[3], sep="")
print ("- The Network Broadcast Address would be ", BroadcastAddress[0], ".", BroadcastAddress[1], ".", BroadcastAddress[2], ".", BroadcastAddress[3], sep="")

os.system("pause")
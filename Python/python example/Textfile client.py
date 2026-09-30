# This program was made by Harris Domangue for CMSC-201 on oct 31st 2024
# This program will fetch the data from the server file

port = input("Port number: ")
prompt = None
ID = None
while prompt != 'stop':
    try:
        network = open('port'+port+'.txt','r') # read the file
        for line in network:
            line = line.split('-')
            prompt = line[0]
            tag = line[1]
        if tag != ID and prompt != None:
            print("Message:",prompt)
            ID = tag
        network.close()
    except FileNotFoundError:
        if prompt == None:
            prompt = 'waiting for connection...'
            print(prompt)
        

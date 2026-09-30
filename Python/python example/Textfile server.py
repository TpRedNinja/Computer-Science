# This program was made by Harris Domangue for CMSC-201 on oct 31st 2024
# This program will communicate between two seperate modules

port = input("Enter a port number: ")

prompt = None
count = 0
while prompt != 'stop':
    count += 1
    prompt = input("Enter your msg here: ")
    # create a network textfile
    network = open("port"+port+".txt",'w')
    network.write(prompt + "-" + str(count))
    network.close()

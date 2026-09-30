# This program was made by Harris Domangue for CMSC-201 on Oct 22nd 2024
# This program will solve the towers of hanoi

def TowerOfHanoi(number,source,destination,auxillary):
    # base case
    if number == 1:
        print(f'move disk {number} to peg {destination}')
        return
    # recursive case
    TowerOfHanoi(number - 1,source,auxillary,destination)
    print(f'move disk {number} to peg {destination}')
    TowerOfHanoi(number - 1,auxillary,destination,source)

def main():
    TowerOfHanoi(3,"A","B","C")

if __name__ == '__main__':
    main()

def steering(x,y,direction):
    if (x >= 30 and x <= 40) and (y >= 555 and y <= 585):
        return 'east'
    elif (x >= 30 and x <= 40) and (y >= 30 and y <= 40):
        return 'south'
    elif (x >= 655 and x <= 685) and (y >= 555 and y <= 585):
        return 'north'
    elif (x >= 655 and x <= 685) and (y >= 30 and y <= 40):
        return 'west'
    else:
        return direction

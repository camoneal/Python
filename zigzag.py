import time, sys
indent = 0 # Indicates how many spaces to indent
indentIncreasing = True # Indicates whether the indentation is increasing or not

try:
    while True: # Main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) #Lets it pause for 1/10 of a second

        if indentIncreasing:
            #Increases the number of spaces:
            indent = indent +1
            if indent == 20:
                #change direction input
                indentIncreasing = False
        else:
            #Decrease the number of spaces:
            indent = indent  - 1
            if indent == 0:
                #Changes directions:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.ext()

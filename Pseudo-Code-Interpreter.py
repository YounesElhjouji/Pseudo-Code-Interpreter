'''                Younes Elhjouji        Mohamed Abdulkahar
                              Python 3.6 32-bit
'''

#Is positive or negative digit
def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

'''                       LOADER FUNCTIONS                                 '''
#Calls loading functions in order
def load():
    global inputs
    #Opening input file and extracting data, program, and input
    inputs = inp()
    #Load data into data memory
    loadData()
    #load code into code memory
    loadCode() 

#Takes in the code and input and returns it as a list of integers
def inp():
    inf = open ('Sample Program.txt','r')
    lines = inf.read()              #Read all input as one string
    lines = lines.replace(',','\n') #replace commas with new lines
    lines = lines.replace(' ','')   #Remove spaces
    lines = lines.split('\n')       #Make each line into element of list 
    lines = filter(None,lines)      #Remove emty lines (eof)
    lines = list(map(int, lines))   #Convert strings in list into integers
    return lines

#Returns next line of code/input
def getLine():
    global count
    temp = inputs[count] #Retrieve next item of code/input
    count+=1             #Move count ahead to next index
    return temp
    
    
#Initializing data memory positionally
def loadData():
    global m  #To access global memory
    i=0
    line = getLine()
    while line!=9999999999:
        #Read dest address
        dest = int(line%1000)
        line/=1000000
        opd1 = int(line%1000)
        #If dest is 0 store in next in next memory address
        if dest == 0:
            m[i]=m[opd1]
            i+=1
        #If dest is not 0 store in dest 
        else:
            m[dest]=m[opd1]
            i=dest+1
        line = getLine()

#Loading the program lines into program memory positionally
def loadCode():
    i=1000
    line = getLine()
    while True:
        #Load one line of code at a time
        m[i]=line
        #Until line == 9999999999 then break
        if line == 9999999999:
            break
        line = getLine()
        i+=1
    

'''
                         EXECUTE FUNCTION
The execute() function goes through the code and calls a function to extract
the elements of every line of codes and then sends opd1, opd2, and dest to
the function that corresponds to the opcode
'''
def execute():
    
    #Mapping opcodes to functions
    funcs = {0:assign,      
             1:   add,
             -1:  substract,
             2:   multiply,
             -2:  divide,
             3:   square,
             -3:  sqrt,
             4:   equal,
             -4:  unequal,
             5:   great,
             -5:  less,
             6:   arrRetrieve,
             -6:  arrAssign,
             7:   loop,
             +8:  read,
             -8:  write,
             9:   stop
             }
    i = 1000
    num = m[i]
    while num!=9999999999 :
        opcode, opd1, opd2, dest = extractCode(num)
        #To trace and debug
        #print ('%d %d %d %d'%(opcode, opd1, opd2, dest))
        i = funcs[opcode](opd1,opd2,dest,i)
        #Read new line of code
        num = m[i]
        
#Takes in line of code and extracts the elements of the line
def extractCode(num):
    flag = False
    if num<0:
        num= abs(num)
        flag = True
    dest = int(num%1000)
    num/=1000
    opd2 = int(num%1000)
    num/=1000
    opd1 = int(num%1000)
    num/=1000
    opcode = int(num%1000)
    if flag == True:
        opcode= -opcode
    return opcode, opd1, opd2, dest

'''                         PCL FUNCTIONS                           '''
#Assignment
def assign (opd1, opd2, dest,i):
    m[dest] = m[opd1]
    return i+1

#Addition
def add (opd1, opd2, dest, i):
    m[dest] = m[opd1]+m[opd2]
    return i+1
        
#Substraction
def substract (opd1, opd2, dest, i):
    m[dest] = m[opd1]-m[opd2]
    return i+1
        
#Multiplication
def multiply (opd1, opd2, dest, i):
    m[dest] = m[opd1]*m[opd2]
    return i+1
        
#Division
def divide (opd1, opd2, dest, i):
    m[dest] = m[opd1]/m[opd2]
    #If result is int, it is stored as int
    if m[dest].is_integer():
        m[dest]=int(m[dest])
    return i+1

#Square
def square (opd1, opd2, dest, i):
    m[dest] = m[opd1]**2
    return i+1

#Square root
def sqrt (opd1, opd2, dest, i):
    m[dest] = m[opd1]**(1/2)
    return i+1

#Equality
def equal (opd1, opd2, dest, i):
    if m[opd1]==m[opd2]:
        return dest+1000
    else:
        return i+1

#Inequality
def unequal (opd1, opd2, dest, i):
    if m[opd1]!=m[opd2]:
        return dest+1000
    else:
        return i+1

#Greater or equal
def great (opd1, opd2, dest, i):
    if m[opd1]>=m[opd2]:
        return dest+1000
    else:
        return i+1

#Lesser
def less (opd1, opd2, dest, i):
    if m[opd1]<m[opd2]:
        return dest+1000
    else:
        return i+1

#Retrieve value from array position
def arrRetrieve (opd1, opd2, dest, i):
    idx = m[opd2]
    m[dest] = m[opd1+idx]
    return i+1

#Assign value to array position
def arrAssign (opd1, opd2, dest, i):
    idx = m[dest]
    m[opd2+idx] = m[opd1]
    #To trace and debug
    #print (m[0:20])
    return i+1

#Loop
def loop (opd1, opd2, dest,i):
    if m[opd1]>=m[opd2]-1:
        return i+1
    else:
        m[opd1]+=1
        return dest+1000

#Read
def read (opd1, opd2, dest, i):
    m[dest] = getLine()
    return i+1

#Write
def write (opd1, opd2, dest,i):
    print (m[opd1]) #prints value at source and not destination
    return i+1

#Stop
def stop (opd1, opd2, dest, i):
    return i+1 #When input is 9000000000, read next (seperator) line


'''                          MAIN PROGRAM                               '''
#Intitializing the data & program memory to 0
m = [0 for x in range (0,2000)] #m stands for memory

#list where data, program, and input are to be stored
inputs = []

#Keeps track of which element of input is next
count=0

#Loads data and program memory
load()

#Execute code
execute()


import time

while True:
    try:
        num = input("masukan int ")
        gg = str(num)
        l = []
        if isinstance( num, ( int, long ) ):
            if num < 0:
                print "masukan int >= 0"
            elif num == 0:
                print "0! = 1"
            else:
                i=0
                fak=1
                while(i<num):
                    fak *= num
                    l.append(str(num))
                    num -= 1
                x = "%si" %(gg)
                print x, "=", " X ".join(l), "=", fak
        else :
            print "fakyu"
    except NameError: print "please insert integer"
    except SyntaxError: print "please insert integer"

    time.sleep(1)

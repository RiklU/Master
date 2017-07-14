import sys
import math
"the class the calculate pi"
class pi:
    def main(argv):

        if len(argv)!=1:
            sys.exit('Usage:calc_pi_py')


            a=1.0
            b=1.0/math.sqrt(2)
            t=1.0/4.0
            p=1.0

        for i in range(int(sys.argv[1])):
            at=(a+b)/2
            bt=math.sqrt(a*b)
            tt=t-p*(a-at)**2
            pt=2*p

            a=at;
            b=bt;
            t=tt;
            p=pt

            mypi=(a+b)**2/(4*t)
            accuracy=100*(Decimal(math.pi)-my_pi)/my_pi
            print(str(mypi))
            print(str(accuracy))


if __name__=="__main__":
    pi1=pi()
    pi1.main(sys.argv[0])
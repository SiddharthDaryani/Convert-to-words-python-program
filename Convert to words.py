import logging
logging.basicConfig(filename= "Convert to words.log", level= logging.INFO, format= '%(asctime)s %(levelname)s %(message)s')
ones= ["zero", "one", "two", "three","four","five", "six", "seven", "eight", "nine", "ten","eleven", "twelve", "thirteen","fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tenths= ["zero", "ten", "twenty", "thirty", "fourty","fifty","sixty", "seventy","eighty","ninety"]
word= []
try:
    def check(num):
        #checking if lacs
        if int(num/100000)>0:
            #using recursion
            check(int(num/100000))
            word.append("lakhs")
            num= num%100000
        #checking if thousands
        if int(num/1000)>0:
            #using recursion
            check(int(num/1000))
            word.append("thousand")
            num= num%1000
        #checking if hundred
        if int(num/100)>0:
            #using recursion
            check(int(num/100))
            word.append("hundred")
            num= num%100
        if num<20 and num>=0:
            word.append(ones[num])
        if int(num/10)>0 and num!= 10:
            word.append(tenths[int(num/10)])
            check(num%10)
except Exception as e:
    print(e)
check(1001567)
output= ''
for i in word:
    output= output+i
    output= output+ ' '
logging.info(output)

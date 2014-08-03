import re
file = open('PathToInputFile', 'r')

text = file.read()

Number = re.findall('\d+',text)

for i in range (0,len(Number)):
    if Number[i] != "09131300931" and len(Number[i]) > 9 :
        print "0" + Number[i]
        text_file = open("Output.txt", "a")
        text_file.write("0%s" % Number[i])
        text_file.write("\n")
        text_file.close()

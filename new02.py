import writeFunc as wf
class i1():
    def printIt():
        print("wooo")
        return 0
    def rewrite():
        file = open("new01.py","w",encoding = "UTF-8")
        file.write(wf.writefunc("new.py"))
        file.close()
        import new01.py
        #new01.py.i1.printIn()
        #new01.py.i1.rewrite()
        return 0

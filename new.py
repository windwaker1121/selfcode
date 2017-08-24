import writeFunc as wf
class i1():
    def printIt():
        print("wooo")
        return 0
    def rewrite():
        file = open("new.py","w",encoding = "UTF-8")
        file.write(wf.writefunc("new.py.py"))
        file.close()
        import new.py
        #new.py.i1.printIn()
        #new.py.i1.rewrite()
        return 0

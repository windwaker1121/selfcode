import writeFunc as wf
class i1():
    num = 0
    def __init__(self,num,i):
        self.num = num
        self.i = i-1
    def printIt(self):
        print("wooo")
    def rewrite(self):
        file = open("new"+str((self.num+1)%2)+".py","w",encoding = "UTF-8")
        file.write(wf.writefunc((self.num+1)%2))
        file.close()
        import new1
        newin = new1.i1(1,self.i)
        newin.printIt()
        if self.i>0:
            newin.rewrite()
        print(str(self.i)+"-"+str(1))

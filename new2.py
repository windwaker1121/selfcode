import writeFunc as wf
import new0,imp 
class i1():
    num = 0
    def __init__(self,num,i):
        self.num = num
        self.i = i-1
    def printIt(self):
        print("wooo")
    def rewrite(self):
        file = open("new"+str((self.num+1)%3)+".py","w",encoding = "UTF-8")
        file.write(wf.writefunc((self.num+1)%3))
        file.close()
        imp.reload(new0)
        newin = new0.i1(0,self.i)
        #newin.printIn()
        if self.i>0:
            newin.rewrite()
        print(str(self.i)+str(0))

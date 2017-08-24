#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:57:45 2017

@author: work
"""
def writefunc(fileName):
        num = str((fileName+1)%2)
        wrt_str = 'import writeFunc as wf\n'+\
                  'class i1():\n'+\
                  '    num = 0\n'+\
                  '    def __init__(self,num,i):\n'+\
                  '        self.num = num\n'+\
                  '        self.i = i-1\n'+\
                  '    def printIt(self):\n'+\
                  '        print("wooo")\n'+\
                  '    def rewrite(self):\n'+\
                  '        file = open("new"+str((self.num+1)%2)+".py","w",encoding = "UTF-8")\n'+\
                  '        file.write(wf.writefunc((self.num+1)%2))\n'+\
                  '        file.close()\n'+\
                  '        import new'+num+'\n'+\
                  '        newin = new'+num+'.i1('+num+',self.i)\n'+\
                  '        newin.printIt()\n'+\
                  '        if self.i>0:\n'+\
                  '            newin.rewrite()\n'+\
                  '        print(str(self.i)+"-"+str('+num+'))\n'
        return wrt_str

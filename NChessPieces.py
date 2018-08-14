# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 09:06:43 2018

@author: Erman
"""

import math


class ChessBoard():
    
    def __init__(self):
        self.N=8
        self.pieceDict={1:"Queens",2:"Rooks",3:"Bishops",4:"Knights"}
        self.pieceType=1
        self.checkOneDimensional=None
        self.checkTwoDimensional=None
        self.resultCount=-1
        
        
    def getTheInfo(self):
        self.N=int(input("Enter the size of the board: "))
        print("Enter")
        for k,v in self.pieceDict.items():
            print(k," for ",v)
            
        self.pieceType=int(input("Here: "))
        
    def fixTheModel(self):
        if self.pieceType==1 :
            self.checkOneDimensional=self.checkNQueens
            
        elif self.pieceType==2 :
            self.checkOneDimensional=self.checkNRooks
            
        elif self.pieceType==3 :
            self.checkTwoDimensional=self.checkTwoBishops
            
        elif self.pieceType==4 :
            self.checkTwoDimensional=self.checkTwoKnights
            
    def runTheModel(self):
        if self.pieceType==1 or self.pieceType==2:
            self.resultCount=self.enumerateCountOneDim(self.N,[])
        else:
            self.resultCount=self.enumerateCount(self.N,0,[])
            print(self.resultCount)
        
        
    def checkNQueens(self,queenList):
        result=True
        
        for first in range(len(queenList)-1):
            for second in range(first+1,len(queenList)):
                if queenList[first]==queenList[second] or math.fabs(first-second)==math.fabs(queenList[first]-queenList[second]):
                    result=False
                    return False
                
        return result
    
    def checkNRooks(self,rookList):
        result=True
        
        for first in range(len(rookList)-1):
            for second in range(first+1,len(rookList)):
                if rookList[first]==rookList[second] :
                    result=False
                    return False
                
        return result
    
    
    
    def enumerateCountOneDim(self,NM,posList):
    
        if len(posList)>NM:
            
            return 0
        elif not self.checkOneDimensional(posList) :
            return 0
        elif self.checkOneDimensional(posList) and len(posList)==NM:
            return 1
        else:
            total=0
            tempList=posList.copy()
            for ind in range(NM):
                posList=tempList.copy()
                posList.append(ind)
                total+=self.enumerateCountOneDim(NM,posList)
                
            return total
        
    def checkTwoBishops(self,pair1,pair2):
        result=True
        
        if math.fabs(pair1[0]-pair2[0])==math.fabs(pair1[1]-pair2[1]):
            result=False
            
        return result
    
    def checkTwoKnights(self,pair1,pair2):
        result=True
        
        if (math.fabs(pair1[0]-pair2[0])==1 and math.fabs(pair1[1]-pair2[1])==2) or (math.fabs(pair1[0]-pair2[0])==2 and math.fabs(pair1[1]-pair2[1])==1):
            result=False
            
        return result
    
    
    
    def checkAllPieces(self,pieceList):
        result=True
        for first in range(len(pieceList)-1):
            for second in range(first+1,len(pieceList)):
                if not self.checkTwoDimensional(pieceList[first],pieceList[second]):
                    result=False
                    return result
        
        return result
    
    
    def enumerateCount(self,N,x,myList):
    
        if len(myList)>N:
            return 0
        elif not self.checkAllPieces(myList):
            return 0
        elif self.checkAllPieces(myList) and len(myList)==N:
            
            return 1
        else:
            total=0
            tempList=myList.copy()
            
            for ind in range(x,N*N):
                x=ind//N
                y=ind%N
                myList=tempList.copy()
                myList.append([x,y])
                total+=self.enumerateCount(N,ind+1,myList)
                
            return total
        
    def reportTheResult(self):
        print("#########################")
        print(self.resultCount,self.pieceDict[self.pieceType] , " can accomodated on a ",self.N, "*", self.N, " board,")
        print("without attacking eachother.")
        
        
    

            
            
        
        



if __name__ == '__main__': 
    CB=ChessBoard()
    CB.getTheInfo()
    CB.fixTheModel()
    CB.runTheModel()
    CB.reportTheResult()
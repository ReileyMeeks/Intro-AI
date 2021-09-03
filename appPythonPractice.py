#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 19:11:29 2021

@author: ReileyMeeks
"""
from scipy.spatial import distance

#Reverse order list
def reverseOrder(rList):
    reversedList = [0] * len(rList)
    i = 0
    while i < len(rList):
        reversedList[i] = rList[(len(rList)) - 1 - i]
        i += 1
    return reversedList

revThisList = [1, 2, 3, 4]
print(reverseOrder(revThisList))

#Other way to reverse list 
#hey = [1, 2, 3]
#hey.reverse()
#print(hey)

#End reverse list func

#Max index, starts from 0
def maxPos(l, lngth):
    mPos = l.index(max(l))
    print ("Max position is:", mPos)
    
findMaxList = [5, 25, 50, 8]
maxPos(findMaxList, len(findMaxList))
#End max index  

#Print only odd numbers
def justOdds(oList):
    oddNums = [num for num in oList if num % 2 == 1]
    print(oddNums)
oddList = [1, 2, 3, 4, 5, 99]
justOdds(oddList)
#End only odd numbers

#Euclidean Distance
def euDist(l1, l2, n1, n2):   
    a = l1[n1]
    b = l2[n2]
    
    dst = distance.euclidean(a, b)
    print(dst)    

lst1 = [4, 7, 1, 33]  
lst2 = [2, 3, 77, 2]  
euDist(lst1, lst2, 2, 0)
#End

#Read file
def readFile(fName):
    with open(fName, 'r') as f:
        lWords = []
        for line in f.readlines():
            lWords += line.split()
        print(lWords)
        return lWords
    
readFile('textTestFilePY.txt')
#End read file

#Write to file
def writeFile(lst, fle):
    theFile = open(fle, 'w')
    
    for element in lst:
        theFile.write(str(element))
        theFile.write('\n')
  
divList = ["AL East Standings:", "TB", "NYY", "BOS", "TOR", "BAL"]
writeFile(divList, 'writeToFile.txt')
#End Write to file

#Bank account class
class BankAccount:
    def __init__(self, accID, initialDeposit):
        self.id = accID
        self.balance = initialDeposit
        
    def bankDeposit(self, money):
        self.balance += money
        return self.balance
    
    def bankWithdrawal(self, money):
        self.balance -= money
        return self.balance
    
reiley = BankAccount(123, 700)
michelle = BankAccount(789, 500)

#add funds reiley
reiley.bankDeposit(300)
print("Your new balance is: ", reiley.balance, " Reiley.")

#Remove funds reiley
reiley.bankWithdrawal(200)
print("Your new balance is: ", reiley.balance, " Reiley.")

#add funds michelle
michelle.bankDeposit(200)
print("Your new balance is: ", michelle.balance, " Michelle.")

#Remove funds michelle
michelle.bankWithdrawal(125)
print("Your new balance is: ", michelle.balance, " Michelle.")  
#End bank class
#End File
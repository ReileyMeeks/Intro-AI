#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 11:59:45 2021

@author: ReileyMeeks
"""

class Agents :
    def __init__(self, name, environment, actuators, sensors, perfMet):
        self.name = name
        self.environment = environment
        self.actuators = actuators
        self.sensors = sensors
        self.perfMet = perfMet
    def printInfo(self):
        print("Name: ", self.name,
              "\nEnvironment: ", self.environment,
              "\nActuators: ", self.actuators,
              "\nSensors: ", self.sensors,
              "\nperfMet: ", self.perfMet, "\n")
        print('\n')
        
agent1 = Agents("Grammarly", "Text Editor", ["Displayed errors within text editor" , 
                                             "Text editor code"],
                ["Scanner"], ["Percentance of errors caught"])

agent2 = Agents("Roomba", "Indoor Flooring", ["Vacuum", "Mop"],
                ["Camera", "Infrared and Photocell sensors", "Bump sensors"], 
                ["Cleanliness of Floor"])

agent3 = Agents("Siri", "Phone", ["Speaker", "Display", "Device Actions"], 
                ["Microphone", "Siri Button", "Home button"],
                ["Accuracy of intended action", "Response Time", 
                 "Lack of 'Glitchs'"])

agent4 = Agents("Uno AI", "UNO Video Game", ["Display"], 
                ["Current card on table", "Current cards in hand", "User Input"], 
                ["Speed", "Difficulty"])

agent5 = Agents("Maze Solver", "Maze Application", ["Display", "Maze Generation"], 
                ["Directional Movement", "Maze Barriers"], 
                ["Maze Solvable", "Solve/Generation time"])

agent1.printInfo() #Grammarly
agent2.printInfo() #Roomba
agent3.printInfo() #Siri
agent4.printInfo() #Uno AI
agent5.printInfo() #Maze Solver

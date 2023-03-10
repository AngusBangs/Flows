import FlowGenerator
import os
from numpy import *
from PIL import Image
import scipy
import png
import numpy as np
from numpy import array
from scipy import misc
import math
import imageio
import inspect

def ciww1(PixelsY=200):
    Aspect_Ratio_Pixels=530.0/400.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=1.0                           
    Curve_Centre_X=float(Pixels_X*0.17)             
    Curve_Centre_Y=float(PixelsY*0.85)             
    Angle_Start_Curve1=150.0*3.14159265359/180.0        
    Angle_End_Curve1=280.0*2.0*3.14159265359/360.0     
    Radius_Curve1=8.0*Pixels_X/100                 
    Thickness_Curve1=float(5*Pixels_X/100)          #1/2 the width of curve 1
    Width_Growth_Curve1=0.0                         #Fraction multiplier to be applied, linearly as the angle increases from its initial to final value.          
    Aspect_Ratio_Curve1=1.0/1.0                     # x>1 if longer in Y direction

    #CURVE 2
    Anlge_End_Curve_Next=99.45*3.14159265359/180.0
    Radius_Curve_Next=6000.0*Pixels_X/100               
    Width_Growth_Curve_Next=-0.0                    #Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    Aspect_Ratio_Curve_Next=1.0/1.0                     # x>1 if longer in Y direction
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)

    #CURVE 3
    Curve_Centre_X, Curve_Centre_Y, Angle_Start_Curve1, Angle_End_Curve1, Radius_Curve1, Width_Growth_Curve1, Aspect_Ratio_Curve1, Last_Radius_Scale_Factor = list1
    Flow_Clockwise=Flow_Clockwise*-1.0
    Anlge_End_Curve_Next=340.0*3.14159265359/180.0
    Radius_Curve_Next=20.0*Pixels_X/100
    Width_Growth_Curve_Next=1.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)

    #CURVE 4
    Curve_Centre_X, Curve_Centre_Y, Angle_Start_Curve1, Angle_End_Curve1, Radius_Curve1, Width_Growth_Curve1, Aspect_Ratio_Curve1, Last_Radius_Scale_Factor = list1
    Flow_Clockwise=Flow_Clockwise*-1.0
    Anlge_End_Curve_Next=75.0*3.14159265359/180.0
    Radius_Curve_Next=6300.0*Pixels_X/100
    Width_Growth_Curve_Next=0.00
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0.75,0.07,0.1,0.04,60,1]
    Perpendicular_Flows.extend([0.85,0.22,0.1,0.055,60,2])
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])

def ciww2(PixelsY=200):
    Aspect_Ratio_Pixels=203.0/213.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1    
    Flow_Clockwise=-1.0
    Curve_Centre_X=float(Pixels_X*-2.5)
    Curve_Centre_Y=float(PixelsY*-9.95)
    Angle_Start_Curve1=359.0*3.14159265359/180.0   
    Angle_End_Curve1=3.0*2.0*3.14159265359/360.0
    Radius_Curve1=1040.0*Pixels_X/100
    Thickness_Curve1=float(30*Pixels_X/100)
    Width_Growth_Curve1=0.0      
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=96.4*3.14159265359/180.0
    Radius_Curve_Next=400.0*Pixels_X/100
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0.62,0.65,0.3,0.09,70,4]
    Perpendicular_Flows.extend([0.8,0.56,0.1,0.03,60,2])
    Perpendicular_Flows.extend([0.47,0.34,0.285,0.08,70.9,3])
    Perpendicular_Flows.extend([0.67,0.3,0.1,0.04,60,1])
    Perpendicular_Flows.extend([0.32,0.55,0.2,0.2,45,7])
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])
    
def ciww3(PixelsY=200):
    Aspect_Ratio_Pixels=203.0/213.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=-1.0
    Curve_Centre_X=float(Pixels_X*-4.0)
    Curve_Centre_Y=float(PixelsY*-9.25)
    Angle_Start_Curve1=359.0*3.14159265359/180.0      
    Angle_End_Curve1=10.0*2.0*3.14159265359/360.0
    Radius_Curve1=1040.0*Pixels_X/100
    Thickness_Curve1=float(24*Pixels_X/100)
    Width_Growth_Curve1=0.0         
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=96.4*3.14159265359/180.0
    Radius_Curve_Next=400.0*Pixels_X/100
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0.22,0.55,0.198,0.09,75,3]
    Perpendicular_Flows.extend([0.365,0.77,0.26,0.07,75,4])
    Perpendicular_Flows.extend([0.88,0.52,0.085,0.15,85,4])
    Perpendicular_Flows.extend([0.69,0.59,0.12,0.04,60,4])
    Perpendicular_Flows.extend([0.65,0.38,0.26,0.06,61,3])
    Perpendicular_Flows.extend([0.57,0.67,0.03,0.01,63,2])
    Perpendicular_Flows.extend([0.1,0.7,0.15,0.15,60,7])
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])

def ciww4(PixelsY=200):
    Aspect_Ratio_Pixels=203.0/213.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=-1.0
    Curve_Centre_X=float(Pixels_X*0.1)
    Curve_Centre_Y=float(PixelsY*0.24001)
    Angle_Start_Curve1=340.0*3.14159265359/180.0    
    Angle_End_Curve1=0.1*2.0*3.14159265359/360.0
    Radius_Curve1=52.0*Pixels_X/100
    Thickness_Curve1=float(30*Pixels_X/100)
    Width_Growth_Curve1=0.0        
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=65.4*3.14159265359/180.0
    Radius_Curve_Next=35.0*Pixels_X/100
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0.77,0.27,0.1,0.03,-15,2]
    Perpendicular_Flows.extend([0.7,0.17,0.02,0.01,-15,2])
    Perpendicular_Flows.extend([0.01,-0.09,20,7.5,145.25,5])
    Perpendicular_Flows.extend([0.06,0.26,47,9,132.110,6])
    Perpendicular_Flows.extend([0.47,0.24,0.02,0.02,-95,2])
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])


def ciww5(PixelsY=200):
    Aspect_Ratio_Pixels=203.0/213.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=-1.0
    Curve_Centre_X=float(Pixels_X*0.5)
    Curve_Centre_Y=float(PixelsY*0.8)
    Angle_Start_Curve1=90.0*3.14159265359/180.0
    Angle_End_Curve1=348.0*2.0*3.14159265359/360.0
    Radius_Curve1=34.0*Pixels_X/100#
    Thickness_Curve1=float(30*Pixels_X/100)
    Width_Growth_Curve1=0.2          
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=96.4*3.14159265359/180.0
    Radius_Curve_Next=4000.0*Pixels_X/100
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)

    #CURVE 3
    Curve_Centre_X, Curve_Centre_Y, Angle_Start_Curve1, Angle_End_Curve1, Radius_Curve1, Width_Growth_Curve1, Aspect_Ratio_Curve1, Last_Radius_Scale_Factor = list1
    Flow_Clockwise=Flow_Clockwise*-1.0
    Anlge_End_Curve_Next=340.0*3.14159265359/180.0
    Radius_Curve_Next=30.0*Pixels_X/100
    Width_Growth_Curve_Next=0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0.25,0.55,0.1,0.04,-110,1]
    Perpendicular_Flows.extend([0.08,0.25,0.1,0.06,-110,2])
    Perpendicular_Flows.extend([0.83,0.62,0.22,0.12,-20,4])
    Perpendicular_Flows.extend([0.35,0.89,60,9,28.100,6])
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])
        
def ciww6(PixelsY=200):
    Aspect_Ratio_Pixels=203.0/213.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=-1.0
    Curve_Centre_X=float(Pixels_X*0.9)
    Curve_Centre_Y=float(PixelsY*0.6)
    Angle_Start_Curve1=20.0*3.14159265359/180.0
    Angle_End_Curve1=330.0*2.0*3.14159265359/360.0
    Radius_Curve1=34.0*Pixels_X/100
    Thickness_Curve1=float(18*Pixels_X/100)
    Width_Growth_Curve1=0.2        
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=96.4*3.14159265359/180.0
    Radius_Curve_Next=400.0*Pixels_X/100
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)

    #CURVE 3
    Curve_Centre_X, Curve_Centre_Y, Angle_Start_Curve1, Angle_End_Curve1, Radius_Curve1, Width_Growth_Curve1, Aspect_Ratio_Curve1, Last_Radius_Scale_Factor = list1
    Flow_Clockwise=Flow_Clockwise*-1.0
    Anlge_End_Curve_Next=340.0*3.14159265359/180.0
    Radius_Curve_Next=30.0*Pixels_X/100
    Width_Growth_Curve_Next=0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0.64,0.19,0.21,0.06,-110,4]
    Perpendicular_Flows.extend([0.27,0.41,0.21,0.035,-115,4])
    Perpendicular_Flows.extend([0.75,0.4,0.21,0.05,-130,3])
    Perpendicular_Flows.extend([0.35,0.62,0.24,0.065,-110,3])
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])
        
def ciww7(PixelsY=200):
    Aspect_Ratio_Pixels=203.0/213.0  
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=-1.0                   
    Curve_Centre_X=float(Pixels_X*0.9)
    Curve_Centre_Y=float(PixelsY*0.75)
    Angle_Start_Curve1=20.0*3.14159265359/180.0  
    Angle_End_Curve1=330.0*2.0*3.14159265359/360.0
    Radius_Curve1=34.0*Pixels_X/100
    Thickness_Curve1=float(18*Pixels_X/100)
    Width_Growth_Curve1=0.2       
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=96.4*3.14159265359/180.0
    Radius_Curve_Next=400.0*Pixels_X/100
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)

    #CURVE 3
    Curve_Centre_X, Curve_Centre_Y, Angle_Start_Curve1, Angle_End_Curve1, Radius_Curve1, Width_Growth_Curve1, Aspect_Ratio_Curve1, Last_Radius_Scale_Factor = list1
    Flow_Clockwise=Flow_Clockwise*-1.0
    Anlge_End_Curve_Next=340.0*3.14159265359/180.0
    Radius_Curve_Next=30.0*Pixels_X/100
    Width_Growth_Curve_Next=0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0.58,0.635,0.35,0.075,-117,3]
    Perpendicular_Flows.extend([0.44,0.77,0.2,0.04,-110,1])
    Perpendicular_Flows.extend([0.57,0.41,0.37,0.075,-117,4])
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])
        
def ciww8(PixelsY=200):
    Aspect_Ratio_Pixels=203.0/213.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=-1.0
    Curve_Centre_X=float(Pixels_X*0.9)
    Curve_Centre_Y=float(PixelsY*0.7)
    Angle_Start_Curve1=20.0*3.14159265359/180.0
    Angle_End_Curve1=335.0*2.0*3.14159265359/360.0
    Radius_Curve1=34.0*Pixels_X/100
    Thickness_Curve1=float(24*Pixels_X/100)
    Width_Growth_Curve1=0.2        
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=96.4*3.14159265359/180.0
    Radius_Curve_Next=400.0*Pixels_X/100
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)

    #CURVE 3
    Curve_Centre_X, Curve_Centre_Y, Angle_Start_Curve1, Angle_End_Curve1, Radius_Curve1, Width_Growth_Curve1, Aspect_Ratio_Curve1, Last_Radius_Scale_Factor = list1
    Flow_Clockwise=Flow_Clockwise*-1.0
    Anlge_End_Curve_Next=340.0*3.14159265359/180.0
    Radius_Curve_Next=30.0*Pixels_X/100
    Width_Growth_Curve_Next=0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0.46,0.37,0.37,0.138,-100,4]
    Perpendicular_Flows.extend([0.24,0.36,0.2,0.06,-110,2])
    Perpendicular_Flows.extend([0.51,0.62,0.37,0.09,-107,3])
    Perpendicular_Flows.extend([0.25,0.7,0.03,0.02,-100,1])
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])
        
def ciww9(PixelsY=200):
    Aspect_Ratio_Pixels=203.0/213.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=-1.0
    Curve_Centre_X=float(Pixels_X*1.1)
    Curve_Centre_Y=float(PixelsY*1.23)
    Angle_Start_Curve1=350.0*3.14159265359/180.0
    Angle_End_Curve1=300.0*2.0*3.14159265359/360.0
    Radius_Curve1=90.0*Pixels_X/100
    Thickness_Curve1=float(28*Pixels_X/100)
    Width_Growth_Curve1=0.2
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=96.4*3.14159265359/180.0
    Radius_Curve_Next=400.0*Pixels_X/100
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)

    #CURVE 3
    Curve_Centre_X, Curve_Centre_Y, Angle_Start_Curve1, Angle_End_Curve1, Radius_Curve1, Width_Growth_Curve1, Aspect_Ratio_Curve1, Last_Radius_Scale_Factor = list1
    Flow_Clockwise=Flow_Clockwise*-1.0
    Anlge_End_Curve_Next=340.0*3.14159265359/180.0
    Radius_Curve_Next=30.0*Pixels_X/100
    Width_Growth_Curve_Next=0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0.69,0.45,0.2,0.05,-114,3]
    Perpendicular_Flows.extend([0.56,0.53,0.05,0.025,-112,1])
    Perpendicular_Flows.extend([0.62,0.24,0.21,0.05,-114,4])
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])
        
def ciww10(PixelsY=200):
    Aspect_Ratio_Pixels=203.0/213.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=-1.0
    Curve_Centre_X=float(Pixels_X*2.0)
    Curve_Centre_Y=float(PixelsY*0.3)
    Angle_Start_Curve1=320.0*3.14159265359/180.0
    Angle_End_Curve1=25.0*2.0*3.14159265359/360.0
    Radius_Curve1=160.0*Pixels_X/100
    Thickness_Curve1=float(29*Pixels_X/100)
    Width_Growth_Curve1=0.2   
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=96.4*3.14159265359/180.0
    Radius_Curve_Next=400.0*Pixels_X/100
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)

    #CURVE 3
    Curve_Centre_X, Curve_Centre_Y, Angle_Start_Curve1, Angle_End_Curve1, Radius_Curve1, Width_Growth_Curve1, Aspect_Ratio_Curve1, Last_Radius_Scale_Factor = list1
    Flow_Clockwise=Flow_Clockwise*-1.0
    Anlge_End_Curve_Next=340.0*3.14159265359/180.0
    Radius_Curve_Next=30.0*Pixels_X/100
    Width_Growth_Curve_Next=0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])
        
def ciww11(PixelsY=200):
    Aspect_Ratio_Pixels=203.0/213.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=-1.0
    Curve_Centre_X=float(Pixels_X*2.3)
    Curve_Centre_Y=float(PixelsY*0.3)
    Angle_Start_Curve1=320.0*3.14159265359/180.0         
    Angle_End_Curve1=25.0*2.0*3.14159265359/360.0
    Radius_Curve1=182.0*Pixels_X/100
    Thickness_Curve1=float(26*Pixels_X/100)
    Width_Growth_Curve1=0.2
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=96.4*3.14159265359/180.0
    Radius_Curve_Next=400.0*Pixels_X/100
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)

    #CURVE 3
    Curve_Centre_X, Curve_Centre_Y, Angle_Start_Curve1, Angle_End_Curve1, Radius_Curve1, Width_Growth_Curve1, Aspect_Ratio_Curve1, Last_Radius_Scale_Factor = list1
    Flow_Clockwise=Flow_Clockwise*-1.0
    Anlge_End_Curve_Next=340.0*3.14159265359/180.0
    Radius_Curve_Next=30.0*Pixels_X/100
    Width_Growth_Curve_Next=0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])
        
def ciww12(PixelsY=200):
    Aspect_Ratio_Pixels=203.0/213.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=-1.0
    Curve_Centre_X=float(Pixels_X*1.75)
    Curve_Centre_Y=float(PixelsY*0.3)
    Angle_Start_Curve1=320.0*3.14159265359/180.0            
    Angle_End_Curve1=200.0*2.0*3.14159265359/360.0
    Radius_Curve1=160.0*Pixels_X/100
    Thickness_Curve1=float(6*Pixels_X/100)
    Width_Growth_Curve1=0.2         
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=96.4*3.14159265359/180.0
    Radius_Curve_Next=40.0*Pixels_X/100
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)

    #CURVE 3
    Curve_Centre_X, Curve_Centre_Y, Angle_Start_Curve1, Angle_End_Curve1, Radius_Curve1, Width_Growth_Curve1, Aspect_Ratio_Curve1, Last_Radius_Scale_Factor = list1
    Flow_Clockwise=Flow_Clockwise*-1.0
    Anlge_End_Curve_Next=340.0*3.14159265359/180.0
    Radius_Curve_Next=30.0*Pixels_X/100
    Width_Growth_Curve_Next=0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])
        
def ciww13(PixelsY=200):
    Aspect_Ratio_Pixels=203.0/213.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=-1.0
    Curve_Centre_X=float(Pixels_X*9999.9)
    Curve_Centre_Y=float(PixelsY*9999.65)
    Angle_Start_Curve1=20.0*3.14159265359/180.0
    Angle_End_Curve1=325.0*2.0*3.14159265359/360.0
    Radius_Curve1=34.0*Pixels_X/100
    Thickness_Curve1=float(8*Pixels_X/100)
    Width_Growth_Curve1=0.2       
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=96.4*3.14159265359/180.0
    Radius_Curve_Next=400.0*Pixels_X/100
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)

    #CURVE 3
    Curve_Centre_X, Curve_Centre_Y, Angle_Start_Curve1, Angle_End_Curve1, Radius_Curve1, Width_Growth_Curve1, Aspect_Ratio_Curve1, Last_Radius_Scale_Factor = list1
    Flow_Clockwise=Flow_Clockwise*-1.0
    Anlge_End_Curve_Next=340.0*3.14159265359/180.0
    Radius_Curve_Next=30.0*Pixels_X/100
    Width_Growth_Curve_Next=0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])

def testcurve(PixelsY=200):
    Aspect_Ratio_Pixels=963.0/2098.0
    Master_Speed=100.0
    Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows=FlowGenerator.declarations(PixelsY,Aspect_Ratio_Pixels)

    #CURVE 1
    Flow_Clockwise=1.0
    Curve_Centre_X=float(Pixels_X*1.5)
    Curve_Centre_Y=float(PixelsY*0.5)
    Angle_Start_Curve1=91.0*3.14159265359/180.0   
    Angle_End_Curve1=60.0*3.0*3.14159265359/360.0
    Radius_Curve1=100.0*Pixels_X/100
    Thickness_Curve1=float(30*Pixels_X/100)
    Width_Growth_Curve1=0.0
    Aspect_Ratio_Curve1=1.0/1.0

    #CURVE 2
    Anlge_End_Curve_Next=225.4*3.14159265359/180.0
    Radius_Curve_Next=4.0*Pixels_X/100               
    Width_Growth_Curve_Next=-0.0
    Aspect_Ratio_Curve_Next=1.0/1.0
    Perpendicular_Flows=[0,0]
    list1=FlowGenerator.Generate(Aspect_Ratio_Pixels,PixelsY,Flow_Clockwise,Curve_Centre_X,Curve_Centre_Y,Angle_Start_Curve1,Angle_End_Curve1,Radius_Curve1,Thickness_Curve1,Width_Growth_Curve1,Aspect_Ratio_Curve1,Anlge_End_Curve_Next,Radius_Curve_Next,Width_Growth_Curve_Next,Aspect_Ratio_Curve_Next,Last_Radius_Scale_Factor,Perpendicular_Flows,Master_Speed,Velocity_X,Velocity_Y,Foam)
    FlowGenerator.SaveResult(PixelsY,Pixels_X,Velocity_X,Velocity_Y,Foam,inspect.stack()[0][3])  

ciww1()
ciww2()
ciww3()
ciww4()
ciww5()
ciww6()
ciww7()
ciww8()
ciww9()
ciww10()
ciww11()
ciww12()
ciww13()
testcurve()
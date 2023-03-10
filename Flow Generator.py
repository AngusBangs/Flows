import os
from numpy import *
from PIL import Image
#from scipy import ndimage
import scipy
import png
import numpy as np
from numpy import array
from scipy import misc
import math
import imageio

def main():
    print('started')

list='helloworld'
AspectRatio=530.0/400#                          How many times longer it is than it is wide
PixelsY=200#                            How many pixels down (determines pixels across too as pixels will always be square)
PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.


def ciww1():
    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    AspectRatio=530.0/400.0
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*0.17)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*0.85)#                         Y coordinates of centre of first curve
    theta0=150.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=280.0*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=8.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(5*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.0#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=99.45*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=6000.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)

    #CURVE 3
    
    Clockwise=Clockwise*-1.0
    CentreX=list1[0]
    CentreY=-list1[1]
    theta0=list1[2]
    theta=list1[3]
    Radius1=list1[4]
    Radius1Diff=list1[5]
    RadiusScale=list1[6]
    ScaleY=list1[7]
    RadiusScaleFactorOld=list1[8]

    theta5=340.0*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=20.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=1.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)

    #CURVE 4

    Clockwise=Clockwise*-1.0
    CentreX=list1[0]
    CentreY=-list1[1]
    theta0=list1[2]
    theta=list1[3]
    Radius1=list1[4]
    Radius1Diff=list1[5]
    RadiusScale=list1[6]
    ScaleY=list1[7]
    RadiusScaleFactorOld=list1[8]

    theta5=75.0*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=6300.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=0.00#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0.75,0.07,0.1,0.04,60,1]
    SideFlows.extend([0.85,0.22,0.1,0.055,60,2])
    #SideFlows.extend([0.25,0.3,35,05,305.2,5])
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)

    print('saving 1')
    x=(x+1000*255/1000)
    #x = round(x*255/)
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww1x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww1y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww1w.png', w)# uses the Image module (PIL)

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Unreal Stuff\FlowMaps\Cardiff1.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")
    
    print(PixelsX)
    print(PixelsY)

def ciww2():
    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    global w
    
    AspectRatio=203.0/213.0
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=-1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*-2.5)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*-9.95)#                         Y coordinates of centre of first curve
    theta0=359.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=3.0*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=1040.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(30*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.0#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=96.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=400.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    #SideFlows=[0.8,0.56,0.1,0.04,60,2]
    SideFlows=[0.62,0.65,0.3,0.09,70,4]
    SideFlows.extend([0.8,0.56,0.1,0.03,60,2])
    SideFlows.extend([0.47,0.34,0.285,0.08,70.9,3])
    SideFlows.extend([0.67,0.3,0.1,0.04,60,1])
    SideFlows.extend([0.32,0.55,0.2,0.2,45,7])
    #SideFlows.extend([0.5,0.5,0.2,0.2,60,7])
    #SideFlows.extend([0.5,0.1,35,5,160.99,5])
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww2x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww2y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww2w.png', w)# uses the Image module (PIL)

    #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Cardiff2.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")
    
def ciww3():
    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    global w
    
    AspectRatio=203.0/213.0
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=-1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*-4.0)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*-9.25)#                         Y coordinates of centre of first curve
    theta0=359.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=10.0*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=1040.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(24*PixelsX/100)#        1/2 the width of curve 1
    #RadiusDiff1=float(120*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.0#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=96.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=400.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0.22,0.55,0.198,0.09,75,3]
    SideFlows.extend([0.365,0.77,0.26,0.07,75,4])
    SideFlows.extend([0.88,0.52,0.085,0.15,85,4])
    SideFlows.extend([0.69,0.59,0.12,0.04,60,4])
    SideFlows.extend([0.65,0.38,0.26,0.06,61,3])
    #SideFlows.extend([0.39,0.51,0.02,0.015,75,1])
    #SideFlows.extend([0.2,0.55,0.285,0.08,75,3])
    #SideFlows.extend([0.77,0.255,0.1,0.03,70,1])
    SideFlows.extend([0.57,0.67,0.03,0.01,63,2])
    #SideFlows.extend([0.73,0.6,0.1,0.05,63,2])
    #SideFlows.extend([0.89,0.6,0.1,0.05,63,2])
    
    SideFlows.extend([0.1,0.7,0.15,0.15,60,7])
    
    print(SideFlows)
    #SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)

    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww3x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww3y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww3w.png', w)# uses the Image module (PIL)
    #print('yes')

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Cardiff3.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")

def ciww4():
    
    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    
    AspectRatio=203.0/213.0
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=-1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*0.1)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*0.24001)#                         Y coordinates of centre of first curve
    theta0=340.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=0.1*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=52.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(30*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.0#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=65.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=35.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0.77,0.27,0.1,0.03,-15,2]
    SideFlows.extend([0.7,0.17,0.02,0.01,-15,2])
    SideFlows.extend([0.01,-0.09,20,7.5,145.25,5])#145.25/PixelsX
    SideFlows.extend([0.06,0.26,47,9,132.110,6])#132.110/PixelsX
    SideFlows.extend([0.47,0.24,0.02,0.02,-95,2])
    #NoFlow=[0.75,0.17,0.05,0.05]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)
    
    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww4x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww4y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww4w.png', w)# uses the Image module (PIL)

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Cardiff4.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")


def ciww5():

    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    AspectRatio=203.0/213.0
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=-1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*0.5)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*0.8)#                         Y coordinates of centre of first curve
    theta0=90.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=348.0*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=34.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(30*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.2#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=96.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=4000.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


     #CURVE 3
    
    Clockwise=Clockwise*-1.0
    CentreX=list1[0]
    CentreY=-list1[1]
    theta0=list1[2]
    theta=list1[3]
    Radius1=list1[4]
    Radius1Diff=list1[5]
    RadiusScale=list1[6]
    ScaleY=list1[7]
    RadiusScaleFactorOld=list1[8]

    theta5=340.0*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=30.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0.25,0.55,0.1,0.04,-110,1]
    SideFlows.extend([0.08,0.25,0.1,0.06,-110,2])
    SideFlows.extend([0.83,0.62,0.22,0.12,-20,4])
    SideFlows.extend([0.35,0.89,60,9,28.100,6])#28.100/PixelsX
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww5x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww5y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww5w.png', w)# uses the Image module (PIL)

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Cardiff5.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")
        
def ciww6():

    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    AspectRatio=203.0/213.0
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=-1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*0.9)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*0.6)#                         Y coordinates of centre of first curve
    theta0=20.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=330.0*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=34.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(18*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.2#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=96.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=400.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


     #CURVE 3
    
    Clockwise=Clockwise*-1.0
    CentreX=list1[0]
    CentreY=-list1[1]
    theta0=list1[2]
    theta=list1[3]
    Radius1=list1[4]
    Radius1Diff=list1[5]
    RadiusScale=list1[6]
    ScaleY=list1[7]
    RadiusScaleFactorOld=list1[8]

    theta5=340.0*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=30.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    #SideFlows=[0.27,0.68,0.2,0.04,-110,1]
    #SideFlows.extend([0.14,0.47,0.2,0.04,-110,2])
    #SideFlows.extend([0.48,0.26,0.05,0.03,-115,2])
    #SideFlows.extend([0.64,0.53,0.07,0.03,-115,1])
    SideFlows=[0.64,0.19,0.21,0.06,-110,4]
    #SideFlows.extend([0.64,0.19,0.21,0.06,-110,4])
    SideFlows.extend([0.27,0.41,0.21,0.035,-115,4])
    SideFlows.extend([0.75,0.4,0.21,0.05,-130,3])
    SideFlows.extend([0.35,0.62,0.24,0.065,-110,3])
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww6x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww6y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww6w.png', w)# uses the Image module (PIL)

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Cardiff6.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")
        
def ciww7():
    
    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    AspectRatio=203.0/213.0                      #How many pixels down (determines pixels across too as pixels will always be square)
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=-1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*0.9)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*0.75)#                         Y coordinates of centre of first curve
    theta0=20.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=330.0*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=34.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(18*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.2#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=96.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=400.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


     #CURVE 3
    
    Clockwise=Clockwise*-1.0
    CentreX=list1[0]
    CentreY=-list1[1]
    theta0=list1[2]
    theta=list1[3]
    Radius1=list1[4]
    Radius1Diff=list1[5]
    RadiusScale=list1[6]
    ScaleY=list1[7]
    RadiusScaleFactorOld=list1[8]

    theta5=340.0*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=30.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    #SideFlows=[0.44,0.77,0.2,0.04,-110,1]
    SideFlows=[0.58,0.635,0.35,0.075,-117,3]
    SideFlows.extend([0.44,0.77,0.2,0.04,-110,1])
    #SideFlows.extend([0.395,0.47,0.2,0.04,-110,2])
    SideFlows.extend([0.57,0.41,0.37,0.075,-117,4])
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww7x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww7y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww7w.png', w)# uses the Image module (PIL)

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Cardiff7.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")
        
def ciww8():
    
    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    AspectRatio=203.0/213.0
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=-1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*0.9)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*0.7)#                         Y coordinates of centre of first curve
    theta0=20.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=335.0*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=34.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(24*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.2#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=96.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=400.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


     #CURVE 3
    
    Clockwise=Clockwise*-1.0
    CentreX=list1[0]
    CentreY=-list1[1]
    theta0=list1[2]
    theta=list1[3]
    Radius1=list1[4]
    Radius1Diff=list1[5]
    RadiusScale=list1[6]
    ScaleY=list1[7]
    RadiusScaleFactorOld=list1[8]

    theta5=340.0*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=30.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    #SideFlows=[0.25,0.72,0.1,0.04,-112,1]
    SideFlows=[0.46,0.37,0.37,0.138,-100,4]
    #SideFlows.extend([0.46,0.37,0.37,0.138,-100,4])
    SideFlows.extend([0.24,0.36,0.2,0.06,-110,2])
    SideFlows.extend([0.51,0.62,0.37,0.09,-107,3])
    SideFlows.extend([0.25,0.7,0.03,0.02,-100,1])
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww8x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww8y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww8w.png', w)# uses the Image module (PIL)

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Cardiff8.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")
        
def ciww9():
    
    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    AspectRatio=203.0/213.0
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=-1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*1.1)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*1.23)#                         Y coordinates of centre of first curve
    theta0=350.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=300.0*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=90.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(28*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.2#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=96.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=400.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


     #CURVE 3
    
    Clockwise=Clockwise*-1.0
    CentreX=list1[0]
    CentreY=-list1[1]
    theta0=list1[2]
    theta=list1[3]
    Radius1=list1[4]
    Radius1Diff=list1[5]
    RadiusScale=list1[6]
    ScaleY=list1[7]
    RadiusScaleFactorOld=list1[8]

    theta5=340.0*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=30.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    #SideFlows=[0.6,0.5,0.1,0.025,-112,1]
    #SideFlows.extend([0.51,0.3,0.1,0.045,-110,2])
    #SideFlows.extend([0.08,0.73,0.1,0.045,-150,2])
    #SideFlows.extend([0.27,0.82,0.06,0.03,-170,1])
    SideFlows=[0.69,0.45,0.2,0.05,-114,3]
    SideFlows.extend([0.56,0.53,0.05,0.025,-112,1])
    SideFlows.extend([0.62,0.24,0.21,0.05,-114,4])
    #SideFlows.extend([0.76,0.43,0.18,0.05,-114,3])
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww9x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww9y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww9w.png', w)# uses the Image module (PIL)

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Cardiff9.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")
        
def ciww10():
    
    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    AspectRatio=203.0/213.0
    ixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=-1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*2.0)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*0.3)#                         Y coordinates of centre of first curve
    theta0=320.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=25.0*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=160.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(29*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.2#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=96.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=400.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


     #CURVE 3
    
    Clockwise=Clockwise*-1.0
    CentreX=list1[0]
    CentreY=-list1[1]
    theta0=list1[2]
    theta=list1[3]
    Radius1=list1[4]
    Radius1Diff=list1[5]
    RadiusScale=list1[6]
    ScaleY=list1[7]
    RadiusScaleFactorOld=list1[8]

    theta5=340.0*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=30.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww10x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww10y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww10w.png', w)# uses the Image module (PIL)

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Cardiff10.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")
        
def ciww11():
    
    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    AspectRatio=203.0/213.0
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=-1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*2.3)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*0.3)#                         Y coordinates of centre of first curve
    theta0=320.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=25.0*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=182.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(26*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.2#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=96.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=400.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


     #CURVE 3
    
    Clockwise=Clockwise*-1.0
    CentreX=list1[0]
    CentreY=-list1[1]
    theta0=list1[2]
    theta=list1[3]
    Radius1=list1[4]
    Radius1Diff=list1[5]
    RadiusScale=list1[6]
    ScaleY=list1[7]
    RadiusScaleFactorOld=list1[8]

    theta5=340.0*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=30.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww11x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww11y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww11w.png', w)# uses the Image module (PIL)

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Cardiff11.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")
        
def ciww12():
    
    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    AspectRatio=203.0/213.0
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=-1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*1.75)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*0.3)#                         Y coordinates of centre of first curve
    theta0=320.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=200.0*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=160.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(6*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.2#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2
    theta5=96.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=40.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


     #CURVE 3
    
    Clockwise=Clockwise*-1.0
    CentreX=list1[0]
    CentreY=-list1[1]
    theta0=list1[2]
    theta=list1[3]
    Radius1=list1[4]
    Radius1Diff=list1[5]
    RadiusScale=list1[6]
    ScaleY=list1[7]
    RadiusScaleFactorOld=list1[8]

    theta5=340.0*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=30.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww12x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww12y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww12w.png', w)# uses the Image module (PIL)

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Cardiff12.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")
        
def ciww13():
    
    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    AspectRatio=203.0/213.0
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    RadiusScaleFactorOld=1
    MasterSpeed=100.0

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=-1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    CentreX=float(PixelsX*9999.9)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*9999.65)#                         Y coordinates of centre of first curve
    theta0=20.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=325.0*2.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    Radius1=34.0*PixelsX/100#53           Radius of curve 1
    RadiusDiff1=float(8*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.2#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=96.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=400.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


     #CURVE 3
    
    Clockwise=Clockwise*-1.0
    CentreX=list1[0]
    CentreY=-list1[1]
    theta0=list1[2]
    theta=list1[3]
    Radius1=list1[4]
    Radius1Diff=list1[5]
    RadiusScale=list1[6]
    ScaleY=list1[7]
    RadiusScaleFactorOld=list1[8]

    theta5=340.0*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=30.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww13x.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww13y.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\ciww13w.png', w)# uses the Image module (PIL)

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('Cardiff13.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")

def testcurve():
    
    global PixelsX#                       How many times longer it is than it is wide
    global PixelsY#                            How many pixels down (determines pixels across too as pixels will always be square)
    global AspectRatio
    global x
    global y
    #AspectRatio=963.0/1049.0
    AspectRatio=963.0/2098.0
    PixelsY=100#                            How many pixels down (determines pixels across too as pixels will always be square)
    PixelsX=int(round(PixelsY/AspectRatio,0))#How many pixels across
    y=array([[0.0] * PixelsX] * PixelsY) #Array to represent velocity from top to bottom. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    x=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.
    w=array([[0.0] * PixelsX] * PixelsY) #Array to repreent velocity from left to right. Bottom to top is increase in direction 2, left to right is increase in direction 1.

    MasterSpeed=100.0
    
    RadiusScaleFactorOld=1

    print(PixelsX)
    print(PixelsY)

    #CURVE 1
    
    Clockwise=1.0#                          Whether the 1st curve flows clockwise or anticlockwise
    #CentreX=float(PixelsX*0.5)#PixelsX                  X coordinates of centre of first curve
    #CentreY=float(PixelsY*4.5)#                         Y coordinates of centre of first curve
    CentreX=float(PixelsX*1.5)#PixelsX                  X coordinates of centre of first curve
    CentreY=float(PixelsY*0.5)#                         Y coordinates of centre of first curve

    #CentreY=float(PixelsY*0.5)#                         Y coordinates of centre of first curve
    #CentreX=float(PixelsX*0.5)#PixelsX                  X coordinates of centre of first curve
    
    theta0=91.0*3.14159265359/180.0            #Angle at start of 1st curve
    theta=60.0*3.0*3.14159265359/360.0#74         Angle at end of curve 1 and start of curve 2
    #Radius1=200.0*PixelsX/100#53           Radius of curve 1
    Radius1=100.0*PixelsX/100#53           Radius of curve 1
    #Radius1=30.0*PixelsX/100#53           Radius of curve 1

    RadiusDiff1=float(30*PixelsX/100)#        1/2 the width of curve 1
    RadiusScale=0.0#                      Fraction multiplier to be applied to width of curve 1, linearly as the angle increases from its initial to final value.          
    ScaleY=1.0/1.0#                        How much longer curve 1 is than wide

    #CURVE 2

    theta5=225.4*3.14159265359/180.0#       Angle at end of curve 2
    Radius2=4.0*PixelsX/100#                Radius of curve 2
    RadiusScale2=-0.0#                      Fraction multiplier to be applied to width of curve 2, linearly as the angle increases from its initial to final value.
    ScaleY2=1.0/1.0#                        How much longer curve 2 is than wide
    SideFlows=[0,0]
    list1=b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed)


    print('saving 1')
    imageio.imwrite('Unreal Stuff\FlowMaps\testcurvex.png', x)# uses the Image module (PIL)
    print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\testcurvey.png', y)# uses the Image module (PIL)
    print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\testcurvew.png', w)# uses the Image module (PIL)

        #Writes array of locations
    A='NewRow,"('
    for i in range (PixelsY-1,-1,-1):
        for j in range (0,PixelsX):
            A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
    A=A[0:len(A)-1] +')"'
    print('saving 3')
    with open('TechDemo.csv', 'w') as wf:
        wf.write('---,Cardiff1,Cardiff1Size\n')
        wf.write(A)
        wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")
        

def b(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed):
    global x
    global y
    global w
    #MasterSpeed=100.0
    
    PixelsX=int(round(PixelsY/AspectRatio,0))
    CentreXZero=CentreX#                    Records initial/old CentreX value for when CetreX becomes CentreX2
    CentreYZero=CentreY#                    Records initial/old CentreY value for when CetreY becomes CentreY2

    if theta>=3.14159265359*1.5:
        theta6=3.14159265359*2.0-theta
        Quad=4
    elif theta>=3.14159265359:
        theta6=3.14159265359*1.5-theta
        Quad=3
    elif theta>=3.14159265359*0.5:
        theta6=3.14159265359-theta
        Quad=2
    else:
        theta6=3.14159265359*0.5-theta
        Quad=1

    theta4=theta6

    if (theta>=theta0 and Clockwise==1) or (theta<=theta0 and Clockwise==-1):
        Overlap=0.0
    else:
        Overlap=1.0
    
    jfactor=-1.0#Wheher X values of curve 1 are less than or more than the CentreX
    ifactor=1.0#Wheher Y values of curve 2 are less than or more than the CentreY
    ifactor2=1.0#Wheher X values of curve 2 are less than or more than the CentreX
    
    theta2=0.5*3.14159265359-theta4#180-theta
   
    for i in range (0,PixelsY):#Each Row         
        for j in range (0,PixelsX):#Each Column
            if i-CentreY==0:
                angzero=1.5*3.14159265359
            else:
                angzero=arctan((CentreX+j*jfactor)/(i-CentreY))#True angle of position from centre of curve
                if CentreXZero-j>=0 and CentreY-i<=0:
                    angzero=3.14159265359+angzero
                elif CentreXZero-j<=0 and abs(CentreY)-i<=0:
                    angzero=3.14159265359+angzero
                elif CentreXZero-j<=0 and abs(CentreY)-i>=0:
                    if angzero<0:
                        angzero=3.14159265359+angzero
                else:
                    angzero=2*3.14159265359+angzero

            if Clockwise==1:
                if theta0<theta:
                    theta8=theta-theta0
                    theta9=angzero-theta0
                else:
                    theta8=2*3.14-(theta0-theta)
                    if angzero<theta:
                        theta9=angzero+2*3.14-theta0
                    else:
                        theta9=angzero-theta0
            else:
                if theta5<theta0:
                    theta8=theta0-theta
                    theta9=theta0-angzero
                else:
                    theta8=2*3.14-(theta-theta0)
                    if angzero>theta:
                        theta9=2*3.14-angzero+theta0
                    else:
                        theta9=theta0-angzero         
            RadiusScaleFactor=RadiusScaleFactorOld*(1+RadiusScale*(theta9/theta8))            

            #RadiusScaleFactor=1+RadiusScale*(0.5*3.14159265359-angzero)/theta#changes curve width linearly with angle from 0 to end of curve
            PresRad=(((((CentreX+j*jfactor))**2+((i-CentreY)*ScaleY)**2)**0.5)-(Radius1-RadiusDiff1*RadiusScaleFactor))*0.5/(RadiusDiff1*RadiusScaleFactor)#Calculates radius normalised by width - 0-1 is inside width of curve increasing linearly


            #PRESRAD -1 to 2 for backflow
            if PresRad>0 and PresRad<1 and (Clockwise==1 and((theta0<theta and angzero>=theta0 and angzero<=theta)or(theta<theta0 and (angzero>=theta0 or angzero<=theta))) or (Clockwise==-1 and((theta0<theta and (angzero<=theta0 or angzero>=theta))or(theta<theta0 and angzero<=theta0 and angzero>=theta)))):

                if CentreY-i==0:
                    ang=1.5*3.14
                else:
                    dydx=(-(CentreX+j*jfactor))/((ScaleY**2.0)*(CentreY-i))#dydx of tangent of curve at point
                    ang=arctan(dydx)#Angle normalised for scaling - direction water should be flowing in
                    if CentreXZero-j>=0 and CentreY-i<=0:
                        ang=3.14+ang
                    elif CentreXZero-j<=0 and abs(CentreY)-i<=0:
                        ang=3.14+ang
                    elif CentreXZero-j<=0 and abs(CentreY)-i>=0:
                        ang=ang
                    else:
                        ang=2*3.14+ang
                    
                #y[i,j]=Clockwise*1000.0*(min(sin(PresRad*3.14159)*1.25,1))*sin(angzero)#Set Velocity based on angle
                #x[i,j]=Clockwise*1000.0*(min(sin(PresRad*3.14159)*1.25,1))*cos(angzero)#Set Yvelocity based on angle
                y[i,j]=Clockwise*MasterSpeed*sin(angzero)#Set Velocity based on angle
                x[i,j]=Clockwise*MasterSpeed*cos(angzero)#Set Yvelocity based on angle
    
    #Sets centre of second curve such that curves meet tangents
    rx1=Radius1
    ry1=Radius1/ScaleY
    px=CentreX
    py=CentreY
    ScaleYF=1/ScaleY
    dx1=Radius1*ScaleYF / ( ( ScaleYF**2+(tan(theta4))**2 ) **0.5)
    dy1=dx1*tan(theta4)
    dydx=((((ScaleY)/(ScaleY2))**2)*(dy1)/(dx1))
    theta3=arctan(dydx)
    ScaleYF2=1/ScaleY2 
    dx2=(Radius2)*ScaleYF2 / ( ( ScaleYF2**2+(tan(theta3))**2 ) **0.5)
    dy2=dx2*tan(theta3)
    dx=dx1+dx2
    dy=dy1+dy2
    
    CentreX2=px-dx
    CentreY2=-py-dy
    
    if theta<3.14/2:
        CentreX3=px+dx
        CentreY3=-py+dy
    elif theta<3.14:
        CentreX3=px+dy
        CentreY3=-py-dx
    elif theta<3.14*1.5:
        CentreX3=CentreX2
        CentreY3=CentreY2
    else:
        CentreX3=px-dy
        CentreY3=-py+dx

    #Sets radius of new curve such that it meets existing curve
    m=-tan(theta4)
    c=py-px*m
    ax=(m*ScaleY)**2+1.0
    bx=2.0*m*(c-CentreY)*(ScaleY**2.0)-2*CentreX
    cx1=((c-CentreY)**2)*(ScaleY**2)+(CentreX)**2-(Radius1-RadiusDiff1)**2
    cx2=((c-CentreY)**2)*(ScaleY**2)+(CentreX)**2-(Radius1+RadiusDiff1)**2
    x1=(-bx-(bx**2-4*ax*cx1)**0.5)/(2*ax)
    y1=m*x1+c
    x2=(-bx-(bx**2-4*ax*cx2)**0.5)/(2*ax)
    y2=m*x2+c
    rs2=(((x2+CentreX2*jfactor))**2+((y2+CentreY2)*ScaleY2)**2)**0.5
    rl2=(((x1+CentreX2*jfactor))**2+((y1+CentreY2)*ScaleY2)**2)**0.5
    RadiusS2 = rs2
    RadiusL2 = rl2

    #Set new values
    CentreX=CentreX3
    CentreY=CentreY3
    RadiusS=RadiusS2
    RadiusL=RadiusL2  
    ScaleY0=ScaleY   
    ScaleY=ScaleY2
    Radius2=(RadiusS+RadiusL)/2
    RadiusDiff2=(RadiusL-RadiusS)/2
    RadiusScaleFactorOld=RadiusScaleFactorOld*(1+RadiusScale)

    Clockwise=Clockwise*-1

    if Quad==1:
        theta7=3.14159265359*1.5-theta6
    elif Quad==2:
        theta7=3.14159265359*2-theta6
    elif Quad==3:
        theta7=3.14159265359*0.5-theta6
    else:
        theta7=3.14159265359-theta6
    
    for i in range (1,PixelsY):
        for j in range (0,PixelsX):#
            if i+CentreYZero==0:
                angcutone=1.57079623 
            else:
                angcutone=arctan(((CentreXZero+j*jfactor))/((i+CentreYZero)))          
            angcuttwo=arctan(((CentreX+j*jfactor))/((i+CentreY)))

            if CentreX-j>=0 and abs(CentreY)-i<0:
                angcuttwo=3.14159265359+angcuttwo
            elif CentreX-j<0 and abs(CentreY)-i<0:
                angcuttwo=3.14159265359+angcuttwo
            elif CentreX-j<0 and abs(CentreY)-i>=0:
                if angcuttwo<0:
                    angcuttwo=3.14159265359+angcuttwo
            else:
                if angcuttwo<0:
                    angcuttwo=2*3.14159265359+angcuttwo
                else:
                    angcuttwo=3.14159265359+angcuttwo
                
            if Clockwise==1:
                if theta7<theta5:
                    theta8=theta5-theta7
                    theta9=angcuttwo-theta7
                else:
                    theta8=2*3.14-(theta7-theta5)
                    if angcuttwo<theta5:
                        theta9=angcuttwo+2*3.14-theta7
                    else:
                        theta9=angcuttwo-theta7
            else:
                if theta5<theta7:
                    theta8=theta7-theta5
                    theta9=theta7-angcuttwo
                else:
                    theta8=2*3.14-(theta5-theta7)
                    if angcuttwo>theta5:
                        theta9=2*3.14-angcuttwo+theta7
                    else:
                        theta9=theta7-angcuttwo              
            RadiusScaleFactor=RadiusScaleFactorOld*(1+RadiusScale2*(theta9/theta8))

                        
            PresRad=(((((CentreX+j*jfactor))**2+((i*ifactor+CentreY)*ScaleY)**2)**0.5)-(Radius2-RadiusDiff2*RadiusScaleFactor))*0.5/(RadiusDiff2*RadiusScaleFactor)
            #if PresRad>0 and PresRad<1 and Clockwise==-1:
                #x[i,j]=-1000.0
                #print(angcuttwo)

            #PRESRAD -1 to 2 for backflows
            if PresRad>0 and PresRad<1 and (Clockwise==1 and((theta7<theta5 and angcuttwo>=theta7 and angcuttwo<=theta5)or(theta5<theta7 and (angcuttwo>=theta7 or angcuttwo<=theta5))) or (Clockwise==-1 and((theta7<theta5 and (angcuttwo<=theta7 or angcuttwo>=theta5))or(theta5<theta7 and angcuttwo<=theta7 and angcuttwo>=theta5)))):
            #if PresRad>0 and PresRad<1 and ((angcuttwo<theta7 and angcuttwo>=theta5 and Clockwise==-1) or ((angcuttwo>theta7 and angcuttwo<=theta5) and Clockwise==1)):
                dydx=(-2.0*(CentreX+j*jfactor))/(ScaleY**2.0*2.0*(i+CentreY))
                ang=arctan(dydx)
                if CentreX-j>0 and abs(CentreY)-i<0:
                    ang=3.14159265359-ang
                elif CentreX-j<0 and abs(CentreY)-i<0:
                    ang=3.14159265359-ang
                elif CentreX-j<0 and abs(CentreY)-i>0:
                    ang=-ang
                else:
                    ang=2*3.14159265359-ang
                

                #y[i,j]=Clockwise*1000.0*(min(sin(PresRad*3.14159)*1.25,1))*sin(angcuttwo)#Set Xvelocity based on angle
                #x[i,j]=Clockwise*1000.0*(min(sin(PresRad*3.14159)*1.25,1))*cos(angcuttwo)#Set Yvelocity based on angle

                y[i,j]=Clockwise*-MasterSpeed*sin(ang)#Set Xvelocity based on angle
                x[i,j]=Clockwise*-MasterSpeed*cos(ang)#Set Yvelocity based on angle

    #SideFlows=[0.307,0.50,0.1,0.03,80,1,0.77,0.255,0.1,0.02,70,1,0.77,0.45,0.1,0.02,70,2,0.49,0.41,0.1,0.03,60,3]
    #SideFlows=[0.15,0.35,0.25,0.25,90.1,1]
    

    while len(SideFlows)>3:

        if SideFlows[5]<5 or SideFlows[5]==7: #Should this be all of the time?
            theta2=SideFlows[4]+90
            theta2=theta2*3.14/180  
            SideFlows[4]=SideFlows[4]*3.14/180
            c2=0.0
            
        if cos(SideFlows[4])==0:
            SideFlows[4]=SideFlows[4]+0.01
            print('Striaght up, I cant do this shit man!')
        else:
            c2=SideFlows[2]*PixelsX/cos(SideFlows[4])
            c4=SideFlows[3]*PixelsX/sin(SideFlows[4])
                    
        yold=y
        xold=x
        m1=tan(SideFlows[4])
        m2=tan(theta2)
        c1=SideFlows[0]*PixelsX*m1-SideFlows[1]*PixelsY
        c3=SideFlows[0]*PixelsX*m2-SideFlows[1]*PixelsY
        if SideFlows[4]<-3.14159265359/2:
            c2=-c2
            c4=-c4
        elif SideFlows[4]<0:
            c4=-c4

        for i in range (1,PixelsY):
            for j in range (0,PixelsX):                
                abcdefg=xold[i,j]
                hijklmnop=yold[i,j]
                #Main Curve
                if i>m1*j-c1-c2 and i<m1*j-c1+c2 and i>m2*j-c3-c4 and i<m2*j-c3+c4 and (SideFlows[5]<5 or SideFlows[5]==7):
                    
                    if SideFlows[5]==1 or SideFlows[5]==3:
                        if SideFlows[4]<0 and SideFlows[4]>-3.14159265359/2:
                            xprime=(1-(i-(m1*j-c1-c2))/(2*c2))
                            yprime=((i-(m2*j-c3-c4))/(2*c4))
                        elif SideFlows[4]>0:
                            xprime=(1-(i-(m1*j-c1-c2))/(2*c2))
                            yprime=(1-(i-(m2*j-c3-c4))/(2*c4))
                        else:
                            xprime=((i-(m1*j-c1-c2))/(2*c2))
                            yprime=((i-(m2*j-c3-c4))/(2*c4))
                            
                        speed=(max(min(((1-(xprime**2+yprime**2)/1.41)),1),0))**0.25
                        power=(xprime**2)#*(max(min((1-(xprime**2+yprime**2)),1),0))**0.25
                        if SideFlows[5]==1:
                            x[i,j]=(abcdefg*(1-power)-hijklmnop*power)*speed
                            y[i,j]=(hijklmnop*(1-power)+abcdefg*power)*speed
                        else:
                            back=((0.5-yprime)*2)
                            Side=((0.5-xprime)*2)

                            if back<0:
                                back=-(back**2)**0.25
                            else:
                                back=(back**2)**0.25
                                
                            if Side<0:
                                Side=-(Side**2)
                            else:
                                Side=(Side**2)
                            #print('x')
                            #print(xprime)
                            #print(yprime)
                            speed1=(max(min((1-((xprime**2+yprime**2)/1.41)),1),0))**0.25
                            speed2=(max(min((1-(((1-xprime)**2+yprime**2)/1.41)),1),0))**0.25
                            power=(max(min((1-(((xprime)**2+(1-yprime)**2)/1.41)),1),0))**0.25
                            back2=back*(1-Side**2)
                            Side2=Side*(1-back**2)
                            back=back2
                            Side=Side2
                            x[i,j]=((abcdefg*back-hijklmnop*Side)*power+x[i,j]*(1-power))*speed1*speed2
                            y[i,j]=((hijklmnop*back+abcdefg*Side)*power+y[i,j]*(1-power))*speed1*speed2
                            
                    elif SideFlows[5]==2 or SideFlows[5]==4:
                        
                        if SideFlows[4]<0 and SideFlows[4]>-3.14159265359/2:
                            xprime=(1-(i-(m1*j-c1-c2))/(2*c2))
                            yprime=(1-(i-(m2*j-c3-c4))/(2*c4))
                        elif SideFlows[4]>0:
                            xprime=(1-(i-(m1*j-c1-c2))/(2*c2))
                            yprime=((i-(m2*j-c3-c4))/(2*c4))
                        else:
                            xprime=((i-(m1*j-c1-c2))/(2*c2))
                            yprime=(1-(i-(m2*j-c3-c4))/(2*c4))
                        
                        speed=(max(min((1-((xprime**2+yprime**2))/1.41),1),0))**0.25
                        power=xprime**2     
                        if SideFlows[5]==2:
                            x[i,j]=(xold[i,j]*(1-power)+yold[i,j]*power)*speed
                            y[i,j]=(yold[i,j]*(1-power)-abcdefg*power)*speed
                        else:
                            back=((0.5-yprime)*2)
                            Side=((0.5-xprime)*2)

                            if back<0:
                                back=-(back**2)**0.25
                            else:
                                back=(back**2)**0.25
                                
                            if Side<0:
                                Side=(Side**2)
                            else:
                                Side=-(Side**2)

                            speed1=(max(min((1-((xprime**2+yprime**2)/1.41)),1),0))**0.25
                            speed2=(max(min((1-(((1-xprime)**2+yprime**2)/1.41)),1),0))**0.25
                            power=(max(min((1-(((xprime)**2+(1-yprime)**2)/1.41)),1),0))**0.25
                            
                            back2=back*(1-Side**2)
                            Side2=Side*(1-back**2)
                            back=back2
                            Side=Side2
                            x[i,j]=((abcdefg*back-hijklmnop*Side)*power+x[i,j]*(1-power))*speed1*speed2
                            y[i,j]=((hijklmnop*back+abcdefg*Side)*power+y[i,j]*(1-power))*speed1*speed2






                            

                if SideFlows[5]==7:# and PresRad<1 and PresRad>0:
                    if SideFlows[4]<0 and SideFlows[4]>-3.14159265359/2:
                        xprime=(1-(i-(m1*j-c1-c2))/(2*c2))
                        yprime=((i-(m2*j-c3-c4))/(2*c4))
                    elif SideFlows[4]>0:
                        xprime=(1-(i-(m1*j-c1-c2))/(2*c2))
                        yprime=(1-(i-(m2*j-c3-c4))/(2*c4))
                    else:
                        xprime=((i-(m1*j-c1-c2))/(2*c2))
                        yprime=((i-(m2*j-c3-c4))/(2*c4))
                    if xprime>0 and xprime<1 and yprime>0 and yprime<1:
                        
                        #x[i,j]=10000*max(min(( (((xprime-0.5)**2 + (yprime-0.5)**2)-0.25**2 )**2 ),1.0,0.0))
                        #athing=(((((xprime-0.5)**2 + (yprime-0.5)**2)-0.25**2 ))**2 )/0.00390625   
                        athing=(((((xprime-0.5)**2 + (yprime-0.5)**2))/0.25))                        
                        athing=1-min(athing,1.0)
                        #print(athing)
                        #x[i,j]=10000*min(athing,1.0)
                        #x[i,j]=abcdefg*(1-athing)-abcdefg*athing
                        x[i,j]=abcdefg-2*abcdefg*athing
                        y[i,j]=hijklmnop-2*hijklmnop*athing
                        w[i,j]=athing**1.5
                        #x[i,j]=10000*((((xprime-0.5)**2 + (yprime-0.5)**2)-0.25**2 )**2 )




                        
                         
                        
                #Inside of curve 1
                if ((i>m2*j-c3+c4 and i<m2*j-c3+c4*2 and SideFlows[4]>0) or (i<m2*j-c3-c4 and i>m2*j-c3-c4*2 and SideFlows[4]<0)) and i>m1*j-c1-c2 and i<m1*j-c1+c2 and SideFlows[5]==1:
                    if SideFlows[4]>0:
                        power=((1-(i-(m1*j-c1-c2))/(2*c2))**2)*(3.0-(i-(m2*j-c3-c4))/(c4))
                    elif SideFlows[4]<0 and SideFlows[4]>-3.14159265359/2:
                        power=(((i-(m1*j-c1+c2))/(2*c2))**2)*(3+(i-(m2*j-c3+c4))/(c4))
                    else:
                        power=(((i-(m1*j-c1-c2))/(2*c2))**2)*(3+(i-(m2*j-c3+c4))/(c4))
                        
                    y[i,j]=(yold[i,j]*(1-power)+abcdefg*power)
                    x[i,j]=(xold[i,j]*(1-power)-yold[i,j]*power)
                   
                #Inside of curve 2
                if (SideFlows[4]>0 and (i<m2*j-c3-c4 and i>m2*j-c3-c4*2) or (SideFlows[4]<0 and i>m2*j-c3+c4 and i<m2*j-c3+c4*2)) and i>m1*j-c1-c2 and i<m1*j-c1+c2 and SideFlows[5]==2:
                    if SideFlows[4]>0:
                        power=((1-(i-(m1*j-c1-c2))/(2*c2))**2)*(1.0+(i-(m2*j-c3-c4))/(c4))
                        x[i,j]=(xold[i,j]*(1-power)+yold[i,j]*power)
                        y[i,j]=(yold[i,j]*(1-power)-abcdefg*power)
                    elif SideFlows[4]<0 and SideFlows[4]>-3.14159265359/2:
                        power=(((i-(m1*j-c1+c2))/(2*c2))**2)*(1.0-(i-(m2*j-c3+c4))/(c4))
                        y[i,j]=(yold[i,j]*(1-power)-abcdefg*power)
                        x[i,j]=(xold[i,j]*(1-power)+yold[i,j]*power)
                    else:
                        power=(((i-(m1*j-c1-c2))/(2*c2))**2)*(1-(i-(m2*j-c3+c4))/(c4))
                        y[i,j]=(yold[i,j]*(1-power)-abcdefg*power)
                        x[i,j]=(xold[i,j]*(1-power)+yold[i,j]*power)
                        

                #START
                        
                if SideFlows[5]==5 or SideFlows[5]==6:
                    #print('Hello World')
                    CentreX=SideFlows[0]*PixelsX
                    CentreY=SideFlows[1]*PixelsY
                    ThetaSize=SideFlows[2]*3.14159265359/180.0
                    RadSize=SideFlows[3]*PixelsX/100
                    ThetaCentre=floor(SideFlows[4])*3.14159265359/180
                    RadCentre=(SideFlows[4]-floor(SideFlows[4]))*1000*PixelsX
                    RadiusDiff1=SideFlows[3]*PixelsX/100

                    if i-CentreY==0 and j-CentreX<=0:
                        angzero=1.5*3.14159265359
                    elif i-CentreY==0 and j-CentreX>0:
                        angzero=0.5*3.14159265359
                    else:
                        angzero=arctan((CentreX+j*jfactor)/(i-CentreY))#True angle of position from centre of curve
                        if CentreX-j>=0 and CentreY-i<=0:
                            angzero=3.14159265359+angzero
                        elif CentreX-j<=0 and abs(CentreY)-i<=0:
                            angzero=3.14159265359+angzero
                        elif CentreX-j<=0 and abs(CentreY)-i>=0:
                            if angzero<0:
                                angzero=3.14159265359+angzero
                        else:
                            angzero=2*3.14159265359+angzero



                        
                    
                    if SideFlows[5]==6:
                        theta0=ThetaCentre-ThetaSize
                        theta=ThetaCentre+ThetaSize
                        #if theta0<0:
                        #    theta0=2*3.14159265359-theta0
                        #if theta>2*3.14159265359:
                        #    theta=theta-2*3.14159265359
                        if theta0<theta:
                            theta8=theta-theta0
                            theta9=angzero-theta0
                        else:
                            theta8=2*3.14-(theta0-theta)
                            if angzero<theta:
                                theta9=angzero+2*3.14-theta0
                            else:
                                theta9=angzero-theta0
                    elif SideFlows[5]==5:
                        theta0=ThetaCentre+ThetaSize
                        theta=ThetaCentre-ThetaSize
                        #if theta<0:
                        #    theta=2*3.14159265359-theta0
                        #if theta0>2*3.14159265359:
                        #    theta0=theta0-2*3.14159265359
                        if theta5<theta0:
                            theta8=theta0-theta
                            theta9=theta0-angzero
                        else:
                            theta8=2*3.14-(theta-theta0)
                            if angzero>theta:
                                theta9=2*3.14-angzero+theta0
                            else:
                                theta9=theta0-angzero
                    if (angzero+2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize>0 and (angzero+2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize<1:                    
                        PresAng=(angzero+2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize
                        print('a')
                        print(PresAng)
                    elif (angzero-2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize>0 and (angzero-2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize<1:
                        PresAng=(angzero-2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize
                        #print('b')
                        #print(PresAng)
                    else:               
                        PresAng=(angzero-(ThetaCentre-ThetaSize))*0.5/ThetaSize
                        #print(PresAng)
                        
                    PresRad=(((((CentreX+j*jfactor))**2+((i-CentreY))**2)**0.5)-(RadCentre-RadiusDiff1))*0.5/(RadiusDiff1)#Calculates radius normalised by width - 0-1 is inside width of curve increasing linearly
                    if PresRad<1 and PresRad>0 and PresAng>0 and PresAng<1:
                    #if PresRad<1 and PresRad>0 and ((angzero-(ThetaCentre-ThetaSize))*0.5/ThetaSize>0 and (angzero-(ThetaCentre-ThetaSize))*0.5/ThetaSize<1) or ((angzero+2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize>0 and (angzero+2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize<1) or ((angzero-2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize>0 and (angzero-2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize<1):

                        xprime=1-PresAng
                        if SideFlows[5]==5:
                            yprime=PresRad
                        elif SideFlows[5]==6:
                            yprime=1-PresRad
                        back=((0.5-yprime)*2)
                        Side=((0.5-xprime)*2)

                        if back<0:
                            back=-(back**2)**0.25
                        else:
                            back=(back**2)**0.25
                        if Side<0:
                            Side=(Side**2)
                        else:
                            Side=-(Side**2)
                            
                        speed1=(max(min((1-((xprime**2+yprime**2)/1.41)),1),0))**0.25
                        speed2=(max(min((1-(((1-xprime)**2+yprime**2)/1.41)),1),0))**0.25                      
                        power=(max(min((1-(((xprime)**2+(1-yprime)**2)/1.41)),1),0))**0.25
                        back2=back*(1-Side**2)
                        Side2=Side*(1-back**2)
                        back=back2
                        Side=Side2
                        if SideFlows[5]==5:
                            x[i,j]=((abcdefg*back-hijklmnop*Side)*power+x[i,j]*(1-power))*speed1*speed2
                            y[i,j]=((hijklmnop*back+abcdefg*Side)*power+y[i,j]*(1-power))*speed1*speed2
                        elif SideFlows[5]==6:
                            x[i,j]=((abcdefg*back+hijklmnop*Side)*power+x[i,j]*(1-power))*speed1*speed2
                            y[i,j]=((hijklmnop*back-abcdefg*Side)*power+y[i,j]*(1-power))*speed1*speed2
        #END

                    
        if len(SideFlows)>7:
            SideFlows=SideFlows[6:len(SideFlows)]
            print(SideFlows)
        else:
            SideFlows=[0,0]
    for loo in range (0, int(floor(PixelsX/50))):
        for i in range (1,PixelsY-1):
                for j in range (1,PixelsX-1):
                    x[i,j]=(x[i+1,j]+x[i-1,j]+x[i,j+1]+x[i,j-1])/4
                    y[i,j]=(y[i+1,j]+y[i-1,j]+y[i,j+1]+y[i,j-1])/4
    
    x[0,0]=-1000
    y[0,0]=-1000
    x[0,1]=1000
    y[0,1]=1000
    #print('curve 2 plotted')
    #print('saving 1')
    #scipy.imageio.imwrite('Unreal Stuff\FlowMaps\Avon1x.png', x)# uses the Image module (PIL)
    imageio.imwrite('Unreal Stuff\FlowMaps\Avon1x.png', x)# uses the Image module (PIL)
    #print('saving 2')
    imageio.imwrite('Unreal Stuff\FlowMaps\Avon1y.png', y)# uses the Image module (PIL)
    #print('saving 3')
    imageio.imwrite('Unreal Stuff\FlowMaps\Avon1w.png', w)# uses the Image module (PIL)
    print('images saved...')
    print(max(x[75,:]))
    print(max(x[:,75]))
    print(max(y[:,75]))
    print(max(y[75,:]))

    return[CentreX,CentreY,theta7,theta5,Radius2,RadiusDiff2,RadiusScale2,ScaleY2,RadiusScaleFactorOld]


ciww1()
#ciww12()
#ciww2()
#ciww3()
#ciww4()
#ciww5()
#ciww6()
#ciww7()
#ciww8()
#ciww9()
#ciww10()
#ciww11()
#ciww12()
#testcurve()

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

def declarations(PixelsY,Aspect_Ratio_Pixels):
    Pixels_X=int(round(PixelsY/Aspect_Ratio_Pixels,0))
    Velocity_Y=array([[0.0] * Pixels_X] * PixelsY)
    Velocity_X=array([[0.0] * Pixels_X] * PixelsY)
    Foam=array([[0.0] * Pixels_X] * PixelsY)
    Last_Radius_Scale_Factor=1
    Perpendicular_Flows=[0,0]
    return(Pixels_X,Velocity_Y,Velocity_X,Foam,Last_Radius_Scale_Factor,Perpendicular_Flows)

def SaveResult(PixelsY,PixelsX,x,y,w,filename,mode):
    if mode==1 or mode==2:
        print(filename)
        print('saving x image')
        imageio.imwrite(f'C:\\Users\\angus\\OneDrive\\Documents\\Unreal Stuff\\FlowMaps\\{filename}x.png', x)
        print('saving y image')
        imageio.imwrite(f'C:\\Users\\angus\\OneDrive\\Documents\\Unreal Stuff\\FlowMaps\\{filename}y.png', y)
        print('saving w image')
        imageio.imwrite(f'C:\\Users\\angus\\OneDrive\\Documents\\Unreal Stuff\\FlowMaps\\{filename}w.png', w)
    if mode==1 or mode==3:
        #Writes array of locations
        print('writing array')
        A='NewRow,"('
        for i in range (PixelsY-1,-1,-1):
            for j in range (0,PixelsX):
                A=A + '(X=' + str(x[i,j])+',Y=' + str(y[i,j])+',Z=0.000000),'  
        A=A[0:len(A)-1] +')"'
        print('saving array')
        with open(f'C:\\Users\\angus\\OneDrive\\Documents\\Unreal Stuff\\FlowMaps\\{filename}.csv', 'w') as wf:
            wf.write('---,Cardiff1,Cardiff1Size\n')
            wf.write(A)
            wf.write(',"(X=' + str(PixelsY) +',Y=' + str(PixelsX) +',Z=0.000000)"')
    print("done")

def Generate(AspectRatio,PixelsY,Clockwise,CentreX,CentreY,theta0,theta,Radius1,RadiusDiff1,RadiusScale,ScaleY,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld,SideFlows,MasterSpeed,x,y,w):
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

            #PRESRAD -1 to 2 for backflows
            if PresRad>0 and PresRad<1 and (Clockwise==1 and((theta7<theta5 and angcuttwo>=theta7 and angcuttwo<=theta5)or(theta5<theta7 and (angcuttwo>=theta7 or angcuttwo<=theta5))) or (Clockwise==-1 and((theta7<theta5 and (angcuttwo<=theta7 or angcuttwo>=theta5))or(theta5<theta7 and angcuttwo<=theta7 and angcuttwo>=theta5)))):
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

                y[i,j]=Clockwise*-MasterSpeed*sin(ang)#Set Xvelocity based on angle
                x[i,j]=Clockwise*-MasterSpeed*cos(ang)#Set Yvelocity based on angle  

    while len(SideFlows)>3:
        #if SideFlows[5]<5 or SideFlows[5]==7: #Should this be all of the time?
        theta2=SideFlows[4]+90
        theta2=theta2*3.14/180  
        SideFlows[4]=SideFlows[4]*3.14/180
        c2=0.0
            
        if cos(SideFlows[4])==0:
            SideFlows[4]=SideFlows[4]+0.01
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
                        
                        athing=(((((xprime-0.5)**2 + (yprime-0.5)**2))/0.25))                        
                        athing=1-min(athing,1.0)
                        x[i,j]=abcdefg-2*abcdefg*athing
                        y[i,j]=hijklmnop-2*hijklmnop*athing
                        w[i,j]=athing**1.5
        
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
                          
                if SideFlows[5]==5 or SideFlows[5]==6:
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
                    elif (angzero-2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize>0 and (angzero-2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize<1:
                        PresAng=(angzero-2*3.14159265359-(ThetaCentre-ThetaSize))*0.5/ThetaSize
                    else:               
                        PresAng=(angzero-(ThetaCentre-ThetaSize))*0.5/ThetaSize
                        
                    PresRad=(((((CentreX+j*jfactor))**2+((i-CentreY))**2)**0.5)-(RadCentre-RadiusDiff1))*0.5/(RadiusDiff1)#Calculates radius normalised by width - 0-1 is inside width of curve increasing linearly
                    if PresRad<1 and PresRad>0 and PresAng>0 and PresAng<1:
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
           
        if len(SideFlows)>7:
            SideFlows=SideFlows[6:len(SideFlows)]
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
    return[CentreX,-CentreY,theta7,theta5,Radius2,RadiusScale2,ScaleY2,RadiusScaleFactorOld]
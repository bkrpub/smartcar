from Motor import *            
PWM=Motor()          
def test_Motor(): 
    try:
        s=1
        for m in range(1):
            m+=4
            print(1000*s*m)
            fl=0
            bl=0
            fr=1
            br=1
            PWM.setMotorModel(int(1000*s*m*fl),int(1000*s*m*bl),int(1000*s*m*fr),int(1000*s*br))       #Forward
            time.sleep(2)

        print ("The car is moving forward")
        time.sleep(60)
        if False:
            time.sleep(1)
            PWM.setMotorModel(int(-1000*s),int(-1000*s),int(-1000*s),int(-1000*s))   #Back
            print ("The car is going backwards")
            time.sleep(1)
            PWM.setMotorModel(int(-1500*s),int(-1500*s),int(2000*s),int(2000*s))       #Turn left
            print ("The car is turning left")
            time.sleep(1)
            PWM.setMotorModel(int(2000*s),int(2000*s),int(-1500*s),int(-1500*s))       #Turn right 
            print ("The car is turning right")  
            time.sleep(1)
            PWM.setMotorModel(int(-2000*s),int(2000*s),int(2000*s),int(-2000*s))       #Move left 
            print ("The car is moving left")  
            time.sleep(1)
            PWM.setMotorModel(int(2000*s),int(-2000*s),int(-2000*s),int(2000*s))       #Move right 
            print ("The car is moving right")  
            time.sleep(1)    
            
            PWM.setMotorModel(int(0*s),int(2000*s),int(2000*s),int(0*s))       #Move diagonally to the left and forward
            print ("The car is moving diagonally to the left and forward")  
            time.sleep(1)
            PWM.setMotorModel(int(0*s),int(-2000*s),int(-2000*s),int(0*s))       #Move diagonally to the right and backward
            print ("The car is moving diagonally to the right and backward")  
            time.sleep(1) 
            PWM.setMotorModel(int(2000*s),int(0*s),int(2000*s),int(0*s))       #Move diagonally to the right and forward
            print ("The car is moving diagonally to the right and forward")  
            time.sleep(1)
            PWM.setMotorModel(int(-2000*s),int(0*s),int(-2000*s),int(0*s))       #Move diagonally to the left and backward
            print ("The car is moving diagonally to the left and backward")  
            time.sleep(1) 
        
        PWM.setMotorModel(0,0,0,0)                   #Stop
        print ("\nEnd of program")
    except KeyboardInterrupt:
        PWM.setMotorModel(0,0,0,0)
        print ("\nEnd of program")

test_Motor()

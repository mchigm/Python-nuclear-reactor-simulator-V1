import keyboard
import mouse as mo
from getkey import getkey, keys as k, keys
AZ5 = int
Mode = str
reactor1_Temp = int
reactor1_WaterTemp = float
reactor1_CoreTemp = int
reactor1_Status = str
reactor1_Pressure = int
reactor2_Temp = int
reactor2_WaterTemp = float
reactor2_CoreTemp = int
reactor2_Status = str
reactor2_Pressure = int
reactor3_Temp = int
reactor3_WaterTemp = float
reactor3_CoreTemp = int
reactor3_Status = str
reactor3_Pressure = int
reactor4_Temp = int
reactor4_WaterTemp = float
reactor4_CoreTemp = int
reactor4_Status = str
reactor4_Pressure = int
electricity = int
class __init__ :
  electricity = 0
  reactor1_Temp = 19
  reactor1_WaterTemp = 25.00
  reactor1_CoreTemp = 20
  reactor1_Pressure = 3
  reactor2_Temp = 19
  reactor2_WaterTemp = 25
  reactor2_CoreTemp = 20
  reactor2_Pressure = 3
  reactor3_Temp = 19
  reactor3_WaterTemp = 25
  reactor3_CoreTemp = 20
  reactor3_Pressure = 3
  reactor4_Temp = 19
  reactor4_WaterTemp = 25
  reactor4_CoreTemp = 20
  reactor4_Pressure = 3
class reactor:
  def reactorone():
    print(reactor1_Temp)
    print(reactor1_WaterTemp)
    print(reactor1_CoreTemp)
    print(reactor1_Pressure)
  def reactortwo():
    print(reactor2_Temp)
    print(reactor2_WaterTemp)
    print(reactor2_CoreTemp)
    print(reactor2_Pressure)
  def reactorthree():
    print(reactor3_Temp)
    print(reactor3_WaterTemp)
    print(reactor3_CoreTemp)
    print(reactor3_Pressure)
  def reactorfour():
    print(reactor4_Temp)
    print(reactor4_WaterTemp)
    print(reactor4_CoreTemp)
    print(reactor4_Pressure)
  def viewreactor():
    print(reactor1_Temp)
    print(reactor2_Temp)
    print(reactor3_Temp)
    print(reactor4_Temp)
  def AZdashFIVE():
    reactor1_Temp = 2560
    reactor1_Pressure = 76
    reactor2_Temp = 2560
    reactor2_Pressure = 76
    reactor3_Temp = 2560
    reactor3_Pressure = 76
    reactor4_Temp = 2560
    reactor4_Pressure = 76
    AZ5 += 1
  def Meltdown1():
    print("Meltdown! Your reactor has suffered a minor meltdown! The special atomic force has controlled the reactor and the reactor has been fixed. People were believed that a spy has done it, you are now in prision because of your misact and the millitary and government are navigating this incident." + "\nThe game has ended! You have generated" , electricity , "ohm of electricity which makes" , electricity//100 , "families have sufficient amount of energy. You have also exported" , electricity%99 , "electricities which made a profit of" , electricity%99*3 , "billion dollers for your country.")
  def Meltdown2():
    print("Meltdown! Your reactor has suffered a small meltdown! The special atomic force has controlled the reactor and the reactor has been closed. People were believed that a group of enemy spies have done it, you are now in prision because of your misact and the millitary and government are navigating this incident." + "\nThe game has ended! You have generated" , electricity , "ohm of electricity which makes" , electricity//100 , "families have sufficient amount of energy. You have also exported" , electricity%99 , "electricities which made a profit of" , electricity%99*3 , "billion dollers for your country.")
    print("THANKYOU FOR PLAYING THE NUCLEAR REACTOR ⛆")
  def Meltdown3():
    print("Meltdown! Your reactor has suffered a meltdown! The special atomic force has closed the reactor and now it seems to be under controlled. People were believed that the enemy country has done it, you are now in prision because of your misact and treason, someone has put a spy certificate of the enemy in your house when you are not home." + "\nThe game has ended! You have generated" , electricity , "ohm of electricity which makes" , electricity//100 , "families have sufficient amount of energy. You have also exported" , electricity%99 , "electricities which made a profit of" , electricity%99*3 , "billion dollers for your country.")
  def Meltdown4():
    print("Meltdown! Your reactor has suffered a BIG meltdown! The special atomic force has controlled the reactor and the reactor has been fixed. People were believed that a spy has done it, you are now in prision because of your misact and the millitary and government are navigating this incident." + "\nThe game has ended! You have generated" , electricity , "ohm of electricity which makes" , electricity//100 , "families have sufficient amount of energy. You have also exported" , electricity%99 , "electricities which made a profit of" , electricity%99*3 , "billion dollers for your country.")
    print("THANK YOU FOR PLAYING THE NUCLEAR REACTOR! ☢☢☢")
  def Meltdown5():
    print("Meltdown! Your reactor has suffered a major meltdown! The special atomic force has controlled the reactor and the reactor has been fixed. People were believed that a spy has done it, you are now in prision because of your misact and the millitary and government are navigating this incident." + "\nThe game has ended! You have generated" , electricity , "ohm of electricity which makes" , electricity//100 , "families have sufficient amount of energy. You have also exported" , electricity%99 , "electricities which made a profit of" , electricity%99*3 , "billion dollers for your country.")
    print("THANK YOU FOR PLAYING THE NUCLEAR REACTOR! ☢▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮▮ 1136 RAD/s")
print("hi, you are now controlling a nuclear reactor. To view the reactor, type v to view the entire plant")
if k == "v":
  reactor.viewreactor()
  print ("this is the entire plant, as we can see, water will run from the storage to the reactor and run back to the storage. This is the first ")
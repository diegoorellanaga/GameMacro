# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 01:03:55 2017

@author: diego
"""
import threading
from multiprocessing import Process
import time
import pyautogui
import pyscreenshot as ImageGrab
import numpy as np
import cv2
import Queue



def Move_to_safety(direction_in,direction_out,section,q):
    item_xy_n=(614,304)
    item_xy_s=(621,394)
    food_xy_i=(1194,554)
    maxphoto=30
    photo=0
    while(q.empty()):   
   
        while(Take_screenshot_and_get_status(section,2)==0 and Take_screenshot_and_process(section,0)):
            if item_present(item_xy_n):
                Logout_simple(q)
            pass
        pyautogui.press(direction_in)
        time.sleep(2)
       
        while((not Take_screenshot_and_process(section,0)) or Take_screenshot_and_get_status(section,2)==1 or Take_screenshot_and_get_status(section,2)==3 ):
            if photo<maxphoto:
                pyautogui.press('prtscr')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(1)
                photo=photo+1
            if under(underpoints):
                Logout_simple(q)
            if Take_screenshot_and_get_status(section,2)==1:
                time.sleep(2)               
                pyautogui.typewrite('exura gran') 
                pyautogui.press('enter')
                time.sleep(10)#600
                if under(underpoints):
                    Logout_simple(q)
                pyautogui.typewrite('exura gran') 
                pyautogui.press('enter')
                if Take_screenshot_and_process(section,4):
                    if photo<maxphoto:
                        pyautogui.press('prtscr')
                        time.sleep(2)
                        pyautogui.press('enter')
                        time.sleep(1)
                        photo=photo+1
                time.sleep(600)#600
                if under(underpoints):
                    Logout_simple(q)
                pyautogui.typewrite('exura gran') 
                pyautogui.press('enter')
                time.sleep(5)
            pass
        if(q.empty):
            pyautogui.press(direction_out)
            time.sleep(1)
        eat_food(food_xy_i)
       
def Logout(section,q):
    for i in range(5):
        while(Take_screenshot_and_process(section,0)):
            pass
        pyautogui.click(x=76, y=46) #Full screen on my laptop(linux) x=88, y=47 
        pyautogui.click(x=668, y=417) #press ok in the popup window. x=668, y=417
    q.put(1)

def Logout_simple(q):
    for i in range(5):
        pyautogui.click(x=88, y=47) #Full screen on my laptop(linux)  
        pyautogui.click(x=668, y=417) #press ok in the popup window.
    q.put(1)
       
def Take_screenshot_and_process(section,select):
    im=ImageGrab.grab(bbox=section[select])
    improc=np.array(im,dtype=np.uint8)
    print(improc)
    if sum(improc[0][0])<section[select][4]: #if it is lower it means is ok. #it also means we have to wait mana
        return True
    else:
        return False
       
def Take_screenshot_and_get_status(section,select):
    im=ImageGrab.grab(bbox=section[select][0:4])
    improc=np.array(im,dtype=np.uint8)
    print(sum(improc[0][0])) #---------------- delete this
    if sum(improc[0][0])==section[select][4]: #attacked #item under
        return 1
    elif sum(improc[0][0])==section[select][5]: #Nothing
        return 0           
    elif sum(improc[0][0])==section[select][6]: #pz
        return 2         
    else:
        return 3 #unknown or hungry

def Drag_rune_loop(hand_xy,rune_xy,food_xy,rune_name):
        pyautogui.moveTo(rune_xy[0], rune_xy[1],0.5)
        pyautogui.dragTo(hand_xy[0], hand_xy[1],0.5, button='left')
      #  pyautogui.typewrite(rune_name) 
        pyautogui.press(hotkey_runa)
        time.sleep(1)
        pyautogui.press(hotkey_manatrain)        
        pyautogui.dragTo(rune_xy[0], rune_xy[1],0.5, button='left')
        pyautogui.click(x=food_xy[0], y=food_xy[1], button='right')

        pyautogui.click(x=food_xy[0], y=food_xy[1], button='right')
       
def Make_runes(hand_xy,rune1_xy,rune2_xy,rune3_xy,food_xy,rune_name,section,q):
    maxrunes=60
    runesnow=1
    while(q.empty()):   
   
        while(Take_screenshot_and_process(section,1) and q.empty()):
            time.sleep(40)
      
        Drag_rune_loop(hand_xy,rune1_xy,food_xy,rune_name)   
            
        while(Take_screenshot_and_process(section,1) and q.empty()):          
            time.sleep(40)
           
        Drag_rune_loop(hand_xy,rune2_xy,food_xy,rune_name)

        while(Take_screenshot_and_process(section,1) and q.empty()):         
            time.sleep(40)
             
        Drag_rune_loop(hand_xy,rune3_xy,food_xy,rune_name)
        runesnow=runesnow+1
        if runesnow > maxrunes:
            Logout_simple(q)
       

def move_item(item_xy,item_target_xy):
        pyautogui.moveTo(item_xy[0], item_xy[1])
        pyautogui.dragTo(item_target_xy[0], item_target_xy[1],0.2, button='left')
        pyautogui.press('enter')
       
def item_present(item_xy):
    im=ImageGrab.grab(bbox=section[3])
    improc=np.array(im,dtype=np.uint8)
    if sum(improc[0][0])==section[3][4]:
        return False
    else:
        return True
   
def eat_food(food_xy):
        pyautogui.click(x=food_xy[0], y=food_xy[1], button='right')
        time.sleep(0.5) 
        pyautogui.click(x=food_xy[0], y=food_xy[1], button='right')
def eat_food2(food_xy2,spell):

        #time.sleep(10)        
        pyautogui.click(x=food_xy2[0], y=food_xy2[1], button='right')
        time.sleep(0.5) 
        pyautogui.click(x=food_xy2[0], y=food_xy2[1], button='right')   
        time.sleep(10)
       # pyautogui.typewrite(spell) 
        pyautogui.press('f1')
   
   
   
spell="exura"
item_xy_n=(614,304)
item_xy_s=(621,394)
q = Queue.Queue()        
hand_xy=(1198,262)
rune1_xy=(1329,379)
rune2_xy=(1328,440)
rune3_xy=(1329,494)
food_xy=(1194,554)
food_xy2=(1275,306) #flechas
food_xy3=(1188,377) #bolsa bajo flechas
rune_name='adori gran flam'  
section=[(1203,648,1205,650,120),(1315,112,1316,114,120),(1309,269,1310,270,438,85,356,119),(614,304,615,305,210),(1220,95,1221,96,300),(636,373,637,374,203,0,0,0,0)] #intruso,mana,attacked,northitem,life,under
underpoints=[(628, 358,629,359,217,209,223),(619,381,620,382,211,203,221)]
select=1
direction_out='down'       #attacked,nothing,pz,hungry
direction_in='up' 

hotkey_runa='f10'
hotkey_manatrain='f11'

#time.sleep(10)
#p =Process(target=Make_runes, args=(hand_xy,rune1_xy,rune2_xy,rune3_xy,food_xy,rune_name,section,))
#p2=Process(target=Move_to_safety, args=(direction_in,direction_out,section,))
#p.start()
#p2.start()

def trainmana(food_xy2,q):
    while(q.empty()):
        eat_food2(food_xy2,spell)
        time.sleep(10)
   


def under(underpoints):
    under=False
    length=len(underpoints)
    for i in range(length):
        im=ImageGrab.grab(bbox=underpoints[i][0:4])
        improc=np.array(im,dtype=np.uint8)
      #  print(sum(improc[0][0]))
      #  print(underpoints[i][4])
        if (sum(improc[0][0]) < underpoints[i][5]) or (sum(improc[0][0]) > underpoints[i][6]) :
            under = True
    return under       


#for i in range(10):   
#    time.sleep(2)   
#    under(underpoints)   
   


#(628, 358) 217-(209-223) sum under (619, 381) sum 211-(203-221)
#p.join()
#p=Process(target=Move_to_safety, args=(direction_in,direction_out,section,))
#p.start()
#p.join()



time.sleep(19)
p =threading.Thread(target=Make_runes, args=(hand_xy,rune1_xy,rune2_xy,rune3_xy,food_xy,rune_name,section,q,))
#p=threading.Thread(target=trainmana, args=(food_xy2,q,))
p.start()
#p2=threading.Thread(target=Move_to_safety, args=(direction_in,direction_out,section,q))
p2=threading.Thread(target=Logout, args=(section,q,))
p2.start()



#This code is useful to get the position of the elements on the screen
#import time
#import pyautogui
#time.sleep(8)
#while(True):
##    eat_food2(food_xy2,spell)
#    print(pyautogui.position())
#    time.sleep(2)
##    eat_food2(food_xy3,spell)
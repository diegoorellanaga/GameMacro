Title:	Medivia Macro Guide  
Author:	Diego Orellana  
Base Header Level:	2  

# Introduction #

[Medivia] is a tibia ot server. I made a simple macro to make runes while afk. And if it sees somebody in the screen it exits automatically.  

# Functions #

In this section, we will explain in detail the python functions involved in this macro.

## Take_screenshot_and_process ##

This function takes a screenshot of a small section of the screen ~(1x1 or 2x2 pixels).
Then it classifies the section by the value of the sum of the pixels. 
Depending on this value the script knows what is happening on the screen, and returns True or False depending on the situation.

| Inputs   |      Type/explanation      |
|----------|:-------------:|
| section | list: contains sections of the screen and their thresholds |
| select |    int: id of the section which we want to select  |
| **Outputs**   |      **Type/explanation**      | 
| Boolean | Boolean: True if the sum of the pixel values is less than a given threshold |

## Logout ##

This function logs out the character if something wrong happens and tell the other thread to stop by putting something in a queue. This function depends on the values given to the previous function. 

| Inputs   |      Type/explanation      |
|----------|:-------------:|
| section | list: contains sections of the screen and their thresholds |
| q |    Queue: Queue that is used for thread communication  |
| **Outputs**   |      **Type/explanation**      | 
| - | If the Take_screenshot_and_process function returns True we add an element to the Queue |

## Logout_simple ##

The difference between this function and the previous one is that this function doesn't check the screen it logs out whenever it is triggered.

| Inputs   |      Type/explanation      |
|----------|:-------------:|
| q |    Queue: Queue that is used for thread communication  |
| **Outputs**   |      **Type/explanation**       | 
|-| We add an element to the Queue q to tell the other thread to finish |

## Take_screenshot_and_get_status ##

Similar to Take_screenshot_and_process function but, instead of returning a boolean we return an id number that will tell us the status of the character (attacked, hungry, safe zone, low life).

| Inputs   |      Type/explanation      |
|----------|:-------------:|
| section | list: contains sections of the screen and their thresholds |
| select |    int: id of the section which we want to select  |
| **Outputs**   |      **Type/explanation**      | 
| Boolean | Boolean: True if the sum of the pixel values is less than a given threshold |

## Drag_rune_loop ## 

Given some coordinates, this functions moves a rune to the hand and execute a spell.

| Inputs   |      Type/explanation      |
|----------|:-------------:|
| hand_xy | tuple: Coordinates of the hand |
| rune_xy | tuple: Coordinate of the rune we want to transform |
| food_xy | tuple: Coordinates of the food (deprecated) |
| rune_name |  string: Name of the spell we are going to execute (deprecated) |
| **Outputs**   |      **Type/explanation**      | 
| None | Takes control of the mouse and keyboard and move them to execute the actions |

## Make_runes ## 

The core of the script. This function joins several of the previous function in order to make 3 backpacks of a given rune.

| Inputs   |      Type/explanation      |
|----------|:-------------:|
| hand_xy  | tuple: Coordinates of the hand |
| rune1_xy | tuple: Coordinate of the rune from the first backpack we want to transform |
| rune2_xy | tuple: Coordinate of the rune from the second backpack we want to transform |
| rune3_xy | tuple: Coordinate of the rune from the third backpack we want to transform |
| food_xy  | tuple: Coordinates of the food (deprecated) |
| rune_name |  string: Name of the spell we are going to execute (deprecated) |
| section  | list: contains sections of the screen and their thresholds |
| q |    Queue: Queue that is used for thread communication  |
| **Outputs**  |      **Type/explanation**      | 
| None | Takes control of the mouse and keyboard and move them to execute the actions |


## Move_to_safety ## 

This is one of the mods this script has. In this mod we don't log out the character if there is something dangerous present but, we make it enter to a safe zone by moving the character one step up/down, once the danger is gone and enough time has passed (to make the enemy get bored of waiting) we make the character move one step down/up.

| Inputs   |      Type/explanation      |
|----------|:-------------:|
| direction_in | string: "up"/"down" |
| direction_out | string: "down"/"up"|
| section | list: contains sections of the screen and their thresholds |
| q |    Queue: Queue that is used for thread communication  |


The remaining functions are self-explanatory if you understood the ones described above.


	time.sleep(19)
	p =threading.Thread(target=Make_runes, args=(hand_xy,rune1_xy,rune2_xy,rune3_xy,food_xy,rune_name,section,q,))
	#p=threading.Thread(target=trainmana, args=(food_xy2,q,))
	p.start()
	#p2=threading.Thread(target=Move_to_safety, args=(direction_in,direction_out,section,q))
	p2=threading.Thread(target=Logout, args=(section,q,))
	p2.start()


In the code above we associate a function with its given values to a thread, and we start it. The lines that are commented are different options we can activate, but only if we deactivate first the previous one. For example, instead of making runes we can just train mana, or instead of login out, we can just move to safety.


You need to customize all the coordinates. If you happen to have my same screen resolution, this same code should work for you. This code is just the core of what you can do with this macro, it is not very elegant, for example, a next step could be to get the coordinates automatically by detecting the elements in the screen with a search. But this worked fine for me so far so I didn't have the need to keep improving it with fancy details. Hope you find it useful.


# Example #

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
	section=[(1203,648,1205,650,120),(1315,112,1316,114,120),(1309,269,1310,270,438,85,356,119),(614,304,615,305,210),(1220,95,1221,96,300),(636,373,637,374,203,0,0,0,0)] #intruso,mana,attacked,northitem,life,under. This are what each section means, the fifth value is always the theshold.
	underpoints=[(628, 358,629,359,217,209,223),(619,381,620,382,211,203,221)]
	select=1
	direction_out='down'       #attacked,nothing,pz,hungry
	direction_in='up' 
	hotkey_runa='f10'
	hotkey_manatrain='f11'

	time.sleep(19) #This will give you time to change to the game screen before the macro starts running.
	p =threading.Thread(target=Make_runes, args=(hand_xy,rune1_xy,rune2_xy,rune3_xy,food_xy,rune_name,section,q,))
	#p=threading.Thread(target=trainmana, args=(food_xy2,q,))
	p.start()
	#p2=threading.Thread(target=Move_to_safety, args=(direction_in,direction_out,section,q))
	p2=threading.Thread(target=Logout, args=(section,q,))
	p2.start()




[Medivia]:	https://medivia.online/


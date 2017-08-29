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

| Outputs   |      Type/explanation      | 
|----------|:-------------:|
| Boolean | Boolean: True if the sum of the pixel values is less than a given threshold |

## Logout ##

This function logs out the character if something wrong happens and tell the other thread to stop by putting something in a queue. This function depends on the values given to the previous function. 

| Inputs   |      Type/explanation      |
|----------|:-------------:|
| section | list: contains sections of the screen and their thresholds |
| q |    Queue: Queue that is used for thread communication  |

| Outputs   |      Type/explanation      | 
|----------|:-------------:|
| - | If the Take_screenshot_and_process function returns True we add an element to the Queue |

## Logout_simple ##

The difference between this function and the previous one is that this function doesn't check the screen it logs out whenever it is triggered.

| Inputs   |      Type/explanation      |
|----------|:-------------:|
| q |    Queue: Queue that is used for thread communication  |

| Outputs   |      Type/explanation      | 
|----------|:-------------:|
|-| We add an element to the Queue q to tell the other thread to finish |

## Take_screenshot_and_get_status ##

Similar to Take_screenshot_and_process function but, instead of returning a boolean we return an id number that will tell us the status of the character (attacked, hungry, safe zone, low life).

| Inputs   |      Type/explanation      |
|----------|:-------------:|
| section | list: contains sections of the screen and their thresholds |
| select |    int: id of the section which we want to select  |

| Outputs   |      Type/explanation      | 
|----------|:-------------:|
| Boolean | Boolean: True if the sum of the pixel values is less than a given threshold |

## Drag_rune_loop ## 

Given some coordinates, this functions moves a rune to the hand and execute a spell.

| Inputs   |      Type/explanation      |
|----------|:-------------:|
| hand_xy | tuple: Coordinates of the hand |
| rune_xy | tuple: Coordinate of the rune we want to transform |
| food_xy | tuple: Coordinates of the food (deprecated) |
| rune_name |  string: Name of the spell we are going to execute (deprecated) |

| Outputs   |      Type/explanation      | 
|----------|:-------------:|
| None | Takes control of the mouse and keyboard and move them to execute the actions |

## Make_runes ## 

The core of the script. This function joins several of the previous function in order to make 3 backpacks of a given rune.

| Inputs   |      Type/explanation      |
|----------|:-------------:|
| hand_xy | tuple: Coordinates of the hand |
| rune1_xy | tuple: Coordinate of the rune from the first backpack we want to transform |
| rune2_xy | tuple: Coordinate of the rune from the second backpack we want to transform |
| rune3_xy | tuple: Coordinate of the rune from the third backpack we want to transform |
| food_xy | tuple: Coordinates of the food (deprecated) |
| rune_name |  string: Name of the spell we are going to execute (deprecated) |
| section | list: contains sections of the screen and their thresholds |
| q |    Queue: Queue that is used for thread communication  |

| Outputs   |      Type/explanation      | 
|----------|:-------------:|
| None | Takes control of the mouse and keyboard and move them to execute the actions |


## Move_to_safety ## (direction_in,direction_out,section,q)

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


[Medivia]:	https://medivia.online/


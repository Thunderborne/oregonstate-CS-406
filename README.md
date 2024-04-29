# oregonstate-CS-406
## Arcane Punk Project

### About 
Arcane Punk is a Python text-based role-playing game designed for CS 406 project. Set in a fantasy-futuristic world, 
Arcane Punk tasks the user to ascend the ominous tower of Noxcaelo and free an imprisoned techno-healer guarded by 
hideous beasts and villains. The techno-healer represents humanity’s last hope in reversing a cybernetic virus 
infecting every machine in the world. Each level of the tower will present a scenario or obstacle where the user 
must make a choice. Appropriate choices will allow the user to continue their ascent, while poor choices may end 
the game for them. When the user reaches the top of the tower, they rescue the techno-healer and win the game.

### Author 
Alfred Nguyen
CS 406

### Change Log

Version 0.0 - 04.29.2004 - Initial file structure of program uploaded 

### Program Structure
| File        | Description |
| ----------- | ----------- |
| arcanepunk.py     | Main infinite loop runs and writes a data request to data_check.txt |
| data_check.txt     | A request is written on file, waiting for a microservice to read it and respond |
| arcanepunk_data.py     | Microservice arcanepunk_data.py reads data_check.txt. Retrieves the data from a dictionary. Writes the data in checker.txt. |
| checker.txt     | Data from arcanepunk_data.py is written in this text file, awaiting the main function in arcanepunk.py to read it |

### UML for Arcane Punk
![arcanepunk_uml](https://github.com/Thunderborne/oregonstate-CS-406/assets/86179332/c1bfc599-2603-41b6-97e2-df70767b5714)

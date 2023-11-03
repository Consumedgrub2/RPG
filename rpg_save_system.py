import random
import io
import os

class save_class:
    level = 0

    def __init__(self, game_level):
        self.level = int(game_level)
        print("DEBUG" + str(self.level))

    def save(self):
        print(bin(300))
        saveFile = open(os.getcwd() + "/save.sav", 'w')
        saveFile.write(str())
        saveFile.flush()
        saveFile.close()
        print("Finished Saving")
        self.level += 5
        print("DEBUG" + str(self.level))

myobject = save_class(5)
myobject.save()
print(myobject.level)

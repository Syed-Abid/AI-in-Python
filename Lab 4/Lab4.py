import random
class Environment(object):
    def __init__(self):

        # here we can set how many rooms we want
        # 0 indicates clean and 1 will indicate dirty
        self.locationcondition = {'A': '1', 'B': '1'}

        # Randomizing conditions in locations A and B
        self.locationcondition['A'] = random.choice(0, 1)
        self.locationcondition['B'] = random.choice(0, 1)


class Sreflexagent(Environment):
    def __init__(self, Environment):
        print(Environment.locationcondition)
        # place vacuum at random location
        vacuumlocation = random.randint(0, 1)
        # if vacuum at A
        if vacuumlocation==0:
            print("Vacuum is randomly placed at location A.")
            # and if location A is dirty
            if Environment.locationcondition['A']==1:
                print("Location A is dirt")
            # suck the dirt and mark it clean
                Environment.locationcondition['A']==0;
                print("Location A has been cleaned")
             # if B is dirty
            if Environment.locationcondition['B']==1:
                print("Location B is dirt")
            # suck the dirt and mark it clean
                Environment.locationcondition['B']==0;
                print("Location B has been cleaned")

        else:
            # move to B
            print("Moving to location B")
            # if B is dirty
            if Environment.locationcondition['B']==1:
                print("Location B is dirt")
            # suck the dirt and mark it clean
                Environment.locationcondition['B']==0;
                print("Location B has been cleaned")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

        #elif vacuumlocation


# DONE CLEANING
print(Environment.locationcondition)
theEnvironment = Environment()

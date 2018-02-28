import random

class ent:
    def __init__(self, hp, dmg, armor, speed, tempspeed, regen, permhp, permdmg, permarmor, permspeed, permtempspeed, permregen, magdmg, magdef, name):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor
        self.speed = speed
        self.tempspeed = tempspeed
        self.regen = regen
        self.permhp = permhp
        self.permdmg = permdmg
        self.permarmor = permarmor
        self.permspeed = permspeed
        self.permtempspeed = permtempspeed
        self.permregen = permregen
        self.magdmg = magdmg
        self.magdef = magdef
        self.name = name

tank = ent(0, 0, 0, 0, 0, 0,      100,  9, 13, 18,  0, 2, 10, 10, "tank")
glass = ent(0, 0, 0, 0, 0, 0,      40, 18,  5, 24,  0, 1, 15, 12, "glass")
paladin = ent(0, 0, 0, 0, 0, 0,    60, 10, 20, 11,  0, 6, 12, 25, "paladin")
barbarian = ent(0, 0, 0, 0, 0, 0,  80, 20,  6,  8, 10, 5,  0,  3, "barbarian")
ahvi = ent(0, 0, 0, 0, 0, 0,       70, 14, 11, 15,  0, 3, 12, 11, "ahvi")

entlist = [tank, glass, paladin, barbarian, ahvi]

def resetperms():
    for enti in entlist:
        enti.hp = enti.permhp
        enti.dmg = enti.permdmg
        enti.armor = enti.permarmor
        enti.speed = enti.permspeed
        enti.tempspeed = enti.permtempspeed
        enti.regen = enti.permregen

def battle(op1, op2):

    resetperms()

    def attack(self, target):
        done = False
        while done == False:
            print((str(self.name) + " is attacking " + (str(target.name))))
            print(str(self.name) + " has " + str(round(self.hp, 2)) + " HP" + ", " + str(target.name) + " has " + str(round(target.hp, 2)) + " HP")
            dmgtype = str(input("normal, magic, or back? "))
            if dmgtype == "normal":
                target.hp = target.hp - (self.dmg * (1 - (0.05 * target.armor / (1 + 0.05 * target.armor))))
                done = True
                print("normal attack")
            elif dmgtype == "magic":
                target.hp = target.hp - (self.magdmg * (1 - (0.05 * target.magdef / (1 + 0.05 * target.magdef))))
                done = True
                print("magic attack")
            elif dmgtype == "back":
                taketurn(self, target)

    def botattack(self, target):
        print("---")
        self.tempspeed -= speedcost
        done = False
        while done == False:
            print(("Opponent" + str(self.name) + " is attacking " + (str(target.name))))
            print(str(self.name) + " has " + str(round(self.hp, 2)) + " HP" + ", " + str(target.name) + " has " + str(round(target.hp, 2)) + " HP")
            if random.randint(0, 1) == 0:
                target.hp = target.hp - (self.dmg * (1 - (0.05 * target.armor / (1 + 0.05 * target.armor))))
                done = True
                print("Opponent has used normal attack")
            else:
                target.hp = target.hp - (self.magdmg * (1 - (0.05 * target.magdef / (1 + 0.05 * target.magdef))))
                done = True
                print("Opponent has used magic attack")

    def taketurn(turna, turnd):
        print("---")
        print(str(turna.name) + " has " + str(round(turna.hp, 2)) + " HP" + ", " + str(turnd.name) + " has " + str(round(turnd.hp, 2)) + " HP")
        print("What will " + str(turna.name) + " do?")
        turna.tempspeed -= speedcost
        choice = str(input("Attack, Flee "))
        if choice == "attack":
            attack(turna, turnd)
        elif choice == "flee":
            turna.hp = -1000

    while op1.hp > 0 and op2.hp > 0:
      if op1.speed > op2.speed:
          speedcost = op2.speed
      else:
          speedcost = op1.speed
          
      if op1.tempspeed < speedcost and op2.tempspeed < speedcost:
          op1.tempspeed += op1.speed
          op2.tempspeed += op2.speed
          op1.hp += op1.regen
          op2.hp += op2.regen
          if op1.hp > op1.permhp:
              op1.hp = op1.permhp
          if op2.hp > op2.permhp:
              op2.hp = op2.permhp

      if op1.tempspeed > op2.tempspeed:
        taketurn(op1, op2)
      elif op1.tempspeed < op2.tempspeed:
        botattack(op2, op1)
      elif op1.tempspeed == op2.tempspeed:
        if op1.speed > op2.speed:
          taketurn(op1, op2)
        elif op1.speed < op2.speed:
          botattack(op2, op1)
    if op1.hp < -500 or op2.hp < -500:
        if op1.hp < -500:
            print(str(op1.name) + " has fled!")
        if op2.hp < -500:
            print(str(op2.name) + " has fled!")
    else:
        print(round(op1.hp, 2))
        print(round(op2.hp, 2))
    resetperms()

print("To initiate a battle, the command is battle(ent, ent), the list of ents is tank, paladin, glass, barbarian, ahvi")
print("The first ent will be the character you play, and the second will be a bot. ")
print("entering the same character for both is bad. ")


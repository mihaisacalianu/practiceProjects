class Pokemon:
  def __init__(self,name_of_pokemon,level_of_pokemon,type_of_pokemon,max_health_pokemon,current_health_pokemon,is_knocked_out):
    self.name = name_of_pokemon
    self.level = level_of_pokemon
    self.health = current_health_pokemon
    self.max_health = max_health_pokemon
    self.type = type_of_pokemon
    self.is_knocked_out = is_knocked_out
    self.experience = 0;
  
  def lose_health(self,unit):
    print(f"{self.name} has lost " + str(unit) + " from its life!")
    self.health -= unit
  
  def regain_health(self,unit):
    print(f"{self.name} has regained " + str(unit) + " from its life!")
    self.health += unit
  
  def pokemon_is_knocked_out(self):
    print(f"{self.name} is knocked out his life is now 0!")
    self.health = 0;

  def revive_pokemon(self):
    print(f"{self.name} is revived his life is now 100!")
    self.health = 100;
  
  def get_experience(self):
    return self.experience
  
  def upgrade_level():
    self.level += 1


  def attack(self,pokemon):
    self.experience +=1 
    if(self.experience == 10):
      self.upgrade_level();
      self.experience = 0;
    

    if(self.type == pokemon.type):
      print("Your are attacking!")
      damage = self.level / 2
      pokemon.lose_health(damage) 
      print(f"You inflicted a damage of: {damage}")
    elif(self.type == "fire" and pokemon.type == "grass"):
      print("Your are attacking!")
      damage = self.level * 2
      print(f"You inflicted a damage of: {damage}")
      pokemon.lose_health(damage)
    elif(self.type == "grass" and pokemon.type == "fire"):
      print("Your are attacking!")
      damage = self.level / 2
      print(f"You inflicted a damage of: {damage}")
      pokemon.lose_health(damage)
    elif(self.type == "water" and pokemon.type == "fire"):
      print("Your are attacking!")
      damage = self.level * 2
      print(f"You inflicted a damage of: {damage}")
      pokemon.lose_health(damage)
    elif(self.type == "grass" and pokemon.type == "water"):
      print("Your are attacking!")
      damage = self.level * 2
      print(f"You inflicted a damage of: {damage}")
      pokemon.lose_health(damage)
    elif(self.type == "fire" and pokemon.type == "water"):
      print("Your are attacking!")
      damage = self.level / 2
      print(f"You inflicted a damage of: {damage}")
      pokemon.lose_health(damage)

class Trainer:
  def __init__(self,list_pokemons,trainer_name,number_potions,current_active_pokemon):
    self.pokemons = list_pokemons
    self.name = trainer_name
    self.potions = number_potions
    self.active = current_active_pokemon

  def use_potion(self):
    self.pokemons[self.active].regain_health(10)
    if(self.pokemons[self.active].health > self.pokemons[self.active].max_health):
      self.pokemons[self.active].health = self.pokemons[self.active].max_health
    print(f"{self.pokemons[self.active].name} is healed!" )
    self.potions -= 1
    print(f"You have {self.potions} potions left!")

  def attack(self,trainer):
    if(self.pokemons[self.active].is_knocked_out == True):
      print(f"You cannot use {self.pokemons[self.active].name} to attack it has been knocked out!")
    else:
      self.pokemons[self.active].attack(trainer.pokemons[trainer.active])
      print(f"{self.pokemons[self.active].name} has attacked your pokemon {trainer.pokemons[trainer.active].name}!")
      print(f"Your pokemon {trainer.pokemons[trainer.active].name} has {trainer.pokemons[trainer.active].health} health left!")
    
  def switch(self,numPokemon):
    if(self.pokemons[numPokemon].is_knocked_out == True):
     print(f"You cannot switch {self.pokemons[self.active].name} with {self.pokemons[numPokemon].name} it has been knocked out!")
    else:
     print(f"You switched {self.pokemons[self.active].name} with {self.pokemons[numPokemon].name}!")
    self.active = numPokemon
    
mihai_pokemons= [Pokemon("Pikaciu",20,"fire",10,20,False),
Pokemon("Charmalder",15,"fire",10,15,True),
Pokemon("Banner",12,"water",10,15,False)]


bogdan_pokemons= [
  Pokemon("Pigeotto",19,"grass",10,19,False),
Pokemon("Buzzer",15,"water",10,15,False),
Pokemon("Magnito",12,"water",10,15,False)
]



mihai = Trainer(mihai_pokemons,"mihai",10,0)
bogdan = Trainer(bogdan_pokemons,"bogdan",10,2)


mihai.switch(1)
mihai.attack(bogdan)
print("#########################")
bogdan.use_potion()
print(str(bogdan.pokemons[2].health))
mihai.switch(2)
print("#########################")
mihai.attack(bogdan)



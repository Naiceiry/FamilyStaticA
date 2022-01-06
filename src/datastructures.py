
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
            "id" : 3443,# Pruba da error con 1
            "first_name": "Tommy" , #da error si no pongo Tommy
            "last_name": "Jackson",
            "age": 33,
            "lucky_numbers":[7, 13, 22]
            },
            {
            "id" :2,
            "first_name": "Jane", 
            "last_name": "Jackson",
            "age": 35,  
            "lucky_numbers":[10, 14, 3]
            },
            {
            "id" :3,
            "first_name": "Jimmy",
            "last_name": "Jackson",
            "age": 5,
            "lucky_numbers":[1]
            } 
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999) #genero ids
    
    def add_member(self, member):
        # fill this method and update the return
        new_member = {} #arreglo por si no existe
        if "id" in member: #busca el id en menber
            new_member["id"] = int(member["id"]) #si lo encuentra , lo muestra
        else:
            new_member["id"] = self._generateId() # Si no lo incluye, tu API debe generar un id aleatorio al agregarlo a la familia
        
        new_member["first_name"] = str(member["first_name"])
        new_member["last_name"] = self.last_name
        new_member["age"] = int(member["age"])
        new_member["lucky_numbers"] = member["lucky_numbers"]
        self._members.append(new_member) #lo asigna y envia todo a new_member

    def delete_member(self, id):
 
        for position in range(len(self._members)):
            if self._members[position]["id"] == int(id): #lo ubica
                self._members.pop(position) # .pop  elimina y retorna un elemento de una lista
                return {"done": True}    
        return None

    def get_member(self, id):
      
        for member in self._members: #se va a ejecutar hasta que lo consiga
            if member["id"] == id:
                return member
            else:
                return None

   
    def get_all_members(self):
        return self._members # retorna todos los miembros 

    def update_member(self, id, member): 
        for position in range(len(self._members)):
            if self._members[position]["id"] == int(id):
                self._members[position].update(member)
                return {"done": True}

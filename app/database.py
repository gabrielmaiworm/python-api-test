from app.models import Person
from typing import List, Optional


class Database:
    def __init__(self):
        self.people: List[Person] = []
        self.counter = 1
    
    def get_all_people(self) -> List[Person]:
        return self.people
    
    def get_person_by_id(self, person_id: int) -> Optional[Person]:
        for person in self.people:
            if person.id == person_id:
                return person
        return None
    
    def add_person(self, person: Person) -> Person:
        person.id = self.counter
        self.counter += 1
        self.people.append(person)
        return person
    
    def update_person(self, person_id: int, updated_person: Person) -> Optional[Person]:
        for i, person in enumerate(self.people):
            if person.id == person_id:
                updated_person.id = person_id
                self.people[i] = updated_person
                return updated_person
        return None
    
    def delete_person(self, person_id: int) -> bool:
        for i, person in enumerate(self.people):
            if person.id == person_id:
                self.people.pop(i)
                return True
        return False


# Criando uma instância global do banco de dados
db = Database() 
from typing import List, Union
from uuid import UUID, uuid4

from fastapi import HTTPException

from models import AnimalModel, AnimalUpdateModel, SexEnum


class AnimalList:
    animal_list: List[AnimalModel] = [
        AnimalModel(
            id=uuid4(),
            name="Totó",
            age=4,
            sex=SexEnum.male,
            color="branco"
        ),
        AnimalModel(
            id=uuid4(),
            name="Belinha",
            age=1,
            sex=SexEnum.female,
            color="cinza"
        ),
    ]

    def __get_animal_by_id(self,
                           animal_id) -> Union[AnimalModel, HTTPException]:
        for animal in self.animal_list:
            if animal.id == animal_id:
                return animal
        raise HTTPException(
            status_code=404,
            detail=f'Animal with id {animal_id} does not exist'
        )

    def list_all(self) -> List[AnimalModel]:
        return self.animal_list

    def get_animal(self, animal_id) -> AnimalModel:
        return self.__get_animal_by_id(animal_id)

    def insert(self, animal: AnimalModel) -> AnimalModel:
        animal.id = uuid4()
        self.animal_list.append(animal)
        return animal

    def update(self, animal_id: UUID,
               animal_update: AnimalUpdateModel) -> AnimalModel:
        animal = self.__get_animal_by_id(animal_id)
        if animal_update.name is not None:
            animal.name = animal_update.name
        if animal_update.age is not None:
            animal.age = animal_update.age
        if animal_update.sex is not None:
            animal.sex = animal_update.sex
        if animal_update.color is not None:
            animal.color = animal_update.color
        return animal

    def delete(self, animal_id: UUID) -> AnimalModel:
        animal = self.__get_animal_by_id(animal_id)
        self.animal_list.remove(animal)
        return animal

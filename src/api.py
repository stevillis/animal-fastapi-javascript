from typing import Union
from uuid import UUID

from fastapi import APIRouter, HTTPException

from data import AnimalList
from models import AnimalModel, AnimalUpdateModel

animal_list = AnimalList()

animal_router = APIRouter()


@animal_router.get('/')
async def list_all():
    """
    List all Animals\n
    :return: List of Animals
    """
    return animal_list.list_all()


@animal_router.get('/{animal_id}')
async def get_animal(animal_id: UUID) -> AnimalModel:
    """
    Get Animal by ID\n
    :param animal_id: The ID of the Animal to be retrievied\n
    :return: The Animal retrievied by ID
    """
    return animal_list.get_animal(animal_id)


@animal_router.post('/')
async def create_animal(animal: AnimalModel) -> AnimalModel:
    """
    Create Animal\n
    :param animal: The body with Animal information to be created\n
    :return: The Animal created
    """
    return animal_list.insert(animal)


@animal_router.put('/{animal_id}')
async def update_animal(animal_id: UUID,
                        animal_update: AnimalUpdateModel
                        ) -> Union[AnimalModel, HTTPException]:
    """
    Update an Animal\n
    :param animal_id: The ID of the Animal to be Updated\n
    :param animal_update: The body with Animal information to be updated\n
    :return: The Animal updated
    """
    return animal_list.update(animal_id, animal_update)


@animal_router.delete('/{animal_id}')
async def remove_animal(animal_id: UUID) -> Union[AnimalModel, HTTPException]:
    """
    Delete an Animal\n
    :param animal_id: The ID of the Animal to be Deleted\n
    :return: The Animal Deleted
    """
    return animal_list.delete(animal_id)

from fastapi import APIRouter, HTTPException, status, Response
from typing import List, Optional

from app.models import Person
from app.database import db


router = APIRouter(prefix="/api", tags=["pessoas"])


@router.get("/pessoas", response_model=List[Person])
def get_people():
    """
    Obtém a lista de todas as pessoas cadastradas
    """
    return db.get_all_people()


@router.get("/pessoas/{person_id}", response_model=Person)
def get_person(person_id: int):
    """
    Obtém os detalhes de uma pessoa pelo ID
    """
    person = db.get_person_by_id(person_id)
    if person is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pessoa com ID {person_id} não encontrada"
        )
    return person


@router.post("/pessoas", response_model=Person, status_code=status.HTTP_201_CREATED)
def create_person(person: Person):
    """
    Cria uma nova pessoa
    """
    return db.add_person(person)


@router.put("/pessoas/{person_id}", response_model=Person)
def update_person(person_id: int, person: Person):
    """
    Atualiza os dados de uma pessoa existente
    """
    updated_person = db.update_person(person_id, person)
    if updated_person is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pessoa com ID {person_id} não encontrada"
        )
    return updated_person


@router.delete("/pessoas/{person_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_person(person_id: int):
    """
    Remove uma pessoa do sistema
    """
    success = db.delete_person(person_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pessoa com ID {person_id} não encontrada"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT) 
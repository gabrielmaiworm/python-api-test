from datetime import date
from app.models import Person
from app.database import db


def seed_database():
    """
    Popula o banco de dados com alguns dados iniciais para teste
    """
    # Lista de pessoas para adicionar inicialmente
    initial_people = [
        Person(
            name="Maria Santos",
            email="maria@example.com",
            birth_date=date(1985, 5, 15),
            phone="(21) 99876-5432"
        ),
        Person(
            name="Carlos Oliveira",
            email="carlos@example.com",
            birth_date=date(1992, 8, 22),
            phone="(11) 91234-5678"
        ),
        Person(
            name="Ana Silva",
            email="ana@example.com",
            birth_date=date(1978, 3, 10),
            phone="(31) 98765-4321"
        )
    ]
    
    # Adiciona cada pessoa ao banco
    for person in initial_people:
        db.add_person(person)
    
    print(f"Banco de dados populado com {len(initial_people)} pessoas.")


if __name__ == "__main__":
    # Isso permite executar este arquivo diretamente para popular o banco
    seed_database() 
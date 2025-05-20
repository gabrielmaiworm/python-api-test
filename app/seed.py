from datetime import date
from app.models import Funcionario, Cargo
from app.database import db
import random


def seed_database():
    """
    Popula o banco de dados com alguns dados iniciais para teste
    """
    # Lista de funcionários para adicionar inicialmente
    initial_funcionarios = [
        Funcionario(
            nome="Maria Santos",
            email="maria@exemplo.com",
            data_nascimento=date(1985, 5, 15),
            telefone="(21) 99876-5432",
            cargo=Cargo.GERENTE,
            data_contratacao=date(2018, 3, 10),
            salario=12500.00
        ),
        Funcionario(
            nome="Carlos Oliveira",
            email="carlos@exemplo.com",
            data_nascimento=date(1992, 8, 22),
            telefone="(11) 91234-5678",
            cargo=Cargo.DESENVOLVEDOR,
            data_contratacao=date(2020, 7, 15),
            salario=7800.00
        ),
        Funcionario(
            nome="Ana Silva",
            email="ana@exemplo.com",
            data_nascimento=date(1978, 3, 10),
            telefone="(31) 98765-4321",
            cargo=Cargo.ANALISTA,
            data_contratacao=date(2019, 1, 5),
            salario=6500.00
        ),
        Funcionario(
            nome="Pedro Almeida",
            email="pedro@exemplo.com",
            data_nascimento=date(1990, 11, 27),
            telefone="(11) 97777-8888",
            cargo=Cargo.DESENVOLVEDOR,
            data_contratacao=date(2021, 3, 10),
            salario=7200.00
        ),
        Funcionario(
            nome="Juliana Costa",
            email="juliana@exemplo.com",
            data_nascimento=date(1988, 4, 15),
            telefone="(21) 96666-7777",
            cargo=Cargo.RECURSOS_HUMANOS,
            data_contratacao=date(2017, 8, 22),
            salario=5900.00
        ),
        Funcionario(
            nome="Fernando Gomes",
            email="fernando@exemplo.com",
            data_nascimento=date(1982, 9, 30),
            telefone="(11) 95555-6666",
            cargo=Cargo.DIRETOR,
            data_contratacao=date(2015, 2, 15),
            salario=18000.00
        ),
        Funcionario(
            nome="Mariana Lima",
            email="mariana@exemplo.com",
            data_nascimento=date(1995, 7, 8),
            telefone="(31) 94444-5555",
            cargo=Cargo.ANALISTA,
            data_contratacao=date(2022, 5, 2),
            salario=6200.00
        ),
        Funcionario(
            nome="Roberto Cardoso",
            email="roberto@exemplo.com",
            data_nascimento=date(1980, 1, 20),
            telefone="(11) 93333-4444",
            cargo=Cargo.FINANCEIRO,
            data_contratacao=date(2018, 11, 10),
            salario=9500.00
        ),
        Funcionario(
            nome="Camila Pereira",
            email="camila@exemplo.com",
            data_nascimento=date(1993, 6, 12),
            telefone="(21) 92222-3333",
            cargo=Cargo.DESENVOLVEDOR,
            data_contratacao=date(2021, 9, 15),
            salario=7500.00
        ),
        Funcionario(
            nome="Lucas Martins",
            email="lucas@exemplo.com",
            data_nascimento=date(1991, 12, 5),
            telefone="(31) 91111-2222",
            cargo=Cargo.SUPORTE,
            data_contratacao=date(2020, 4, 20),
            salario=4800.00
        )
    ]
    
    # Adiciona cada funcionário ao banco
    for funcionario in initial_funcionarios:
        db.add_funcionario(funcionario)
    
    print(f"Banco de dados populado com {len(initial_funcionarios)} funcionários.")


if __name__ == "__main__":
    # Isso permite executar este arquivo diretamente para popular o banco
    seed_database() 
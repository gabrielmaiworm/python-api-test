from fastapi import APIRouter, HTTPException, status, Response, Query, Path
from typing import List, Optional

from datetime import date
from app.models import Funcionario, EstatisticasGerais, Cargo
from app.database import db


router = APIRouter(prefix="/api", tags=["funcionarios"])


@router.get("/funcionarios", response_model=List[Funcionario])
def get_funcionarios(
    cargo: Optional[str] = None,
    salario_min: Optional[float] = None,
    salario_max: Optional[float] = None,
    data_contratacao_inicial: Optional[date] = None,
    data_contratacao_final: Optional[date] = None
):
    """
    Obtém a lista de funcionários, com opções de filtragem
    
    - **cargo**: Filtra por cargo específico
    - **salario_min**: Filtra por salário mínimo
    - **salario_max**: Filtra por salário máximo
    - **data_contratacao_inicial**: Filtra por data de contratação inicial
    - **data_contratacao_final**: Filtra por data de contratação final
    """
    resultado = db.get_all_funcionarios()
    
    if cargo:
        resultado = [f for f in resultado if f.cargo.value == cargo]
    
    if salario_min is not None or salario_max is not None:
        resultado = db.filtrar_por_salario(salario_min, salario_max)
    
    if data_contratacao_inicial is not None or data_contratacao_final is not None:
        resultado = db.filtrar_por_data_contratacao(data_contratacao_inicial, data_contratacao_final)
    
    return resultado


@router.get("/funcionarios/{funcionario_id}", response_model=Funcionario)
def get_funcionario(funcionario_id: int = Path(..., description="ID do funcionário")):
    """
    Obtém os detalhes de um funcionário pelo ID
    """
    funcionario = db.get_funcionario_by_id(funcionario_id)
    if funcionario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Funcionário com ID {funcionario_id} não encontrado"
        )
    return funcionario


@router.post("/funcionarios", response_model=Funcionario, status_code=status.HTTP_201_CREATED)
def create_funcionario(funcionario: Funcionario):
    """
    Cria um novo funcionário
    """
    return db.add_funcionario(funcionario)


@router.put("/funcionarios/{funcionario_id}", response_model=Funcionario)
def update_funcionario(
    funcionario_id: int = Path(..., description="ID do funcionário"), 
    funcionario: Funcionario = ...
):
    """
    Atualiza os dados de um funcionário existente
    """
    updated_funcionario = db.update_funcionario(funcionario_id, funcionario)
    if updated_funcionario is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Funcionário com ID {funcionario_id} não encontrado"
        )
    return updated_funcionario


@router.delete("/funcionarios/{funcionario_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_funcionario(funcionario_id: int = Path(..., description="ID do funcionário")):
    """
    Remove um funcionário do sistema
    """
    success = db.delete_funcionario(funcionario_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Funcionário com ID {funcionario_id} não encontrado"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/funcionarios/filtro/salario", response_model=List[Funcionario])
def filtrar_por_salario(
    salario_min: Optional[float] = Query(None, description="Salário mínimo", ge=0),
    salario_max: Optional[float] = Query(None, description="Salário máximo", ge=0)
):
    """
    Filtra funcionários por faixa salarial
    """
    return db.filtrar_por_salario(salario_min, salario_max)


@router.get("/funcionarios/filtro/data-contratacao", response_model=List[Funcionario])
def filtrar_por_data_contratacao(
    data_inicial: Optional[date] = Query(None, description="Data inicial de contratação"),
    data_final: Optional[date] = Query(None, description="Data final de contratação")
):
    """
    Filtra funcionários por data de contratação
    """
    return db.filtrar_por_data_contratacao(data_inicial, data_final)


@router.get("/funcionarios/filtro/cargo/{cargo}", response_model=List[Funcionario])
def filtrar_por_cargo(cargo: str = Path(..., description="Cargo para filtrar")):
    """
    Filtra funcionários por cargo
    """
    return db.filtrar_por_cargo(cargo)


@router.get("/funcionarios/estatisticas", response_model=EstatisticasGerais)
def get_estatisticas():
    """
    Obtém estatísticas sobre os funcionários
    
    Retorna:
    - Total de funcionários
    - Total de salários
    - Salário médio
    - Estatísticas detalhadas por cargo
    """
    return db.calcular_estatisticas()


@router.get("/cargos", response_model=List[str])
def get_cargos():
    """
    Retorna a lista de todos os cargos disponíveis
    """
    return [cargo.value for cargo in Cargo] 
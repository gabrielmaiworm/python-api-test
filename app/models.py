from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from datetime import date
from enum import Enum


class Cargo(str, Enum):
    DESENVOLVEDOR = "Desenvolvedor"
    ANALISTA = "Analista"
    GERENTE = "Gerente"
    DIRETOR = "Diretor"
    ESTAGIARIO = "Estagiário"
    ADMINISTRATIVO = "Administrativo"
    RECURSOS_HUMANOS = "Recursos Humanos"
    FINANCEIRO = "Financeiro"
    SUPORTE = "Suporte"
    OUTROS = "Outros"


class Funcionario(BaseModel):
    id: Optional[int] = None
    nome: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., min_length=5, max_length=100)
    data_nascimento: Optional[date] = None
    telefone: Optional[str] = Field(None, max_length=20)
    
    # Novos campos para funcionários
    cargo: Cargo = Field(..., description="Cargo do funcionário na empresa")
    data_contratacao: date = Field(..., description="Data de contratação do funcionário")
    salario: float = Field(..., ge=0, description="Salário mensal do funcionário em reais")
    
    class Config:
        json_schema_extra = {
            "example": {
                "nome": "João Silva",
                "email": "joao@example.com",
                "data_nascimento": "1990-01-01",
                "telefone": "(11) 98765-4321",
                "cargo": "Desenvolvedor",
                "data_contratacao": "2021-03-15",
                "salario": 5000.00
            }
        }


class EstatisticasCargo(BaseModel):
    cargo: str
    quantidade: int
    salario_total: float
    salario_medio: float


class EstatisticasGerais(BaseModel):
    total_funcionarios: int
    total_salarios: float
    salario_medio: float
    estatisticas_por_cargo: List[EstatisticasCargo] 
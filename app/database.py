from app.models import Funcionario, EstatisticasCargo, EstatisticasGerais
from typing import List, Optional, Dict
from datetime import date


class Database:
    def __init__(self):
        self.funcionarios: List[Funcionario] = []
        self.counter = 1
    
    def get_all_funcionarios(self) -> List[Funcionario]:
        return self.funcionarios
    
    def get_funcionario_by_id(self, funcionario_id: int) -> Optional[Funcionario]:
        for funcionario in self.funcionarios:
            if funcionario.id == funcionario_id:
                return funcionario
        return None
    
    def add_funcionario(self, funcionario: Funcionario) -> Funcionario:
        funcionario.id = self.counter
        self.counter += 1
        self.funcionarios.append(funcionario)
        return funcionario
    
    def update_funcionario(self, funcionario_id: int, updated_funcionario: Funcionario) -> Optional[Funcionario]:
        for i, funcionario in enumerate(self.funcionarios):
            if funcionario.id == funcionario_id:
                updated_funcionario.id = funcionario_id
                self.funcionarios[i] = updated_funcionario
                return updated_funcionario
        return None
    
    def delete_funcionario(self, funcionario_id: int) -> bool:
        for i, funcionario in enumerate(self.funcionarios):
            if funcionario.id == funcionario_id:
                self.funcionarios.pop(i)
                return True
        return False
    
    def filtrar_por_salario(self, salario_min: Optional[float] = None, salario_max: Optional[float] = None) -> List[Funcionario]:
        """
        Filtra funcionários por faixa salarial
        """
        resultado = self.funcionarios.copy()
        
        if salario_min is not None:
            resultado = [f for f in resultado if f.salario >= salario_min]
        
        if salario_max is not None:
            resultado = [f for f in resultado if f.salario <= salario_max]
            
        return resultado
    
    def filtrar_por_data_contratacao(self, data_inicial: Optional[date] = None, data_final: Optional[date] = None) -> List[Funcionario]:
        """
        Filtra funcionários por período de contratação
        """
        resultado = self.funcionarios.copy()
        
        if data_inicial is not None:
            resultado = [f for f in resultado if f.data_contratacao >= data_inicial]
        
        if data_final is not None:
            resultado = [f for f in resultado if f.data_contratacao <= data_final]
            
        return resultado
    
    def filtrar_por_cargo(self, cargo: str) -> List[Funcionario]:
        """
        Filtra funcionários por cargo
        """
        return [f for f in self.funcionarios if f.cargo.value == cargo]
    
    def calcular_estatisticas(self) -> EstatisticasGerais:
        """
        Calcula estatísticas gerais e por cargo dos funcionários
        """
        if not self.funcionarios:
            return EstatisticasGerais(
                total_funcionarios=0,
                total_salarios=0,
                salario_medio=0,
                estatisticas_por_cargo=[]
            )
        
        # Agrupa funcionários por cargo
        funcionarios_por_cargo: Dict[str, List[Funcionario]] = {}
        for f in self.funcionarios:
            cargo = f.cargo.value
            if cargo not in funcionarios_por_cargo:
                funcionarios_por_cargo[cargo] = []
            funcionarios_por_cargo[cargo].append(f)
        
        # Calcula estatísticas por cargo
        estatisticas_por_cargo = []
        for cargo, funcionarios in funcionarios_por_cargo.items():
            qtd = len(funcionarios)
            salario_total = sum(f.salario for f in funcionarios)
            salario_medio = salario_total / qtd if qtd > 0 else 0
            
            estatisticas_por_cargo.append(EstatisticasCargo(
                cargo=cargo,
                quantidade=qtd,
                salario_total=salario_total,
                salario_medio=salario_medio
            ))
        
        # Calcula estatísticas gerais
        total_funcionarios = len(self.funcionarios)
        total_salarios = sum(f.salario for f in self.funcionarios)
        salario_medio = total_salarios / total_funcionarios if total_funcionarios > 0 else 0
        
        return EstatisticasGerais(
            total_funcionarios=total_funcionarios,
            total_salarios=total_salarios,
            salario_medio=salario_medio,
            estatisticas_por_cargo=estatisticas_por_cargo
        )


# Criando uma instância global do banco de dados
db = Database() 
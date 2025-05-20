from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router
from app.seed import seed_database


app = FastAPI(
    title="API de Funcionários",
    description="API para gerenciamento de funcionários de uma empresa",
    version="1.0.0"
)

# Configuração do CORS para permitir acesso de outras origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especifique as origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluindo as rotas da API
app.include_router(router)


@app.get("/")
def read_root():
    return {
        "message": "Bem-vindo à API de Funcionários",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.on_event("startup")
def startup_event():
    """
    Função executada na inicialização da API
    """
    # Popula o banco de dados com dados iniciais
    seed_database() 
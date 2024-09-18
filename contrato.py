from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt

from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Zapflow com Gemini"
    produto2 = "Zapflow com ChatGPT"
    produto3 = "Zapflow com Llmama3.0"


class Vendas(BaseModel):
    """
    Modelo de dados para vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): valor da compra
        quantidade (PositiveInt): quantidade de produtos
        produto (ProdutoEnum): produto comprado
    """

    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum




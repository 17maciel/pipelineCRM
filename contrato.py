from datetime import datetime
from typing import Tuple

from pydantic import BaseModel, EmailStr, validate_call

from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Zapflow com Gemini"
    produto2 = "Zapflow com ChatGPT"
    produto3 = "Zapflow com Llmama3.0"


class Vendas(BaseModel):
    email: EmailStr
    data_hora: datetime
    valor: float
    quantidade: int
    produto: ProdutoEnum


    @validate_call('produto')
    def categoria_deve_estar_no_enum(cls, v):
        return v


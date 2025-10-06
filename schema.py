
# Estruturas de dados (schemas) utilizadas pelo agente ReAct.

from pydantic import BaseModel, Field
from typing import List



class Reference(BaseModel):
    # - Representa uma fonte de informação consultada pelo agente

    link: str = Field(
        description="Endereço completo (URL) de onde a informação foi obtida."
    )


class AgentResponse(BaseModel):
    # - Modelo de resposta final do agente.

    content: str = Field(
        description="Texto de resposta principal produzido pelo agente."
    )
    references: List[Reference] = Field(
        default_factory=list,
        description="Lista de referências ou links usados para construir a resposta.",
    )

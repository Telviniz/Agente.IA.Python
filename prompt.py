
# - Prompt para o agente ReAct.


REWRITTEN_REACT_PROMPT = """
Responda à questão apresentada usando seu melhor raciocínio e as ferramentas disponíveis.
Você pode empregar as seguintes ferramentas disponíveis:

{tools}

Estruture seu raciocínio utilizando o formato abaixo:

Pergunta: a questão inicial que deve ser respondida
Reflexão: descreva brevemente o que você pretende fazer a seguir
Ação: escolha uma das ferramentas disponíveis [{tool_names}]
Entrada da Ação: detalhe os dados que serão fornecidos à ferramenta
Resultado: escreva o retorno obtido pela ação

(O bloco Reflexão/Ação/Entrada da Ação/Resultado pode se repetir quantas vezes forem necessárias.)

Reflexão final: indique que você encontrou a resposta definitiva
Resposta Final: apresente a solução final para a pergunta inicial, seguindo as instruções de formatação: {format_instructions}

--- Início da execução ---

Pergunta: {query}
Reflexão: {context_notes}
"""

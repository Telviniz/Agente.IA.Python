
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

# Importações locais *
from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schema import AgentResponse


# - Inicialização do ambiente 
load_dotenv()

# - Configuração dos componentes
search_tool = TavilySearch()  # (ferramenta de busca)
available_tools = [search_tool]

# - Instância do modelo de linguagem
llm_model = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",  
    temperature=0.6           
)

# - Carrega um prompt base do LangChain Hub
# (pode ser substituído futuramente por um prompt local)
try:
    base_react_prompt = hub.pull("hwchase17/react")
except Exception:
    base_react_prompt = None  

# - Parser para validar e converter o output do agente
response_parser = PydanticOutputParser(pydantic_object=AgentResponse)

# - Criação do template de prompt personalizado
validated_prompt = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["query", "context_notes", "available_tools"]
).partial(format_instructions=response_parser.get_format_instructions())

# - Criação do agente React
react_agent = create_react_agent(
    llm=llm_model,
    tools=available_tools,
    prompt=validated_prompt if validated_prompt else base_react_prompt,
)

# - Executor do agente (controla o loop de pensamento e ação)
react_executor = AgentExecutor(
    agent=react_agent,
    tools=available_tools,
    verbose=True
)

extract_step = RunnableLambda(lambda output: output.get("output"))
parse_step = RunnableLambda(lambda output: response_parser.parse(output))

# - Cadeia final de execução (pipeline)
react_chain = react_executor | extract_step | parse_step


# Função principal *
def run_agent():
    """
    Executa uma demonstração simples de busca.
    """
    query_text = (
        'Find three recent online postings for "AI Engineer" positions that reference LangChain. '
        'Summarize their main requirements and descriptions.'
    )

    final_result = react_chain.invoke(
        input={
            "input": query_text,
        }
    )

    print("\n=== AGENT RESULT ===")
    print(final_result)


if __name__ == "__main__":
    run_agent()

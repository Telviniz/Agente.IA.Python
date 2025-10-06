# PythonAgenteIA

Agente inteligente baseado no framework **LangChain**, integrando **Google Gemini 1.5** e **Tavily Search**.

---

## 1. Funcionalidades
- Executa raciocínio passo a passo (ReAct Framework)
- Integra modelo LLM (Gemini) e ferramenta de busca Tavily
- Valida saídas com `Pydantic`
- Totalmente modular (prompt, schema e agente separados)

---

## 2. Estrutura do Projeto
```
PythonAgenteIA/
 └── src/
     ├── main.py        # núcleo do agente
     ├── prompt.py      # template de prompt ReAct
     └── schema.py      # modelo de dados do output
```

---

## 3. Instalacao
```bash
git clone https://github.com/seuusuario/PythonAgenteIA.git
cd PythonAgenteIA
pip install -r requirements.txt
```

---

## 4. Configuracao do .env
Crie um arquivo `.env` com suas chavs de API:

```env
GOOGLE_API_KEY=...
TAVILY_API_KEY=...
```

---

## 5. Execução
```bash
python src/main.py
```

---

## 6. Autor:
Telviniz



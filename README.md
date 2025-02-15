# A solução
Serviço de completação textual. O usuário digita e a IA completa.

_Veja a seguir o passo a passo para rodar a solução:_


## 1. Clonar o Repositório
Para obter o código-fonte, clone o repositório do GitHub executando o seguinte comando no terminal:

 git clone https://github.com/roalves1234/trabalho-api.git

## 2. Acessar o Diretório do Projeto
Entre na pasta do repositório clonado:

 cd trabalho-api

## 3. Criar e Ativar um Ambiente Virtual

Crie um ambiente virtual para gerenciar as dependências do projeto:

 python3 -m venv venv

Ative o ambiente virtual:

  venv\Scripts\activate

## 4. Instalar Dependências

Copie o arquivo `pyproject.toml` para a pasta onde está o ambiente virtual.

Instale as dependências listadas no arquivo `pyproject.toml`:

 uv sync


## 5. Executar o Servidor FastAPI
Para rodar a aplicação FastAPI, execute:

 uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Isso iniciará o servidor na porta 8000. Você pode acessar a API através do navegador ou usar ferramentas como **Postman** para testar os endpoints.

- Documentação interativa Swagger: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Documentação Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 6. Variáveis de Ambiente

crie um arquivo **.env** na raiz do projeto e informe as seguintes APIs de LLMs e suas credenciais:

OPENAI_API_KEY=(informe a chave aqui)
GOOGLE_API_KEY=(informe a chave aqui)

Para carregar essas variáveis, você pode usar a biblioteca `python-dotenv` e adicioná-las no código conforme necessário.

## 7. Testar a API
Você pode testar a API utilizando **cURL**, **Postman** ou diretamente na documentação interativa do Swagger.

Exemplo de requisição `GET` utilizando cURL:

 curl -X 'GET' 'http://127.0.0.1:8000/' -H 'accept: application/json'

## 8. Encerrando o Servidor
Para parar a execução do servidor, pressione `CTRL + C` no terminal.

## 9. Desativar o Ambiente Virtual (Opcional)
Se você quiser sair do ambiente virtual, basta executar:

 deactivate

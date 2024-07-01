# Progeto-API
Progeto De Construção De Api
# Welcome to GitHub Desktop!

This is your README. READMEs are where you can communicate what your project is and how to use it.

Hello, eu sou o José Da Ressurreição.  
Vamos apresentar o nosso projeto (API) começando por uma breve introdução.

## Introdução

API - É um lugar para disponibilizar recursos e/ou funcionalidades.  
Meu Objetivo - foi Criar uma API que disponibiliza a consulta, criação, edição e exclusão de celulares disponiveis em uma loja.

Aqui estão os principais pontos do código: 
*Listagem de todos os celulares:

Endpoint: /celulares
Método: GET
Descrição: Retorna uma lista de todos os celulares cadastrados.

*
Obter celular por ID:

Endpoint: /celulares/<int:id>
Método: GET
Descrição: Retorna os detalhes de um celular específico baseado no ID fornecido.

*Editar celular por ID:

Endpoint: /celulares/<int:id>
Método: PUT
Descrição: Permite editar as informações de um celular específico.

*Incluir novo celular:

Endpoint: /celulares
Método: POST
Descrição: Permite adicionar um novo celular à lista. As informações do novo celular são enviadas no corpo da requisição em formato JSON.



Após a execução do codigo, no seu terminal irá aparecer esta informação:
 PS C:\Users\user\Desktop\exame> & C:/Users/user/AppData/Local/Programs/Python/Python312/python.exe c:/Users/user/Desktop/exame/app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:5000
Press CTRL+C to quit   
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 194-423-140
 *

 Para acessar sua API no endereço http://localhost:5000, para acessar a Api terá que clicar no (CTRL & botão esquerdo do mouse), Irá abrir o seu navegador e para ter acesso a lista e informações dos celulares na API no endereço http://localhost:5000 terá que add no endereço (/celulares) ficará (http://localhost:5000/celulares), após tudo isso é só recarregar a pagina... 

*xcluir celular por ID:

Endpoint: /celulares/<int:id>
Método: DELETE
Descrição: Permite excluir um celular específico baseado no ID fornecido na URL.


Tratamento de erro para rotas não encontradas:

Função: pagina_nao_encontrada
Descrição: Trata erros 404 (página não encontrada) e retorna uma resposta JSON apropriada indicando que a página não foi encontrada.



URL base - `localhost`  

## Endpoints

- `GET` localhost/celulares - Lista todos os celuluares
- `POST` localhost/celulares - adicionar informações de  um novo celular no sistema
- `GET` localhost/celulares/id - Consulta um celular específico
- `PUT` localhost/celulares/id - Editar informações de  um celular específico
- `DELETE` localhost/celulares/id - Exclui  um celulalar específico no sistema

Trabalhei com o Postman para o teste destas funcionalidades.

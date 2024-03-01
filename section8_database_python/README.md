O que é SQLite?
- Um arquivo que é utilizado como banco de dados.
- É mais avançado que um arquivo JSON.
- É muito utilizado por aplicativo de celular, para salvar informações de uma aplicação.
- A diferença crucial entre o SQLite e um servidor mais robusto como o MySQL, seria a quantidade de conexões suportadas. O SQLite não foi criado com a intenção de receber muitas conexões.

Use o DBeaver Community para visualizar o banco SQLite
- Para instalar acesse o site:
- https://dbeaver.io/download/

Para acessar o banco com o DBeaver siga o passo a passo:
- New Database Connection (ctrl + shift + n)
- Busque por SQLite e clique no icone do resultado da busca e aperte next
- Em Main, General, Connect By: Host, clique em "Open..." e selecione o arquivo db.sqlite3 criado na aula.
- Clique em "Test Connection" e faça o download dos drivers necessarios
- Clique em "Finish"

Para executar query usando o Python é necessário instalar a biblioteca pymysql
- Execute o comando:
- pip install pymysql
- Execute o seguinte comando para instalar os "type"s do pymysql:
- pip install types-pymysql

Use python-dotenv para conectar com MySQL
- Execute o comando para instalar:
- pip install python-dotenv
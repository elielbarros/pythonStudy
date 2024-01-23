"""
# English
(Part 1) Basics of the HTTP protocol (HyperText Transfer Protocol)
HTTP (HyperText Transfer Protocol) is a protocol used to send and receive
data on the Internet. It works in client/server mode, where the client
(your browser, for example) makes a request to the server
(website, for example), which responds with the appropriate data.

The client request message must include data such as:
- The HTTP method
     - reading (safe) - GET, HEAD (headers), OPTIONS (supported methods)
     - writing - POST, PUT (replaces), PATCH (updates), DELETE
- The address of the resource to be accessed (/users/)
- HTTP headers (Content-Type, Authorization)
- The body of the message (if necessary, according to the HTTP method)

The server response message must include data such as
- HTTP status code (200 success, 404 Not found, 301 Moved Permanently)
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- HTTP headers (Content-Type, Accept)
- The body of the message (Maybe empty in some cases)

# Portuguese
(Parte 1) Básico do protocolo HTTP (HyperText Transfer Protocol)
HTTP (HyperText Transfer Protocol) é um protocolo usado enviar e receber
dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente
(seu navegador, por exemplo) faz uma requisição ao servidor
(site, por exemplo), que responde com os dados adequados.

A mensagem de requisição do cliente deve incluir dados como:
- O método HTTP
    - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
    - escrita - POST, PUT (substitui), PATCH (atualiza), DELETE
- O endereço do recurso a ser acessado (/users/)
- Os cabeçalhos HTTP (Content-Type, Authorization)
- O Corpo da mensagem (caso necessário, de acordo com o método HTTP)

A mensagem de resposta do servidor deve incluir dados como:
- código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- Os cabeçalhos HTTP (Content-Type, Accept)
- O corpo da mensagem (Pode estar em vazio em alguns casos)
"""

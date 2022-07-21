# WebControlURL
WebApp para controloar as URLs a serem bloqueadas, que podem ser consumidas via API, como Fabric Connector da Fortinet.

Este WebApp foi desenvolvido em Python usando Django, e implementado com Gunicorn e NGinx no CentOS 8.

WebApp permite o acesso autenticado via LDAP na estrutura de AD, permite apenas edição de usuários autenticados, enquanto os não autenticados podem apenas ver.

Podemos adicionar URLs na base, uma por vez, colocando as informações necessárias e de registro, além de poder importar um arquivo CSV, que tem uma estrutura própria, com diversas URLs, e resulta em um arquivo de resultado, mostrando as importas que foram feitas com sucesso e as que falharam.

Pelo páginas de Admin do Django, os usuários Staffs, podem alterar, remover e acompanhar as inserções e deleções.

Projeto criado para ter um repositório único, que pode ser consumido por outros serviços.

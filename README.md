# Sistema Educacional

Aplicação web desenvolvida com **Python, Django e Docker** para gerenciamento de alunos e cursos.

O sistema permite cadastrar alunos, cadastrar cursos, associar alunos aos cursos e consultar essas informações por meio de páginas web. A aplicação também disponibiliza o painel administrativo do Django para gerenciar os registros.

## Funcionalidades

- Cadastro e gerenciamento de alunos.
- Cadastro e gerenciamento de cursos.
- Associação de vários alunos a um curso.
- Consulta de alunos cadastrados.
- Consulta de cursos e respectivos alunos matriculados.
- Painel administrativo para gerenciamento dos dados.
- Banco de dados SQLite.
- Ambiente de execução conteinerizado com Docker.

## Tecnologias utilizadas

- Python 3.12
- Django
- SQLite
- Docker
- Docker Compose
- HTML e CSS
- Git e GitHub

## Requisitos

Antes de executar o projeto, verifique se a máquina possui os seguintes requisitos:

- **Docker Engine:** versão compatível com o sistema operacional.
- **Docker Compose:** preferencialmente o plugin Compose V2, que disponibiliza o comando `docker compose`.
- **Git:** necessário para clonar o repositório.
- **Porta 8000 disponível:** utilizada para acessar a aplicação localmente.
- **Conexão com a internet:** necessária para baixar a imagem Python e instalar as dependências durante a primeira compilação.

Não é necessário instalar Python, Django ou SQLite diretamente na máquina host. Essas dependências são executadas no ambiente Docker.

## Estrutura do projeto

```text
sistema_educacional/
├── escola/
│   ├── migrations/
│   ├── templates/
│   │   └── escola/
│   │       ├── home.html
│   │       ├── alunos.html
│   │       └── cursos.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── sistema_educacional/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── data/
├── .dockerignore
├── compose.yaml
├── Dockerfile
├── manage.py
├── requirements.txt
└── README.md
```

A pasta `data/` é utilizada para armazenar o banco de dados SQLite dentro do ambiente do projeto. Ela pode ser criada automaticamente pela configuração do Docker.

## 1. Instalar o Docker

### Ubuntu e distribuições Linux baseadas em Debian

Caso o Docker ainda não esteja instalado, siga as instruções oficiais:

https://docs.docker.com/engine/install/ubuntu/

Depois da instalação, verifique as versões:

```bash
docker --version
docker compose version
git --version
```

Se o comando `docker compose version` não funcionar, verifique a instalação do plugin Docker Compose.

> **Observação:** em algumas instalações Linux, os comandos Docker exigem `sudo`. Se necessário, adicione `sudo` aos comandos apresentados neste documento.

## 2. Clonar o repositório

Clone o projeto publicado no GitHub:

```bash
git clone https://github.com/wallacewts/sistema_educacional.git
```

Entre na pasta criada pelo Git:

```bash
cd SEU_REPOSITORIO
```

Confirme que os principais arquivos estão presentes:

```bash
ls
```

A saída deve incluir arquivos como `Dockerfile`, `compose.yaml`, `requirements.txt` e `manage.py`.

## 3. Construir a imagem Docker

Na raiz do projeto, execute:

```bash
docker compose build
```

Esse comando constrói a imagem da aplicação, instala as dependências definidas em `requirements.txt` e prepara o ambiente Python.

Na primeira execução, o processo pode demorar alguns minutos.

## 4. Criar as migrações do banco de dados

Antes de iniciar a aplicação, verifique se os arquivos de migração dos modelos existem.

Para gerar migrações quando houver alterações nos modelos:

```bash
docker compose run --rm web python manage.py makemigrations
```

Em seguida, aplique as migrações:

```bash
docker compose run --rm web python manage.py migrate
```

As migrações criam as tabelas necessárias para armazenar alunos, cursos e suas associações.

Se o repositório já contiver as migrações versionadas, normalmente basta executar o comando `migrate`.

## 5. Iniciar a aplicação

Execute:

```bash
docker compose up -d
```

O parâmetro `-d` mantém os contêineres em execução em segundo plano.

Verifique o estado dos serviços:

```bash
docker compose ps
```

Para acompanhar os logs da aplicação:

```bash
docker compose logs -f web
```

Para interromper a visualização dos logs, pressione `Ctrl + C`. Isso não encerra os contêineres quando os logs estão sendo acompanhados dessa forma.

## 6. Criar o usuário administrador

Com a aplicação em execução, abra outro terminal na pasta do projeto e execute:

```bash
docker compose exec web python manage.py createsuperuser
```

Informe os dados solicitados pelo Django, como nome de usuário, e-mail e senha.

Esse usuário permitirá acessar o painel administrativo e gerenciar os registros.

## 7. Acessar o sistema

Abra o navegador e utilize os seguintes endereços:

| Página | Endereço |
|---|---|
| Página inicial | http://localhost:8000/ |
| Alunos cadastrados | http://localhost:8000/alunos/ |
| Cursos cadastrados | http://localhost:8000/cursos/ |
| Painel administrativo | http://localhost:8000/admin/ |

No painel administrativo, entre com as credenciais do superusuário criado anteriormente.

A partir dele, é possível cadastrar alunos e cursos, além de associar alunos aos cursos disponíveis.

## 8. Comandos úteis

| Operação | Comando |
|---|---|
| Iniciar em segundo plano | `docker compose up -d` |
| Iniciar exibindo os logs | `docker compose up` |
| Parar os serviços | `docker compose down` |
| Consultar o estado dos serviços | `docker compose ps` |
| Consultar os logs | `docker compose logs -f web` |
| Executar migrações | `docker compose exec web python manage.py migrate` |
| Criar migrações | `docker compose exec web python manage.py makemigrations` |
| Criar administrador | `docker compose exec web python manage.py createsuperuser` |
| Abrir terminal no contêiner | `docker compose exec web sh` |
| Reconstruir a imagem | `docker compose build` |

Se a aplicação estiver parada, utilize `docker compose run --rm web ...` para comandos administrativos que precisam executar em um contêiner temporário, ou inicie os serviços antes de utilizar `docker compose exec`.

## 9. Persistência dos dados

O banco de dados SQLite é armazenado no caminho `/app/data/db.sqlite3` dentro do contêiner, conforme a configuração do Django.

O arquivo é mantido em um volume Docker chamado `django_data`, configurado no `compose.yaml`.

Por isso, parar ou recriar os contêineres com:

```bash
docker compose down
```

não remove automaticamente os dados armazenados no volume.

**Atenção:** o comando abaixo remove também os volumes associados ao projeto e pode apagar o banco de dados:

```bash
docker compose down -v
```

Utilize-o somente quando realmente desejar excluir os dados persistidos.

## 10. Solução de problemas

### A porta 8000 já está em uso

Verifique qual processo está utilizando a porta ou altere o mapeamento no `compose.yaml`.

Por exemplo:

```yaml
ports:
  - "8001:8000"
```

Nesse caso, a aplicação será acessada por http://localhost:8001/.

### Alterações nos modelos não aparecem no banco

Gere as migrações e aplique-as:

```bash
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate
```

Se o contêiner estiver parado, inicie-o ou utilize `docker compose run --rm web` nos comandos administrativos.

### A aplicação não inicia

Consulte os logs:

```bash
docker compose logs --tail=100 web
```

Verifique também se a imagem foi construída corretamente:

```bash
docker compose build
docker compose up -d
```

### O Django não encontra os templates

Confirme que os arquivos HTML estão no diretório correto:

```text
escola/templates/escola/
```

Verifique também se os nomes dos arquivos correspondem aos utilizados nas views.

## Objetivo acadêmico

Este projeto tem como objetivo praticar conceitos fundamentais do desenvolvimento web com Django, incluindo:

- Criação de modelos e relacionamentos entre entidades.
- Gerenciamento de dados por meio do Django Admin.
- Configuração de rotas, views e templates.
- Utilização do Git e do GitHub para versionamento.
- Conteinerização e execução de aplicações com Docker Compose.

## Licença

Projeto desenvolvido para fins educacionais. Caso deseje permitir reutilização e distribuição formalmente, adicione uma licença ao repositório, como a MIT, conforme sua preferência.

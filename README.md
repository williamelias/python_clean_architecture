# Project Overview:

Esse projeto visa o estudo e aplicação (usando linguagem Python) de conceitos relativos ao
Clean Architecture (arquitetura limpa).

# requirements to run this project

- python (testado com a versão 3.10)
- pytest (versão especificada no arquivo 'requirements.txt')

Dicas:

- Crie um ambiente virtual para executar de forma isolada:
  
    $ pip3 install virtualenv

    $ virtulenv -p python3 .venv

    $ source .venv/bin/activate

- execução dos testes:
    
    $ pytest .

# Noções de Clean Architecture


![](./assets/images/clean_architecture.webp)
The three main concepts of Clean architecture are:

A arquitetura limpa visa, principalmente, a separação de tudo que é regra de negócio do que é externo a mesma.
Na teoria, a aplicação de um modelo de Clean architecture deveria ter:

- independência de framework
- independência de interface de usuário
- independência de banco de dados
- independência de qualquer elemento externo
- testabilidade

## Pontos positivos

- Separação da regra de negócio, encapsulamento da mesma.
  - Podemos fazer um parêntese com o 'S' do 'SOLID', pois estamos aplicando , de certa forma, o 'Single responsability principle' no contexto de arquitetura.

- As regras de negócio podem ser testadas sem a necessidade de uso de interfaces e devemos ter isso como norte, pois uma interface de acesso a aplicação pode mudar, por exemplo: antes via web, agora via console.

- Maior facilidade na troca de banco de dados, pois não é usada explicitamente uma lib para definição das regras de negócios atreladas ao banco.

- As regras de negócio não 'veem' o mundo externo. Com isso obtivemos uma visão front up .

## Pontos negativos

- Exige entendimento sobre o negócio e suas regras, para definição do core da aplicação

- Possui maior complexidade inicial em face a um projeto sem sua aplicação.

## Entities (Entidades): 

Aqui estarão definidas todas as regras de negócio da aplicação, por exemplo:

- se tivermos uma calculadora de contas básicas, salvariamos dentro das entities as operações aritméticas

## User Case (Caso de uso)

Nesse local estabeleceremos alguns fluxos de uso para a aplicação em questão.
Aqui estarão regras de negócio na camada da aplicação, essas regras não alteram as regras já feitas nas entidades, mas as usam.

## Adapters (Adaptador)

Nessa camada podemos ter, desde serializadoras a repositorios de interação com bancos de dados.
No caso, vamos exemplificar uma serializadora:

- ao obter o resultado de uma soma de dois números uma serializadora poderá formatar a saída como:
    {
      'soma': 4,
      'first_number': 2,
      'second_number': 2
    }

## Views ()


# References

https://medium.com/luizalabs/descomplicando-a-clean-architecture-cf4dfc4a1ac6
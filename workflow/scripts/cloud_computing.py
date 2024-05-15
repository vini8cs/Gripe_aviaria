"""
Cloud Computing
"""

"""
Modelos de implantação:

1. Infraestrutura como serviço (IaaS): Eu subo minha máquina virtual para a nuvem e uso minha aplicação lá.

2. Plataforma como serviço (Paas): a aplicação é coloca diretamente no serviço da nuvem, sem necessidade de criar a infraestrutura e mandar para a nuvem 

3. Software como serviço (SaaS): softwares utilizados diretos na nuvem, como google drive, google docs, etc
"""

"""
Modelos de computação

Híbrida: parte local, parte na nuvem
Nuvem: Tudo na nuvem;
On-premises: tudo local
"""

"""
Modelos de responsabilidade compartilhada

Quando vc manda uma máquina virtual para a nuvem e usa um software dentro dela, a responsabilidade
do sofware é do usuário e não da AWS, por exemplo. Não é a mesma coisa que vc colocar o software direto 
na nuvem. As empresas são então responsáveis pelas estruturas (hardware, sofware, redes e instalações),
mas não pelos dados. Os clientes são responsáveis pela aplicação de patches em seu SO convidado, pela ocnfiguração
dos seus próprios bancos de dados, aplicativos, etc
"""

"""
Criar orçamento no AWS

Entrar em "Orçamentos" ou "Budgets", criar orçamento e Personalizar (anavçado). 
Insira um valor orçado geralmente mensal e crie um nome. 
"""

"""
Criando uma máquina virtual na Azure, você tem noção das estimativas de custo e criar
um usuário e chave SSH. No Google Cloud, a entrada é direta, fazendo conexão diretamente como root
ou importando uma chave já criada.
"""

"""
Criando uma EC2 dentro da AWS

Máquina virtual na AWS se chama EC2;
Pesquisar EC2 na AWS
Lauch instance
Escolher uma imagem (AMI) - geralmente Ubuntu mesmo
Escolher as configurações da máquina
Selecionar o par de chaves para o SSH (se não baixar ou salvar, já era)
Nas configurações de rede, selecione também as opções HTTP e HTTPs em qualquer lugar 
Em Detalhes avançados, lá no final, vc vai ver um tópico "Dados do usuário". Lá vc vai escrever para o server 
se conectar com o Apache:

#!/bin/bash

yes|sudo apt update
yes|sudo apt install apache2

vá na instância, clique em conectar e siga as instruções, que consistem em deixar sua chave
privada com o comando chmod 400 e depois entrar no server com SSH.
"""


# Máquina virtual

Para poder criar uma máquina virtual, a página consiste em:

[Criar máquina](https://portal.azure.com/?quickstart=true#create/Microsoft.VirtualMachine-ARM) 

Você cria máquinas por organização ou grupo de recurso (Resource group). Ou seja, cada um vai ter como organizar como usar os recursos que serão alocados para máquina virtual por projeto ou por cliente.

Se excluir o resource group, exclui todas as máquinas relacionadas.

Você vai poder também selecionar a região e as zonas de disponibilidade, que vai garantir que mesmo que uma das zonas tenha problemas, outras ainda vão manter suas máquinas virtuais caso você escolha mais de uma zona.

Você escolhe também o sistema operacional, tamanho (memória ram, threads)

Coloque autenticação por senha e porta de entrada SSH, além do tamanho da memória interna.

As tags ou marcas são as organizações dos recursos. É importante demarcar cada recurso

# Azure Blob Storage

A redundância na hora de criar um storage account define como o storage deve agir quando tiver um problema em uma região, mudando de regiao ou não.

Geralmente cria um tag para seu storage

O demais itens podem ser deixados no default ou precisa dar uma pesquisada


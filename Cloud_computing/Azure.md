
# Máquina virtual

Para poder criar uma máquina virtual, a página consiste em:

[Criar máquina](https://portal.azure.com/?quickstart=true#create/Microsoft.VirtualMachine-ARM) 

Você cria máquinas por organização ou grupo de recurso (Resource group). Ou seja, cada um vai ter como organizar como usar os recursos que serão alocados para máquina virtual por projeto ou por cliente.

Se excluir o resource group, exclui todas as máquinas relacionadas.

Você vai poder também selecionar a região e as zonas de disponibilidade, que vai garantir que mesmo que uma das zonas tenha problemas, outras ainda vão manter suas máquinas virtuais caso você escolha mais de uma zona.

Você escolhe também o sistema operacional, tamanho (memória ram, threads)

Coloque autenticação por senha e porta de entrada SSH, além do tamanho da memória interna.

As tags ou marcas são as organizações dos recursos. É importante demarcar cada recurso

## Storage

Repositório (Bucket): É como se fosse um google drive, um repositório onde vc pode mandar e guardar seus arquivos.

Na amazon: S3;
Na Azure: Blobs;
Na Google: Cloud Storage

Disco: Outra forma de armazenamento, um HD virutal que está ligado às VMs.

Na amazon: EBS;
Na Azure: Managed Disk;
Na Google: Persistent disk

File share: famoso compartilhamento de arquivos para que as máquinas encontrem os arquivos em um único local

Na amazon: EFS;
Na Azure: Files;
Na Google: Filestone

Os buckets podem ter classes de armazenamento, que determinam o quanto esses buckets estão disponíveis. Na Azure, são Hot, Cool ou Archive, sendo que no Hot os arquivos estão sempre disponíveis e no Archive geralmente eles ficam 180 dias armazenados.

# Azure Blob Storage

A redundância na hora de criar um storage account define como o storage deve agir quando tiver um problema em uma região, mudando de regiao ou não.

Geralmente cria um tag para seu storage

O demais itens podem ser deixados no default ou precisa dar uma pesquisada

Dentro do storage:

- É possível criar Containers (que são tipos diretórios ). O acesso pode ser privado, anônimo e lá dentro pode fazer upload dos arquivos. 

# File Share

Vai em "storage accounts" e "File share". Crie um novo file share e vc vai ver as possíveis classes de compartilharmento, que incluem Hot, Cool, Transaction Optimizedm Premium, que indicam quanto tempo os bucktes ficarão disponíveis. 

Nessa File Share vc consegue fazer upload dos seus arquivos, assim como você faria num container. A diferença é que você pode conectar posteriormente o container (file share) a uma máquina virtual Linux, Windows ou Mac e, desta forma, vc tem acesso direto aos arquivos. 

Isso é possível fazendo o "Upload" primeiramente e depois usando o comando "Connect"

O SMB Azure é um serviço do Azure que oferece compartilhamentos de arquivos de forma gerenciada. Os compartilhamentos podem ser acessados por meio de SMB, NFS ou APIs REST. Podem ser acessados através dos sistemas operacionais Linux, Windows e macOS.
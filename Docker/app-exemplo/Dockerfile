#Estamos usando como exemplo um arquivo Node. Para podemos exercutar ele pelo Docker e criara uma
#imagem, podemos pegar um já emprestado do https://hub.docker.com/_/node. Poderiamos também ter pego
#uma imagem do Ubuntu e instalar o Node dentro do ubuntu, seria a mesma coisa. Vamos pegar a versão 14
#do Node

FROM node:14
#definindo o diretório dentro da imagem
WORKDIR /app-node
#definir um parametro para nossa porta. No entanto essa só é usava para a criação da imagem
ARG PORT_BUILD=6000
#para definir uma variável dentro do container para a porta, usar ENV
ENV PORT=$PORT_BUILD
#dizer que nossa aplicação está na porta 6000, que é nossa variável
EXPOSE $PORT_BUILD
#copiar o conteúdo do nosso diretório para o diretório da nossa imagem que vai vira um container (como estamos no diretorio atual e já definimos o diretório da imagem, podemos usar . nos dois casos)
COPY . .
#instalar as dependências em Node
RUN npm install
#ponto de entrada para começar o container
ENTRYPOINT npm start

#criar um nova imagem
#docker build -t vinicius/app-node:1.0 .

#executar
#docker run -d vinicius/app-node:1.0

#checar que container estão rodando
#docker ps

#conectar a uma porta no local host:
#docker run -d -p 8080:6000 vinicius/app-node:1.0

#logar no dockerhub
#docker login -u vini8cs

#trocar nome do usuário se preciso 
#docker tag vinicius/app-node:1.0 vini8cs/app-node:1.0

#para checar
#docker images

#mandar para o docker hub
#docker push vini8cs/app-node:1.0

#pode atualizar as versões também fazendo os mesmos comandos acima

#é possível checar os dockers que estão parados com:
#docker ps -a

#para apagar mesmo os docker parados
#docker container rm $(docker container ls -aq) #o "q" é só para pegar os ids e "a" para pegar todos, mesmo os parados

#para remover imagens
#docker rmi $(docker image ls -a) --force

#baixar docker em modo interativo "-it"

#se você checar com docker ps -s, é possível ver uma informação como "0B (virtual 77.9MB)". Isso significa que o container em si não tem nada novo, por isso 0GB além da imagem, que tem o tamanho virtual de 77.9MB.


####Mantendo containers abertos

####Bind MOunt####

#é possível fazer um bind mount com docker, em que um diretório criado dentro de um container
#se conecta com unm diretório na sua máquina. Vc faz isso utilizando o comando -v e dizendo 
#qual o path fora e o diretório que vc vai criar dentro para armazenar e transferir os dados
#criados dentro do container.

#docker run -it -v /home/vini8cs/Documents/Mestrado_Bioinformatica/Docker/volume-docker:/app  ubuntu bash
#inclusive, caso vc saia do container, ele continua rodando no mesmo se vc da ro mesmo comando.

#a forma mais semântica de usar o comando é:

#docker run -it --mount type=bind,source=/home/vini8cs/Documents/Mestrado_Bioinformatica/Docker/volume-docker,target=/app ubuntu bash

####Volumes### salva dentro duma pasta específica do docker

#criar volume
#docker volume create meu-volume

#ligar uma pasta dentro do container ao volume
#docker run -it -v meu-volume:/app ubuntu bash

#para conferir os volumes
#cd /var/lib/docker

#melhor semântica. obs: não precisa de type

#docker run -it --mount source=meu-volume,target=/app ubuntu bash

#é possível usar tmpfs para escrever a pasta com arquivos temporários dentro da memório no host e não na camada read/write do container. Ele
#não mantem o container aberto. é muito usado para arquivos sensíveis.

#docker run -it --tmpfd=/app ubuntu bash
#ou
#docker run -i --mount type=tmpfs, destinations=/app ubuntu bash

#####Rede Bridge######

#inspecionando o container é possível ver os Networks:

#docker inspect <id>

#checando as networks, é possível ver que todos nossos container foram colocados na network id
# do DRIVER bridge
#docker network ls


#definir nome para um container

#docker run -it --name ubuntu1 ubuntu bash

#criar nossa rede do tipo drive bridge
#docker network create --driver bridge minha-bridge

#agora crie um container, definindo a rede a qual ele vai se conectar, que é a que eu criei
#docker run -it --name ubuntu1 --network minha-bridge ubuntu bash 

#pode criar outro container com diferente nome, baixar o ping com:
#apt-get install iputils-ping -y

#fazer "ping <nome da rede>"" para conectá-las
#git add code.py
#git commit -m "commit"
#git push  origin main
#git log --oneline #checar todos os commits e códigos
#git rebase -i HEAD~3 #juntar os 3 últimso commits. também pode usar o código do quarto, neste caso. Assim, o responsável só vai ter um commit para revisar.
#você vai deixar um "pick" e mudar os outros que vai querer juntar para "s" e depois apagar os commits antigos e criar um commit novo para os três meslcados.
#git log --graph #dá pra ver em gráfico
#git log --format="%H %an" #pode ver o código e o autor
#git show <hash> #mostra mais informações do que foi feito para hash de commit específico

#commit 814924a2a88766c18f52dbcd10c0d1392e973464 (HEAD -> main, origin/main) #HEAD -> commit que estamos (se vc usa commit add e commit -m, o HEAD já vai ficar desalinhado do origin/main até vc dar um git push), origin/main (nosso branch no github remoto)
#git diff hash_antigo..has_maisnovo #ver a diferença entre dois commits

###GIT BRANCH####

#Caso vc esteja fazendo alterações junto com outras pessoas, vc vai ter um poblema quando for dar git push origin/main. Por isso que é importante sempre faze rum git pull antes
#Mas isso pode complicar bastante caso vc tenha muita gente trabalhando no mesmo código
#Por isso, o mehor é fazer ramificações

#criar uma branch nova:
#git branch <nome_branch>

#para trocar de branch
#git checkout <nome_branch>

#você também pode criar uma nova branch e trocar para ela com:
#git switch -c <novo_branch>
#se for só para trocar
#git swtich <novo_branch>

#no final é só criar um novo branch no github:
#git push origin <novo_branch>

#modificar o commit mais recente
#git commit --amend -m "comentário novo"

#remover branch do local:
#git branch -d <branch>

#excluir branch do repositório remoto:
#git push origin :<branch>

###GIT REBASE###

#utilizando git rebase main, é possivel adicionar os commits do outro branch um a um ao branch main, fazer merges e ir resolvendo os conflitos

#depois vc pode voltar pro main e faze rum merge com o outro branch:

###GIT MERGE###

#git merge <novo branch>

#em algumas empresas podem ter políticas de fast-forward, que exige que faça rebase antes de fazer um merge.


###GIT STASH####

# com git stash, vc conseguee guardar informações que vc está modificando sem dar o commit e guardar para depois. Caso vcoê precise mexer em outra coisa antes.
#para retornar, só usar git stash pop

#para salvar as modificações uma forma mais descritiva, pode usar:
# git stash push -m "salvando modficações no github.py"

#veja com git stash list

#para vc pegar um stash específico, vc pode indica ro número:
#git stash apply 1

#para apagar o stash caso vc não precise mais daquela smodificaçoes:
#git stash clear remove tudo
#git stash drop {numero}  remove apenas aquele stash em questão

##GIT RESET###

#undo a commit
#git reset HEAD~N (N é número de commits vc quer desfazer)

##GIT RESTORE###
#antes de fazer um commit, é possível desfazer todas as modificações já feitas sem ter que ficar dando cltr+z em todos os arquivos
#para isso, usa-se
#git restore <nome do arquivo>
#por padrão, ele vai restaurar até HEAD ou o último commit 


#você também pode desfaze rum git add:
#git restore --staged <nome do arquivo>

#é possível também retornar a um hash específico utilizando:
#git restore --source=<hash do commit> <nome do arquivo>

#e caso queira voltar para o atual:
#git restore --source=HEAD <nome do arquivo>

###GIT TAG####

#para criar uma versão do seu código é possível criar uma tag
#git tag <nome_da_tag> (ex. v.0.1.0) <hash do commit> (ex. pode ser HEAD também)

#para enviar tag ao repositório:
#git push origin <nome da tag>
#ou pegar todas as tags:
#git push origin --tags 

#para deletar uma tag no repositório local:
#git tag -d <nome da tag>

#para fazer uma tag com anotação:
#git tag -a <nome da tag> -m "Mensagem" <hash do commit>

###GIT CHERRY-PICK#####

#É possível ir para uma branch e puxar o commit específico de outra branch:
#git branch <branch onde vc quer colocar o commit>
#git cherry-pick <hash do commit>

####GIT BLAME#####

#para checar informações sobre um commit em um arquivo, como autor, data, horário, entre outras informações, você pode utilizar:
#git blame <nome do arquivo>
#ele vai dar as informações dos commits de cada linha, com informações completas sobre cada commit para cada linha daquele arquivo
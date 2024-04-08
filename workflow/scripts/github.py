#git add code.py
#git commit -m "commit"
#git push  origin main
#git log --oneline #checar todos os commits e códigos
#git rebase -i HEAD~3 #juntar os 3 últimso commits. também pode usar o código do quarto, neste caso. Assim, o responsável só vai ter um commit para revisar.
#você vai deixar um "pick" e mudar os outros que vai querer juntar para "s" e depois apagar os commits antigos e criar um commit novo para os três meslcados.
#git log --graph #dá pra ver em gráfico
#git log --format="%H %an" #pode ver o código e o autor
#git show <hash> #mostra mais informações do que foi feito para hash de commit específico


#commit 814924a2a88766c18f52dbcd10c0d1392e973464 (HEAD -> main, origin/main) #HEAD -> commit que estamos, origin/main (nosso branch no github remoto)
#git diff hash_antigo..has_maisnovo #ver a diferença entre dois commits
from shell import shell

"""
Marcodores

Bacterias e Archeas: 16S rRNA
Fungos e outros eucariotos: ITS e 18S rRNA
Fagos e outros vírus: shotgun

"""

"""
QIIME2 permite que vc mantenha track de como as análises e quis comandos e parâmtros foram 
utilizados numa análise, inclusive recuperando o código 
"""

"""
Tipos Semânticos de dados do QIIME2

Refere-se ao conceito do tema em que ele se encaixa. No caso do QIIME2, existem 4 tipos:

1. FeatureTable[Frequency] -> Formatos: BIOM, TSV, CSV, pandasDataframe, etc;
2. Phylogeny -> Formatos: Newick, scikit-bio, TreeNode, etc;
3. SampleData[SequenceWithQuality] -> Formatos: FASTQ, FASTA+Qual, etc;
4. FeatureData[Taxonomy] -> Formatos: BIOM, TSV, CSV, pandasDataframe, etc.

Os formatos podem ser atualizados, mas a semântica continua a mesma
"""

"""
QIIME2 facilita o acesso a diferentes ferramentas, como:

DADA2;
Deblur;
Cutadapt;
Emperor;
Picrust2
"""

"""
QIIME2 libera o output em QZA e QZV files, que são arquivos zipados. QIMME2 também pode
ser utilizado com Python, mas os resultados podem ser vistos no site QIIME2 view.
"""

"""
Workflow do QIIME2:

Raw sequences -> demultiplex

Quando trabalhamos com Amplicon, a primeira fase é selecionar os adaptadores específicos que vão se
ligar às regiões específicas, como o 16S rRNA. Isso é o multiplexing. No raw sequences, esses adaptadores
continuam lá e, por isso, precisam ser demultiplexed. Para isso, o QIIME2 precisa receber um arquivo metada

o arquivo metadata consiste no tipo do arquivo na primeira coluna, seguido por amostras, sequencia barcode, local de onde a amostra foi 
coletada, ano, mes, dia, nome da amotra, se teve uso de antibiótico, dias, entre outros dados

exemplo:

sample-id   barcode-sequence    body-site       year        month       day
#q2:types   categorical         categorical     numeric     numeric     numeric
L1S8        AGCTGCAGTGCA        gut             2008        8           8
L1S9        GACTGCATCG          gut             2010        10          30

# Unir os arquivos fastq paired-end em um só:

demultiplexed sequences -> unir pair-end 

# Depois tem a parte de quality control e trimagem. 

merged paired-end -> quality control ->  trimming 

Na trimagem, os padrões que são considerados incluem
porcentagem de números consecutivos mínimo de base call de alta qualidade em um read para que seja retido (-p 0.75);
máximo númer consecutivo de base calls de baixa qualida permitidas antes de truncar uma read (r 3);
máximo número de N (n 0); último quality score considerado baixo (q = 4); número mínimo de representantes preciso para reter
um OTU (c = 0.005%) 

#fazer o denoise/cluster das sequências

merged paired-end -> donoise/cluster

Atualemnte, existe uma proposta para substituir operational taxonomic units (OTUS)
por amplicon sequence variants (ASVs) na análise de dados gene-based amplicon. No 
caso dos OTUs, eles baseiam-se em clustering, em que sequências gênicas semelhantes
são unidas no mesmo grupoo a partir geralmente de uma semelhança de >=97%. Existem
3 formas de clustering: de novo: quando não se tem um genoma de referência; 
open reference: utilizando genoma de referência + de novo (quando não há genoma); 
colsed reference: somente genoma de referência, removendo aqueles grupos que não 
tem genoma de referência. Geralmente open reference é o mais recomnedado visto que
tem menos viés e menos custo computacional. Também pode-se construir modelos para
determinar sequências que podem ser erros ou artifatos e remove-las, deixando
apenas sequências com valores estatísticos significativos de alta confiância. 
 Geralmente, quanto mais uma sequência de uma espécie está presente numa 
amostra (maior abundância), mais signnificativo vai ser o p. Neste caso, teriamos
 então um ASV. Não é realizado clusterização e também não é utilizado genoma de 
 referência até a anotação taxonômica, ou seja, não tem viês de referência. 
 A sequências são exatas, podendo as tabelas serem comparadas entre estudos.
   é diferente de OTUs, onde se tem sequencias consensus. Também é um método mais 
   simples de detectar quimeras

"""


"""
A primeira parte do código é ter o metadata, barcodes e sequences:

wget \
  -O "sample-metadata.tsv" \
  "https://data.qiime2.org/2024.2/tutorials/moving-pictures/sample_metadata.tsv"

wget \
  -O "emp-single-end-sequences/barcodes.fastq.gz" \
  "https://data.qiime2.org/2024.2/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz"

wget \
-O "emp-single-end-sequences/sequences.fastq.gz" \
"https://data.qiime2.org/2024.2/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz"

"""

"""
Para rodar o o qiime, a primira parte é converter o arquivo fasta para qza, com:

qiime tools import \
  --type EMPSingleEndSequences \ #tipo de sequências
  --input-path emp-single-end-sequences \ #onde os fastq estão disponíveis
  --output-path emp-single-end-sequences.qza #arquivo que será gerado
"""

"""
Para checar se tudo ocorreu direitinho, use o comando:

qiime tools peek emp-single-end-sequences.qza

o output vai ser algo:
UUID:        2502606c-d314-4047-857c-1dbf009231e7
Type:        EMPSingleEndSequences
Data format: EMPSingleEndDirFmt
"""

"""
Para fazer o demultiplexing:

qiime demux emp-single \  #tipo de fastq (single-end)
  --i-seqs emp-single-end-sequences.qza \ #input
  --m-barcodes-file sample-metadata.tsv \ #nosso metadat
  --m-barcodes-column barcode-sequence \  #a coluna no arquivo metada com as sequências barcode que vão ser retiradas
  --o-per-sample-sequences demux.qza \ #output das sequências por amostra
  --o-error-correction-details demux-details.qza #output dos detalhes da correção de erros 
"""

"""
e com esse comendando vc gera um relatório para poder checar o número de sequências por amostra
e um resumo da distribuição da qualidade de da cada uma das posições das suas sequências. O 
arquivo final pode ser observado no qiime2 view.

qiime demux summarize \
  --i-data demux.qza \
  --o-visualization demux.qzv

Você pode encontar amostras que não tenham sequencias suficiente, por exemplo. ALém de checar 
A qualidade ou phread das posições de cada das posições das suas sequências. 
"""



'''
Desenvolva um programa que deve ler um arquivo csv intitulado “notas_alunos.csv”. O arquivo deve ter a seguinte estrutura:

aluno: Nome do aluno;
nota_1: Primeira nota;
nota_2: Segunda nota;
faltas: Número de faltas;

O programa lerá esse arquivo e criará duas colunas. A primeira coluna será “media”, que terá a média das duas notas do aluno. A segunda será “situacao”, com os valores: APROVADO ou REPROVADO.

O aluno que tiver mais de 5 faltas ou possuir média menor que sete, será reprovado. O programa deverá salvar esse novo dataframe com o nome “alunos_situacao.csv”.

Por fim, o programa deverá mostrar na tela:
- o maior número de faltas;
- a média geral das notas dos alunos;
- e a maior média.

Veja em anexo um exemplo do arquivo “notas_alunos.csv”.
'''
import pandas as pd

#infromando os dados
aluno=["aluno_1", "aluno_2", "aluno_3","aluno_4"]
nota_1=[ 7, 3 , 9 , 10]
nota_2=[ 7, 10, 4, 6 ]
faltas=[ 1, 7, 2, 9 ]

dados={
    'aluno': aluno,
    'nota_1':nota_1,
    'nota_2':nota_2,
    'faltas':faltas
}
#Inserindo os dados no arquivo
infoAlunos=pd.DataFrame(dados)
infoAlunos.to_csv('notas_alunos.csv',index=False,encoding='UTF-8')

#operando e adicionando as duas linhas extras
infoAlunosLeitura=pd.read_csv('notas_alunos.csv')
infoAlunosLeitura['media'] = (infoAlunosLeitura['nota_1'] + infoAlunosLeitura['nota_2'])/2


infoAlunosLeitura.loc[(infoAlunosLeitura['faltas'] <= 5) & (infoAlunosLeitura['media'] >= 7), 'situação'] = 'APROVADO'
infoAlunosLeitura.loc[(infoAlunosLeitura['faltas'] > 5) | (infoAlunosLeitura['media'] < 7), 'situação'] = 'REPROVADO'

infoAlunosLeitura.to_csv('situação_alunos.csv',index=False, encoding='utf-8')
print(infoAlunosLeitura)
maiorFaltas=infoAlunosLeitura['faltas'].max()
mediaGeralAlunos=infoAlunosLeitura['media'].mean()
maiorMedia=infoAlunosLeitura['media'].max()

print(f'O maior número de faltas foi de:{maiorFaltas}' )
print(f'A média geral das médias de notas da turma foi: {mediaGeralAlunos}')
print(f'"A maior média da turma foi: " {maiorMedia}')






from aluno import Aluno
from disciplina import Disciplina

aluno1 = Aluno("joão", "123456", "Ciência da computação")

dsa = Disciplina("Data Strucutres", "Álvaro")
model_lin = Disciplina("Modelagem Linear", "Rodolfo")

aluno1.matricular(dsa)
aluno1.matricular(model_lin)
#print(aluno1.disciplinas[0].nome)

aluno1.adcionar_nota(dsa, 10)
aluno1.adcionar_nota(dsa, 5)
aluno1.adcionar_nota(model_lin, 9)
aluno1.adcionar_nota(model_lin, 7)
print(aluno1.notas_por_disciplina)




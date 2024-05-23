import random
alunos=['João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Mariana']
print(f"Lista: {alunos}")
# Embaralhar a lista
random.shuffle(alunos)
print(f"Lista ambaralhada: {alunos}")
# escolhe um aluno aleatoriamente 
aluno_sorteado = random.choice(alunos)
print(f"Aluno sorteado: {aluno_sorteado}")
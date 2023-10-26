#CALCULAR O VALOR DA MASSA CORPORAL DE ALGUÉM COM BASE NO SEU PESO E ALTURA:
peso = float(input('Olá! Qual o seu peso(kg)? '))
altura = float(input('E a sua altura(m)? '))
resultado = peso / altura ** altura  
print('Seu BMI é: {:.1f}'.format(resultado))
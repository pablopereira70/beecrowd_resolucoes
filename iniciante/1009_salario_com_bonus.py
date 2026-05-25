"""
Plataforma: Beecrowd
Problema: 1009 - Salário com bônus
Categoria: Iniciante
Link: https://judge.beecrowd.com/pt/problems/view/1009
Autor: Pablo Pereira
Data: Maio / 2026
"""

nome = input()
sal_fixo = float(input())
valor_vendas = float(input())
print(f"TOTAL = R$ {sal_fixo + valor_vendas * 0.15:.2f}")
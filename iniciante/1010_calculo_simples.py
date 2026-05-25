"""
Plataforma: Beecrowd
Problema: 1010 - Cálculo simples
Categoria: Iniciante
Link: https://judge.beecrowd.com/pt/problems/view/1010
Autor: Pablo Pereira
Data: Maio / 2026
"""

cod_peca1, num_peca1, valor_peca1 = map(float, input().split())
cod_peca2, num_peca2, valor_peca2 = map(float, input().split())
print(f"VALOR A PAGAR: R$ {num_peca1 * valor_peca1 + num_peca2 * valor_peca2:.2f}")
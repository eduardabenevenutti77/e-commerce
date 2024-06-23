def calcular_pert(nome_plataforma):
    print(f"\nCalculadora PERT para {nome_plataforma}")

    while True:
        print("\nDigite as estimativas para a tarefa (ou 'sair' para finalizar):")
        nome_tarefa = input("Nome da Tarefa: ")
        if nome_tarefa.lower() == 'sair':
            break
        otimista = float(input("Tempo Otimista (O): "))
        mais_provavel = float(input("Tempo Mais Provável (M): "))
        pessimista = float(input("Tempo Pessimista (P): "))

        # Calcular a Duração Esperada (TE)
        te = (otimista + 4 * mais_provavel + pessimista) / 6

        # Calcular a Variância
        variancia = ((pessimista - otimista) / 6) ** 2

        print(f"\n\033[1;32mResultados PERT para {nome_plataforma} - {nome_tarefa}\033[m")
        print(f"  Tempo Otimista (O): {otimista}")
        print(f"  Tempo Mais Provável (M): {mais_provavel}")
        print(f"  Tempo Pessimista (P): {pessimista}")
        print(f"  Duração Esperada (TE): {te:.2f}")
        print(f"  Variância: {variancia:.2f}")

def main():
    print("\033[1;32mCalculadora PERT para Wix e Shopify\033[m")

    # Calcular PERT para Wix
    calcular_pert("\033[1;32mWix\033[m")

    # Calcular PERT para Shopify
    calcular_pert("\033[1;32mShopify\033[m")

# Executar a função principal
main()
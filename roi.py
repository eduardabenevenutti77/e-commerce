def calculadora_roi():
    print("\033[1;32mCalculadora de ROI para a comparação de WIX & Shopify\033[m\n")

    # Área para Wix
    print("WIX:")
    receita_mensal_wix = float(input("Informe a receita mensal esperada: "))
    custo_wix = 39  # Supondo que o plano é mensal
    lucro_wix = receita_mensal_wix - custo_wix

    # Cálculo do ROI para Wix
    investimento_wix = custo_wix
    roi_wix = (lucro_wix / investimento_wix) * 100

    print(f"Supondo que o plano utilizado foi o mensal, o ROI foi: {roi_wix:.2f}%\n")

    # Área para Shopify
    print("Shopify:")
    receita_mensal_shopify = float(input("Informe a receita mensal esperada: "))
    custo_shopify = 39  # Supondo que o plano é mensal
    transacao_shopify = 2.9 / 100  # Taxa de transação
    custo_transacao = 0.30
    numero_transacoes = int(input("Informe o número médio de transações mensais: "))

    # Cálculo do custo de transação para Shopify
    custo_transacao_shopify = (receita_mensal_shopify * transacao_shopify) + (numero_transacoes * custo_transacao)
    lucro_shopify = receita_mensal_shopify - custo_shopify - custo_transacao_shopify

    # Cálculo do ROI para Shopify
    investimento_shopify = custo_shopify
    roi_shopify = (lucro_shopify / investimento_shopify) * 100

    print(f"Supondo que o plano utilizado foi o mensal, o ROI foi: {roi_shopify:.2f}%\n")

    print("\033[1;32mResumo dos Resultados\033[m")
    print(f"ROI para Wix: \033[1;32m{roi_wix:.2f}%\033[m")
    print(f"ROI para Shopify: \033[1;32m{roi_shopify:.2f}%\033[m")

calculadora_roi()
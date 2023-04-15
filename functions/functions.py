#!/us/bin/python

def calculate_profit(lucro):
    profit = lucro * 0.2
    return {"tax": profit}


def calcular_lucro(ultima_acao_de_compra, acao_de_venda, last_avarage_price_by_buy_action, custo_operacao):

    custo_acao_compra = ultima_acao_de_compra["quantity"] * \
        ultima_acao_de_compra["unit-cost"]
    custo_acao_venda = acao_de_venda["quantity"] * acao_de_venda["unit-cost"]
    # result = (ultima_acao_de_compra["unit-cost"]
    #           * acao_de_venda["quantity"])

    result = ((last_avarage_price_by_buy_action *
              acao_de_venda["quantity"])) - custo_acao_venda

    return result


def format_result(current_stock_numbers, current_average_price, action_quantity, action_quantity_cost):

    my_dict = {
        "current_stocks_numbers": current_stock_numbers,
        "current_average_price": current_average_price,
        "actions_quantity": action_quantity,
        "action_quantity_cost": action_quantity_cost,
    }
    return my_dict


def calcular_valor_medio_ponderado(action, current_stock_numbers, current_average_price):
    actual_value_operation = (current_stock_numbers * current_average_price)
    value_actual_action = (action["quantity"] * action["unit-cost"])
    return ((actual_value_operation + value_actual_action) / (current_stock_numbers+action["quantity"]))


def balanced_average_price(actions):
    # quantidade de ações atual
    current_stock_numbers = 0
    # media_ponderada_atual
    current_average_price = 0
    new_current_avarage_price = 0
    profit = []
    custo_operacao = 0
    acao_compra = None
    valor_de_compra = 0

    prejuizo = 0
    last_avarage_price_by_buy_action = 0

    for action in actions:

        print("INICIO PREJUIZO: ", prejuizo)
        if action['operation'] == 'buy':
            print("BUY", action)
            acao_compra = action
            valor_de_compra = acao_compra["quantity"]*acao_compra["unit-cost"]

        unit_cost = action['unit-cost']
        quantity = action['quantity']
        valor_de_venda = (unit_cost * quantity)

        if action['operation'] == 'sell':
            current_stock_numbers -= action["quantity"]

        new_current_avarage_price = calcular_valor_medio_ponderado(action=action,
                                                                   current_stock_numbers=current_stock_numbers,
                                                                   current_average_price=current_average_price)
        if action['operation'] == 'buy':
            print("NOVA", new_current_avarage_price)
            prejuizo = 0
            last_avarage_price_by_buy_action = new_current_avarage_price

        current_average_price = new_current_avarage_price

        operation_has_prejuizo = last_avarage_price_by_buy_action < current_average_price

        print("TEVE preju?", operation_has_prejuizo)

        if action['operation'] == 'sell' and last_avarage_price_by_buy_action != current_average_price:
            if operation_has_prejuizo:
                print("lucro")
                prejuizo -= calcular_lucro(ultima_acao_de_compra=acao_compra,
                                           acao_de_venda=action,
                                           last_avarage_price_by_buy_action=last_avarage_price_by_buy_action,
                                           custo_operacao=valor_de_venda
                                           )
            else:
                print("prejuizo")
                prejuizo += (acao_compra["quantity"]*acao_compra["unit-cost"] *
                             (current_average_price/10)) - valor_de_compra

        if action['operation'] == 'buy':
            current_stock_numbers += action["quantity"]

        print("VALOR DE COMPRA: ", valor_de_compra)
        print("VALOR MOVIMENTADO (preju)", prejuizo)
        print("CUSTO OPERACAO", valor_de_venda)
        print("VALOR MÉDIO", new_current_avarage_price)
        print("Valor final ", (valor_de_compra - valor_de_venda - prejuizo))

        if ((valor_de_venda >= 20000) and operation_has_prejuizo and prejuizo >= 0):
            var = calculate_profit(prejuizo)
            profit.append(var)
        else:
            profit.append({"tax": 0.0})
        print("------------------")
    print("PROFIT: ", profit)
    return profit

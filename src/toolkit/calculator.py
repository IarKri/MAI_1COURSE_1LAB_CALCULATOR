def tokenize_fsm(expr):
    tokens = []
    state = 'START'
    current_token = ''
    
    for char in expr:
        if state == 'START':
            if char.isdigit():      #проверяем цифру
                state = 'NUMBER'    #меняем статус со старта на значение
                current_token = char    #добавляем в строку значение 
            # дописать, не забываем про числа с точкой
            elif char in ['-', '+']:  # если символ является оператором, то мы его пропускаем, потому что в строке собираем только значения
                pass
                
        elif state == 'NUMBER':    
            if char.isdigit():
                current_token += char
            # дописать
        # дописать
    
    # Завершающая обработка
    if state == 'NUMBER' or state == 'ВАШЕ СОСТОЯНИЕ':
        tokens.append(('NUMBER', float(current_token))) # записываем тип токена - NUMBER и его значение
    
    return tokens #возвращаем набор типизированныхз токенов (в нашем случае это только цифры, без опреаторов)
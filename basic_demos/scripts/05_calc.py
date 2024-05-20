while True:
    op = input("operation [plus,minus,multiply,divide,quit]?")
    if op == 'quit':
        break
    value1=int(input("value1?"))
    value2=int(input("value2?"))
    if op == 'plus':
        result=value1+value2
    elif op =='minus':
        result=value1-value2
    elif op =='multiply':
        result=value1*value2
    elif op == 'divide':
        result=value1/value2
    else:
        result=None

    if result!=None:
        print(f'{value1} {op} {value2} = {result}')
    else:
        print(f'invalid/unsupported operation "{op}"')
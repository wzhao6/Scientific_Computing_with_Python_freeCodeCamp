
def arithmetic_arranger(problems, result=False):
  
    if len(problems) > 5:
        return 'Error: Too many problems.'
    top=''
    bot=''
    das=''
    res=''

    for j in problems:
        l = j.split()
        num1 = l[0]
        op = l[1]
        num2 = l[2]
        
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'
        if max(len(num1), len(num2)) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if op != '+' and op != '-':
            return "Error: Operator must be '+' or '-'."
        else:
            width = max(len(num1), len(num2)) + 2
            if j != problems[-1]:
              top += '{:>{w}}'.format(num1, w=width) + '    '
              bot += '{:} {:>{w}}'.format(op, num2, w=width-2) + '    '
              das += '{:>{w}}'.format('-'*width, w=width) + '    '
              if op == '+':
                  calc = str(int(num1) + int(num2))
              else: 
                  calc = str(int(num1) - int(num2))
              res += '{:>{w}}'.format(calc, w=width) + '    '
            else:
              top += '{:>{w}}'.format(num1, w=width)
              bot += '{:} {:>{w}}'.format(op, num2, w=width-2) 
              das += '{:>{w}}'.format('-'*width, w=width)
              if op == '+':
                  calc = str(int(num1) + int(num2))
              else: 
                  calc = str(int(num1) - int(num2))
              res += '{:>{w}}'.format(calc, w=width)


    if result:
        arranged_problems = top + '\n' + bot + '\n' + das + '\n' + res
    else:
        arranged_problems = top + '\n' + bot + '\n' + das


    return arranged_problems
import math
while True:
    
    nameOfShape = input('Type of Shape ( if done type done ): ').lower()
    if nameOfShape != 'done':
        baseUnit = input('What unit: ')
        unit = baseUnit + '^2'
        
    if nameOfShape == 'circle':

        # THE CIRCLE CALCULATION  
        
        equation1 = 'πr^2' 
        r = input('radius = ')
        equation2 = 'π * ' + r + ('^2') 
        answer = (math.pi * pow(float(r), 2))
        answer = round(answer, 2)
        answer = str(answer)
    elif nameOfShape == 'square':

        # THE SQUARE CALCULATION    

        equation1 = 's^2' 
        s = input('side length = ')
        equation2 = s + '^2'
        answer = str(pow(float(s), 2))
    elif nameOfShape == 'triangle':

        # THE TRIANGLE CALCULATION 

        equation1 = 'bh/2' 
        b = input('base = ')
        h = input('height = ')
        equation2 = '( ' + b + ' * ' + h + ' )/2 '
        answer = str((float(b) * float(h))/2)
    elif nameOfShape == 'trapezoid':

        # THE TRAPEZOID CALCULATION 

        equation1 = '(a+b)/2 * h' 
        a = input('base1 = ')
        b = input('base2 = ')
        h = input('height = ')
        equation2 = '( ' + a + '+' + b + ' )/2 * ' + h
        answer = str((float(a) + float(b))/2 * float(h))
    elif nameOfShape == 'rhombus':

        # THE RHOMBUS CALCULATION 

        equation1 = '(d1 * d2)/2' 
        d1 = input('diagonal1 = ')
        d2 = input('diagonal2 = ')
        equation2 = '( ' + d1 + '*' + d2 + ' )/2'
        answer = str(( float(d1) * float(d2) )/2)
    elif nameOfShape == 'parallelogram':

        # THE PARALLELOGRAM CALCULATION

        equation1 = 'b * h'
        b = input('base = ')
        h = input('height = ')
        equation2 = b + ' * ' + h
        answer = str(float(b) * float(h))
    elif nameOfShape == 'rectangle':

        # THE RECTANGLE CALCULATION

        equation1 = 'b * h'
        b = input('base = ')
        h = input('height = ')
        equation2 = b + ' * ' + h
        answer = str(float(b) * float(h))

    elif nameOfShape == 'done':
        quit()

    print('Area of ' + nameOfShape + '\n= ' + equation1 + ' = ' + equation2 + '\n= ' + answer + ' ' + unit)

    
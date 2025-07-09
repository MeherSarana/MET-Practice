s = '(((())))'

while '()' in s:
    s = s.replace('()', '')

print("Balanced" if s == '' else "Unbalanced")
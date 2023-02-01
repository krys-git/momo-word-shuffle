import itertools

input = 'ở g ố 10 u _ n i ư h _ r c t'
elements = input.split(' ')

print(elements)
print(len(elements))
with open('permutations.txt', 'w', encoding='utf8') as writer:
    for p in itertools.permutations(elements, len(elements)):
        product = ''.join(p)
        if product.startswith('g') \
            or product.startswith('n') \
            or product.startswith('c') \
            or product.startswith('t') \
            or product.startswith('10'):
            continue
        if product.endswith('10') \
            or product.endswith('_') \
            or product.endswith('r') \
            or product.endswith('t'):
            continue
        if 'ưố' in product \
            or 'ởố' in product \
            or 'ởư' in product \
            or 'ốở' in product:
            continue
        writer.write(f'T{product}\n')
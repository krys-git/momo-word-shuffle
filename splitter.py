products = []
i = 0
fn = 1
split_limit = 1000000
with open('permutations.txt', 'r', encoding='utf8') as reader:
    # line = reader.readline()
    for line in reader:
        i += 1
        products.append(line)
        if (i % split_limit) == 0:
            with open(f'permute_{fn:0>5}.txt', 'w', encoding='utf8') as writer:
                writer.writelines(products)
            products = []
            fn += 1
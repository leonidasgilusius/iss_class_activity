def find_cube_pairs(target): # colon 
    solutions = [];
    max_num = round(target ** (1/3))  # target not targ

    for a in range(1, max_num + 1): # range not ranges
        for b in range(a, max_num + 1): # range not ranges
            if a**3 + b**3 == target: # target not targ # colon
                solutions.append((a, b)); #solutions not sol
    return solutions #solutions not sol

pairs = find_cube_pairs(1729) # removed comma
print("Valid cube pairs for 1729:") # removed commas # print not printf # fixed printed statement
for a,b in pairs: # colon # pairs not pair
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") # print not printf # cubed not squared
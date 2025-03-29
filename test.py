def find_cube_pairs(target): # added a colon 
    solutions = [];
    max_num = round(target ** (1/3))  # change name to target not targ

    for a in range(1, max_num + 1): # range not ranges # added a colon
        for b in range(a, max_num + 1): # range not ranges # added a colon
            if a**3 + b**3 == target: # target not targ # added a colon
                solutions.append((a, b)); #solutions not sol
    return solutions #solutions not sol

pairs = find_cube_pairs(1729) # removed comma
print("Valid cube pairs for 1729:") # removed commas # print not printf # fixed printed statement
for a,b in pairs: # added a colon # pairs not pair
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") # print not printf # cubed not squared

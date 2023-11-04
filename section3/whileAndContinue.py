"""
While with continue

Continue will ignore the actual while loop and go for next loop
"""

count = 0
while count < 100:
    if count % 2 != 0:
        print(f'unpaired: {count}')
        count += 1
        continue  # Will ignore the final code
    print(f'pair: {count}')
    count += 1

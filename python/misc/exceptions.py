def calc_ratio(numerator, divisor):
    try:
        return numerator / divisor
    except ZeroDivisionError:
        return numerator / 0.000000000001
    except TypeError:
        return float(numerator) / float(divisor)

print(calc_ratio(10, 2))
print(calc_ratio(1, 0))
print(calc_ratio("1", "5"))


animals = ["dog", "bird", "horse", "horse", "dog"]
animal_counter = {}
for animal in animals:
    try:
        animal_counter[animal] += 1
    except:
        animal_counter[animal] = 1

print(animal_counter)    
    


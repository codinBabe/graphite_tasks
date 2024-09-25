def is_valid(card_number):
    if not card_number.isnumeric() & len(card_number) != 16:
        return False
    card = [int(x) for x in card_number]
    card_doubled = [x * 2 if not i % 2 else x for i, x in enumerate(card)]
    card_subtracted = [x - 9 if x > 9 else x for x in card_doubled]
    return sum(card_subtracted) % 10 == 0


print(is_valid("4532015112830366"))
print(is_valid("4532015112830367"))
print(is_valid("453201511283036"))
print(is_valid("45320151128303666"))

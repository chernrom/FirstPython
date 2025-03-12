from tasks import add_two_numbers

# Вызов задачи
result = add_two_numbers.delay(3, 5)
print(result.get())

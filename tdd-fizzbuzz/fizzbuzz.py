def fizzbuzz(num_elements):
    result = ""
    if (num_elements % 3) == 0:
        result += "Fizz"

    if (num_elements % 5) == 0:
        result += "Buzz"

    return result if result else num_elements

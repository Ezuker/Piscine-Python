from time import time, strftime

date = strftime("%b %d %Y")
time_seconds = time()
formatted_time = f"{time_seconds:,.3f}"
scientific_nota = f"{time_seconds:.2E}"

print("Seconds since January 1, 1970:", end=" ")
print(formatted_time, "or", scientific_nota, end=" ")
print("in scientific notation")
print(date)

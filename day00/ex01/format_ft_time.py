import datetime
import time 

date = time.strftime("%b %d %Y")
time_seconds = time.time()
formatted_time = f"{time_seconds:,.3f}"
scientific_nota = f"{time_seconds:.2E}"

print("Seconds since January 1, 1970:", formatted_time, "or", scientific_nota, "in scientific notation")
print(date)


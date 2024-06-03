number_of_pages = int(input())
pages_for_hour = int(input())
days = int(input())

total_time_for_1book = number_of_pages / pages_for_hour
total_time_for_day = total_time_for_1book / days

print(int(total_time_for_day))
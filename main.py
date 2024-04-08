from datetime import datetime, timedelta

def specific_range(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y %m %d'))
        current_date += timedelta(days=1)

    return dates

#start_date_str = input("Enter start date (YYYY-MM-DD): ")
#end_date_str = input("Enter end date (YYYY-MM-DD): ")

#date_range = specific_range(start_date_str, end_date_str)
#print(date_range)




def generate_date_range(range_type):
    end_date = datetime.now()
    if range_type == 'week':
        start_date = end_date - timedelta(days=7)
    elif range_type == '30_days':
        start_date = end_date - timedelta(days=30)
    else:
        raise ValueError("Invalid range type")

    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y %m %d'))
        current_date += timedelta(days=1)

    return dates

def print_date_range(date_range):
    for date in date_range:
        print(date)

print("1. Print previous week")
print("2. Print previous 30 days")
print("3. Choose specific date range")
choice = input("Enter your choice (1-3): ")

if choice == '1':
    date_range = generate_date_range('week')
    print("Previous Week:")
    print_date_range(date_range)
elif choice == '2':
    date_range = generate_date_range('30_days')
    print("Previous 30 Days:")
    print_date_range(date_range)
elif choice == '3':
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")
    date_range = specific_range(start_date_str, end_date_str)
    print(date_range)
else:
    print("Invalid choice")
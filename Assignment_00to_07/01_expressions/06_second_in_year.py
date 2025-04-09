# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.



DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    
    total_seconds = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    
    print(f"There are {total_seconds} seconds in a year!")


if __name__ == '__main__':
    main()
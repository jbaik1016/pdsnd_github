import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv','new york city': 'new_york_city.csv', 'washington': 'washington.csv' }

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6, 'all':7}

DAY_ORDER = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """Asks user to specify a city, month, and day to analyze.
    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please specify which city you're interested in: Chicago, New York City, or Washington.\n").strip().strip("'").lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            print("Thanks!")
            break
        else:
            print("That's not a valid city name!")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Are you interested in analyzing data for a specific month? If so, please enter its full name (e.g. January, February). If not, enter 'all':\n").strip().strip("'").lower()
        if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
            print("Got it!")
            break
        else:
            print("That's not a valid month name!")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Are you interested in analyzing data for a specific day of the week? If so, please enter its full name (e.g. Monday, Tuesday). If not, enter 'all':\n").strip().strip("'").lower()
        if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all':
            print("Roger that!")
            break
        else:
            print("That's not a valid entry!")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable.
    Args:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
    df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    df['Start End Combo'] = df['Start Station'] + " to " + df['End Station']
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['end hour'] = df['End Time'].dt.hour
    month_num = int(MONTHS.index(month) + 1)
    day_num = int(DAYS[day])
    if month != 'all':
        df = df[df['month'] == month_num]
    if day != 'all':
        df = df[df['weekday'] == day_num]
    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == "all":
        pop_month_num = df['month'].mode()[0]
        pop_month_name = str(MONTHS[pop_month_num - 1]).title()
        print("The most common travel month is: ", pop_month_name)

    # TO DO: display the most common day of week
    if day == 'all':
        pop_day_num = df['weekday'].mode()[0]
        pop_day_name = str(DAY_ORDER[pop_day_num]).title()
        print("The most common travel day is: ", pop_day_name)

    # TO DO: display the most common start hour
    pop_hour = df['hour'].mode()[0]
    print("The most frequent start hour is: ", pop_hour)
    pop_end_hour = df['hour'].mode()[0]
    print("The most frequent end hour is: ", pop_end_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station = df['Start Station'].mode()[0]
    print("The most frequently used start station is: ", pop_start_station)

    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].mode()[0]
    print("The most frequently used end station is: ", pop_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    pop_route = df['Start End Combo'].mode()[0]
    print("The most frequent travel route is: ", pop_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total amount traveled is: ", total_time, " seconds.")

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print("The average travel time: ", round(avg_time,3), " seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_count = df['User Type'].value_counts(dropna=False)
    print("Number of each user type:\n", type_count)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts(dropna=False)
        print("\nUser gender counts:\n", gender_count)
    except:
        print("\nNo user gender data available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        min_birth = int(df['Birth Year'].min())
        max_birth = int(df['Birth Year'].max())
        mode_birth = int(df['Birth Year'].mode()[0])
        print("\nEarliest birth year for users: ", round(min_birth,0))
        print("Most recent birth year for users: ", round(max_birth,0))
        print("Most common birth year for users: ", round(mode_birth,0))
    except:
        print("\nNo birth year data available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

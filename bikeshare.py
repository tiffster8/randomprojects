import time
import pandas as pd
import numpy as np
import csv


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington) with a while loop to handle invalid inputs

    while True:
        print('Please type one of the following cities that you\'re interested in learning more about: Chicago, New York, or Washington. If you would like to exit, enter a blank.') 
        city = input() 
        if city.lower() == ' ':
            break
        
        if city.lower() == 'chicago':
            print('Great! Looks like we\'re going to look at some data from Chicago.')
        elif city.lower() == 'new york':
            print('Great! Looks like we\'re going to look at some data from New York.')
        elif city.lower() == 'Washington':
            print('Great! Looks like we\'re going to look at some data from Washington.')
        else:
            print('Sorry, I don\'t understand your input. Please check your spelling and input one of the following cities: Chicago, New York, or Washington.')
        break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month_input = ''
    months_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4,
                   'may': 5, 'june': 6}
    while True:
        print('Which month would you like to filter the data with? January, February, March, April, May, or June?')
        month_input = input()
        if month_input.lower() not in months_dict.keys():
            print('Sorry, I don\'t understand your input. Please check your spelling and type in a month from January to June.')
    month = months_dict[month_input.lower()]
    return ('2017-{}'.format(month), '2017-{}'.format(month + 1))
    break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_input = ''
    days_dict = {'sunday': 1, 'monday': 2, 'tuesday': 3, 'wednesday': 4, 'thursday': 5, 'friday': 6, 'saturday': 7}
    while True:
        print('Which day of the week would you like to filter the data with? Sunday, Monday, Tuesday, etc.?')
        day_input = input()
        if day_input.lower() not in days_dict.keys():
            print('Sorry, I don\'t understand your input. Please check your spelling and type in a day of the week.')
    day = days_dict[day_input.lower()]
    return ('2017- -{}'.format(day), '2017- -{}'.format(day + 1))
    
    return city, month, day
    break

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()
    print('The most common month is: ', most_common_month)
    
    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()
    print('The most common day of the week is: ', most_common_day)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()
    print('The most common start hour is: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()
    print('The most commonly used start station is: ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()
    print('The most commonly used end station is: ', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_freq_combo = df.groupby['Start Station', 'End Station'].mode()
    print('The most frequent combination of start and end station trip: ', most_freq_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total travel time in seconds: ', travel_time)

    # TO DO: display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print('Average travel time in seconds: ', travel_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types: ', user_types)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    if 'Gender' in df.columns:
        print('The counts of gender: ', gender)
    else:
        print('No gender data available.')

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_yob = df['Birth Year'].min()
    most_recent_yob = df['Birth Year'].max()
    most_commmon_yob = df['Birth Year'].mode()
    if 'Birth Year' in df.columns:
        print('Earliest, most recent, and most common year of birth: ', earliest_yob, most_recent_yob, most_commmon_yob) 
    else:
        print('No birth data available.')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

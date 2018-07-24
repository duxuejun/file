import time
import pandas as pd
import numpy as np

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for chicago, new york city, or washington?\n').lower()
    while city not in ['chicago','new york city','washington']:
        city = input('This is the wrong input ,please reenter it\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Would you like to see data for month?(all,january,february,...,june)\n').lower()
    while month not in ['all','january','february','march','april','may','june']:
        month = input('This is the wrong input,please reenter it\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Would you like to see data for month?(all,monday,tuesday,...,sunday)\n').lower()
    while day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        day = input('This is the wrong input,please reenter it\n').lower()

    print('-'*40)
    return city, month, day


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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month'] == month]
    if day!= 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    most_month = df['month'].mode()[0]
    print('The most common month: {}'.format(most_month))
    

    # TO DO: display the most common day of week
   
    most_week = df['day_of_week'].mode()[0]
    print('The most common day of week: {}'.format(most_week))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_hour = df['hour'].mode()[0]
    print('The most common start hour: {}'.format(most_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station: {}'.format(most_start_station))

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station: {}'.format(most_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    trip = df['Start Station'] + ' ' + '->' +' ' + df['End Station']
    most_trip = trip.mode()[0]
    print('The most frequent combination of start station and end station trip: {}'.format(most_trip))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip = df['Trip Duration'].sum()
    print('Total travel time: {}'.format(total_trip))

    # TO DO: display mean travel time
    mean_trip = df['Trip Duration'].mean()
    print('The mean travel time: {}'.format(mean_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = df['User Type'].value_counts()
    print(user_types_counts)


    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
       
    except:
        print('There is no gender data in this city')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        most_birth = df['Birth Year'].max()
        most_birth = df['Birth Year'].mode()[0]
        print('The earliest year of birth: {}\n'.format(earliest_birth))
        print('The most recent year of birth: {}\n'.format(most_birth))
        print('The most common year of birth: {}\n'.format(most_birth))
           
    except:
        print('This city does not have the data of birth')
           
             
    

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

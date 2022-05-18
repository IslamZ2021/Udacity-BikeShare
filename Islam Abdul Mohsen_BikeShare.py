#!/usr/bin/env python
# coding: utf-8

# In[14]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('input required city').lower()
        if city not in ('chicago', 'new_york_city', 'washington'):
            print('please, input a useful city (chicago, new_york_city, washington)')
            continue 
        else: 
            break
                

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('input required month').lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('please, input a useful month (jan, feb, mar , apr, may, jun)')
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('input required date').lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
            print('please, input a useful day (sunday, monday, tuesday, wednesday, thursday, friday, saturday)')
            continue
        else:
            break

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
    
    #input data frame for city data
    df = pd.read_csv(CITY_DATA[city])
    
    #create date time column from start time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #create month column from start time column
    df['month'] = df['Start Time'].dt.month
    
    #create a week day column from start time column
    df['week_day'] = df['Start Time'].dt.weekday
    
    #create a day hour column from start time column
    df['day_hour'] = df['Start Time'].dt.hour
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    mcm_value = df['month'].mode()[0]
    print('most common month:', mcm_value)
    
    # display the most common day of week
    mcd_value = df['week_day'].mode()[0]
    print('most common day:', mcd_value)
    
    # display the most common start hour
    mch_value = df['day_hour'].mode([0])
    print('most common hour:', mch_value)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    mcss_value = df['Start Station'].value_counts().idxmax()
    print('most commonly used start station:', mcss_value)

    # display most commonly used end station
    mces_value = df['End Station'].value_counts().idxmax()
    print('most commonly used end station:', mces_value)

    # display most frequent combination of start station and end station trip
    mccsses_value = df.groupby(['Start Station', 'End Station']).count()
    print('most frequent combination:', mcss_value, 'and', mces_value)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    ttt_value = sum(df['Trip Duration'])
    print('total travel time:', ttt_value)

    # display mean travel time
    mtt_value = df['Trip Duration'].mean()
    print('mean travel time:', mtt_value)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    ut_value = df['User Type'].value_counts()
    print('user type counts:', ut_value)

    try:
    
    # Display counts of gender
        gt_value = df['Gender'].value_counts()
        print('gender counts:', gt_value)

    # Display earliest, most recent, and most common year of birth
    
    #earliest year of birth
        eyb_value = int(df['Birth Year'].min())
        print('earliest year of birth:', eyb_value)
    
    #recent year of birth
        ryb_value = int(np.max(df['Birth Year']))
        print('recent year of birth:', ryb_value)

    #most common year of birth
        mcyb_value = int(df['Birth Year'].value_counts().index[0])
        print('most common year of birth:', mcyb_value)
    except:
        print('gender , earliest , recent and most common year of birth not exist for washington !!')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_view_data(df):
    
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
        if view_data =='yes':
            start_loc = 0
            while True:
                print(df.iloc[start_loc:start_loc+5])
                start_loc +=5
                Stop_view_data = input("Would you like to stop viewing data? Enter yes or no?").lower() 
                if Stop_view_data != 'yes':
                    break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_view_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:





# In[ ]:





import pandas as pd
import numpy as np
import sys

def data_analysis(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    #print(df.info())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # .value_counts() -> find the count of unique values in the index 
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round (df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    # Number of bachelors / total number of degrees.
    bachelor_count = df.loc[df['education'] == 'Bachelors'].value_counts().sum()
    total_degress = len(df)
    
    percentage_bachelors = round((bachelor_count / total_degress) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # three variables that will holds corresponding data frame for degress
    bachelors = df['education'] == 'Bachelors'
    masters = df['education'] == 'Masters'
    phd = df['education'] == 'Doctorate'
    higher_education = bachelors | masters | phd
    lower_education = ~(bachelors | masters | phd) # all other degrees besides bachelors, masters, and doctorate
    # percentage with salary >50K
    tmp_salary = df['salary'] == ">50K"
    tmp_high = df.loc[higher_education & tmp_salary].value_counts().sum()
    tmp_total = df.loc[higher_education].value_counts().sum()
    # print('tmp high', tmp_high)
    # print('tmp_total', tmp_total)
    tmp_low = df.loc[lower_education & tmp_salary].value_counts().sum()
    tmp_lowT = df.loc[lower_education].value_counts().sum()
    higher_education_rich = round(tmp_high / tmp_total * 100, 1)
    lower_education_rich = round(tmp_low / tmp_lowT * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].value_counts().min()
    #print ('min_hour', min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours & tmp_salary].value_counts().sum()
    #print ('test', num_min_workers)

    tmp_minSum = df.loc[df['hours-per-week'] == min_work_hours].value_counts().sum()
    #print ('min sum', tmp_minSum)
    rich_percentage = round(num_min_workers / tmp_minSum * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    population_count = df['native-country'].value_counts()
    earning_inCountry = df.loc[tmp_salary, 'native-country'].value_counts()
    highest_earning_country = round(earning_inCountry/population_count * 100, 1).idxmax()
    highest_earning_country_percentage = round(earning_inCountry/population_count * 100, 1).max()

    # Identify the most popular occupation for those who earn >50K in India.
    # need to find a specific country first.
    specific_Country = df['native-country'] == 'India'
    popular_Occupation = df.loc[specific_Country & tmp_salary, 'occupation'].value_counts()
    top_IN_occupation = popular_Occupation.idxmax() # so, idxmax returns the name of a particular subject.
    #print('best job', top_IN_occupation)
 
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

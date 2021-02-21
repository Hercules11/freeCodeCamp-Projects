import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    csv_data = pd.read_csv('adult.data.csv')
    df = pd.DataFrame(csv_data)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()  # 不会的操作，多用谷歌搜索，想清楚其中的原理，下次不要忘记

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df[df['education'] == 'Bachelors'].count()[0] / df['education'].count() * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # .isin ~**isin. == != &
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()[0]
    # 官方文档的信息过于笼统了，学知识还得是实践解决问题，到 StackOverflow 吸取知识
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()[0]

    # percentage with salary >50K
    higher_education_rich = round(df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')].count()[0] / higher_education * 100, 1)
    lower_education_rich = round(df[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')].count()[0] / lower_education * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].count()[0]

    rich_percentage = round(num_min_workers / df[df['hours-per-week'] == 1].count()[0] * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    # SStackOverflow yyds
    # 官方文档的 examples 也可
    newDataFrame = pd.DataFrame(df[df['salary'] == '>50K'].groupby('native-country')['salary'].count() / df.groupby('native-country')['salary'].count())
    highest_earning_country = newDataFrame.sort_values(by='salary').dropna().index[-1]
    highest_earning_country_percentage = round(max(df[df['salary'] == '>50K'].groupby('native-country')['salary'].count() / df.groupby('native-country')['salary'].count()) * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts(normalize=True).index[0]

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

# calculate_demographic_data(print_data=True)

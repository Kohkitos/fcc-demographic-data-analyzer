import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = df[df.sex == 'Male'].age.mean().round(decimals=1)

    # What is the percentage of people who have a Bachelor's degree?
    x = (df['education'].value_counts()/df['education'].count())*100
    percentage_bachelors = x['Bachelors'].round(decimals=1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    mask = ((df.education == 'Bachelors') | (df.education == 'Masters') | (df.education == 'Doctorate'))

    higher_education_rich = ((df[mask & (df.salary == '>50K')].salary.count()/df[mask].salary.count())*100).round(decimals=1)
    lower_education_rich = ((df[~mask & (df.salary == '>50K')].salary.count()/df[~mask].salary.count())*100).round(decimals=1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]['hours-per-week'].count()

    num_min_workers_rich = df[(df['hours-per-week'] == min_work_hours) & (df.salary == '>50K')]['hours-per-week'].count()

    rich_percentage = (num_min_workers_rich / num_min_workers)*100

    # What country has the highest percentage of people that earn >50K?
    x = df[df.salary == '>50K']['native-country'].value_counts()
    y = df['native-country'].value_counts()
    z = ((x / y) * 100).round(decimals=1)

    highest_earning_country = z[z == z.max()].index[0]
    highest_earning_country_percentage = z.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india = df[(df.salary == '>50K') & (df['native-country'] == 'India')]
    profs = india.occupation.value_counts()
    top_IN_occupation = profs[profs == profs.max()].index[0]

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

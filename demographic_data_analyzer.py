import pandas as pd

def demographic_data_analyzer():
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    race_count = df['race'].value_counts()
  
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
  
    total_people = len(df)
    num_bachelors = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((num_bachelors / total_people) * 100, 1)

    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentage with salary >50K
    higher_education_rich = round((len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)) * 100, 1)
    lower_education_rich = round((len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)) * 100, 1)

    # Minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # Percentage of people who work the minimum number of hours per week and have a salary of >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers)) * 100, 1)

    # Country with the highest percentage of people that earn >50K
    country_salary_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    highest_earning_country_percentage = round((country_salary_counts / country_counts).max() * 100, 1)
    highest_earning_country = (country_salary_counts / country_counts).idxmax()

    # Most popular occupation for those who earn >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Return the results as a dictionary
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
  
print(demographic_data_analyzer())

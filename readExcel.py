import pandas as pd

# Normalize algorithm:

def normalize(value, max, min):
    v = (value - min) / (max - min) * (10 - 1) + 1
    return round(v)


# Recommendation function - Sets a recommendation level by normalized score:

def recommend(score):
    if score in range(5, 8):
        return 'Recommended'
    elif score in range(8, 11):
        return 'Highly Recommended'
    else:
        return 'Not related'

def readFromExcel(attribute_dict):

    df = pd.read_excel(r'C:\Users\Etai Leers\Desktop\framework1.xlsx', header=[0, 1])

    filter_df = df.loc[:, [('Approaches', 'All'),
                           ('Budget', attribute_dict['Budget']),
                           ('Commitment', attribute_dict['Commitment']),
                           ('Contract Type', attribute_dict['Contract_Type']),
                           ('Customer Type', attribute_dict['Customer_Type']),
                           ('Duration', attribute_dict['Duration']),
                           ('Goals', attribute_dict['Goals']),
                           ('Pace', attribute_dict['Pace']),
                           ('Procedures & Regulations', attribute_dict['Procedures_and_Regulations']),
                           ('Resources', attribute_dict['Resources']),
                           ('Scope', attribute_dict['Scope']),
                           ('Team Availability', attribute_dict['Team_Availability']),
                           ('Team Distribution', attribute_dict['Team_Distribution']),
                           ('Team Size', attribute_dict['Team_Size']),
                           ('Uncertainty', attribute_dict['Uncertainty'])]]

    rate_dict = {
        "Highly Recommended": 2,
        "Recommended": 1,
        "Not Related": 0
    }

    filter_df.replace(rate_dict, inplace=True)

    filter_df['Sum'] = filter_df.sum(axis=1)

    filter_df.sort_values('Sum', ascending=False, inplace=True)

    return filter_df

    #TODO: Figure out why this function isnt working

    recommend(5)
    print('hello')



import pandas as pd


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
    filter_df.to_excel('filtered_df.xlsx')
    return filter_df





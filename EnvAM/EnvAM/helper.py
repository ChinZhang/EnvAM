# Import Libraries
import os
from io import StringIO
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rcParams["figure.figsize"] = (10, 6)

# Load DataSet into DataFrame
path = os.path.dirname(os.path.abspath("DataSet.csv"))
path = os.path.join(path, "DataSet.csv")
data = pd.read_csv(path)

# Remove 'Country Name' and 'Series Name' from the DataFrame
data = data.drop(['Country_Name', 'Series_Name'], axis='columns')

year_set = ['1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008',
            '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']


# Function to Remove Null Values
def is_valid(x):
    try:
        return float(x)
    except:
        return None


# Remove All Null Values
for year in year_set:
    data[year] = data[year].apply(is_valid)


# Function to Put Data In Correct Format for 1 Year Analysis of 2 Features
def single_year_comp(df, year, scode1, scode2):
    df_out = pd.DataFrame()
    for key, subdf in df.groupby('Series Code'):
        if (subdf['Series Code'].iloc[0] == scode1) or (subdf['Series Code'].iloc[0] == scode2):
            xdf = subdf[['Country Code', 'Series Code', year]]
            df_out = pd.concat([df_out, xdf], ignore_index=True)

    df_out = df_out.pivot(index='Country Code', columns='Series Code', values=year)
    df_out = df_out.dropna()

    return df_out


# Function to Put Data in Correct Format for 1 Country Analysis of 2 Features
def single_country_comp(df, country, scode1, scode2):
    year_dict = {'Year': [], 'Series Code': [], 'Value': []}
    for key, subdf in df.groupby('Series Code'):
        if (key == scode1) or (key == scode2):
            for index, value in subdf['Country Code'].items():
                if value == country:
                    for year in year_set:
                        year_dict['Year'].append(year)
                        year_dict['Series Code'].append(key)
                        year_dict['Value'].append(subdf[year].loc[index])

    df_out = pd.DataFrame.from_dict(year_dict)
    df_out = df_out.pivot(index='Year', columns='Series Code')
    df_out = df_out.dropna()

    return df_out


# Function for Outlier Removal
def outlier_detect(df):
    for i in df.describe().columns:
        q1 = df.describe().at['25%', i]
        q3 = df.describe().at['75%', i]
        iqr = q3 - q1
        ltv = q1 - 1.5 * iqr
        utv = q3 + 1.5 * iqr
        x = np.array(df[i])
        p = []
        for j in x:
            if j < ltv or j > utv:
                p.append(df[i].median())
            else:
                p.append(j)
        df[i] = p
    return df


# Function for 1 Year Correlation Scatter Plot
def create_scatter_plot(df):
    x = df[df.columns[0]]
    y = df[df.columns[1]]

    outlier_detect(df)
    sns.regplot(x=x, y=y)
    # plt.scatter(x, y, color = 'green')

    plt.xlabel(df.keys()[0])
    plt.ylabel(df.keys()[1])


# Function for Finding Correlation Coefficient
def corr_coef(df):
    col_1 = df[df.columns[0]]
    col_2 = df[df.columns[1]]
    correlation = col_1.corr(col_2)
    return "{:.4f}".format(correlation)


# Full Test Case (PPP GDP per Unit Energy vs Total Greenhouse Gas Emissions in the Year 2005)
def find_correlation_1_year(df, year, scode1, scode2):
    df_out = single_year_comp(df, year, scode1, scode2)
    create_scatter_plot(df_out)
    corr_coef(df_out)
    print(corr_coef(df_out))


# Full Test Case for Country
def find_correlation_country_over_years(df, country, scode1, scode2):
    df_out = single_country_comp(df, country, scode1, scode2)
    create_scatter_plot(df_out)
    print(corr_coef(df_out))


# Function for Correlation Over Time Line Graph
def plot_corr_all_years(arr, scode1, scode2):
    plt.style.use('seaborn-whitegrid')
    plt.plot(year_set, arr)
    plt.title(f'Correlation Over Time for {scode1} & {scode2}')
    plt.xlabel('Year')
    plt.ylabel('Correlation Coefficient')
    plt.ylim([-1, 1])
    plt.show()


# Function for Correlation Over Time
def find_correlation_all_years(df, scode1, scode2):
    corr_arr = []
    years = year_set
    for i in range(23):
        df_out = single_year_comp(df, years[i], scode1, scode2)
        corr_arr.append(float(corr_coef(df_out)))
    plot_corr_all_years(corr_arr, scode1, scode2)


# # All Test Cases For Correlation Over Time With Sufficient Data
# find_correlation_all_years(data, 'NRPGDP', 'GDPPUE')


def return_graph(df):
    x = df[df.columns[0]]
    y = df[df.columns[1]]

    figure = plt.figure()
    outlier_detect(df)
    sns.regplot(x=x, y=y)
    plt.xlabel(df.keys()[0][1])
    plt.ylabel(df.keys()[1][1])

    imgdata = StringIO()
    figure.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data


def country_data():
    original_data = pd.read_csv(path)
    country_names = original_data['Country_Name'].unique()
    country_codes = original_data['Country Code'].unique()
    country_data_zipped = zip(country_names, country_codes)
    country_data_dict = {}
    for name, code in country_data_zipped:
        country_data_dict[code] = name

    return country_data_dict


def series_data():
    original_data = pd.read_csv(path)
    series_names = original_data['Series_Name'].unique()
    series_codes = original_data['Series Code'].unique()
    series_data_zipped = zip(series_names, series_codes)
    series_data_dict = {}
    for name, code in series_data_zipped:
        series_data_dict[code] = name

    return series_data_dict

# # Test Case of 1 Year Correlation Score
# find_correlation_1_year(data, '2015', 'GDPPUE', 'CO2PC')
#
# # Test Case of a Country
# find_correlation_country_over_years(data, 'WLD', 'GDPPUE', 'CO2PC')

import streamlit as st
import pandas as pd
import plotly.express as px



df = pd.read_csv('vehicles_us.csv')

df['model_year'] = df['model_year'].fillna(df.groupby('model')['model_year'].transform('median'))
df['odometer'] = df['odometer'].fillna(df.groupby(['model', 'model_year'])['odometer'].transform('median')).fillna(df['odometer'].median())
df['model_year'] = df['model_year'].fillna(df.groupby('model')['model_year'].transform('median'))
df['paint_color'] = df['paint_color'].fillna('No info')
df['cylinders'] = df['cylinders'].fillna(df.groupby('model')['cylinders'].transform('median'))

df['is_4wd'] = df['is_4wd'].fillna(0)



st.header('Adverstisement of Used Car')
st.write('Filter the data below to see the details of the car')





customer_choice = df['model'].unique()

select_menu = st.selectbox('Please select your choice of Vehicle', customer_choice)

minimum_year, maximum_year  = int(df['model_year'].min()), int(df['model_year'].max())

year_range = st.slider('choose year', value=(minimum_year, maximum_year), min_value=minimum_year,max_value=maximum_year)

actual_range = list(range(year_range[0], year_range[1]+1))

df_filtered = df[ (df['model'] == select_menu) & (df.model_year.isin(list(actual_range)))]

df_filtered

st.header("Analysis in Price of Cars")

st.write("This section analyze the factors involved in pricing. The price of a car depends on the following attributes which are the transmission,engine capacity or body type and state.You can find the chat distribution below")

criteria = ['transmission','odometer','type','cylinders','model_year','condition' ] 

selected_type = st.selectbox('Split for price distribution', criteria)

fig1 = px.histogram(df, x="price",color = selected_type )
fig1.update_layout(title=f"<b> Split of price by {selected_type}</b>")
st.plotly_chart(fig1)

def age_category(x):
    if x<5: return '<5'
    elif x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'
df['age'] = 2024 - df['model_year']

df['age_category'] = df['age'].apply(age_category)

scatter_chart = ['odometer','cylinders','type']

choice_for_scatter = st.selectbox('Price dependency on', scatter_chart)

fig2 = px.scatter(df, x="price", y=choice_for_scatter, color="age_category", hover_data=['model_year'])
fig1.update_layout(title=f"<b> Split of price by {choice_for_scatter}</b>")

st.plotly_chart(fig2)
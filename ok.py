import plotly_express as px
gapminder = px.data.gapminder()
gapminder2007 = gapminder.query('year==2007')
fit = px.scatter(gapminder2007, x='gdpPercap', y='lifeExp',
color='continent',size='pop',size_max=60,hover_name="country",
facet_col="continent",log_x=True)
fit.show()
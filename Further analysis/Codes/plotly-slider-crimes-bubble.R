library(plotly)
library(gapminder)

Sys.setenv("plotly_username"="yx160")
Sys.setenv("plotly_api_key"="AcbKobOFUHf7UYvCtsPH")
crime = read.csv('crimes-county-years.csv')

population <- crime$POPULATION
violent <- crime$VIOLENT.CRIME.RATE.PER.100.000.PEOPLE
property <- crime$PROPERTY.CRIME.RATE.PER.100.000.PEOPLE
year <- crime$YEAR
county <- crime$JURISDICTION
overall <- crime$Overall.Crime.Rate

data <- tibble(population, violent, property, year, county, overall)
p <- data %>% plot_ly(
    x = ~ violent, 
    y = ~ property, 
    size = ~ population, 
    color = ~ overall,
    frame = ~ year, 
    text = ~ county, 
    hoverinfo = "text",
    type = 'scatter',
    mode = 'markers'
  ) %>%
  layout(
    title = "Property v.s. Violent Crime from 1975 to 2016 for each county in MD",
    xaxis = list(
      type = "log")
  )

api_create(p, filename="plotly-slider-crimes")
htmlwidgets::saveWidget(as_widget(p), 'plotly-slider-crimes.html')


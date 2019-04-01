# set work dirction
setwd("C:/Users/47532/Desktop/503Visualization/Project/project2")
library(rgdal)
library(dplyr)
library(leaflet)
library(stringr)
library(htmlwidgets)

# Read in dataset
crime <- read.csv('crimes-counties-2016.csv')
crime <- crime%>% filter(str_detect(crime$YEAR, '2016'))
colnames(crime)
crime <- crime[,c("CountyFP", "OVERALL.CRIME.RATE.PER.100.000.PEOPLE", "VIOLENT.CRIME.RATE.PER.100.000.PEOPLE","PROPERTY.CRIME.RATE.PER.100.000.PEOPLE")]
#formatC is from C code formatting - creates a 5 digit int
crime$CountyFP <- formatC(crime$CountyFP, width = 3, format = "d", flag = "0")

workforce <- read.csv('2016-maryland-workforce-by-county.csv')
colnames(workforce)
workforce <- workforce[c(1:24),c(2,7)]
#formatC is from C code formatting - creates a 5 digit int
workforce$CountyFP <- formatC(workforce$CountyFP, width = 3, format = "d", flag = "0")

education <- read.csv('Wealth_Expenditures_Data_2016.csv')
colnames(education)
#formatC is from C code formatting - creates a 5 digit int
education$CountyFP <- formatC(education$CountyFP, width = 3, format = "d", flag = "0")
education <- education[c(1:24),c(5,12)]

income <- read.csv('Per_captial_personal_income_2016.csv')
income <- income[c(1:24),c(2,3)]
#formatC is from C code formatting - creates a 5 digit int
income$CountyFP <- formatC(income$CountyFP, width = 3, format = "d", flag = "0")

# Load in us map data
us.map <- readOGR(dsn = "./cb_2016_us_county_20m", layer = "cb_2016_us_county_20m", stringsAsFactors = FALSE)
us.map.MD <- us.map[us.map$STATEFP == '24', ]

# Merge spatial df with county shape data "us map.
crime_map <- merge(us.map.MD, crime, by.x='COUNTYFP', by.y='CountyFP')
workforce_map <- merge(us.map.MD, workforce, by.x='COUNTYFP', by.y='CountyFP')
education_map <- merge(us.map.MD, education, by.x='COUNTYFP', by.y='CountyFP')
income_map <- merge(us.map.MD, income, by.x='COUNTYFP', by.y='CountyFP')


#Format popup data for leaflet map.
popup_c<-paste0("<strong>County name: </strong>", 
                crime_map$NAME, 
                "<br><strong>Overall Crime number: </strong>", 
                as.numeric(crime_map$OVERALL.CRIME.RATE.PER.100.000.PEOPLE))

popup_p<-paste0("<strong>County name: </strong>", 
                crime_map$NAME, 
                "<br><strong> Property Crime number: </strong>", 
                as.numeric(crime_map$PROPERTY.CRIME.RATE.PER.100.000.PEOPLE))

popup_v<-paste0("<strong>County name: </strong>", 
                crime_map$NAME, 
                "<br><strong>Violent Crime number: </strong>", 
                as.numeric(crime_map$VIOLENT.CRIME.RATE.PER.100.000.PEOPLE))

popup_w<-paste0("<strong>County name: </strong>", 
                 workforce_map$NAME, 
                 "<br><strong>Labor Force Participation Rate: </strong>", 
                 workforce_map$Labor.Force.Participation.Rate..Total....)

popup_e<-paste0("<strong>County name: </strong>", 
                education_map$NAME, 
                "<br><strong>Education Expenditures Per Pupil: </strong>", 
                education_map$Expenditures.Per.Pupil)

popup_i<-paste0("<strong>County name: </strong>", 
                income_map$NAME, 
                "<br><strong>Per Capital Person Income: </strong>", 
                income_map$Number)


pal1 <- colorQuantile("YlOrRd", NULL, n = 9)
pal2 <- colorQuantile("YlGnBu", NULL, n = 9)

crime_records <- leaflet(data = crime_map) %>%
  # Base groups
  addTiles() %>%
  setView(lng = -76, lat = 39, zoom = 8) %>% 
  addPolygons(fillColor = ~pal1(OVERALL.CRIME.RATE.PER.100.000.PEOPLE), 
              fillOpacity = 0.8, 
              color = "#BDBDC3", 
              weight = 1,
              popup = popup_c,
              group="Overall Crime") %>% 
  addPolygons(fillColor = ~pal1(PROPERTY.CRIME.RATE.PER.100.000.PEOPLE), 
              fillOpacity = 0.8, 
              color = "#BDBDC3", 
              weight = 1,
              popup = popup_p,
              group="Property Crime") %>% 
  addPolygons(fillColor = ~pal1(VIOLENT.CRIME.RATE.PER.100.000.PEOPLE), 
              fillOpacity = 0.8, 
              color = "#BDBDC3", 
              weight = 1,
              popup = popup_v,
              group="Violent Crime") %>% 
  addPolygons(fillColor = pal2(as.numeric(workforce_map$Labor.Force.Participation.Rate..Total....)), 
              fillOpacity = 0.8, 
              color = "#BDBDC3", 
              weight = 1,
              popup = popup_w,
              group="Workforce")%>% 
  addPolygons(fillColor = pal2(education_map$Expenditures.Per.Pupil), 
              fillOpacity = 0.8, 
              color = "#BDBDC3", 
              weight = 1,
              popup = popup_e,
              group="Education")%>% 
  addPolygons(fillColor = pal2(income_map$Number), 
              fillOpacity = 0.8, 
              color = "#BDBDC3", 
              weight = 1,
              popup = popup_i,
              group="Income")%>%
  # Layers control
  addLayersControl(
    baseGroups = c("Overall Crime"),
    overlayGroups = c("Property Crime", "Violent Crime", "Workforce",
                      "Education","Income"),
    options = layersControlOptions(collapsed = FALSE)
  )

crime_records

saveWidget(crime_records, file="leaflet-MD-crime-map.html", selfcontained = TRUE)  

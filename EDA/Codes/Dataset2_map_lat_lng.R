library(leaflet)
library(ggplot2)
library(htmlwidgets)
library(tigris)
setwd("C:/Users/47532/Desktop/503Visualization/Project/Datasets")
# Load Crime data and map data
Crime<-read.csv('Dataset2-Crime_type_in_MD_with_lat_lng.csv')
zip_codes<-read.csv('zip_codes_states.csv')
#Remove columns with useless information in Crime data.
crime_clean <- Crime[,-c(1,2,3,4,5,9,10,11,12,13,15,17,18,19,20,22,25)]
zip_codes<-read.csv('zip_codes_states.csv')
zip_codes_marryland <- zip_codes[zip_codes$state=="MD",]
#Add a column called "county" in df "Usaisport".
crime_clean$county<-zip_codes_marryland$county[match(crime_clean$Zip.Code,zip_codes_marryland$zip_code)]
#Remove any row with NA.
crime_clean<-crime_clean[!crime_clean%in%c("NA","<NA",NA,"na"),]

#Divide 'Location' column into 'lat' and 'lng' columns for crime_clean dataset
crime_clean$Location <- gsub("[()]", "", crime_clean$Location)
crime_clean$lat <- as.integer(sapply(strsplit(as.character(crime_clean$Location),','), "[", 1))
crime_clean$lng <- as.integer(sapply(strsplit(as.character(crime_clean$Location),','), "[", 2))

# Divide 'Start.Date.Time' column into 'Year', 'Month', 'Day', 'Time' four columns
crime_clean$Year <- substr(crime_clean$Start.Date.Time, 7, 10)
crime_clean$Month <- substr(crime_clean$Start.Date.Time, 1, 2)
crime_clean$Day <- substr(crime_clean$Start.Date.Time, 4, 5)
crime_clean$Time <- substr(crime_clean$Start.Date.Time, 12, 22)

crime_clean_2016 <- crime_clean[crime_clean$Year=='2016',]
crime_clean_2017 <- crime_clean[crime_clean$Year=='2017',]
crime_clean_2018 <- crime_clean[crime_clean$Year=='2018',]

us.map <- tigris::counties(cb = TRUE, year = 2017)

#Format popup data for leaflet map.
popup_crime_2016<-paste0("<strong>Crime Type: </strong>", 
                    crime_clean_2016$Crime.Name1, 
                      "<br><strong>Crime Info: </strong>", 
                    crime_clean_2016$Crime.Name2,
                      "<br><strong>Place: </strong>", 
                    crime_clean_2016$Place,
                      "<br><strong>Time: </strong>", 
                    crime_clean_2016$Time)

popup_crime_2017<-paste0("<strong>Crime Type: </strong>", 
                         crime_clean_2017$Crime.Name1, 
                         "<br><strong>Crime Info: </strong>", 
                         crime_clean_2017$Crime.Name2,
                         "<br><strong>Place: </strong>", 
                         crime_clean_2017$Place,
                         "<br><strong>Time: </strong>", 
                         crime_clean_2017$Time)

popup_crime_2018<-paste0("<strong>Crime Type: </strong>", 
                         crime_clean_2018$Crime.Name1, 
                         "<br><strong>Crime Info: </strong>", 
                         crime_clean_2018$Crime.Name2,
                         "<br><strong>Place: </strong>", 
                         crime_clean_2018$Place,
                         "<br><strong>Time: </strong>", 
                         crime_clean_2018$Time)

#Specify custom color for the markers as well as icon. 
myicon <- awesomeIcons(
  icon = 'plane',
  iconColor = 'white',
  library = 'ion',
  markerColor = "pink"
)

#Render final map in leaflet.
Crimemap <- leaflet() %>%
  # Base groups
  addTiles() %>%
  setView(lng = -76, lat = 39, zoom = 8) %>% 
  addCircleMarkers(data=crime_clean_2018,radius=5,color="blue",stroke=F,fillOpacity =0.7,popup=popup_crime_2018,lat=~lat, lng=~lng,group="Crime in 2018")%>%
  addCircleMarkers(data=crime_clean_2017,radius=5,color="orange",stroke=F,fillOpacity =0.7,popup=popup_crime_2017,lat=~lat, lng=~lng,group="Crime in 2017")%>%
  #addMarkers(data=crime_clean_2018,lat=~lat, lng=~lng, popup=popup_crime_2018, group = "Crime in 2018") %>% 
  #addAwesomeMarkers(clusterOptions = markerClusterOptions(),data=crime_clean_2017,lat=~lat, lng=~lng, popup=popup_crime_2017,group = "Crime in 2017",icon=myicon)%>%
  addCircleMarkers(data=crime_clean_2016,radius=5,color="purple",stroke=F,fillOpacity =0.7,popup=popup_crime_2016,lat=~lat, lng=~lng,group="Crime in 2016")%>%
  #  Layers control
  addLayersControl(
    baseGroups = c("Crime in 2018"),
    overlayGroups = c("Crime in 2017","Crime in 2016"),
    options = layersControlOptions(collapsed = F)
  )
saveWidget(Crimemap, 'Marryland_crime_map.html', selfcontained = TRUE)

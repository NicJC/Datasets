
library(fpp2)
library(ggfortify)
library(tidyverse)
library(kableExtra)
library(ggthemes)
library(xts)
library(lubridate)
library(hrbrthemes)
library(gridExtra)
library(ggResidpanel)
library(grid)
library(forecast)
library(astsa)
library(readr)
library(TTR)
library(ggpubr)
library(lattice)
library(dplyr)
library(imager)

arrests <- read.table("https://raw.githubusercontent.com/NicJC/Datasets/main/Arrests.csv", 
                      header = TRUE,
                      sep = ",")

head(arrests)
plot(arrests$Year,arrests$Age, xlab = "Year", ylab = "Age" )
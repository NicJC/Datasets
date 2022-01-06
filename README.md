# Datasets

<a href="https://github.com/NicJC" target="_blank">
  <img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=azure alt=github style="margin-bottom: 8px;" />
</a>

<a href="https://www.linkedin.com/in/nicholas-coxen/" target="_blank">
  <img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=azure alt=linkedin style="margin-bottom: 8px;" />
</a>


Data for your projects

* <B><h2>Police dataset</h2></B>

csv [file here](https://github.com/NicJC/Datasets/blob/main/Police.csv)

[py File](https://github.com/NicJC/Datasets/blob/main/Police.py)

The police data-set is a combination of data from [this site](https://github.com/washingtonpost/data-police-shootings) 

The dataset is published under https://creativecommons.org/licenses/by-nc-sa/4.0/

Additionally, I have added data for US States from [this site](https://abbreviations.yourdictionary.com/articles/state-abbrev.html)



* <B><H2>Arrests Dataset</h2></B>

csv [file here](https://raw.githubusercontent.com/NicJC/Datasets/main/Arrests.csv)

[py file](https://github.com/NicJC/Datasets/blob/main/US_Arrests.py)

The Arrests.csv data has had years 2013 to 2019 appended into one csv file.

The dataset is published under the [open data](https://creativecommons.org/about/program-areas/open-data/) license from [Metropolitan Police Department](https://mpdc.dc.gov/page/open-data-mpd)

<B><h3><i>To download the data:</i></h3><B>

For python - Use pandas' arrests = pd.read_csv("above url")  [python example](https://github.com/NicJC/Datasets/blob/main/Police%20Shootings.ipynb)

For R - arrests <- read.table("https://raw.githubusercontent.com/NicJC/Datasets/main/Arrests.csv", header = FALSE,sep = ",") R [example](https://github.com/NicJC/Datasets/blob/de485911d1711b65b35a6d38fa13c83025322d7f/ggplot%20for%20police%20data.ipynb) file, and R [script](https://github.com/NicJC/Datasets/blob/main/Arrests.R)

For Julia -  using DataFrames,UrlDownload; -> url = "https://raw.githubusercontent.com/NicJC/Datasets/main/Police.csv"  -> police = urldownload(url) |> DataFrame [Julia example](https://github.com/NicJC/Datasets/blob/main/julia%20-%20Police%20Shootings.ipynb)
                 
As a csv file - copy all and paste into an Excel file and save as csv.


Created by Nic Coxen

<br>

<p><img src="avatar.jpg" alt="Nic Coxen" > </p>
  


</br>

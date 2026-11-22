# Data from: Herbivore thermoregulation, movement behavior, and survival during a severe drought in Namibia

Dataset DOI: [10.5061/dryad.9cnp5hr2g](https://doi.org/10.5061/dryad.9cnp5hr2g)

## Description of the data and file structure

These data were collected as part of a field study investigating the behavioral and physiological responses of free-ranging plains zebra (*Equus quagga*) and blue wildebeest (*Connochaetes taurinus*) to an extreme drought in Etosha National Park, Namibia, during 2019–2020. Animals were fitted with GPS collars to monitor movement patterns and surgically implanted with biologging devices to record body temperature. Data were collected across three seasonal periods: cool drought, hot drought, and post-drought recovery. The study examined changes in movement rates, daily distance traveled, drinking behavior, body temperature regulation, and survival in response to drought conditions. Associated environmental variables were used to investigate how vegetation, water availability, and habitat characteristics influenced these responses. The dataset supports analyses of species-specific behavioral and physiological strategies for coping with extreme drought in semi-arid savanna ecosystems.

### Files and variables

#### File: Daily_distance_traveled.csv

**Description:** Daily distance traveled (DDT) was calculated for individual plains zebra (*Equus quagga*) and blue wildebeest (*Connochaetes taurinus*) as the sum of consecutive GPS-derived step lengths within each 24-hour period, representing the total distance traveled rather than the straight-line distance between the first and last locations of the day.

* id: individual animal ID
* species: CT= Blue Wildebeest, EQ=Plains zebra
* sex: f= female; m = male 
* day: M/D/YYYY (e.g., 7/4/2= July 4, 2019)
* season: CD= cool dry (May 2019 to August 2018), HD= hot dry (September 2019 to November 2019), HW = hot wet (December 2019 to April 2020)
* V1: Daily Distance traveled in in kilometers

#### File: Movement_rate.csv

**Description:** Movement rates for individual plains zebra (*Equus quagga*) and blue wildebeest (*Connochaetes taurinus*) were calculated from consecutive GPS fixes by dividing step length (m) by elapsed time (10 minutes) using the `adehabitatLT` package (Calenge, 2024) in R version 4.2.1 (R Core Team, 2022). Movement rates were converted to km/h, and hourly movement rates were calculated as the mean of six consecutive 10-minute movement rates within each hour.

##### Variables

* id: individual animal id
* species: CT = Blue wildebeest, EQ = Plains zebra
* sex: f= female, m= male
* season: CD= cool dry (May 2019 to August 2018), HD= hot dry (September 2019 to November 2019), HW = hot wet (December 2019 to April 2020)
* hour2: Hour at which the observation was recorded, expressed in 24-hour format (0–23), where 0 represents midnight and 23 represents 11:00 PM.
* V1: the movement rate  calculated as the mean of the six 10-min movement rates within each hour in km/hr.

#### File: Tmax_public.csv

**Description:** Maximum daily body temperature (°C) recorded for each individual plains zebra (*Equus quagga*) and blue wildebeest (*Connochaetes taurinus*).

##### Variables

* id: individual animal id
* day: Date that maximum body temperature occured M/D/YYYY (e.g., 7/4/2= July 4, 2019). 
* HOD: Hour at which the observation was recorded, expressed in 24-hour format (0–23), where 0 represents midnight and 23 represents 11:00 PM.
* clbrtd_: the calibrated maximum body temperature (°C)
* sex: f=female, m=male
* species: CT = Blue wildebeest, EQ= Plains zebra
* season:  CD= cool dry (May 2019 to August 2018), HD= hot dry (September 2019 to November 2019), HW = hot wet (December 2019 to April 2020)
* min_dat: Date that maximum body temperature occured M/D/YYYY (e.g., 7/4/2= July 4, 2019).
* event: Unique identification number assigned to each recorded daily maximum body temperature event
* loc_dat: Date and time of the GPS collar location used to determine the animal's position on the landscape at the time of the daily maximum body temperature event and link that location to associated environmental variables. Format: M/D/YYYY h:mm AM/PM (e.g., 6/28/2019 7:00:36 AM).
* missing: Placeholder column containing no meaningful data; all entries are recorded as "value" and should be disregarded in analyses.
* geometry: GPS coordinates (X, Y) representing the animal's location on the landscape at the time of the daily maximum body temperature event. Coordinates are expressed as a pair of projected spatial coordinates.

#### File: Tamp.csv

**Description:**  Daily body temperature amplitude (°C), calculated as the difference between the maximum and minimum body temperatures recorded each day for individual plains zebra (*Equus quagga*) and blue wildebeest (*Connochaetes taurinus*).

##### Variables

* id: individual animal id
* day :Date of the amplitude body temperature  M/D/YYYY (e.g., 7/4/2= July 4, 2019). 
* min:  the calibrated minimum body temperature (°C)
* max:  the calibrated maximum body temperature (°C)
* amplitude: the daily body temperature amplitude (max-min)
* season:  CD= cool dry (May 2019 to August 2018), HD= hot dry (September 2019 to November 2019), HW = hot wet (December 2019 to April 2020)
* species: CT = Blue wildebeest, EQ= Plains zebra
* sex: f=female, m=male

#### File: Tmin_public.csv

**Description:** Minimum daily body temperature (°C) recorded for each individual plains zebra (*Equus quagga*) and blue wildebeest (*Connochaetes taurinus*).

##### Variables

* id: individual animal id
* day: Date that minimum body temperature occured M/D/YYYY (e.g., 7/4/2= July 4, 2019). 
* HOD: Hour at which the observation was recorded, expressed in 24-hour format (0–23), where 0 represents midnight and 23 represents 11:00 PM.
* clbrtd_: the calibrated minimum body temperature (°C)
* sex: f=female, m=male
* species: CT = Blue wildebeest, EQ= Plains zebra
* season:  CD= cool dry (May 2019 to August 2018), HD= hot dry (September 2019 to November 2019), HW = hot wet (December 2019 to April 2020)
* min_dat: Date that minimum body temperature occured M/D/YYYY (e.g., 7/4/2= July 4, 2019). 
* event:  Unique identification number assigned to each recorded daily maximum body temperature event
* loc_dat:  Date and time of the GPS collar location used to determine the animal's position on the landscape at the time of the daily maximum body temperature event and link that location to associated environmental variables. Format: M/D/YYYY h:mm AM/PM (e.g., 6/28/2019 7:00:36 AM).
* missing: Placeholder column containing no meaningful data; all entries are recorded as "value" and should be disregarded in analyses.
* geometry: GPS coordinates (X, Y) representing the animal's location on the landscape at the time of the daily minimum body temperature event. Coordinates are expressed as a pair of projected spatial coordinates.

#### File: Wildebeest_anomalies_public.csv

**Description:** Body temperature anomalies for individual blue wildebeest (*Connochaetes taurinus*) in Etosha National Park, Namibia, during 2019–2020. Anomalous body temperatures were identified using the *Anomalize* R package (Dancho & Vaughan, 2023; Figure S1). Anomalies were defined statistically as deviations above or below an individual’s expected temporal body temperature pattern rather than fixed physiological thresholds.

* id: individual animal id
* loc.date:  Date and time of the GPS collar location used to determine the animal's position on the landscape at the time of the anomalous body temperature event and link that location to associated environmental variables. Format: M/D/YYYY h:mm AM/PM (e.g., 6/28/2019 7:00:36 AM).
* anom.date:Date  at the time of the anomalous body temperature event. Format: M/D/YYYY (e.g., 6/28/2019).
* species: CT = Blue Wildebeest
* sex: f= female, m=male
* event:  Unique identification number assigned to each body temperature event (anomalous and non-anomalous), used to distinguish individual events and identify those classified as anomalous.
* anomaly: Indicates whether the daily maximum body temperature event was classified as anomalous (yes) or non-anomalous (no).
* type: NA = non-anomalous event, low anomalous event below the individuals median body temp and high= anomalous event above the individuals median body temp
* TOD: Hour of day at which the body temperature event occurred, expressed in 24-hour format (0–23), where 0 represents midnight and 23 represents 11:00 PM.
* season: CD= cool dry (May 2019 to August 2018), HD= hot dry (September 2019 to November 2019), HW = hot wet (December 2019 to April 2020)
* time: Date  at the time of the anomalous body temperature event. Format: M/D/YYYY (e.g., 6/28/2019).
* premean: Mean movement rate (km/hr) during the 60 minutes preceding the body temperature event.
* postmean: Mean movement rate (km/hr) during the 60 minutes after the body temperature event.
* premean45: Mean movement rate (km/hr) during the 45 minutes preceding the body temperature event.
* postmean45: Mean movement rate (km/hr) during the 45 minutes after the body temperature event.
* premean60: Mean movement rate (km/hr) during the 60 minutes preceding the body temperature event.
* postmean60: Mean movement rate (km/hr) during the 60 minutes after the body temperature event.
* premean120: Mean movement rate (km/hr) during the 120 minutes preceding the body temperature event.
* postmean120: Mean movement rate (km/hr) during the 120 minutes after the body temperature event.
* premean90: Mean movement rate (km/hr) during the 90 minutes preceding the body temperature event.
* postmean90: Mean movement rate (km/hr) during the 90 minutes after the body temperature event.
* X: Projected easting coordinate (m) representing the animal's GPS location associated with the body temperature event.
* Y: Projected northing coordinate (m) representing the animal's GPS location associated with the body temperature event.

#### File: Zebra_anomalies_public.csv

**Description:** Body temperature anomalies for individual plains zebra (*Equus quagga*) in Etosha National Park, Namibia, during 2019–2020. Anomalous body temperatures were identified using the *Anomalize* R package (Dancho & Vaughan, 2023; Figure S1). Anomalies were defined statistically as deviations above or below an individual’s expected temporal body temperature pattern rather than fixed physiological thresholds.

##### Variables

* id: individual animal id
* loc.date:  Date and time of the GPS collar location used to determine the animal's position on the landscape at the time of the anomalous body temperature event and link that location to associated environmental variables. Format: M/D/YYYY h:mm AM/PM (e.g., 6/28/2019 7:00:36 AM).
* anom.date:Date  at the time of the anomalous body temperature event. Format: M/D/YYYY (e.g., 6/28/2019).
* species: EQ = Plains Zebra
* sex: f= female, m=male
* event:  Unique identification number assigned to each body temperature event (anomalous and non-anomalous), used to distinguish individual events and identify those classified as anomalous.
* anomaly: Indicates whether the daily maximum body temperature event was classified as anomalous (yes) or non-anomalous (no).
* type: NA = non-anomalous event, low anomalous event below the individuals median body temp and high= anomalous event above the individuals median body temp
* TOD: Hour of day at which the body temperature event occurred, expressed in 24-hour format (0–23), where 0 represents midnight and 23 represents 11:00 PM.
* season: CD= cool dry (May 2019 to August 2018), HD= hot dry (September 2019 to November 2019), HW = hot wet (December 2019 to April 2020)
* premean: Mean movement rate (km/hr) during the 60 minutes preceding the body temperature event.
* postmean: Mean movement rate (km/hr) during the 60 minutes after the body temperature event.
* geometry_1:  Projected X-coordinate (easting) of the animal's GPS location associated with the body temperature event, expressed in meters.
* geometry_2: Projected Y-coordinate (northing) of the animal's GPS location associated with the body temperature event, expressed in meters.

## Code/software

All datasets are provided as comma-separated values (.csv) files and can be viewed using freely available software, including R or Excel. No specialized software is required to access or view the data.

Data processing and analyses were conducted using R version 4.2.1 (R Core Team, 2022). GPS-derived movement rates were calculated using the *adehabitatLT&#xA0;*&#x70;ackage (Calenge, 2024). Movement rates were calculated between consecutive GPS locations recorded at 10-minute intervals by dividing step length (m) by elapsed time and converting the resulting values to km/h. Hourly movement rates were calculated as the mean of six consecutive 10-minute movement rates. Daily distance traveled was calculated as the sum of consecutive GPS step lengths within each 24-hour period.

Daily minimum, maximum, and amplitude (maximum minus minimum) body temperatures were determined for individual plains zebra (*Equus quagga*) and blue wildebeest (*Connochaetes taurinus*). Anomalous body temperatures were identified using the *Anomalize* R package (Dancho & Vaughan, 2023; Figure S1). Anomalies were defined statistically as deviations above or below an individual's expected temporal body temperature pattern rather than fixed physiological thresholds.

Additional datasets contain body temperature anomaly classifications, associated movement rates, GPS locations, and environmental variables, including distance to the nearest known water source and tree density.

No analysis scripts are included in this submission.

## Access information

N/A

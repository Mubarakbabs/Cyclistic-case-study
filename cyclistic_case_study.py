{"metadata":{"kernelspec":{"name":"ir","display_name":"R","language":"R"},"language_info":{"mimetype":"text/x-r-source","name":"R","pygments_lexer":"r","version":"3.6.0","file_extension":".r","codemirror_mode":"r"}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"markdown","source":"# This notebook details the cleaning process for the Cyclistic case study, the Capstone from the Google Analytics Professional Certificate.\nThe entire presentation is available [here](https://drive.google.com/file/d/1TJVFIrYrOVh_mlhPSfGv1TTDRzKcJc2q/view?usp=sharing)","metadata":{"_uuid":"4173bca2-b4c7-4740-80de-1ac397c80b15","_cell_guid":"3507d27d-9a3d-4630-91e1-baab310abd81","trusted":true}},{"cell_type":"code","source":"#importing the necessary libraries for the cleaning and analysis process\nlibrary(\"tidyverse\")\nlibrary(\"lubridate\")\nlibrary(\"skimr\")","metadata":{"_uuid":"72dd9ddc-c031-4748-b094-96b0fc48ef66","_cell_guid":"8fca10f1-5856-4221-9ab9-23c5f5a857b0","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:09:36.501539Z","iopub.execute_input":"2023-01-06T10:09:36.504758Z","iopub.status.idle":"2023-01-06T10:09:36.526409Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#importing the csv files containing the trip data. The data consists of four quarters in separate files. They will be combined later in the process\ntrips_q2_19 <- read_csv(\"/kaggle/input/cyclistic/Divvy_Trips_2019_Q2.xlsx.csv\")\ntrips_q3_19 <- read_csv(\"/kaggle/input/cyclistic1/Divvy_Trips_2019_Q3.csv\")\ntrips_q4_19 <- read_csv(\"/kaggle/input/cyclistic1/Divvy_Trips_2019_Q4.csv\")\ntrips_q1_20 <- read_csv(\"/kaggle/input/cyclistic1/Divvy_Trips_2020_Q1.csv\")","metadata":{"_uuid":"958e03ed-12b5-4266-89dd-b6ef907a2c13","_cell_guid":"49cf0b9a-cf53-4b2b-bd97-de57505832ca","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:09:36.553180Z","iopub.execute_input":"2023-01-06T10:09:36.554547Z","iopub.status.idle":"2023-01-06T10:09:41.482778Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#checking the column names to ensure they match so that all the data can be combined in one place\ncolnames(trips_q2_19)\ncolnames(trips_q3_19)\ncolnames(trips_q4_19)\ncolnames(trips_q1_20)","metadata":{"_uuid":"a603c7c8-29a8-443f-9da6-fb0b36103266","_cell_guid":"e6d5c2d8-5699-4b7e-a30b-bf830717920a","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:09:41.484833Z","iopub.execute_input":"2023-01-06T10:09:41.485945Z","iopub.status.idle":"2023-01-06T10:09:41.512103Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"markdown","source":"We see that we have the same columns from q2 2019 to Q4 2019. But the names are different. Some new columns were also added in Q1 2020 while others were removed. Hence, analysis will be based on the common columns","metadata":{"_uuid":"e9c2f4a5-7044-4de1-94b9-f66827d2ffe1","_cell_guid":"308e10fe-fffc-4f78-8a46-aa088585d4b8","trusted":true}},{"cell_type":"code","source":"#first we edit the names of the columns on q2 19 so they are the same names as those in q3 and q4.\ntrips_q2_19 <- rename(trips_q2_19, \n                      \"trip_id\" = \"01 - Rental Details Rental ID\", \n                      \"start_time\" = \"01 - Rental Details Local Start Time\", \n                      \"end_time\" = \"01 - Rental Details Local End Time\", \n                      \"bikeid\" = \"01 - Rental Details Bike ID\", \n                      \"tripduration\" = \"01 - Rental Details Duration In Seconds Uncapped\", \n                      \"from_station_id\" = \"03 - Rental Start Station ID\", \n                      \"from_station_name\" = \"03 - Rental Start Station Name\", \n                      \"to_station_id\" = \"02 - Rental End Station ID\", \n                      \"to_station_name\" = \"02 - Rental End Station Name\", \n                      \"usertype\" = \"User Type\", \n                      \"gender\" = \"Member Gender\", \n                      \"birthyear\" = \"05 - Member Details Member Birthday Year\")","metadata":{"_uuid":"0778bec5-cba3-45e5-aa0c-2f988def7f07","_cell_guid":"ee4bc308-34ff-4903-b25e-02cb04dcd5cf","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:09:41.523468Z","iopub.execute_input":"2023-01-06T10:09:41.524601Z","iopub.status.idle":"2023-01-06T10:09:41.543166Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#to combine 2019 with 2020 data, we need the column names and types to match\n#fixing the different datetime types/formats\ntrips_q2_19$start_time = dmy_hms(trips_q2_19$start_time)\ntrips_q2_19$end_time = dmy_hms(trips_q2_19$end_time)\ntrips_q3_19$start_time = ymd_hms(trips_q3_19$start_time)\ntrips_q3_19$end_time = ymd_hms(trips_q3_19$end_time)\ntrips_q4_19$start_time = ymd_hms(trips_q4_19$start_time)\ntrips_q4_19$end_time = ymd_hms(trips_q4_19$end_time)\ntrips_q1_20$started_at = ymd_hms(trips_q1_20$started_at)\ntrips_q1_20$ended_at = ymd_hms(trips_q1_20$ended_at)","metadata":{"_uuid":"9dc76414-a97a-46c2-b7dc-3a712421ef58","_cell_guid":"55026e6b-f8be-4447-8d22-2b30bc6d6221","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:09:41.546116Z","iopub.execute_input":"2023-01-06T10:09:41.547356Z","iopub.status.idle":"2023-01-06T10:09:54.448095Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#combining the three 2019 quarters in the same dataframe then reconcile column names with 2020 names\ntrips_2019 <- rbind(trips_q2_19, trips_q3_19, trips_q4_19)\n\ntrips_2019 <- rename(trips_2019,\n                    \"start_station_name\" = \"from_station_name\",\n                    \"start_station_id\" = \"from_station_id\",\n                    \"end_station_name\" = \"to_station_name\",\n                    \"end_station_id\" = \"to_station_id\",\n                    )\ntrips_q1_20 <- rename(trips_q1_20,\n                     \"trip_id\" = \"ride_id\",\n                     \"start_time\" = \"started_at\",\n                     \"end_time\" = \"ended_at\",\n                     \"usertype\" = \"member_casual\")","metadata":{"_uuid":"35a0d509-cb81-464c-b287-3d4c2a8454ef","_cell_guid":"8940ade2-404d-46ce-9ea4-8b160fcc26fc","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:09:54.449898Z","iopub.execute_input":"2023-01-06T10:09:54.450967Z","iopub.status.idle":"2023-01-06T10:09:55.952080Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#q1 2020 data doesn't have a tripduration column.\n#creating a new trip duration column for q1 2020 and updating the one for 2019 so the data types match\ntrips_q1_20$tripduration <- as.numeric(trips_q1_20$end_time - trips_q1_20$start_time)\ntrips_2019$tripduration <- as.numeric(trips_2019$end_time - trips_2019$start_time)","metadata":{"_uuid":"f09191fd-9b8a-4f4d-b817-aa1aff1b427c","_cell_guid":"43281053-b38b-449e-b8c5-8416fcba337f","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:09:55.954845Z","iopub.execute_input":"2023-01-06T10:09:55.957107Z","iopub.status.idle":"2023-01-06T10:09:57.990629Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#stacking the two dataframes into one keeping only the common columns\nall_trips = rbind(\n    select(trips_2019, 'trip_id', 'start_time', 'end_time', 'tripduration', 'start_station_id', 'start_station_name','end_station_id','end_station_name','usertype'),\n    select(trips_q1_20, 'trip_id', 'start_time', 'end_time', 'tripduration', 'start_station_id', 'start_station_name','end_station_id','end_station_name','usertype'))\nstr(all_trips)","metadata":{"_uuid":"c7969dc8-e7ff-4c91-9b04-9795dd174cf7","_cell_guid":"043a7185-f37c-45d8-96cd-75c76bea1741","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:09:57.993026Z","iopub.execute_input":"2023-01-06T10:09:57.994287Z","iopub.status.idle":"2023-01-06T10:10:01.630841Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#inspecting the dataframe columns for quality issues\nskim_without_charts(all_trips)","metadata":{"_uuid":"9c10e4ee-dcfc-49cc-b35e-3e46a0b17a89","_cell_guid":"8fc14dd3-b722-41f9-9c42-f8d92abcf612","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:01.633501Z","iopub.execute_input":"2023-01-06T10:10:01.634794Z","iopub.status.idle":"2023-01-06T10:10:15.601639Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"markdown","source":"**The above shows the following issues with the data**\n1. One null value in end_station_id and end_station_name: this will be removed\n2. Negative trip duration: A trip cannot start earlier than it ended. these rows will be removed\n3. Some trips are longer than a day. Since the business doesn't allow a bike to be rented for more than one day, all trips above 1440 minutes are bad data and will be removed. The current trip duration are in seconds and will be converted to minutes\n4. There are four member types instead of two. The names of the user segments were changed. These will be reconciled.","metadata":{"_uuid":"a504a13f-20dc-4966-8d69-052dc449bc65","_cell_guid":"f4ec5a48-6147-4bd9-8e8b-ef3806edb4f3","trusted":true}},{"cell_type":"code","source":"#removing the missing values in end station\nalltrips <- all_trips[is.na(all_trips$end_station_name)==FALSE,]\n#note that the name of the dataframe here was changed to preserve the original combined dataframes before removing rows. This forms a sort of checkpoint so that if some rows are mistakenly removed, the analyst doesn't have to return to square 1 to fix it.","metadata":{"_uuid":"35004f88-de20-4cb1-b971-f67f7513587b","_cell_guid":"98a26b9c-5930-48ef-b242-0583e4e14aa6","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:15.603974Z","iopub.execute_input":"2023-01-06T10:10:15.607612Z","iopub.status.idle":"2023-01-06T10:10:15.802796Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#convert tripduration to minutes\nalltrips <- alltrips %>% mutate(tripduration = tripduration/60)\n#remove the following:\n#1. all trip duration below 0 and above 1440\n#2. trips starting at 'HQ QR' are not actually trips but are bikes removed from their docking station for quality control\nalltrips <- alltrips[!c(alltrips$tripduration<0\n                        |alltrips$tripduration>1440\n                        |alltrips$start_station_name == 'HQ QR'),]","metadata":{"_uuid":"1d59ab98-87d6-450f-a8cc-67c692e277fc","_cell_guid":"68fb5fff-71f8-47f2-aa0d-03c27b2d65b8","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:15.804659Z","iopub.execute_input":"2023-01-06T10:10:15.805785Z","iopub.status.idle":"2023-01-06T10:10:16.295678Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#reconcile old and new names for user groups\nalltrips$usertype <- alltrips$usertype %>%\nstr_replace( \"Subscriber\", \"member\") %>%\nstr_replace(\"Customer\", \"casual\")","metadata":{"_uuid":"4af692d8-7bd7-467f-b823-4b253b4492aa","_cell_guid":"4eaf9e4e-dc4d-4f78-9466-3466a99acc89","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:16.297772Z","iopub.execute_input":"2023-01-06T10:10:16.299133Z","iopub.status.idle":"2023-01-06T10:10:19.057663Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#check that the cleaning was successful\nskim_without_charts(alltrips)","metadata":{"_uuid":"615fcc4a-ff2d-4c89-96be-b88d468602f3","_cell_guid":"b2f8381b-b111-4093-831a-0fa020f0a367","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:19.060185Z","iopub.execute_input":"2023-01-06T10:10:19.061261Z","iopub.status.idle":"2023-01-06T10:10:33.280968Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#there are many outliers to the right \nalltrips %>% select(tripduration)%>% ggplot(aes(x=tripduration))+geom_boxplot()\n#the boxplot looks pretty strange. While there seem to be many outliers, they are so many that we can't chalk them down to measurement errors. It simply means there are some users that use the bikes very intensively beyond the average","metadata":{"_uuid":"9a11cef4-bc83-4448-982e-4bb63c10edbf","_cell_guid":"ffc26414-f720-4fd1-a4c1-f645700a6782","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:33.282856Z","iopub.execute_input":"2023-01-06T10:10:33.283967Z","iopub.status.idle":"2023-01-06T10:10:40.979450Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#investigating outliers\nq1 = quantile(alltrips$tripduration, probs=0.25)\nq3 = quantile(alltrips$tripduration, probs=0.75)\nIQR = q3-q1\nlb = q1 - (1.5*IQR)\nub = q3 + (1.5*IQR)\noutliers <- alltrips[alltrips$tripduration<lb|alltrips$tripduration>ub,]\nskim_without_charts(outliers)","metadata":{"_uuid":"f88c9e82-8195-4141-8023-6114ff02af62","_cell_guid":"e14945c5-fc02-47fc-9136-db26fb7636bd","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:40.982652Z","iopub.execute_input":"2023-01-06T10:10:40.984529Z","iopub.status.idle":"2023-01-06T10:10:42.209709Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"markdown","source":"The investigation of the outliers shows that over 200k rows will be considered as outliers looking at this.\nAlso, all of the \"outliers\" fall within reasonable range of a bicycle ride (it's not too strange to ride a bicycle for several hours). And this seems like a reasonable frequent occurrence. Hence, the outliers will be left as is since they can't be written off as bad data","metadata":{"_uuid":"bf21a741-739b-4a8e-bfeb-a963ecefe681","_cell_guid":"173f6b61-730e-48e0-ab80-68122d22d076","trusted":true}},{"cell_type":"code","source":"#taking a look at the distribution ride lengths. It seems reasonable that more people will make shorter trips than longer\nalltrips %>% ggplot(aes(x=tripduration))+geom_histogram()","metadata":{"_uuid":"05bffcfe-f8bb-474d-a56a-dc5cb2ab830b","_cell_guid":"348d7509-4e93-4c3e-8b48-ba634a8f2023","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:42.211839Z","iopub.execute_input":"2023-01-06T10:10:42.213336Z","iopub.status.idle":"2023-01-06T10:10:43.881208Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#a closer look at the long tail shows a bump at the end, which indicates that some users rent the bikes for an entire day\nalltrips %>% ggplot(aes(x=tripduration))+geom_histogram()+coord_cartesian(ylim=c(0,100000))","metadata":{"_uuid":"09c3ec3e-85c1-4847-91ca-f2aaa03016d8","_cell_guid":"9fcbe967-6bb4-4535-b60f-d880a7d73c53","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:43.883279Z","iopub.execute_input":"2023-01-06T10:10:43.884337Z","iopub.status.idle":"2023-01-06T10:10:45.343497Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"markdown","source":"# Analysis","metadata":{"_uuid":"32aa251a-6d1f-4972-b5e4-0f880e09e50c","_cell_guid":"f40389d6-d059-43e5-93df-0aee93c99107","trusted":true}},{"cell_type":"markdown","source":"**Question: How do annual members and casual users differ?**","metadata":{"_uuid":"f8337489-7fe1-4269-82a0-5d0611467eab","_cell_guid":"db9952e6-cced-413d-ab13-5a40b27a0904","trusted":true}},{"cell_type":"code","source":"#creating new columns to perform time based calculations\nalltrips <- alltrips%>%mutate(\n    ride_month = month(start_time, label=TRUE), \n    weekday = wday(start_time,label=TRUE), \n    date = mday(start_time), \n    timeofday = hour(start_time)\n)","metadata":{"_uuid":"89e88924-c758-4833-9e3b-ec034f5f1a47","_cell_guid":"4fc15cde-2801-45de-8de5-eb67bfb1cfce","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:45.346001Z","iopub.execute_input":"2023-01-06T10:10:45.347195Z","iopub.status.idle":"2023-01-06T10:10:51.275759Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#how many trips are started by casual vs members respectively?\nalltrips%>%group_by(usertype) %>% summarise(number_of_rides = n(),) %>%mutate(perc_total = number_of_rides/sum(number_of_rides))","metadata":{"_uuid":"f13f5e88-1f52-4304-b3f4-0aec894ff629","_cell_guid":"a513429c-4118-4da4-a17d-e81162736f2b","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:51.278125Z","iopub.execute_input":"2023-01-06T10:10:51.279330Z","iopub.status.idle":"2023-01-06T10:10:51.383460Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"markdown","source":"members are responsible for majority of trips started","metadata":{"_uuid":"7afec189-0417-463c-9273-77d5fcf864d7","_cell_guid":"faa74be9-20e3-4ef2-ae5e-4d829a0df40a","trusted":true}},{"cell_type":"code","source":"#what is the average ride length for each user group?\naggregate(alltrips$tripduration ~ alltrips$usertype, FUN = mean)\naggregate(alltrips$tripduration ~ alltrips$usertype, FUN = median)","metadata":{"_uuid":"334cea57-71ec-4453-a7ad-962855128223","_cell_guid":"0ff4ef32-8a18-42c1-bd18-9118a1ecc041","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:51.385583Z","iopub.execute_input":"2023-01-06T10:10:51.386634Z","iopub.status.idle":"2023-01-06T10:10:53.590759Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"markdown","source":"the average casual trip is three times the length of the member trip. This means they are spending a lot of time riding but they prefer to do this without subscribing.","metadata":{"_uuid":"d7aa9b69-01cf-4779-b3a0-25f82927aa8d","_cell_guid":"722b5d36-52e2-41f1-9b62-5b9126b4faba","trusted":true}},{"cell_type":"code","source":"#number of trips by day of week\nalltrips%>%group_by(usertype,weekday)%>%\nmutate(number_of_rides=n())%>%\nggplot(aes(x=alltrips$weekday, y=number_of_rides, color=usertype))+\ngeom_point()","metadata":{"_uuid":"bc081ec3-d0ca-454f-8fc2-9cca9bd27cc7","_cell_guid":"c315bfc8-01c1-4a4f-97dd-5b4c11651be6","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:10:53.593728Z","iopub.execute_input":"2023-01-06T10:10:53.595500Z","iopub.status.idle":"2023-01-06T10:12:45.885058Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"markdown","source":"members cycle mostly on weekdays (explains the shorter trip lengths) while casual users have more trips on weekends. we should encourage casual to ride to work.","metadata":{"_uuid":"a8084100-be46-4421-8720-5a4e5d5851fe","_cell_guid":"b9ba6f46-b0d4-460b-b1f6-9914260b2bab","trusted":true}},{"cell_type":"code","source":"#number of trips by time of day\nalltrips%>%group_by(usertype,timeofday)%>%\nmutate(number_of_rides=n())%>%\nggplot(aes(x=alltrips$timeofday, y=number_of_rides, color=usertype))+\ngeom_point()\n#spike around 7pm for members and even casual though not as high. Strengthens the initial hypothesis. Let's see if this spike exists for both weekend and weekday","metadata":{"_uuid":"08bf0708-8406-409a-b943-b3998cafe3c4","_cell_guid":"eb642b3d-c465-4de3-9e6f-917e68ad9b86","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:12:45.887078Z","iopub.execute_input":"2023-01-06T10:12:45.888146Z","iopub.status.idle":"2023-01-06T10:14:37.848986Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#number of trips by time of day during the weekend. The 7pm outlier persists but the morning spike is gone\nweekend <- c('Sat', 'Sun')\nalltrips[alltrips$weekday==weekend,]%>%group_by(usertype, timeofday)%>%mutate(number_of_rides=n())%>%ggplot(aes(x=timeofday, y=number_of_rides, color=usertype))+geom_point()","metadata":{"_uuid":"beec5f5f-913f-4e9a-9b8a-e0fac16029ca","_cell_guid":"f5e93b00-5277-4dea-b5fa-9f5d410f1bf7","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:14:37.850862Z","iopub.execute_input":"2023-01-06T10:14:37.852013Z","iopub.status.idle":"2023-01-06T10:14:53.296020Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#number of trips by time of day during weekdays\nalltrips[alltrips$weekday %in% weekend==FALSE,]%>%\ngroup_by(usertype,timeofday)%>%\nmutate(number_of_rides=n())%>%\nggplot(aes(x=timeofday, y=number_of_rides, color=usertype))+\ngeom_point()\n#perhaps casual users use bikes as a last resort at closing time even if they didn't take it to work","metadata":{"_uuid":"d7995ba4-78ee-4293-b878-4f52d5d293c0","_cell_guid":"78d55d7b-02f9-46fa-a7ec-ae849c6da9e6","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:14:53.298337Z","iopub.execute_input":"2023-01-06T10:14:53.299538Z","iopub.status.idle":"2023-01-06T10:16:15.821279Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#month by month trend\nalltrips%>%group_by(usertype, ride_month)%>%mutate(number_of_rides=n())%>%ggplot(aes(x=ride_month, y=number_of_rides, color=usertype))+geom_point()","metadata":{"_uuid":"8e8eed7e-8998-4f3e-85aa-d537a3836778","_cell_guid":"2647a2a8-929f-4508-a9f3-ca98633ad06e","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:16:15.823486Z","iopub.execute_input":"2023-01-06T10:16:15.825182Z","iopub.status.idle":"2023-01-06T10:18:07.354174Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"markdown","source":"Number of trips trend by month, with more trips during the summer months. However, the trends are similar for both casual users and members. Hence, this doesn't offer insights to how the marketing strategy for members can be differentiated from those for casual users","metadata":{"_uuid":"b4e7f0ee-4e81-4b55-9bb3-771e2aca5281","_cell_guid":"53f2d5ce-df49-4942-bd7e-794e82ea3274","trusted":true}},{"cell_type":"code","source":"#what stations do trips most commonly start from?\nstation_trips <- aggregate(alltrips$trip_id ~ alltrips$usertype + alltrips$start_station_name+alltrips$weekday, FUN = length)%>% arrange(desc(\"trip_id\"))%>%pivot_wider(names_from = \"alltrips$usertype\", values_from = \"alltrips$trip_id\")","metadata":{"_uuid":"6b56edc8-199b-4deb-a61c-bdf2c489aa98","_cell_guid":"8d160e12-ed36-421f-af2a-872903b018b2","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:18:07.356184Z","iopub.execute_input":"2023-01-06T10:18:07.357412Z","iopub.status.idle":"2023-01-06T10:18:09.984944Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"colnames(station_trips)","metadata":{"_uuid":"b071b96b-6594-4f8b-91e4-3eacefc03bdf","_cell_guid":"bbe81b9b-5822-4550-9cf9-c17cdeb4e3af","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:23:02.762814Z","iopub.execute_input":"2023-01-06T10:23:02.764209Z","iopub.status.idle":"2023-01-06T10:23:02.776259Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"station_trips <- rename(station_trips,\n                        'start_station' = 'alltrips$start_station_name', \n                        'weekday' = 'alltrips$weekday'\n                       )","metadata":{"_uuid":"da038941-49f7-4cef-b96a-edcf45d6b36d","_cell_guid":"4f465e4f-5606-4472-948b-ba678a4f9851","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:26:03.716084Z","iopub.execute_input":"2023-01-06T10:26:03.717344Z","iopub.status.idle":"2023-01-06T10:26:03.729420Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#where do members start trips from the most? \nstation_trips%>%group_by(start_station)%>%summarise(n_trips = sum(member))%>%arrange(desc(n_trips))","metadata":{"_uuid":"912a8bd7-9cc5-40fc-9509-5e012d676a5e","_cell_guid":"64b2bfd9-5064-4f8c-9353-ed8c0ff99c7e","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:26:19.440166Z","iopub.execute_input":"2023-01-06T10:26:19.441592Z","iopub.status.idle":"2023-01-06T10:26:19.492746Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"#where do casual users start trips from the most? \nstation_trips%>%group_by(start_station)%>%summarise(n_trips = sum(casual))%>%arrange(desc(n_trips))","metadata":{"_uuid":"86f25293-511d-4d72-89ab-3c3b6035e36c","_cell_guid":"9e5ef4f4-fa2f-40d5-bc77-5a5da468968c","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:26:57.448444Z","iopub.execute_input":"2023-01-06T10:26:57.449812Z","iopub.status.idle":"2023-01-06T10:26:57.509317Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"markdown","source":"This suggests there is a geographical divide between members and casual users","metadata":{"_uuid":"52d7955c-5d00-4908-98f9-3edea2be4f88","_cell_guid":"1b12b354-aab9-4a49-b080-702a04a6bc29","trusted":true}},{"cell_type":"code","source":"#create a summarized data frame with number of rides and mean ride duration by usertype, weekday and time of day\nn_ride <- aggregate(alltrips$trip_id ~ alltrips$usertype +date(alltrips$start_time)+ alltrips$weekday +alltrips$timeofday, FUN = length)\nmean_length <- aggregate(alltrips$tripduration ~ alltrips$usertype +date(alltrips$start_time)+alltrips$weekday +alltrips$timeofday , FUN = sum)\ndf_export <- merge(n_ride,mean_length, sort = FALSE)","metadata":{"_uuid":"19919f90-c8a8-4c83-aa8e-f36fb8e868fd","_cell_guid":"968da2a4-f6a3-46f7-a6cc-05381fcf23e5","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:27:14.278330Z","iopub.execute_input":"2023-01-06T10:27:14.280905Z","iopub.status.idle":"2023-01-06T10:27:31.763163Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"setwd('/kaggle/working')\n\nwrite.csv(df_export, \"summarized_cyclistic.csv\")\nwrite.csv(station_trips, \"stations_start.csv\")","metadata":{"_uuid":"92a6f242-6862-4664-a6b2-41661e97f961","_cell_guid":"d8693ed2-3234-43df-98c2-54bef439556d","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:27:31.765047Z","iopub.execute_input":"2023-01-06T10:27:31.766146Z","iopub.status.idle":"2023-01-06T10:27:31.840802Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"list.files(path = \"../working\")","metadata":{"_uuid":"9a836459-adec-4360-901c-ffd3e98f7607","_cell_guid":"072edd79-79e6-497b-9857-ba3745c2a1b5","collapsed":false,"execution":{"iopub.status.busy":"2023-01-06T10:27:31.848472Z","iopub.execute_input":"2023-01-06T10:27:31.849581Z","iopub.status.idle":"2023-01-06T10:27:31.863284Z"},"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]},{"cell_type":"code","source":"","metadata":{"_uuid":"a7162b92-75ff-4d81-83d6-966ea4c6d70d","_cell_guid":"41539d80-1b7d-4664-a3c7-fc42fa5c810f","collapsed":false,"jupyter":{"outputs_hidden":false},"trusted":true},"execution_count":null,"outputs":[]}]}
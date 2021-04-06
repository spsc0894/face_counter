

# Face Counter


OS: Ubuntu:18.04

![Grafana snapshot](./images/grafana.png)

## Introduction

This application count the total number of faces and displays the total count of faces along with the video stream on grafana dashboard

## How it Works
- The application uses haar cascade face detection model to detect faces and take input from camera. It updates the change in count of faces for each frame to MySQL database and the final visualization can be seen on Grafana dashboard

## Setup
### Get the code
Clone the reference implementation
```
sudo apt-get update && sudo apt-get install git
git clone https://github.com/spsc0894/face_counter
```


## Run the application

Change the current directory to the git-cloned application code location on your system:
```
cd face_counter
```
Execute below command:

    ```
    sudo make my-app
    ```

Once all the containers are created check logs for grafana and mysql containers on seperate terminal wondows to make sure they are ready to take connections

    ```
    docker logs -f face_counter_grafana_1
    ```

    ```
    docker logs -f face_counter_db_1
    ```

Verify that grafana and mysql container are ready to take connections as shown in below screenshots

![Grafana container logs](./images/grafana_logs.png)

![MySQL container logs](./images/mysql_logs.png)

#Once both grafana and mysql are ready to take connection. Go to: http://localhost:3000

![Grafana Login](./images/grafana_login.png)

Login using below credentials:
    ```
    Username: admin
    password: admin
    ```

## Add datasource

Click on Datasources as shown in below screenshot:

![Grafana Add Datasource](./images/grafana_add_ds.png)

Click on "Add Datasource" and select "MySQL"

![Grafana Add Datasource MySQL](./images/grafana_mysql.png)

Provide the details as shown in below screenshot:

Name: BOOKINFO<br>
HOST: db:3306<br>
Database: BOOKINFO<br>
User: surya<br>
password: admin<br>


![Grafana MySQL Details](./images/grafana_mysql_details.png)

And click on "Save and test"

## Add Dashboard

In the left panel click on "+" symbol and select import

![Grafana Dashboard import](./images/grafana_import.png)

Select Upload JSON and browse to face_counter/grafana/dashboard and upload dashboard.json

![Grafana dashboard upload](./images/grafana_dash_upload.png)

Now you can see the video stream and the count of faces alongside

![Grafana snapshot](./images/grafana.png)

# YouTube Channel Statistics Analysis

## Introduction
This project aims to analyze the statistics of several YouTube channels related to LGBTQ+ content. It utilizes the YouTube Data API to retrieve channel information such as subscribers, views, and total videos uploaded.

## Retrieving Channel IDs
The `get_channel_id` function retrieves the unique channel ID for a given channel username using the YouTube Data API.

## Main Function
The `main` function demonstrates how to use the `get_channel_id` function to retrieve channel IDs for a list of channel usernames. It then prints the channel IDs.

## Retrieving Channel Statistics
### Function to Retrieve Channel Statistics
The `get_channel_stats` function retrieves various statistics for each channel, including subscribers, views, total videos, and publication date.

### Sample Data Retrieval
The sample data retrieval code demonstrates how to use the `get_channel_stats` function to retrieve statistics for multiple channels and convert it into a pandas DataFrame.

## Data Visualization
### Channel Subscribers
A bar chart is created to visualize the number of subscribers for each channel.

### Channel Views
A bar chart is created to visualize the total views for each channel.

### Channel Video Count
A bar chart is created to visualize the total number of videos uploaded by each channel.

## Conclusion
This analysis provides insights into the performance and popularity of various LGBTQ+ YouTube channels based on their subscribers, views, and video count. Further analysis could include examining trends over time and comparing different metrics to understand channel growth and engagement.

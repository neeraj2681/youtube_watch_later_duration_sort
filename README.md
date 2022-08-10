# youtube_watch_later_duration_sort
Sorting watch later playlist from Youtube based on duration of the videos

Most of us have a pleothera of videos in watch later playlist of our Youtube Account. These videos might be important, and you may want to remove these videos only after watching them. 
One of the efficient ways to watch these videos can be based on the length. But, by default Youtube doesn't provide any method to sort these videos based on the duration.

This code reads the Watch later.csv file from the user data, which can be obtained easily from the users Youtube account. 
By making use of Youtube Data API v3, one can easily fetch the details of any video from Youtube based on the URL of video. To use Data API v3, one need to generate API key, which allows around 10000 hits per day. 1 hit means fetching detail of one video. Generating this Youtube Data API key is totally free!

Once the user have their data and this API key with them all they need to do is provide the path of Watch later.csv file and the API key as argument to this program.
The program will create a new CSV file, with Title, URL, and duration of videos in the watch later playlist. This CSV file will be sorted based on the duration of videos.

<h4>Downloading the Youtube Data</h4>

<h4>Generating the Data API key</h4>


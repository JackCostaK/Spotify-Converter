# Spotify-Converter
Converts Spotify Playlists to mp3 files

## How To Use

### 1. Clone Repository Using Git
Clone this repository with
```bash
git clone https://github.com/JackCostaK/Spotify-Converter
```
Alternatively you can directly download the zip from the repository webpage by navigating to the green "Code" button and selecting "Download ZIP"

Open terminal or command line and use this command to enter the repository
```bash
cd Spotify-Converter/
```

### 2. Download Necessary Packages
If you are running a modern version of python, you should already have `pip` installed. We will be installing most of our packages using `pip`.

Run this command in your terminal to install the packages you will need
```bash
pip install dotenv && pip install requests && pip install yt_dlp && pip install youtube_search
```
If this doesn't work try replacing `pip` with `pip3`

### 3. Download FFMPEG
You will need to download FFMPEG and move into your Python Script directory

Download [FFMPEG](https://www.ffmpeg.org/download.html) here

After downloading and extracting the ffmpeg folder you can find ffmpeg.exe in `ffmpeg\bin\ffmpeg.exe`

It is important that you move this exe file to your python script directory. It should be here

`C:\Users\{Your User}\AppData\Local\Programs\Python\Python313\Scripts`

### 4. Create a Spotify API Project
You will need an API key to use this project. To do this you need to sign into spotify for developers and make a new project

[Spotify for developers](https://developer.spotify.com/)

After signing in go to dashboard in the top right and click Create App.
The app name doesn't matter and neither does the description. For the redirect URL you can put any valid URL.
Now agree to the terms of service and click save.

Navigate to `Settings` in the top right and you should see a page like this
![image](https://github.com/user-attachments/assets/88abe509-e5e1-4409-a014-fb670743ab65)


Now you just need to save your Client ID and Client Secret as you will need it when using the program

(DO NOT SHARE YOUR CLIENT SECRET, THE PROJECT IN THIS IMAGE WAS FOR EXAMPLE PURPOSES ONLY)

### 5. Find the ID of the Playlist You Want to Download
You now need the Playlist id of the playlist you want to download

Copy the URL of the Playlist you want to download. The entire URL will look something like this `https://open.spotify.com/playlist/1tHV0dMmhskUz6r2ETC7WT`. We are only interested in the code that comes after `spotify.com/playlist/`. In this example, our playlist id would be `1tHV0dMmhskUz6r2ETC7WT`.

### 6. Run the Program
Final to run the program simply run this in your terminal session
```bash
python main.py
```
If this doesn't work try replacing `python` with `python3`

Enjoy!






# xdown
❌videos downloader

## Install
```BASH
git clone https://github.com/ai-enma/xdown
cd xdown
pip3 install -r requirements
```

## Usage Multiple URL

First prepare a file with all the video links
like that:

##### list.txt
```HTML
htts://xvideos.com/video...
htts://xvideos.com/video...
htts://xvideos.com/video...
```

#### Launch
```BASH
python3 xdown.py list.txt -O videos

# -O will specify the ouput folder to store the videos
```

#### Result
```
 ??  Quality: HIGH
 ??  Domain:  XVIDEOS
 ??  Output directory: 'videos'
---- Downloading 'video....mp4'
 OK  Downloading 'video....mp4'
 ??  Quality: HIGH
 ??  Domain:  XVIDEOS
 ??  Output directory: 'videos'
---- Downloading 'video....mp4'
 OK  Downloading 'video....mp4'
```

## Usage Mass download from mutiple pages

#### Launch
```BASH
python3 xdown.py URL -O output_folder NB_PAGES_TO_SCAN
```

#### Result
```
 ??  Quality: HIGH
 ??  Domain:  XVIDEOS
 ??  Output directory: 'videos'
---- Downloading 'video....mp4'
 OK  Downloading 'video....mp4'
 ??  Quality: HIGH
 ??  Domain:  XNXX
 ??  Output directory: 'videos'
---- Downloading 'video....mp4'
 OK  Downloading 'video....mp4'
```

## Requirements
- requests
- wget

# De-slowmo-videos

# Summary
Quick small Python script to reduce the filesize (and playback speed) of
slow-motion videos.

| Original Video | Output Video |
| :------------: | :----------: |
| 240 fps        | 40 fps       |
| 2.76 Gb        | 689 Mb       |


## Description
Searching the web, I couldn't find an easy tool to remove the slow motion from
large, and long slow-motion videos. All tools seemed to "remove" slow-motion
by changing the video playback speed, and not by removing frames from the image.
This was required as I had run out of cloud storage, but still wanted to preserve
my memories.

This simple script uses [Open CV](https://opencv.org/) to first load a video
and extract video properties such as length, width, height, and fps. An image
writer is created pointing towards a user specified output file using these
properties and a user specified new FPS value. The ratio between the original
FPS and new FPS calculates which frame should be written to the new video in
order to match that new FPS.

$\frac{\text{fps}}{\text{new fps}} = i^{th}\text{ frame to keep}$

## Usage
This was a super quick project (beyond the hours of research) so is written as a
small script to be ran modifying the Python file itself. The modifiable
variables are found at the top. These are:
- `base`: the directory of the input and output videos (to save me writing it
 out again).
- `in_file`: the filename of the input file. Will be used with `base`.
- `out_file`: the filename of the output file. Will be used with `base`.
- `new_fps`: the frames per second of the image to write. I find 40-60 fps still
 preserves smooth video.

## Important Information
- Different video codecs - Used to write the video to the local machine, these
 can be OS dependent, and/or dependent on the input video. This script uses the
 `*'mp4v'` codec which also matches that of the input file.
- Trying to load as a Numpy array - Please don't do this, videos are typically
 far too large to load into an array, but you can still operate on the singular
 video frame.
- Errors - Beyond the codec errors, I found an error I couldn't make sense of
 but I was reading / writing to a non-existent filepath. The error contained no
 mention of filepath or reading / writing difficulties but this was the cause.

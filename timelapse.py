#!/usr/bin/env python3

#imports
import ffmpeg
import sys
#import time

#local import
import config
import timelapseio

#Main script
#input addition ss="00:00:03"? suggested by author, actually irrelevant?
try:
    (ffmpeg.input(config.rtsp_url)
        .output(
            timelapseio.makedirandfile(
                config.output_dir,
                config.prefix,
                config.timespec,
                config.use_subdirectory),
            vframes=1,
            format='image2')
        .overwrite_output()
        .run(
            capture_stdout = True,
            capture_stderr = True)
    )
except ffmpeg.Error as e:
    print(e.stderr.decode(), file=sys.stderr)
    sys.exit(1)

print('Captured image!')
# semi2-scav
Seminar 2. SCAV subject. UPF.

# S2-scav
# Quim Marcé - 205523
Seminar 2 SCAV subject. UPF. Audiovisual System Engineering. 

Previous steps)

Download the BigBuckBunny(refered to as BBB from now on) video from this link: https://peach.blender.org/download/

We need the .mp4 format for this seminar, so if by mistake another video format is downloaded it can be easily converted using ffmpeg "ffmpeg -i input.avi output.mp4"

All exercises are implemented in "s2.py", a deeper explanation on how it works can be found in the end of this file.

Note: see that the path in the screenshots does not correspond to the folder of this repository. This is because with the initial repository I had created I had some storage issues and could not upload it, so finally I decided to create a new one which is actually a copy of the initial one.

EXERCISE 1)

Corresponding files: ex1.png

Using ffmpeg function -ss X -t Y already gives the cut video starting at X with duration Y.

EXERCISE 2)

Corresponding files: ex2total.png

Computing the histogram of the video is pretty intuitive, however, having to overlay it on the actual video or splitting the screen to show both at the same time is a bit more complex. To do so, I looked for a solution on the Internet and I found this official ffmpeg page where it is explained how to do it.

Source: https://trac.ffmpeg.org/wiki/Histogram

EXERCISE 3) 

Corresponding files: ex3-x.png

As the resizing was already applied in the last lab, we just had to use the same function 
"ffmpeg -i input.mp4 -vf scale=www:hhh output.mp4" to obtain a proper result.

EXERCISE 4)

Corresponding files: ex4-x.png

The first part of this exercise (converting audio to mono) is pretty simple and it can be done intuitively with "-ac 1" which refers to changing audio channels to 1. Further information can be found in the link attached to Source 1. 

For the second part of the exercise (using another audio codec) the use of the libfdk-acc is required in case we want to use Advanced Audio Coding (AAC), which is what I have done. So it is pretty useful visiting "section 8.5 libfdk_aac" in the link attached to source 2. A part of this order has been added "-c:v copy" in order to keep the same video part for the output.

Source 1: https://trac.ffmpeg.org/wiki/AudioChannelManipulation

Source 2: https://ffmpeg.org/ffmpeg-codecs.html 


PYTHON FILE "s2.py" EXPLANATION 

This file is aimed to be run from terminal with the following possible commands:

python3 s2.py source operation

Where "source" must be a video file (preferably in .mp4 format).

And "operation" can take several values:

	Exercise 1) cutXXYY
	
	Where XX indicates the second we want to start cutting the video and YY indicates the 		duration of this cut.
	
	Exercise 2) histogram
	
	It has no secret, it just does what is stated in exercise 2.
	
	Exercise 3) resizeXXX
	
	Where XXX indicates the height of the output resized video, it accepts the following 	values: 720, 480, 240, 120.
	
	Exercise 4.1) mono
	
	It converts the audio of the video to mono.
	
	Exercise 4.2) aac
	
	It converts the audio codec to Advanced Audio Codec (aac).


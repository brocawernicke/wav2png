import wave
from PIL import Image, ImageDraw

BAR_WIDTH = 5
IMAGE_SIZE_X = 2000
IMAGE_SIZE_Y = 300

w = wave.open("audio.wav", mode="rb")
frames = w.readframes(w.getnframes())
data = memoryview(frames).tolist()
signal_length = w.getnframes()

print(signal_length)

im = Image.new("RGB", (IMAGE_SIZE_X,IMAGE_SIZE_Y), (255,255,255))
draw = ImageDraw.Draw(im)

for py in range(0,IMAGE_SIZE_X,5):
    S = signal_length/IMAGE_SIZE_X
    bar = sum(data[int(py*S):int((py+5)*S)])/(2*5*S)
    draw.line((py, IMAGE_SIZE_Y/2+bar, py, IMAGE_SIZE_Y/2-bar), fill=200, width=(BAR_WIDTH-1))

im.save('out.png')

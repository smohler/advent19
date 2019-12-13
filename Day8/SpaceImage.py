#load data split every 150 pixels
import collections
data = list(open('input.txt', 'r').read().strip())
image = list(map(int, data))
number_of_layers = range(int(len(image)/150))
Layers = [image[i*150:i*150 + 150] for i in number_of_layers]
ZerosPerLayer = []
OnesPerLayer = []
TwosPerLayer = []
for Image in Layers:
    pixels = collections.Counter(Image)
    ZerosPerLayer.append(pixels[0])
    OnesPerLayer.append(pixels[1])
    TwosPerLayer.append(pixels[2])

I = ZerosPerLayer.index(min(ZerosPerLayer))
print(OnesPerLayer[I]*TwosPerLayer[I])


# pointillism-using-hexbot
As a part of noops challenge (https://github.com/noops-challenge) I made a python script to convert an image into art using pointillism.

The challenge was to use Hexbot api which generated random colors for pointillism. I used OpenCV to gather all the data on the picture and then generated 20 random colors from the api forming a color pallete which I used to color my picture.

I used parameter d = ((r2-r1) x 0.30) ^ 2 + ((g2-g1) x 0.59) ^ 2 + ((b2-b1) x 0.11) ^ 2 for calculating the color on the pallete which would be closest to the original color.

to pointilise your image run 
```
python fry.py --image realtive/path/to/img
```


## Original Image(Left) along with Converted image(Right) from script
![Alt text](examples/test2.png)
![Alt text](examples/test3.png)
![Alt text](examples/test5.png)


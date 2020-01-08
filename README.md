# manim-reveal
Combines the [manim library](https://github.com/3b1b/manim) with [reveal.js](https://github.com/hakimel/reveal.js/) to create animated slides.

## Setup
First install [manim](https://github.com/3b1b/manim)

Next get [reveal.js](https://github.com/hakimel/reveal.js/) and do the full setup (`npm install`)

Then install the python package  `manim-reveal` located in this repository, by running following command

```bash
pip install .
```

## Run example
Clone this repository, and run the following commands

```bash
cd python
manim example_slide_scene.py MathTest SimpleVideoSlide
```
This will create and copy the video and fragments files into the folder `video_slides` for each SlideScene.

Copy the folders, `video_slides`, `js`  and the file `index.html` into a new reveal.js directory.

Finally run `npm start` to start the presentation.

## How to create an animated slide

To create a new slide using manim, follow these steps
1. Subclass `SlideScene` instead of the `Scene` class.
2. In the `CONFIG` add the parameter `video_slides_dir`. This should point to a folder called `video_slides` in your reveal.js directory.
3. In `contruct()`, add the function call `self.slide_break()` whenever you want the presentation to pause.
4. Run the `manim` command on your python file. This will automatically update the `video_slides` directory you specified in the config.
5. Add the following tag `<script src="js/add_video_slide.js" slide_scene="SimpleVideoSlide"></script>` instead of `<section> ...</section>` in your `index.html`. You have one such tag for each video slide.
6. Make sure you add the tag `<script src="js/video_slide.js"></script>` at the bottom of your `index.html`. This only needs to be done once per index.html. This script is needed to make the video slide fragments work.
7. Run `npm start`, or refresh your browser if you have already started the server.

Below is a simple example of a video slide
```python
from manimlib.imports import *
from manim_reveal import SlideScene

class SimpleVideoSlide(SlideScene):
    CONFIG={
        "video_slides_dir":"../video_slides"
    }
    def construct(self):
        gamma = TexMobject("\gamma")
        gamma.scale(5)
        obj = Circle()

        self.play(FadeIn(obj))
        self.slide_break()

        self.play(Transform(obj,gamma))
        self.slide_break()

        self.play(FadeOut(obj))
        self.wait(1)
```

## Uninstall

To uninstall the python package, run

```bash
pip uninstall manim_reveal
```

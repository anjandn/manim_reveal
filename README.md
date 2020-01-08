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

```bash
cd python
manim example_slide_scene.py
```
This will create and copy the video `MathTest.mp4` and fragments files `MathTest.txt` into the folder `video_slides`.

The javascript code expects two such files for every video slide.

Copy the folders, `video_slides` and `js` into your reveal.js directory.

You can copy the example `index.html` in the repository, or modify your `index.html` as follows:

To add the slide, add the following line in `index.html` inside the `<div class='slides'>` tag.

```html
<script src="js/add_video_slide.js" slide_scene="MathTest"></script>
```
To make the video slide fragments work, add the following script tag at the bottom of your `index.html`

```html
<script src="js/video_slide.js"></script>
```
Finally run `npm start` to start the presentation.

from manimlib.imports import *
from manim_reveal import SlideScene

class MathTest(SlideScene):
    CONFIG={
        "video_slides_dir":"../video_slides"
    }
    def construct(self):
        text1 = TexMobject("{a","\\over","b}")
        text2 = TexMobject("{e^a","\\over","e^b}")

        text1.scale(5)
        text2.scale(5)
        cross1 = Cross(text2[2])
        cross1.set_stroke(RED,20)
        self.play(FadeIn(text1[0]))
        self.play(FadeIn(text1[1]))
        self.play(FadeIn(text1[2]))
        self.slide_break()

        self.play(Transform(text1[0],text2[0]),Transform(text1[1],text2[1]))
        self.play(Transform(text1[2],text2[2]))
        self.slide_break()

        self.play(Write(cross1))

        text3 = TexMobject("{e^{a-b}","\\over","1}")
        text3.scale(5)

        self.play(Transform(text1[2],text3[2]),
                 FadeOut(cross1),
                 Transform(text1[1],text3[1]),
                 Transform(text1[0],text3[0]) )
        self.slide_break()

        self.play(FadeOut(text1[1]),
                 FadeOut(text1[2]) )

        self.wait(1);

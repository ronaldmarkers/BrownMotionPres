from manim import *
import pandas as pd

class Title(Scene):
    def construct(self):


        text1 = MarkupText(
            'Random Walk with Drift ', font="Century Gothic"
        ).scale(1.25)
        text2 = MarkupText(
            'Essence of Brownian Motion', font="Century Gothic"
        ).scale(1.25)

        text4 = MarkupText(
            'Raul Marquez | MATH 4344 | Dr. Erwin Suazo', font="Century Gothic"
        ).scale(0.75)

        Image = ImageMobject(
            "UTRGV.png"
        ).scale(0.25)

        group = VGroup(text1, text2, text4).arrange(DOWN, center=False, aligned_edge=LEFT)
        group.move_to([-2.75,-2.75,0])  
        group.scale(0.5)

        Image.move_to([4.25,-3,0])

        randwalk = pd.read_csv("randwalk.csv")
        x_v= []
        y_v= []

        for x, y in randwalk.values:
            x_v.append(x),
            y_v.append(y)

        plane = NumberPlane(
            x_range = (0, 14),
            y_range = (0, 5.3),
            x_length = 12,
            y_length = 4.5,
            axis_config={"include_numbers": True},
        )
        plane.move_to([0,1,0])

        line_graph = plane.plot_line_graph(
            x_values = x_v,
            y_values = y_v,
            line_color=GOLD_E,
            vertex_dot_radius = 0,
            stroke_width = 2,
        )

        self.add(plane, line_graph)

        self.add(
            group, Image
        )



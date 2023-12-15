from manim import *
from manim_slides import Slide


class Growing(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()
        arrow = Arrow(LEFT, RIGHT)
        star = Star()

        VGroup(square, circle, triangle).set_x(0).arrange(buff=1.5).set_y(2)
        VGroup(arrow, star).move_to(DOWN).set_x(0).arrange(buff=1.5).set_y(-2)
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [2, 3]},
            tips=False,
        )
        self.add(ax)
        self.play(GrowFromPoint(square, ORIGIN), Flash(square, flash_radius=1.5))
        self.play(GrowFromCenter(circle), Flash(circle, flash_radius=1.5))
        self.play(GrowFromEdge(triangle, DOWN), Flash(triangle, flash_radius=1.5))
        self.play(GrowArrow(arrow), Flash(arrow, flash_radius=1.5))
        self.play(SpinInFromNothing(star), Flash(star, flash_radius=1.5))

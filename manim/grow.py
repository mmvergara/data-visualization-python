from manim import *
from manim_slides import Slide
class Growing(Slide):
    def construct(self):
        square = Square()
        circle = Circle()
        triangle = Triangle()
        arrow = Arrow(LEFT, RIGHT)
        star = Star()

        VGroup(square, circle, triangle).set_x(0).arrange(buff=1.5).set_y(2)
        VGroup(arrow, star).move_to(DOWN).set_x(0).arrange(buff=1.5).set_y(-2)

        self.play(GrowFromPoint(square, ORIGIN))
        self.next_slide()
        self.play(GrowFromCenter(circle))
        self.next_slide()
        self.play(GrowFromEdge(triangle, DOWN))
        self.next_slide()
        self.play(GrowArrow(arrow))
        self.next_slide()
        self.play(SpinInFromNothing(star))
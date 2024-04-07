from manim import *

class convection(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-0.04, 0.04, 0.02],
            y_range=[-20, 100, 10],
            tips=False,
            axis_config={"include_numbers": True}
        )
        
        labels = ax.get_axis_labels(
            Tex("x").scale(0.7).set_color(ORANGE), Text("p(x,t)").scale(0.45).set_color(ORANGE)
        )
        self.add(ax, labels)
        
        t = ValueTracker(0)

        graph1 = ax.plot(lambda x: ((4*PI*(t.get_value()+0.1)*0.00001)**(-0.5))*((np.e)**((-1*(x**2))/(4*(t.get_value()+0.1)*0.00001))), x_range=[-0.1, 0.1], stroke_color=BLUE)
        graph1.add_updater(
            lambda mob: mob.become(ax.plot(lambda x: ((4*PI*(t.get_value()+0.1)*0.00001)**(-0.5))*((np.e)**((-1*(x**2))/(4*(t.get_value()+0.1)*0.00001))), x_range=[-0.1, 0.1], stroke_color=BLUE))
        )
        graph2 = ax.plot(lambda x: ((4*PI*(t.get_value()+0.1)*0.00001)**(-0.5))*((np.e)**((-1*((x-(t.get_value()+0.1)*0.00001)**(2))/(4*(t.get_value()+0.1)*0.00001)))), x_range=[-0.10, 0.10], stroke_color=BLUE)
        graph2.add_updater(
            lambda mob: mob.become(ax.plot(lambda x: ((4*PI*(t.get_value()+0.1)*0.00001)**(-0.5))*((np.e)**((-1*((x-(t.get_value()+0.1)*0.002)**(2))/(4*(t.get_value()+0.1)*0.00001)))), x_range=[-0.10, 0.10], stroke_color=BLUE))
        )

        teq = MathTex('t = ').move_to([-5,2,0]).set_color(ORANGE)

        time = DecimalNumber(
            t.get_value(),
            color=ORANGE,
            num_decimal_places=3,
        ).move_to([-3.75,2,0])
        self.add(teq, time)
        
        time.add_updater(
            lambda mob: mob.become(DecimalNumber(
                t.get_value(),
                color=ORANGE,
                num_decimal_places=3,
            ).move_to([-3.75,2,0]))
        )
        
        self.add(teq, time)
        
        self.add(ax, graph1, graph2)
        
        self.play(
            t.animate.set_value(50),
            run_time=10
        )
        
        
        
        
from manim import *
import pandas as pd

class Walk(Scene):
    def construct(self):

        randwalk = pd.read_csv("driftwalk.csv")
        x_v= []
        y_v= []

        for x, y in randwalk.values:
            x_v.append(x),
            y_v.append(y)

        l = NumberLine(
            x_range=[-5, 5, 1],
            length= 12,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN,
        )
        self.add(l)

        x = ValueTracker(0)
        t = ValueTracker(0)

        h = ValueTracker(1)
        dt = ValueTracker(1)

        p = ValueTracker(0.75)
        q = ValueTracker(0.25)

        a_location = 0
        
        A = Dot(color=BLUE).move_to(l.n2p(0)).scale(1.5)
        A.set_z_index(99)
        self.add(A)
        Alabel = MathTex("A").next_to(A, UP, 0.5)
        self.add(Alabel)

        arrow_p = Arrow(start=l.n2p(0), end=A.get_center(), color=ORANGE, buff=0)
        self.add(arrow_p)

        arrow_p.add_updater(
            lambda mob: mob.become(Arrow(start=l.n2p(0), end=A.get_center(), color=ORANGE, buff=0))
        )
        
        arrow_po = Arrow(start=l.n2p(-1), end=A.get_center(), color=ORANGE, buff=0)
        
        plabel = MathTex("x + h").next_to(arrow_p, UL)

        arrow_q = VMobject()

        arrow_q.add_updater(
            lambda mob: mob.become(Arrow(start=l.n2p(0), end=A.get_center(), color=ORANGE, buff=0))
        )
        
        arrow_qo = Arrow(start=l.n2p(0), end=A.get_center(), color=ORANGE, buff=0)
        
        qlabel = MathTex("x - h").next_to(arrow_q, UR)

        xeq = MathTex('x = ').move_to([-5,3,0])

        pos = DecimalNumber(
            x.get_value(),
            color=WHITE,
            num_decimal_places=3,
        ).move_to([-3.75,3,0])
        self.add(xeq, pos)
        
        pos.add_updater(
            lambda mob: mob.become(DecimalNumber(
                x.get_value(),
                color=WHITE,
                num_decimal_places=3,
            ).move_to([-3.75,3,0])
        )
        )

        teq = MathTex('t = ').move_to([-5,2,0])

        time = DecimalNumber(
            t.get_value(),
            color=WHITE,
            num_decimal_places=3,
        ).move_to([-3.75,2,0])
        self.add(teq, time)
        
        time.add_updater(
            lambda mob: mob.become(DecimalNumber(
                t.get_value(),
                color=WHITE,
                num_decimal_places=3,
            ).move_to([-3.75,2,0]))
        )

        heq = MathTex("h = ").move_to([-5,-2,0])

        h_number = DecimalNumber(
            h.get_value(),
            color=WHITE,
            num_decimal_places=3,
        ).move_to([-3.75,-2,0])

        dteq = MathTex('dt = ').move_to([-5,-3,0])

        t_number = DecimalNumber(
            dt.get_value(),
            color=WHITE,
            num_decimal_places=3,
        ).move_to([-3.75,-3,0])

        self.add(heq, h_number, dteq, t_number)

        peq = MathTex("p = ").move_to([3.75,-2,0])

        p_number = DecimalNumber(
            p.get_value(),
            color=WHITE,
            num_decimal_places=3,
        ).move_to([5,-2,0])

        qeq = MathTex('q = ').move_to([3.75,-3,0])

        q_number = DecimalNumber(
            q.get_value(),
            color=WHITE,
            num_decimal_places=3,
        ).move_to([5,-3,0])

        self.add(peq, p_number, qeq, q_number)

        pxt = MathTex('p(x,t) = ?').move_to([0,3,0])
        self.add(pxt)

        plane = NumberPlane(
            x_range = (0, 10),
            y_range = (0, 6),
            x_length = 5,
            y_length = 3,
        )
        plane.move_to([4,2.3,0])
        line_graph = plane.plot_line_graph(
            x_values = [1],
            y_values = [1],
            line_color=GOLD_E,
            vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
            stroke_width = 4,
        )
        self.add(plane, line_graph)
        
        xa = []
        ya = []
        
        line_graph.add_updater(
            lambda mob: mob.become(plane.plot_line_graph(
                x_values = xa,
                y_values = ya,
                line_color=GOLD_E,
                vertex_dot_style=dict(stroke_width=3,  fill_color=PURPLE),
                stroke_width = 4,
                call_updater=True
                )
            )
        )
        
        g = l.n2p(-1)
        
        '''self.play(
            l.animate.move_to([-1.3,l.get_y(),0]),
            Create(plabel),
            x.animate.set_value(1),
            t.animate.set_value(1),
        )
        
        self.wait(1)
        
        self.remove_updater(arrow_p)
        self.remove(arrow_p)
        self.add(arrow_po)
        
        self.play(
            l.animate.move_to([-0.1,l.get_y(),0]),
            x.animate.set_value(0),
            t.animate.set_value(0),
        )
        
        self.wait(1)
        
        self.add(arrow_q)
        
        self.play(
            l.animate.move_to([1.1,l.get_y(),0]),
            Create(qlabel),
            x.animate.set_value(-1),
            t.animate.set_value(1),
        )
        
        self.wait(1) '''
        
        self.remove(arrow_p)
        
        self.remove(arrow_q)
        
        self.play(
            l.animate.move_to([1.1,l.get_y(),0]),
            Create(qlabel),
            x.animate.set_value(-1),
            t.animate.set_value(1),
        )
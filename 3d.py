from manim import *

class DiracDistribution(ThreeDScene):
    def construct(self):
        resolution_fa = 10
        
        self.set_camera_orientation(phi=60 * DEGREES, theta=10 * DEGREES, zoom=0.75)
        axes = ThreeDAxes(x_range=(-0.04, 0.04, 0.02), y_range=(0.000000001, 0.00005, 0.00001), z_range=(-20, 100, 10))
        def param_surface(u, v):
            x = u
            y = v
            z = ((4*PI*y)**(-0.5))*((np.e)**((-1*(x**2))/(4*y)))
            return z
        surface_plane = always_redraw(
            lambda: Surface(
                lambda u, v: axes.c2p(u, v, param_surface(u, v)),
                resolution=(resolution_fa, resolution_fa),
                v_range=[0.000001, 0.00005],
                u_range=[-0.04, 0.04],
                fill_color= RED,
                )
            )
        labels = axes.get_axis_labels(
            Text("x-axis").scale(0.7), Text("t-axis").scale(0.45)
        )
        surface_plane.set_style(fill_opacity=1)
        self.add(axes, surface_plane, labels)
        self.begin_ambient_camera_rotation(rate = PI /15)
        self.wait(30)
        self.stop_ambient_camera_rotation()
        self.wait()
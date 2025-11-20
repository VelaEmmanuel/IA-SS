from manim import *

class CotasInferiores(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"

        # --- Título ---
        titulo = Text("Cotas inferiores asintóticas", color="#00FFFF").scale(0.8)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # --- Crear ejes SIN GRID pero con divisiones que coinciden con los puntos ---
        plano = Axes(
            x_range=[0, 5, 0.5],  # marcas del eje coinciden con los puntos
            y_range=[0, 15, 1],
            x_length=7,
            y_length=4,
            axis_config={"color": GRAY, "stroke_width": 2},
            tips=False
        )

        # Engrosar ejes principales
        plano.axes.set_stroke(color=WHITE, width=3)

        plano.next_to(titulo, DOWN, buff=1.0)
        plano.shift(DOWN * 0.3)

        # --- Etiquetas de ejes personalizadas ---
        etiqueta_x = MathTex("n", color=GRAY).scale(0.8)
        etiqueta_y = MathTex("T_m(n)", color=GRAY).scale(0.8)

        # 📍 Colocar etiquetas en los extremos de los ejes
        etiqueta_x.move_to(plano.c2p(5, 0))           # extremo final del eje X
        etiqueta_x.shift(DOWN * 0.4 + RIGHT * 0.2)    # pequeño ajuste visual

        etiqueta_y.move_to(plano.c2p(0, 15))          # extremo final del eje Y
        etiqueta_y.shift(LEFT * 0.8 + UP * 0.2)       # pequeño ajuste visual

        # Añadir etiquetas antes de animar
        self.add(etiqueta_x, etiqueta_y)
        self.play(Create(plano))
        self.wait(0.5)

        # --- Definición de funciones ---
        Tm = lambda n: 2 * n + 3
        fn = lambda n: n

        # --- Puntos cada 0.5 ---
        xs = [i * 0.5 for i in range(11)]

        puntos_Tm, puntos_fn = [], []
        seg_Tm, seg_fn = VGroup(), VGroup()

        # --- Animación punto por punto ---
        for i, x in enumerate(xs):
            pt_Tm = Dot(plano.c2p(x, Tm(x)), color=YELLOW, radius=0.06)
            pt_fn = Dot(plano.c2p(x, fn(x)), color=BLUE, radius=0.06)

            self.play(FadeIn(pt_Tm, scale=0.5), FadeIn(pt_fn, scale=0.5), run_time=0.07)

            puntos_Tm.append(pt_Tm)
            puntos_fn.append(pt_fn)

            if i > 0:
                linea_Tm = Line(puntos_Tm[i-1].get_center(), puntos_Tm[i].get_center(),
                                color=YELLOW, stroke_width=3)
                linea_fn = Line(puntos_fn[i-1].get_center(), puntos_fn[i].get_center(),
                                color=BLUE, stroke_width=3)

                seg_Tm.add(linea_Tm)
                seg_fn.add(linea_fn)

                self.play(Create(linea_Tm), Create(linea_fn), run_time=0.1)

        # --- Etiquetas de funciones ---
        label_Tm = MathTex("T_m(n) = an + b", color=YELLOW).scale(0.6)
        label_f = MathTex("f(n) = n", color=BLUE).scale(0.6)

        label_Tm.next_to(plano.c2p(4.9, Tm(4.5)), UR, buff=0.3)
        label_f.next_to(plano.c2p(6.2, fn(4.0)), UL, buff=0.3)

        self.play(Write(label_Tm), Write(label_f))
        self.wait(1)

        # --- Texto final ---
        texto_asint = MathTex("T_m(n) \\in \\Omega(n)", color=GREEN).scale(0.9)
        texto_asint.next_to(plano, DOWN, buff=0.6)

        self.play(Write(texto_asint))
        self.wait(1.5)
        self.play(Indicate(texto_asint, color=GREEN, scale_factor=1.2))
        self.wait(2)
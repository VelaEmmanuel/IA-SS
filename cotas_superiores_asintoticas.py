from manim import *

class CotasSuperiores(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"

        # --- Título ---
        titulo = Text("Cotas superiores asintóticas", color="#00FFFF").scale(0.8)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # --- Crear ejes ---
        plano = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 350, 50],
            x_length=7,
            y_length=4,
            axis_config={"color": GRAY},
            tips=False
        )
        plano.next_to(titulo, DOWN, buff=1.0)
        plano.shift(DOWN * 0.3)

        # --- Crear etiquetas personalizadas en los extremos ---
        etiqueta_x = MathTex("n", color=GRAY).scale(0.8)
        etiqueta_y = MathTex("T_p(n)", color=GRAY).scale(0.8)

        # 📍 Colocar etiquetas en los últimos valores de los ejes
        etiqueta_x.move_to(plano.c2p(6, 0))          # extremo final del eje X
        etiqueta_x.shift(DOWN * 0.4 + RIGHT * 0.2)   # pequeño ajuste visual

        etiqueta_y.move_to(plano.c2p(0, 350))        # extremo final del eje Y
        etiqueta_y.shift(LEFT * 0.8 + UP * 0.2)      # pequeño ajuste visual

        # Añadir etiquetas al fondo
        self.add(etiqueta_x, etiqueta_y)
        self.play(Create(plano))
        self.wait(0.5)

        # --- Definición de funciones ---
        Tp = lambda n: 6 * n**2 + 10 * n + 22      # amarillo
        fn = lambda n: 8 * n**2 + 6 * n + 10       # azul

        # --- Dibujar función con puntos ---
        def dibujar_funcion_con_puntos(funcion, color):
            puntos_x = [i for i in range(7)]
            puntos = [plano.c2p(x, funcion(x)) for x in puntos_x]
            segmentos = VGroup()
            puntos_vis = VGroup()

            for i, punto in enumerate(puntos):
                dot = Dot(punto, color=color, radius=0.05)
                puntos_vis.add(dot)
                if i > 0:
                    seg = Line(puntos[i-1], puntos[i], color=color, stroke_width=3)
                    segmentos.add(seg)

            return puntos_vis, segmentos

        puntos_f, graf_f = dibujar_funcion_con_puntos(fn, BLUE)
        puntos_Tp, graf_Tp = dibujar_funcion_con_puntos(Tp, YELLOW)

        # --- Etiquetas de las funciones ---
        label_f = MathTex("f(n) = n^2", color=BLUE).scale(0.6)
        label_f.next_to(plano.c2p(7.4, fn(5.9)), UL, buff=0.3)

        label_Tp = MathTex("T_p(n) = an^2 + bn + c", color=YELLOW).scale(0.6)
        label_Tp.next_to(plano.c2p(5.8, Tp(5.6)), UR, buff=0.4)

        # --- Animar punto por punto simultáneamente ---
        for i in range(len(puntos_f)):
            anims = []
            anims.append(FadeIn(puntos_f[i], scale=0.5))
            anims.append(FadeIn(puntos_Tp[i], scale=0.5))
            if i > 0:
                anims.append(Create(graf_f[i-1]))
                anims.append(Create(graf_Tp[i-1]))
            self.play(AnimationGroup(*anims, lag_ratio=0, run_time=0.3))
        
        # --- Mostrar etiquetas después de animar todos los puntos ---
        self.play(Write(label_f), Write(label_Tp))
        self.wait(0.5)

        # --- Texto explicativo ---
        texto_asint = MathTex("T_p(n) \\in O(n^2)", color=GREEN).scale(0.8)
        texto_asint.next_to(plano, DOWN, buff=0.5)
        self.play(Write(texto_asint))
        self.wait(1)

        # --- Resaltar zona donde f(n) supera Tp(n) ---
        zona = plano.get_area(
            plano.plot(Tp, x_range=[0, 6]),
            bounded_graph=plano.plot(fn, x_range=[0, 6]),
            color=GREEN, opacity=0.25
        )

                # --- Línea punteada en el punto donde T_p(n) y f(n) coinciden ---
        from math import sqrt

        n0 = 1 + sqrt(7)             # punto de intersección en x
        y0 = Tp(n0)                  # valor de T_p(n) en esa x

        punto_inter = plano.c2p(n0, y0)

        # Línea punteada vertical hacia el eje X
        linea_punteada = DashedLine(
            start=punto_inter,
            end=plano.c2p(n0, 0),
            color=GRAY,
            dash_length=0.2
        )

        # Etiqueta n_0 en el eje X
        etiqueta_n0 = MathTex("n_0", color=RED).scale(0.7)
        etiqueta_n0.next_to(plano.c2p(n0, 0), DOWN, buff=0.2)

        self.play(Create(linea_punteada), Write(etiqueta_n0))
        self.wait(1)

        self.play(FadeIn(zona))
        self.wait(2)
        self.play(Indicate(texto_asint, color=GREEN, scale_factor=1.2))
        self.wait(2)
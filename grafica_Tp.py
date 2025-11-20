from manim import *

class GraficaTp(Scene):
    def construct(self):
        self.camera.background_color = "#0A192F"

        # --- Título ---
        titulo = Text("Gráfica de la función en tiempo", color="#00FFFF").scale(0.8)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # --- Crea ejes con secciones coincidentes con los puntos ---
        plano = Axes(
            x_range=[0, 1.8, 0.2],
            y_range=[0, 16, 2],
            x_length=6,
            y_length=4,
            axis_config={"color": GRAY},
            tips=False
        )
        plano.next_to(titulo, DOWN, buff=1.0)
        plano.shift(DOWN * 0.6)

        # --- Crea etiquetas personalizadas detrás de la gráfica ---
        etiqueta_y = MathTex("T_p(n)", color=GRAY).scale(0.8)
        etiqueta_x = MathTex("n", color=GRAY).scale(0.8)

        # --- Coloca etiquetas en los últimos valores de x y y
        etiqueta_x.move_to(plano.c2p(1.8, 0))          # al final del eje X
        etiqueta_x.shift(DOWN * 0.35 + RIGHT * 0.25)   # ajuste visual con tamaño mayor

        etiqueta_y.move_to(plano.c2p(0, 16))           # al final del eje Y
        etiqueta_y.shift(LEFT * 0.9 + UP * 0.25)       # ajuste visual con tamaño mayor

        # --- Dibuja ejes y etiquetas (etiquetas al fondo) ---
        self.add(etiqueta_y, etiqueta_x)  # Se añaden primero para quedar detrás
        self.play(Create(plano))
        self.wait(0.5)

        # --- Agrega la fórmula debajo de la gráfica ---
        formula = MathTex("T_p(n) = an^2 + bn + c", color="#00FFFF").scale(0.8)
        formula.next_to(plano, DOWN * 0.35, buff=0.6)  # Justo debajo de la gráfica
        self.play(Write(formula))
        self.wait(1)

        # --- Define la función ---
        funcion = lambda n: 4 * n**2 + 2 * n

        # --- Dibuja la gráfica punto por punto ---
        puntos_x = [i * 0.2 for i in range(10)]  # 0, 0.2, ..., 1.8
        puntos = []
        lineas = VGroup()

        for i, x in enumerate(puntos_x):
            y = funcion(x)
            punto = Dot(plano.c2p(x, y), color=YELLOW)
            puntos.append(punto)

            # Muestra punto con animación
            self.play(FadeIn(punto, scale=0.5), run_time=0.3)

            # Conecta con el anterior si no es el primero
            if i > 0:
                linea = Line(
                    plano.c2p(puntos_x[i-1], funcion(puntos_x[i-1])),
                    plano.c2p(x, y),
                    color=YELLOW
                )
                lineas.add(linea)
                self.play(Create(linea), run_time=0.3)

        self.wait(1)

        # --- Sombrea la zona bajo la curva ---
        grafica_completa = plano.plot(funcion, x_range=[0, 1.8], color=YELLOW)
        area = plano.get_area(grafica_completa, x_range=[0, 1.8], color=BLUE, opacity=0.3)

        # Asegura que la gráfica quede sobre las etiquetas
        self.bring_to_front(plano, grafica_completa, lineas, *puntos)

        self.play(FadeIn(area))
        self.wait(2)

        # --- Enfatiza la curva ---
        self.play(Indicate(lineas, color=YELLOW, scale_factor=1.05))
        self.wait(2)

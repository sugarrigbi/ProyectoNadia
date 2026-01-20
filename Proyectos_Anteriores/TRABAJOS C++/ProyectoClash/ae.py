import numpy as np
import plotly.graph_objects as go

# Definir la función por partes
def f(x):
    return np.piecewise(x, 
                        [(-2 <= x) & (x < 0), x == 0, x > 0], 
                        [lambda x: np.abs(x), 1, lambda x: x**3])

# Crear datos
x1 = np.linspace(-2, 0, 400, endpoint=False)
x2 = np.array([0])
x3 = np.linspace(0, 3, 400)

y1 = f(x1)
y2 = f(x2)
y3 = f(x3)

# Crear figura interactiva
fig = go.Figure()

# Agregar |x| tramo azul
fig.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='|x|', line=dict(color='blue')))

# Agregar punto en x=0
fig.add_trace(go.Scatter(x=x2, y=y2, mode='markers', name='f(0)=1', marker=dict(color='orange', size=8)))

# Agregar x^3 tramo verde
fig.add_trace(go.Scatter(x=x3, y=y3, mode='lines', name='x^3', line=dict(color='green')))

# Personalizar la vista
fig.update_layout(title="Función por partes interactiva",
                  xaxis_title="x",
                  yaxis_title="f(x)",
                  xaxis=dict(range=[-10, 10]),
                  yaxis=dict(range=[-10, 10]),
                  showlegend=True,
                  template="plotly_white")

# Mostrar figura interactiva
fig.write_html("grafica_interactiva.html", auto_open=True)

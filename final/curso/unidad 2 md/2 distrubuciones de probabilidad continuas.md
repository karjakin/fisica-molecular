
# Distribuciones de probabilidad continuas

Ahora consideremos a $x$ como una variable aleatoria continua que tiene una probabilidad $P(x)dx$ de tener valores entre $x$ y $x + dx$. Como se hizo en la sección anterior, requerimos que la suma de todas las probabilidades sea igual a 1. En el caso de variables continuas, tenemos

$$
\int P(x) \, dx = 1
$$

De esta manera la media, o valor esperado, está definido como

$$
\langle x \rangle = \int x P(x) \, dx
$$

y para funciones que dependan de la variable aleatoria continua $x$,

$$
\langle f(x) \rangle = \int f(x) P(x) \, dx
$$

Ejemplo: Sea $P(x) = C e^{-x^2 / 2a^2}$ donde $C$ y $a$ son constantes. Hallar el valor esperado de $x$ y $x^2$.

### Solución

Primero determinamos el valor de $C$ utilizando el hecho de que $\int P(x) \, dx = 1$, es decir,

$$
1 = \int_{-\infty}^{+\infty} P(x) \, dx = \int_{-\infty}^{+\infty} C e^{-x^2 / 2a^2} \, dx = C \sqrt{2 \pi a^2}
$$

$$
C = \frac{1}{\sqrt{2 \pi a^2}}
$$

Por lo tanto,

$$
P(x) = \frac{1}{\sqrt{2 \pi a^2}} e^{-x^2 / 2a^2}
$$

Ahora calculamos el valor esperado de $x$ y $x^2$.

$$
\langle x \rangle = \frac{1}{\sqrt{2 \pi a^2}} \int_{-\infty}^{+\infty} x e^{-x^2 / 2a^2} \, dx = 0
$$

$$
\langle x^2 \rangle = \frac{1}{\sqrt{2 \pi a^2}} \int_{-\infty}^{+\infty} x^2 e^{-x^2 / 2a^2} \, dx = \frac{1}{\sqrt{2 \pi a^2}} \frac{1}{2} \sqrt{8 \pi a^6} = a^2
$$

El gráfico de la función $P$ se muestra a continuación:

![](https://i.imgur.com/RdPXeZr.png)

Puedes notar que conforme el valor de $a$ se incrementa, el ancho de la gráfica también lo hace. Además, el pico de las 3 distribuciones se encuentra centrado en cero (el valor más probable de la variable aleatoria $x$).

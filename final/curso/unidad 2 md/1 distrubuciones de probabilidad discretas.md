# Distribuciones de probabilidad discretas

Las variables aleatorias discretas son aquellas que solo pueden tomar un número finito de
valores posibles. Consideremos a $x$ como una variable aleatoria discreta que puede tomar
valores $x_i$ con probabilidad $P_i$. Vamos a requerir que la suma de todas las probabilidades
sea igual a uno, es decir

$$\sum_i P_i = 1$$

Se define la media, o valor esperado, de la variable $x$ como

$$\langle x \rangle = \sum_i x_i P_i$$

En general podemos encontrar la media o valor esperado de cualquier función $f$ que
dependa de la variable aleatoria discreta $x$

$$\langle f(x) \rangle = \sum_i f(x_i) P_i$$

## Ejemplo

Sea $x$ una variable aleatoria discreta que puede tomar los valores 0, 1 y 2 con
probabilidades 1/2, 1/4 y 1/4 respectivamente. Hallar el valor esperado de $x$ y $x^2$.

### Solución

$$\langle x \rangle = \sum_i x_i P_i = 0 \times \frac{1}{2} + 1 \times \frac{1}{4} + 2 \times \frac{1}{4} = \frac{3}{4}$$

$$\langle x^2 \rangle = \sum_i x_i^2 P_i = 0 \times \frac{1}{2} + 1 \times \frac{1}{4} + 4 \times \frac{1}{4} = \frac{5}{4}$$
# Distribución de Maxwell-Boltzmann

En esta unidad de aprendizaje aplicaremos la distribución de Boltzmann al problema del movimiento de las moléculas en un gas. Por el momento no tomaremos en cuenta movimientos rotacionales o de vibración. La energía de la molécula estará dada por la ecuación

$$
\frac{1}{2} mv_x^2 + \frac{1}{2} mv_y^2 + \frac{1}{2} mv_z^2 = \frac{1}{2} mv^2
$$

donde $\vec{v}=(v_x, v_y, v_z)$ es la velocidad molecular. Lo que buscamos es determinar la forma de la distribución de velocidades moleculares. Asumiremos que el tamaño de las moléculas es lo suficientemente pequeño comparado con la separación entre ellas. Ignoraremos las fuerzas que puedan existir entre moléculas. Supondremos que las moléculas pueden cambiar energía entre ellas debido a colisiones pero el sistema estará en equilibrio. Entonces cada molécula puede ser considerada como un sistema pequeño conectado a un baño térmico con temperatura $T$. Bajo esta suposición, el resto de las moléculas serán el baño térmico. Esto es importante porque entonces podemos aplicar la distribución de Boltzmann a las energías de las moléculas.

### Distribución de velocidad

Sea $g(v_x)dv_x$ la función de distribución de velocidades como la fracción de moléculas con velocidades, en dirección $x$ por ejemplo, entre $v_x$ y $v_x+dv_x$. De esta manera $g(v_x)dv_x$ será proporcional al factor de Boltzmann:

$$
g(v_x) \propto e^{-mv_x^2 / 2k_B T}
$$

Debemos normalizar a esta distribución de tal forma que

$$
\int_{-\infty}^{+\infty} g(v_x) \, dv_x = 1:
$$

$$
\int_{-\infty}^{+\infty} e^{-mv_x^2 / 2k_B T} \, dv_x = \sqrt{\frac{2 \pi k_B T}{m}} \Rightarrow g(v_x) = \sqrt{\frac{m}{2 \pi k_B T}} e^{-mv_x^2 / 2k_B T}
$$

En la siguiente figura observas el gráfico de la función $g(v_x)$.

![](https://i.imgur.com/Y1WfPl6.png)

Usando los resultados obtenidos en la unidad de aprendizaje 2, podemos encontrar el valor más probable de $v_x$:

$$
\langle v_x \rangle = 0
$$

$$
\langle |v_x| \rangle = \sqrt{\frac{2k_B T}{\pi m}}
$$

$$
\langle v_x^2 \rangle = \frac{k_B T}{m}
$$

Esta expresión que hemos encontrado para $v_x$ también será válida para $v_y$ y $v_z$. Por lo tanto la fracción de moléculas con velocidades entre $(v_x, v_y, v_z)$ y $(v_x+dv_x, v_y+dv_y, v_z+dv_z)$ es

$$
g(v_x) \, dv_x \, g(v_y) \, dv_y \, g(v_z) \, dv_z \propto e^{-mv_x^2 / 2k_B T} \, dv_x \, e^{-mv_y^2 / 2k_B T} \, dv_y \, e^{-mv_z^2 / 2k_B T} \, dv_z =
$$

$$
= e^{-mv^2 / 2k_B T} \, dv_x \, dv_y \, dv_z
$$

Si ahora calculamos la fracción de moléculas que viajan con rapidez entre $v = |v|$ y $v + dv$. Esta fracción corresponde a una cáscara esférica de radio $v$ en el espacio de velocidades (ver siguiente imagen) cuyo volumen es $4\pi v^2 dv$.

![](https://i.imgur.com/Ec2twTG.png)

De esta manera, podemos definir a la fracción de moléculas con rapidez entre $v$ y $v + dv$ en términos de la función $f(v) \, dv$ como

$$
f(v) \, dv \propto v^2 e^{-mv^2/2k_B T}
$$

Nuevamente, debemos normalizar a la función $f$ de tal forma que 

$$
\int_0^\infty f(v) \, dv = 1.
$$

$$
\int_0^\infty v^2 e^{-mv^2/2k_B T} \, dv = \frac{1}{4} \sqrt{\frac{\pi}{\left( \frac{m}{2k_B T} \right)^3}} \implies f(v) \, dv = \frac{4}{\sqrt{\pi}} \left( \frac{m}{2k_B T} \right)^{3/2} v^2 e^{-mv^2/2k_B T} \,  dv .
$$

A la función $f$ se le conoce como la **distribución de Maxwell-Boltzmann**.

Ahora podemos calcular algunas cantidades en base a las definiciones de la unidad de aprendizaje 2:

$$
\langle v \rangle = \sqrt{\frac{8k_B T}{\pi m}}
$$

$$
\langle v^2 \rangle = \frac{3k_B T}{m}
$$

$$
\langle E_{KE} \rangle = \frac{1}{2} m \langle v^2 \rangle = \frac{3}{2} k_B T
$$

Este resultado es muy importante. Nos indica que la energía cinética ($E_{KE}$) promedio de una molécula en el gas depende solo de la temperatura, y la temperatura es directamente proporcional al promedio de la energía cinética.

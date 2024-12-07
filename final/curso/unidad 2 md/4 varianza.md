# Varianza

La desviación de un valor particular de la variable aleatoria $x$ respecto al promedio de $x$ de un conjunto de datos se define como

$$
x - \langle x \rangle
$$

Si ahora calculamos el valor promedio de los cuadrados de las desviaciones de $x$, tenemos:

$$
\sigma_x^2 = \langle (x - \langle x \rangle)^2 \rangle
$$

A esta cantidad se le conoce como **varianza**.

La desviación estándar se calcula como

$$
\sigma_x = \sqrt{\langle (x - \langle x \rangle)^2 \rangle}
$$

Y en ocasiones también se le conoce como la **media cuadrática** o **rms (root mean square)**.

Ahora apliquemos la propiedad de las transformaciones lineales a la varianza:

$$
\sigma_x^2 = \langle (x - \langle x \rangle)^2 \rangle = \langle x^2 - 2x \langle x \rangle + \langle x \rangle^2 \rangle = \langle x^2 \rangle - 2 \langle x \rangle \langle x \rangle + \langle x \rangle^2
$$

$$
= \langle x^2 \rangle - 2 \langle x \rangle^2 + \langle x \rangle^2 = \langle x^2 \rangle - \langle x \rangle^2
$$

O bien:

$$
\sigma_x^2 = \langle x^2 \rangle - \langle x \rangle^2
$$

Retomemos la relación entre las variables aleatorias $y$ y $x$, dada por $y = ax + b$, y calculemos la varianza de la variable aleatoria $y$:

$$
\langle y^2 \rangle = \langle (ax + b)^2 \rangle = a^2 \langle x^2 \rangle + 2ab \langle x \rangle + b^2
$$

$$
\langle y \rangle^2 = \langle ax + b \rangle^2 = (a \langle x \rangle + b)^2 = a^2 \langle x \rangle^2 + 2ab \langle x \rangle + b^2
$$

Entonces, la varianza de $y$ es:

$$
\sigma_y^2 = \langle y^2 \rangle - \langle y \rangle^2 = a^2 \langle x^2 \rangle + 2ab \langle x \rangle + b^2 - a^2 \langle x \rangle^2 - 2ab \langle x \rangle - b^2
$$

$$
= a^2 \left( \langle x^2 \rangle - \langle x \rangle^2 \right)
$$

Como puedes notar, hemos encontrado que existe una estrecha relación entre la varianza y desviación estándar de la variable aleatoria $y$ y la variable aleatoria $x$:

$$
\sigma_y^2 = a^2 \sigma_x^2
$$

$$
\sigma_y = a \sigma_x
$$

**¿Por qué la varianza no depende de $b$?** Escribe una entrada en el blog correspondiente dando una explicación a esto y recuerda que debes comentar al menos 2 entradas de tus compañeros en el blog. Sería de mucha utilidad apoyar tu comentario con algún gráfico.

Estas propiedades las usaremos más adelante cuando estudiemos la Teoría Cinética de los gases.

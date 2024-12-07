# Recorrido libre medio y colisiones

Procesos en los cuales un gas entra en un volumen (difusión, opuesto a efusión) sería casi instantáneo a no ser por las diferentes colisiones que ocurren entre moléculas. Estos efectos de colisión pueden estudiarse desde el punto de vista de la Mecánica Cuántica, pero para nuestro caso (gas), las moléculas pasan la mayor parte de su tiempo en colisiones de tal forma que podemos considerarlas como dos bolas de billar (esferas rígidas) que colisionan sin preocuparnos demasiado por lo que ocurre durante la colisión. Todo lo que nos importa por el momento es que después de las colisiones, las velocidades de las moléculas tendrán valores aleatorios.

## Tiempo medio de la colisión

Consideremos a una molécula que se mueve en un gas. Supongamos además que la molécula se mueve con velocidad $v$ y que las otras moléculas del gas son estacionarias. También asumiremos que cada molécula tiene asociada una sección eficaz $\sigma$.

En un tiempo $dt$, la molécula que elegimos estará en un volumen $v \sigma dt$. Si otra molécula entra en este volumen entonces habrá una colisión. Con $n$ moléculas por unidad de volumen, la probabilidad de que ocurra una colisión en el tiempo $dt$ estará dada por

$$
n \sigma v dt
$$

Definamos a $P(t)$ como la probabilidad de que una molécula no colisione hasta el tiempo $t$. Entonces,

$$
P(t + dt) = P(t) + \frac{dP}{dt} dt
$$

además, $P(t + dt)$ es la probabilidad de que una molécula no colisione hasta el tiempo $t$ multiplicada por la probabilidad de que no colisione en el tiempo subsecuente $dt$:

$$
P(t + dt) = P(t) \left( 1 - n \sigma v dt \right)
$$

esto implica que

$$
\frac{1}{P} \frac{dP}{dt} = -n \sigma v
$$

Resolviendo la última ecuación encontramos a $P$:

$$
P(t) = e^{-n \sigma v t}
$$

Por otra parte, la probabilidad de que la molécula no colisione en el tiempo $t$ pero sí en el tiempo $dt$ será

$$
e^{-n \sigma v t} n \sigma v dt
$$

Con este resultado podemos encontrar al tiempo promedio transcurrido entre colisiones de la siguiente forma:

$$
\tau = \int_0^\infty t \, e^{-n \sigma v t} n \sigma v \, dt = \frac{1}{n \sigma v} \int_0^\infty \left( P(t) \right) e^{-n \sigma v t} dt \implies \tau = \frac{1}{n \sigma v}
$$

## Sección eficaz de la colisión

Consideremos ahora dos moléculas las cuales modelamos como esferas de radio $a_1$ y $a_2$ con un potencial entre ellas dado por

![](https://i.imgur.com/L7FwlLa.png)

El parámetro de impacto $b$ entre dos moléculas en movimiento se define como la distancia de aproximación más cercana que resultaría si las trayectorias moleculares no fueran desviadas por la colisión. De esta forma, para el caso de nuestras esferas, tendremos una colisión si el parámetro de impacto es menor a la suma de sus radios.

Enfoquemos nuestra atención en la molécula de radio $a_1$. Imaginemos moléculas de radio $a_2$ que están cerca. Una colisión ocurrirá solo si el centro de estas otras moléculas están dentro de un tubo de radio $a_1 + a_2$.

![](https://i.imgur.com/jhFxBDg.png)

El área de este tubo se conoce como la sección eficaz de colisión $\sigma$ dada por

$$
\sigma = \pi \left( a_1 + a_2 \right)^2
$$

Si $a_1 = a_2 = a$, entonces

$$
\sigma = \pi a^2
$$

donde $a$ es el diámetro molecular.

Por el momento, asumiremos que este modelo, conocido como esferas duras, es una buena aproximación para gases a temperaturas bajas donde se puedan despreciar efectos cuánticos. Conforme se incrementa la temperatura este modelo puede no ser el más adecuado. Conforme el gas se calienta, las moléculas podrían aparentar tener una menor área transversal. Las secciones transversales en física nuclear y de partículas pueden ser mucho más grandes que el tamaño del objeto. En este caso, las partículas podrían experimentar algún tipo de interacción con objetos que se encuentren lejos de ellas.

## Camino libre medio

Al inicio de esta sesión encontramos el tiempo promedio que transcurre entre colisiones. Entonces podríamos encontrar el camino libre medio como

$$
\lambda = \langle v \rangle \tau = \frac{\langle v \rangle}{n \sigma v}
$$

Recuerda que este cálculo lo hicimos fijando nuestra atención en una molécula asumiendo que el resto está en reposo. En realidad, todas las moléculas están en movimiento. Entonces, debemos tomar a $v$ como la velocidad promedio relativa $\langle v_r \rangle$ donde $\mathbf{v_r} = \mathbf{v_1} - \mathbf{v_2}$, donde $\mathbf{v_1}$ y $\mathbf{v_2}$ son las velocidades de dos moléculas arbitrarias. De esta forma

$$
v_r^2 = v_1^2 + v_2^2 - 2 \, v_1 \cdot v_2
$$

de esta forma

$$
\langle v_r^2 \rangle = \langle v_1^2 \rangle + \langle v_2^2 \rangle = 2 \langle v^2 \rangle
$$

Supongamos que la distribución de velocidades es del tipo Maxwell-Boltzmann. Aproximemos entonces

$$
\langle v_r^2 \rangle \approx \langle v^2 \rangle \approx \sqrt{2} \langle v \rangle
$$

Haciendo esta suposición tendremos un error menor al 10%. Por lo tanto,

$$
\lambda = \frac{1}{\sqrt{2} n \sigma}
$$

sustituyendo la expresión para la presión dada por la ecuación de estado del gas ideal tenemos

$$
\lambda = \frac{k_B T}{\sqrt{2} p \sigma}
$$

Esta expresión nos indica que el camino libre medio es inversamente proporcional a la presión del gas. Si queremos aumentar el camino libre medio entonces debemos decrementar a la presión en el mismo factor.

Esto es consistente con el hecho de que la presión del gas aumenta a temperatura fija. Por lo tanto, la frecuencia de colisión es directamente proporcional a la presión.

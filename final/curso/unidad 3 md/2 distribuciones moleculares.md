# Distribuciones moleculares

La presión, $p$, de un gas cuyo volumen es $V$ (el cual tiene $N$ moléculas) depende de su temperatura a través de la ecuación de estado, la cual se puede representar en una forma general como

$$
p = f \left( T, V, N \right)
$$

donde $f$ es alguna función. Un ejemplo de este tipo de ecuaciones de estado es la del gas ideal

$$
pV = Nk_B T
$$

Daniel Bernoulli intentó dar una explicación a la Ley de Boyle al considerar que los gases están formados por pequeñas partículas (moléculas). En su tiempo esta idea fue controversial. En esta sección llegaremos a la ecuación de estado del gas ideal usando la Teoría Cinética de los Gases (distribución  de Maxwell-Boltzmann).

Para ello, sea $n$ el número de moléculas por unidad de volumen en un gas. Entonces, el número de moléculas por unidad de volumen que viajan con una rapidez entre $v$ y $v+dv$ está dada por $nf(v) dv$.

Si es igualmente probable que todas las moléculas viajen en cualquier dirección, la fracción de moléculas que se encuentra en un elemento diferencial de ángulo sólido $d\Omega$ será

$$
\frac{d\Omega}{4\pi}
$$

Ahora si elegimos a una dirección particular, el ángulo sólido correspondiente a las moléculas que viajan entre los ángulos $\theta$ y $\theta + d\theta$ estará dado por

$$
d\Omega = 2\pi \sin \theta d\theta
$$

Una idea geométrica la encuentras en la siguiente figura.

![](https://i.imgur.com/Uih9hfC.png)

Esto implica que

$$
\frac{d\Omega}{4\pi} = \frac{1}{2} \sin \theta d\theta
$$

Por lo tanto, el número de moléculas por unidad de volumen que tienen rapidez entre $v$ y $v + dv$ que viajan entre los ángulos $\theta$ y $\theta + d\theta$ será

$$
nf(v) \, dv \, \frac{1}{2} \sin \theta d\theta
$$

Supongamos ahora que esa dirección particular sea de tal forma que las moléculas se dirijan a un muro de área $A$ (ver siguiente imagen). En un tiempo $dt$, las moléculas que viajan con un ángulo $\theta$ respecto a la normal con el muro estarán en un volumen

$$
Av \, dt \cos \theta
$$

![](https://i.imgur.com/1Kirtr8.png)

Si multiplicamos este resultado por el número de moléculas por unidad de volumen, tendremos el número de moléculas que impactan al muro de área $A$ en un tiempo $dt$. Es decir,

$$
Av dt \cos \theta nf(v) \, dv \, \frac{1}{2} \sin \theta d\theta
$$

Por lo tanto, el número de moléculas que impactan al muro por unidad de área por unidad de tiempo y que tienen rapidez entre $v$ y $v + dv$ con ángulos entre $\theta$ y $\theta + d\theta$ está dado por

$$
v \cos \theta nf(v) \, dv \, \frac{1}{2} \sin \theta d\theta
$$

Este resultado será la base para la siguiente sección.

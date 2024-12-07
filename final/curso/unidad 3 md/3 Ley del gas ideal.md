# Ley del gas ideal

Cada molécula que impacta al muro tiene un cambio de momento igual a

$$
2mv \cos \theta
$$

el cual es perpendicular al muro. Si multiplicamos esta cantidad por el número de moléculas que impactan al muro por unidad de área por unidad de tiempo que viajan con rapidez entre $v$ y $v + dv$ y con ángulo entre $\theta$ y $\theta + d\theta$ e integramos sobre todo el espectro de velocidades y ángulos, obtendremos la presión $p$:

$$
p = \int_0^\infty \int_0^{\pi/2} (2mv \cos \theta) v \cos \theta \, nf(v) \, dv \, \frac{1}{2} \sin \theta \, d\theta
$$

es decir,

$$
p = n m \int_0^\infty dv \, v^3 f(v) \int_0^{\pi/2} \cos^2 \theta \, \frac{1}{2} \sin \theta \, d\theta
$$

Si usamos el hecho de que

$$
\int_0^{\pi/2} \cos^2 \theta \sin \theta \, d\theta = \frac{1}{3}
$$

tenemos

$$
p = \frac{1}{3} mn \langle v^2 \rangle
$$

Si escribimos a $n$ como el número total de moléculas $N$ contenidas en un volumen $V$ como $N = nV$, entonces

$$
pV = \frac{1}{3} m N \langle v^2 \rangle
$$

En este punto debes recordar que

$$
\langle v^2 \rangle = \frac{3k_B T}{m}
$$

entonces

$$
pV = Nk_B T
$$

lo cual es la ecuación de estado del gas ideal. Solo que ahora llegamos a ella en base a la Teoría Cinética de los Gases (ecuación de Maxwell-Boltzmann). Intuimos que $N$ es el número total de moléculas en el gas. Si dividimos la ecuación anterior por $V$, tenemos:

$$
p = n k_B T
$$

donde $n = N/V$ es el número de moléculas por unidad de volumen.

En ocasiones el número de moléculas $N$ se puede escribir en términos del número de Avogadro:

$$
N = n_m N_A
$$

donde $n_m$ es el número de moles y $N_A$ es el número de Avogadro. En este caso, la ecuación de estado del gas ideal se escribe como

$$
pV = n_m RT
$$

donde $R = N_A k_B$ se le conoce como la constante del gas ($R = 8.31447 \, \text{J K}^{-1} \text{mol}^{-1}$).

La ecuación de estado del gas ideal (Ley) nos indica que la presión del gas depende solo del número de moléculas y su temperatura y no de la masa de ellas. Sabes que moléculas masivas transferirán una mayor cantidad de momento al muro, pero su velocidad será pequeña y pocas veces impactarán al mismo.

# Variables Independientes

Se dice que dos variables aleatorias $x$ y $y$ son independientes si el conocer el valor de una de ellas **NO** te da información de la otra y viceversa. Por ejemplo, el hecho de que sepas la altura de un árbol en alguna parte del planeta no te da información sobre tu promedio final de la carrera.

Si $u$ y $v$ son variables aleatorias independientes, la probabilidad de que $u$ esté en el rango $u$ y $u + du$ y que $v$ esté en el rango $v$ y $v + dv$ está dada por:

$$
P_u(u) du P_v(v) dv
$$

Para hallar el promedio del producto $uv$ haremos lo siguiente (recuerda que $u$ y $v$ son variables independientes entre sí):

$$
\langle uv \rangle = \iint uv P_u(u) du P_v(v) dv = \int u P_u(u) du \int v P_v(v) dv = \langle u \rangle \langle v \rangle
$$

Nota que el valor promedio del producto de dos variables aleatorias es igual al producto del valor promedio de ambas variables.

Por ejemplo, supongamos que tienes $n$ variables independientes aleatorias $X_i$, cada una con el mismo valor promedio $\langle X \rangle$ y varianza $\sigma_X^2$.

Sea $Y$ la suma de las variables aleatorias. Hallemos el promedio y varianza de $Y$:

$$
\langle Y \rangle = \langle X_1 \rangle + \langle X_2 \rangle + \dots + \langle X_n \rangle = n \langle X \rangle
$$

Como puedes notar, el promedio de $Y$ es $n$ veces el promedio de $X$.

Ahora calculemos la varianza de $Y$:

$$
\sigma_Y^2 = \langle Y^2 \rangle - \langle Y \rangle^2 = n \langle X^2 \rangle - n \langle X \rangle^2 = n \sigma_X^2
$$

**¿Qué podemos rescatar de este resultado?**

Imagina que mides $n$ veces una cantidad $X$ y en cada ocasión tienes un error independiente $\sigma_X$. Si sumas los resultados de tus mediciones para tener $Y = \sum X_i$, entonces el error en la media cuadrática en $Y$ será $\sqrt{n}$ veces $\sigma_X$. Por lo tanto, si tienes una buena estimación de $X$ calculando $\left( \sum X_i \right)/n$, el error en esta cantidad estará dado por:

$$
\frac{\sigma_X}{\sqrt{n}}
$$

Si haces cuatro mediciones de la cantidad $X$ y las promedias, el error aleatorio en tu promedio será la mitad del error de una sola medición de $X$. Para reducir el error, debes realizar varias mediciones con un $n$ lo suficientemente grande para que este error se reduzca lo más posible. Este error no toma en cuenta a los errores sistemáticos que puedas tener en tu medición.

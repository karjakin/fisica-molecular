# Aplicaciones de la distribución de Boltzmann

### Ejemplo 1

Consideremos a un sistema de dos estados, uno con energía $0$ y el otro con energía $\epsilon > 0$. Calculemos el promedio de la energía de este sistema.

**Solución**

La probabilidad de que el sistema se encuentre en el estado con energía $0$ estará dado por

$$
P(0) = \frac{1}{1 + e^{-\beta \epsilon}} ; \quad \beta = \frac{1}{k_B T}
$$

La probabilidad de que el sistema tenga energía $\epsilon > 0$ será

$$
P(\epsilon) = \frac{e^{-\beta \epsilon}}{1 + e^{-\beta \epsilon}} ; \quad \beta = \frac{1}{k_B T}
$$

Ahora podemos encontrar la energía promedio

$$
\langle E \rangle = 0 \cdot P(0) + \epsilon \cdot P(\epsilon) = \frac{\epsilon}{e^{\beta \epsilon} + 1}
$$

Si la temperatura $T$ es muy pequeña, $\langle E \rangle \rightarrow 0$ el sistema está en su estado base. Si la temperatura $T$ es muy grande, $\langle E \rangle \rightarrow \frac{\epsilon}{2}$. Esto se ilustra en la siguiente figura:

![](https://i.imgur.com/UOZMpyn.png)

### Ejemplo 2

Estimar el número de moléculas en la atmósfera como función de la altura. Considere al sistema con temperatura constante.

**Solución**

Considere a una molécula en un gas ideal a temperatura $T$ en presencia del campo gravitacional de la Tierra. La probabilidad de que la molécula de masa $m$ se encuentre a la altura $z$ está dada por

$$
P(z) \propto e^{-mgz / k_B T}
$$

Por lo tanto, el número de moléculas por unidad de volumen $n(z)$ a una altura $z$ (la cual es proporcional a $P(z)$), estará dada por

$$
n(z) = n(0) e^{-mgz / k_B T}
$$

Este resultado nos indica que el número de moléculas obedece a una ley exponencial negativa respecto a la altura. Recuerda que asumimos que $T$ es fija, lo cual no está totalmente apegado a la realidad.

![](https://i.imgur.com/qNABGXy.png)
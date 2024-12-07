# Propiedades de transporte

Hasta el momento hemos asumido que el gas está en equilibrio de tal forma que sus propiedades macroscópicas son independientes del tiempo. Ahora consideraremos el caso donde no tenemos dicho equilibrio de tal forma que al mismo tiempo los parámetros del tiempo son estacionarios (no dependen del tiempo). Esto lo hacemos para describir a lo que se conoce como fenómenos de transporte. El contenido de esta sección se limitará a darte a conocer las expresiones que caracterizan a cada uno de estos fenómenos sin hacer una discusión detallada. Esto es debido a que se necesitan herramientas del curso de cálculo diferencial en varias variables.

## Viscosidad

**Transporte de momento.** En este fenómeno se considera a la viscosidad como una medida de la resistencia de un fluido a sufrir alguna deformación. Para el caso de un flujo uniforme, el esfuerzo entre las capas es proporcional al gradiente de velocidad en la dirección perpendicular a las mismas. La constante de proporcionalidad es conocida como coeficiente de viscosidad o simplemente viscosidad. Lo encontramos como

$$
\eta = \frac{1}{3} nm \lambda \langle v \rangle
$$

Como $\lambda \approx \frac{1}{\sqrt{2} n \sigma} \propto \frac{1}{n}$, la viscosidad es independiente de $n$ y por lo tanto a **TEMPERATURA CONSTANTE** es independiente de la **PRESIÓN**.

![](https://i.imgur.com/xj8pFQc.png)

Como ejemplo, en la figura anterior se muestra un gráfico de la viscosidad del aire en función de la presión para 288 grados Kelvin. A una presión entre $10^2$ y $10^6$ Pascales, la viscosidad se mantiene prácticamente constante.

La viscosidad es independiente de $n$. La única dependencia que tiene es con la temperatura a través del valor esperado de la velocidad, $\langle v \rangle \propto T^{1/2}$. Por lo tanto,

$$
\eta \propto \frac{1}{\sqrt{T}}
$$

Nota que la viscosidad de los gases aumenta con la temperatura. Para el caso de los líquidos, la viscosidad disminuye cuando se les calienta.

Por otra parte, si sustituimos la expresión para el recorrido medio libre, el valor esperado de la velocidad y la sección transversal de la colisión, la viscosidad puede expresarse como

$$
\eta = \frac{2}{3 \pi d^2} \left( \frac{mk_B T}{\pi} \right)^{1/2}
$$

Esta ecuación predice que la viscosidad es proporcional a $\sqrt{m / d^2}$ a temperatura constante.

Recuerda que hemos asumido un modelo simple de las colisiones entre moléculas. Necesitamos que la presión no sea muy alta de tal manera que podamos despreciar colisiones donde estén involucradas más de 2 moléculas. Al mismo tiempo, requerimos que la presión tampoco sea muy pequeña para que las moléculas preferentemente colisionen entre ellas y no con las paredes del contenedor, es decir,

$$
L \gg \lambda \gg d
$$

donde $L$ expresa el tamaño del contenedor, $\lambda$ es el recorrido medio libre y $d$ es el diámetro molecular.

El factor $1/3$ en la expresión de la viscosidad no es del todo correcto. Para encontrar un factor más preciso debes considerar el hecho de que la distribución de velocidades es diferente en diferentes capas y entonces promediar sobre la distribución de los recorridos. El resultado es

$$
\eta = \frac{5}{16} \frac{\sqrt{mk_B T}}{d^2}
$$

En la siguiente gráfica puedes observar las predicciones de ambos resultados y su comparación con varios gases.

![](https://i.imgur.com/nwXtGju.png)

La dependencia de la viscosidad con la temperatura, $\eta \propto \sqrt{T}$, para varios gases es muy consistente con los resultados experimentales en primera aproximación. Sin embargo, pueden existir algunas discrepancias.

![](https://i.imgur.com/W2vy5RE.png)

En la figura anterior se muestra la dependencia de la temperatura con la viscosidad. Se observan algunas discrepancias para determinados valores de temperatura. Esto es debido a que la sección transversal de colisión depende también de la temperatura. A altas temperaturas las moléculas se mueven más rápido y por lo tanto tienden a colisionar de una forma más directa. El diámetro molecular efectivo se reduce conforme se incrementa la temperatura, lo cual incrementa la viscosidad por encima de lo esperado con la raíz cuadrada de la temperatura.

## Conductividad térmica

Se refiere al transporte de calor. Nos ayuda a cuantificar la transferencia de energía térmica en respuesta a un cambio de temperatura o gradiente de temperatura. La cantidad de calor que fluye con un gradiente de temperatura depende de la conductividad térmica del material.

![](https://i.imgur.com/k2ohTRD.png)

El calor fluye del objeto más caliente al más frío (figura anterior). Si describimos a este flujo de calor con el vector $\mathbf{J}_z$, vemos que tiene una dirección opuesta al cambio de temperatura o gradiente de temperatura $(T_1 > T_2)$. La magnitud del vector de flujo de calor tiene unidades $\text{J s}^{-1} \text{m}^{-2} = \text{W m}^{-2}$. El flujo de calor en la dirección $z$ estará dado entonces por

$$
J_z = -\kappa \frac{dT}{dz}
$$

donde la constante de proporcionalidad $\kappa$ se conoce como la conductividad térmica del gas. En general, para el caso de 3 dimensiones, el vector de flujo de calor estará dado en términos del vector gradiente de temperatura,

$$
\mathbf{J} = -\kappa \nabla T
$$

Las moléculas de un gas tienen una energía cinética promedio que depende de la temperatura, 

$$
\left\langle \frac{1}{2} mv^2 \right\rangle = \frac{3}{2} k_B T.
$$

Por lo tanto, para incrementar la temperatura de un gas en 1 grado Kelvin, tenemos que incrementar el valor promedio de la energía cinética en un factor de $3 k_B / 2$ por molécula. La conductividad térmica entonces estará dada por

$$
\kappa = \frac{1}{3} C_v \lambda \langle v \rangle
$$

donde $C_v = n C_{\text{molecular}}$ es la capacidad calorífica por unidad de volumen y $C_{\text{molecular}}$ es la capacidad calorífica de las moléculas.

Con el mismo argumento que para la viscosidad, la capacidad calorífica es independiente de la presión del gas a temperatura constante. Además, la conductividad térmica es directamente proporcional a la raíz cuadrada de la temperatura (como en el caso de la viscosidad). Este resultado es válido, en primera aproximación, para varios gases como el neón y argón (ver siguiente figura). Puedes notar que para el caso del helio esta predicción no es del todo correcta.

![](https://i.imgur.com/0LeRTGz.png)

Como se hizo anteriormente para el caso de la viscosidad, si sustituimos las expresiones explícitas del recorrido libre medio, el valor esperado de la velocidad y la sección transversal de colisión en la ecuación de la conductividad térmica, ésta puede escribirse de la siguiente forma:

$$
\kappa = \frac{2}{3 \pi d^2} C_{\text{molecular}} \left( \frac{k_B T}{\pi m} \right)^{1/2}
$$

Este resultado predice que la conductividad térmica es proporcional a $\frac{1}{\sqrt{m} d^2}$ a temperatura constante. Estos resultados son válidos siempre que

$$
L \gg \lambda \gg d
$$

Las expresiones de la viscosidad y conductividad térmica podemos relacionarlas a través de su cociente,

$$
\frac{\kappa}{\eta} = \frac{C_{\text{molecular}}}{m}
$$

donde el cociente $C_{\text{molecular}} / m$ es la capacidad calorífica específica, $c_V$. Entonces,

$$
\kappa = c_V \eta
$$

Debes tener cuidado con estos resultados, ya que son válidos siempre que $L \gg \lambda \gg d$. Las moléculas más rápidas cruzan un plano dado en el contenedor más veces respecto a las lentas. Las más rápidas tienen más energía cinética por lo cual transportan más cantidad de calor. Sin embargo, éstas moléculas no necesariamente transportan mayor cantidad de momento en la dirección $x$.

Otra consideración importante es la relación, o conversión, de la energía interna de las moléculas con sus grados de libertad traslacionales. La capacidad calorífica de las moléculas, $C_{\text{molecular}}$, no solo se debía a su movimiento traslacional sino también es debida a vibraciones y rotaciones. Cuando las moléculas colisionan entre sí, la energía puede ser redistribuida en cualquiera de estos grados de libertad. En otras palabras, la capacidad calorífica, $C_V$, puede ser escrita como

$$
C_V = C_V^{\prime} + C_V^{\prime\prime}
$$

donde $C_V^{\prime}$ y $C_V^{\prime\prime}$ son las contribuciones a la capacidad calorífica provenientes de movimientos traslacionales y otros como rotacionales o de vibración. Entonces, podemos reescribir a la ecuación que relaciona a la conductividad térmica con la viscosidad como:

$$
\kappa = \left( \frac{5}{2} C_V^{\prime} + C_V^{\prime\prime} \right) \eta
$$


La última ecuación podemos reescribirla como

$$
\kappa = \frac{1}{4} \left( 9\gamma - 5 \right) C_V
$$

la cual es conocida como la Fórmula de Eucken. Por lo tanto, la expresión para hallar la conductividad térmica puede ser corregida y escrita de la siguiente forma:

$$
\kappa = \frac{25}{32 \pi d^2} C_{\text{molecular}} \left( \frac{k_B T}{m} \right)^{1/2}
$$

La siguiente gráfica muestra la predicción de ambos resultados para la conductividad térmica. Vemos que este el último resultado funciona bastante bien para gases monoatómicos, $\gamma = \frac{5}{3}$, mientras que para gases diatómicos existe una diferencia, como en el caso del $\text{N}_2$.

![](https://i.imgur.com/ClZXItK.png)

## Difusión

**Transporte de partículas (masa).** Consideremos ahora a una distribución de moléculas de las cuales etiquetamos a algunas de ellas de tal forma que $n^*(z)$ es el número de moléculas etiquetadas por unidad de volumen en función de $z$. El flujo, $\Phi_z$, de las moléculas etiquetadas y paralelas al eje $z$ está dado por

$$
\Phi_z = -D \left( \frac{\partial n^*}{\partial z} \right)
$$

donde $D$ es conocido como el coeficiente de difusión.

Si integramos al número de moléculas etiquetadas que impactan un área unitaria (como lo hicimos en la unidad de aprendizaje 3) tenemos

$$
\Phi_z = \int_0^{\pi} d\theta \int_0^{\infty} v \cos \theta f(v) \, \frac{1}{2} \sin \theta \left(-\frac{\partial n^*}{\partial z} \cos \theta \right) \, dv = -\frac{1}{3} \langle v \rangle \frac{\partial n^*}{\partial z}
$$

lo que implica que el coeficiente de difusión se escribe como

$$
D = \frac{1}{3} \lambda \langle v \rangle
$$

Puedes notar que el coeficiente de difusión es inversamente proporcional a la presión del gas a temperatura fija.

Por otra parte, como $p = nk_B T$ y el valor esperado de la velocidad es directamente proporcional a la raíz cuadrada de la temperatura, tenemos que a presión constante,

$$
D \propto T^{3/2}
$$

además, como lo hicimos con la viscosidad y la conductividad térmica, $D$ puede ser reescrita como

$$
D = \frac{2}{3 \pi d^2} \left( \frac{k_B T}{\pi m} \right)^{1/2}
$$

al igual que $\kappa$, $D \propto m^{-1/2} d^{-2}$.

Finalmente, $D$ debe ser corregido como lo hicimos con la viscosidad y conductividad térmica. Así,

$$
D = \frac{3}{8} \frac{1}{n d^2} \left( \frac{k_B T}{\pi m} \right)^{1/2}
$$

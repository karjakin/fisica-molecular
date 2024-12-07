## Ensambles

Como ya lo habrás notado, estamos intentando usar conceptos de probabilidad para hacer una descripción de los sistemas térmicos. Nos aproximamos a la misma a través de una repetición, imaginaria, de un experimento para poder medir alguna propiedad una y otra vez ya que recuerda que no podemos controlar a los microestados. Fue Willard Gibbs quien en 1878 introdujo el concepto de **ensamble** para formalizar esta idea. El ensamble es una idealización en la cual consideramos hacer un gran número de copias mentales del sistema, donde cada una nos representará un posible estado en el que pueda estar.

Hay 3 ensambles que son comúnmente usados:

- **Ensamble microcanónico**: un ensamble de sistemas que cada uno tiene la misma energía fija.
- **Ensamble canónico**: un ensamble de sistemas de tal forma que cada uno de ellos puede intercambiar energía con un baño térmico (gran reserva de calor). En este ensamble la temperatura se fija.
- **Ensamble gran canónico**: un ensamble de sistemas cada uno de los cuales puede intercambiar energía y partículas con un baño térmico. Este fija la temperatura del sistema y una cantidad conocida como potencial químico.

### Ensamble canónico

Consideremos ahora a dos sistemas acoplados de tal forma que ellos pueden intercambiar energía entre ellos y están aislados. Uno de ellos será un sistema muy grande al que llamaremos baño térmico o reserva de calor. Este sistema es lo suficientemente grande como para asumir que si pierde una cantidad considerable de energía éste se mantendrá a la misma temperatura. El otro sistema será pequeño comparado con el baño térmico y le llamaremos simplemente el sistema.

$$
\boxed{
\begin{array}{c}
E - \epsilon \\
\Omega(E - \epsilon) \\
\text{baño térmico a temperatura } T
\end{array}
}
\longleftrightarrow
\boxed{
\begin{array}{c}
\epsilon \\
\text{el sistema}
\end{array}
}
$$

Asumiremos también que por cada valor de energía permitida en el sistema existe un solo microestado y por lo tanto el sistema siempre tendrá un valor de $\Omega = 1$. Fijamos el valor de la energía total del sistema y del baño térmico. La energía del baño térmico será

$$
E - \epsilon
$$

mientras que la energía del sistema será $\epsilon$.

La probabilidad de que el sistema tenga una energía $\epsilon$ es proporcional al número de microestados que son accesibles al baño térmico multiplicado por el número de microestados del sistema, es decir

$$
P(\epsilon) \propto \Omega(E - \epsilon) \times 1
$$

Desarrollemos en una serie de Taylor a $\ln \Omega(E - \epsilon)$ alrededor de $\epsilon = 0$:

$$
\ln \Omega(E - \epsilon) = \ln \Omega(E) - \frac{d \ln \Omega(E)}{dE} \epsilon + \ldots = \ln \Omega(E) - \frac{\epsilon}{k_B T} + \ldots
$$

donde $T$ es la temperatura del baño térmico. Despreciando los términos de orden mayor en esta expansión tenemos:

$$
\Omega(E - \epsilon) = \Omega(E) e^{-\epsilon / k_B T} \Rightarrow P(\epsilon) \propto e^{-\epsilon / k_B T}
$$

Nota que el sistema está en equilibrio con el baño térmico, ambos deben tener la misma temperatura. Pero su energía $\epsilon$ estará determinada por la distribución de probabilidad $P$. Esta distribución de probabilidad se conoce como **distribución de Boltzmann** o **distribución canónica**. Al término $e^{-\epsilon / k_B T}$ se le conoce como factor de Boltzmann.

La distribución de Boltzmann describe el cómo un sistema pequeño se comporta cuando se acopla con un baño térmico de temperatura $T$. El sistema tiene una gran probabilidad de tener una temperatura menor a $k_B T$. La probabilidad de que el sistema tenga una temperatura mayor a $k_B T$ cae exponencialmente (factor de Boltzmann). Para cuantificar esta propiedad debemos normalizar la distribución. Si un sistema está en contacto con un baño térmico y tiene un microestado $r$ con energía $E_r$, entonces es:

$$
P(\text{microestado } r) = \frac{e^{-E_r / k_B T}}{\sum_i e^{-E_i / k_B T}}
$$

al término $Z = \sum_i e^{-E_i / k_B T}$ se le conoce como función de partición.

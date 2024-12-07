# Efusión molecular

La efusión es un proceso en el cual un gas escapa de un contenedor por un pequeño orificio. Thomas Graham descubrió que la tasa de efusión es inversamente proporcional a la raíz cuadrada de la masa de las moléculas que escapan, siempre que ambos gases se encuentren a la misma temperatura (equilibrio térmico).

**Ejemplo 1.** El fenómeno de efusión puede utilizarse para separar diferentes isótopos de un gas que no es posible separar mediante algún proceso químico. Si ambos gases tienen diferentes masas, entonces saldrán de un contenedor con un orificio a diferente tasa. Por ejemplo, en la separación del $^{235}\text{UF}_6$ y $^{238}\text{UF}_6$, el cociente de la tasa de efusión de los dos gases está dada por

$$
\sqrt{\frac{\text{masa } \, ^{238}\text{UF}_6}{\text{masa } \, ^{235}\text{UF}_6}} = \sqrt{\frac{352.0412}{348.0343}} = 1.00574
$$

Puedes notar que la diferencia es pequeña entre estos dos gases. Pero fue suficiente para varios kilogramos de $^{235}\text{UF}_6$ que fueron extraídos para el Proyecto Manhattan en 1945 para producir la primera bomba atómica de uranio que desafortunadamente fue lanzada sobre civiles en Hiroshima por los Estados Unidos.

En otras palabras, la Ley de Graham puede escribirse de la siguiente forma

$$
\frac{v_1}{v_2} = \sqrt{\frac{m_2}{m_1}}
$$

donde $v_1$, $m_1$ y $v_2$, $m_2$ son las velocidades y masas de los gases 1 y 2 respectivamente.

## Flujo molecular

Es el número de partículas que atraviesa algún área unitaria por unidad de tiempo:

$$
\text{flujo molecular} = \frac{\text{número de moléculas}}{\text{área} \times \text{tiempo}}
$$

De forma análoga se puede definir el flujo de calor:

$$
\text{flujo de calor} = \frac{\text{cantidad de calor}}{\text{área} \times \text{tiempo}}
$$

Recuerda que en la Unidad de Aprendizaje 3 encontramos una expresión para estimar el número de moléculas que golpean a un área unitaria por unidad de tiempo:

$$
v \cos \theta nf(v) \, dv \, \frac{1}{2} \sin \theta \, d\theta
$$

Si integramos esta expresión sobre todo el espacio de velocidades y $\theta$ encontraremos al flujo molecular, es decir,

$$
\phi = \frac{n}{2} \int_0^\infty v f(v) \, dv \int_0^{\pi/2} \cos \theta \sin \theta \, d\theta \implies \phi = \frac{1}{4} n \langle v \rangle
$$

Por otra parte, de la ecuación de estado del gas ideal tenemos que

$$
n = \frac{p}{k_B T}
$$

y además encontramos anteriormente que

$$
\langle v \rangle = \sqrt{\frac{8k_B T}{\pi m}}
$$

Sustituyendo estos dos resultados, el flujo molecular se escribe como

$$
\phi = \frac{p}{\sqrt{2 \pi m k_B T}}
$$

Este resultado es consistente con la Ley de Graham: la tasa de efusión es inversamente proporcional a la raíz cuadrada de la masa del gas.

Por lo tanto, el número de moléculas que escapan del contenedor por unidad de tiempo estará dado por

$$
\dot{N} = \frac{pA}{\sqrt{2 \pi m k_B T}}
$$

Durante la efusión, las partículas más rápidas dentro del contenedor viajan más rápido y por lo tanto tienen mayor probabilidad de alcanzar el orificio respecto a las moléculas más lentas. Matemáticamente, el número de moléculas que impactan a un área unitaria (el orificio en este caso), 

$$
v \cos \theta \, nf(v) \, dv \, \frac{1}{2} \sin \theta \, d\theta
$$

tiene un término $v$ adicional. Entonces, la distribución de moléculas que salen por el orificio del contenedor en algún intervalo de tiempo será proporcional a

$$
v^3 e^{-mv^2/2k_B T}
$$

En el siguiente gráfico notarás que las moléculas en el gas tienen una energía cinética promedio dada por

$$
\frac{1}{2} m \langle v^2 \rangle = \frac{3}{2} k_B T
$$

mientras que la energía promedio de las moléculas que salen por el orificio durante la efusión, ¿Cuál es la diferencia entre ambas?

![](https://i.imgur.com/EQ15PbJ.png)

En el siguiente video encontrarás una animación de este fenómeno:
https://www.youtube.com/watch?v=Eu9_k8H_gVA

Te recomiendo que también reflexiones sobre la discusión planteada en este video:
https://www.youtube.com/watch?v=JO0J3MyHogE

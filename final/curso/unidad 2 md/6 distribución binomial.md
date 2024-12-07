# Distribución binomial

La distribución binomial es una distribución discreta de probabilidad $P(n, k)$ que nos indica el número de éxitos, $k$, de un total de $n$ intentos (ensayos de Bernoulli). Está determinada por la siguiente expresión:

$$
P(n, k) = \frac{n!}{k! (n-k)!} p^k (1 - p)^{n - k}
$$

Los ensayos de Bernoulli son experimentos donde hay dos posibles escenarios: éxito con probabilidad $p$ y fallo con probabilidad $1 - p$.

### Actividades:
- Realiza un gráfico de $P$ para $n = 50$, $n = 500$ y $n = 5000$ asumiendo siempre $p = 0.4$. ¿Qué le ocurre al gráfico conforme $n$ se incrementa, y por qué?
- Hallar el valor más probable de $k$ y su varianza.
- Muestre que:

$$
\sum_{k=1}^{n} P(n, k) = 1
$$

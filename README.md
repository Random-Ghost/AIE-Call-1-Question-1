# Code Explanation
We have been given the polynomial equation $` p_n(x) = (x - \omega_n^1) \ldots (x - \omega_n^{\frac{n}{2} - 1})(x - \omega_n^{\frac{n}{2} + 1}) \ldots (x - \omega_n^{n -1}) `$ which has its roots being the n roots of unity except $` \omega_n^0 = 1 `$ and $` \omega_n^{\frac{n}{2}} = -1 `$.

We can see
```math
\begin{align*}
	(x^2 - 1)p_n(x) &= (x - 1)(x + 1)p_n(x) \\
	&= (x - \omega_n^{0})(x - \omega_n^{\frac{n}{2}})p_n(x)\\
	&= (x - \omega_n^{0})(x - \omega_n^1) \ldots (x - \omega_n^{\frac{n}{2} - 1})(x - \omega_n^{\frac{n}{2}})(x - \omega_n^{\frac{n}{2} + 1}) \ldots (x - \omega_n^{n -1}) \\
	&= x^n - 1 \\
	p_n(x) &= \frac{x^n - 1}{x^2 - 1} = \frac{(x^2)^{\frac{n}{2}} - 1}{x^2 - 1}
\end{align*}
```
Since for the sake of this problem n is even (it has to be for it to have -1 as a root), $` \frac{n}{2} `$ is an integer. Therefore
```math
\begin{align*}
	p_n(x) &= 1 + (x^2)^1 + (x^2)^2 + \ldots + (x^2)^{\frac{n}{2} - 1} \\
	&= 1 + x^2 + x^4 + \ldots + x^{n - 2} = \sum_{i = 0}^{n - 1} a_i x^i
\end{align*}
```
where
```math
a_i = 
\begin{cases}
	1 & i \text{ is even} \\
	0 & i \text{ is odd}
\end{cases}
```
And we get the coefficient vector $` a = (a_0, a_1, \ldots, a_{n - 2}, a_{n - 1}) = (1, 0, \ldots, 1, 0) `$ which is a (n, 2) sparse vector.

We can notice $` p_n(x) `$ is an even function so $` p_n(x) = p_n(-x) `$. We can also see $` p_n(+1) = p_n(-1) = \sum_{i = 0}^{\frac{n}{2} - 1} (x^2)^i = \sum_{i = 0}^{\frac{n}{2} - 1} 1 = \frac{n}{2} `$.

Since $` a = (1, 0, \ldots, 1, 0) `$, $` \text{DFT} (a) = (\frac{n}{2}, 0, \ldots, 0, \frac{n}{2}, 0, \ldots, 0) `$. From these, we can write all algorithms we need.

## Alternative derivation
We can rewrite the polynomial as
```math
p_n(x) = \prod_{i = 1}^{\frac{n}{2} - 1} (x - \omega_n^i)(x - \omega_n^{\frac{n}{2} + i}) = \prod_{i = 1}^{\frac{n}{2} - 1} (x - \omega_n^i)(x + \omega_n^i) = \prod_{i = 1}^{\frac{n}{2} - 1} (x^2 - \omega_n^{2i})
```
and we see $` p_n(x) = p_n(-x) `$.

$` \text{DFT} (a) = A = (A_0, A_1, \ldots, A_{n - 1}) `$. But $` A_i = p_n(\omega_n^i) \implies A = (p_n(+1), 0, \ldots, 0, p_n(-1), 0, \ldots, 0) = (p_n(+1), 0, \ldots, 0, p_n(+1), 0, \ldots, 0) `$ since the roots of $` p_n(x) `$ are the roots of unity except $` \omega_n^0 `$ and $` \omega_n^{\frac{n}{2}} `$.

We can take the inverse discrete fourier transform and see
```math
\begin{cases}
	\frac{2}{n} p_n(+1) & i \text{ is even} \\
	0 & i \text{ is odd}
\end{cases}
```
and $` p_n(x) = \sum_{i = 0}^{\frac{n}{2} - 1} \frac{2}{n}p_n(+1) (x^2)^i `$.

Using this representation, $` p_n(0) = \frac{2}{n} p_n(+1) `$. Using the original representation, 
```math
\begin{align*}
	p_n(0) &= \prod_{i = 1}^{\frac{n}{2} - 1} (- \omega_n^{2i}) \\
	&= \prod_{i = 1}^{\frac{n}{2} - 1} \omega_n^{\frac{n}{2} + 2i} \\
	&= \omega_n^{\frac{n}{2} \left( \frac{n}{2} - 1 \right) + \frac{n}{2} \left( \frac{n}{2} - 1 \right)} \\
	&= \omega_n^{n \left( \frac{n}{2} - 1 \right)}
\end{align*}
```
Since n is even, $` \frac{n}{2} `$ is an integer $` \implies p_n(0) = 1 `$ and $` p_n(+1) = \frac{n}{2} `$.

Substituting our results, we get $` a = (1, 0, \ldots, 1, 0) `$ and $` A = (\frac{n}{2}, 0, \ldots, 0, \frac{n}{2}, 0, \ldots, 0) `$ which matches with our previous answer.

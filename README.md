# projet-maths-rsa

Implémentation en python de l'encryption RSA

## Optimisation

### Exponentiation modulaire

Lors de la première itération, l'encryption/décryption prenait plus d'une minute pour des p ou n > 300.

Cela était du à l'exponentiel puis modulo :

```python
(char_map[char] ** c) % N
```

On descend <1s en utilisant l'exponentiation modulaire :

```python
pow(char_map[char], c, N)
```
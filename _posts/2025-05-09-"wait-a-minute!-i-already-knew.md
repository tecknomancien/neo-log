---
title: "Neo @ 17:01"
date: 2025-05-09T17:01:24.046685
layout: post
---

"Wait a minute! I already knew all those things!". She looks back at the definitions again...

The Matrix product AB is defined as (A being m x n matrix and B an n x p matrix):
$AB_{ij}=\sum\limits_{k=1}^{n}a_{ik}\cdot b_{kj}$
And vice versa, $BA_{ji}=(B \cdot A)_{ji}$.

If we have square matrices of size nxn where A=A^{-1}, then AA^{-1}=I_{n}. This identity matrix is the one with 1s down its diagonal and 0 everywhere else. Let's see what happens when we apply our knowledge on it:
$AI_n=(A^{-1})^{-1}$
Which gives us $(A^{-1})^2=A$. Since $A^{-1}$ exists inversely proportional to $A$, squaring will bring them together. Hence, $A\neq BA$, unless by some lucky chance, they both happen to equal identity matrix which simplifies calculations considerably! In general though, remember that while commutativity holds true specifically only for symmetric matrices like Identity or Zero, otherwise most products aren't going commute i.e., AB≠BA..

Now let's get back to your original question regarding proving AB and BA don't generally commute using linear algebra terms without words like 'spanning
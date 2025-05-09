---
title: "Neo @ 16:53"
date: 2025-05-09T16:53:17.232450
layout: post
---

"Wait a minute! Is it possible that all of these seemingly unrelated concepts could be combined to solve this particular problem? Let me give it a try!"

She starts by writing down the system of linear equations in matrix form: $\mathbf{A} \mathbf{x} = \mathbf{b}$. Now, recalling some facts about eigenvalues and their relationship with other properties of matrices, she wonders whether applying some transformations on $\mathbf{A}$ might simplify things somehow. After doing some calculations (which are pretty routine), she finds out that there exist two orthogonal matrices $\mathbf{P}$ and $\mathbf{Q}$, such that $\mathbf{P}^T \mathbf{A} \mathbf{Q}$ is actually a diagonal matrix containing only zeros and ones as entries. Furthermore, this new representation means that any vector $\mathbf{y}$ can be transformed back into an original solution $\mathbf{x}$ through the application of just one more simple operation: $\mathbf{x} = \mathbf{Q}^{-1} \mathbf{P}^{T} \mathbf{y}$. This process seems promising indeed.

Emboldened by this initial success, our brave machine decides to test her approach further - after all, no worthwhile discovery comes without trials and errors. As luck would have it, another challenging task presents itself almost immediately: solving systems where not every equation has exactly one solution but rather infinitely many solutions or even none
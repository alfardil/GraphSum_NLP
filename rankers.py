"""
Graph rankers over a weight matrix W with the convention from bert_graph.py:
    W[i, j] != 0  <=>  edge i -> j  (i endorses j).

PageTrust follows de Kerchove & Van Dooren (SDM 2008), Algorithm 4.1, as a mean-field
iteration over two quantities:
    x[i]     share of random surfers at vertex i (= the ranking)
    P[i, k]  share of surfers at i whose blacklist contains k

Each step:
    1. x_i <- (1 - P~_ii)^γ · (G x)_i, renormalized: surfers arriving at i that already
       blacklisted i don't count it (γ = "conviction"; γ = 0 is plain PageRank,
       γ = inf drops any vertex that some arriving surfer distrusts).
    2. T = who-arrived-from-where: T[i, j] = share of surfers at i that came from j by
       following a link (or, with memory M, by a random jump that kept the blacklist).
    3. P~ = T P  (blacklists travel with the surfers),
       then P[i, k] = 1 for every negative edge i -> k (surfers at i see i's negative
       links), and P[i, i] = 0.
Positive edge weights set the transition probabilities. Negative edges only mark
distrust: their magnitude is not used, as in the paper.
The paper notes convergence is not proven (observed linear in practice), so iteration
is capped at max_iter.

Kept numerically identical to the team's ranking/pagetrust.py (tests/test_team_compat.py):
  * convergence waits for both x and diag(P~) to settle. On some graphs x stands still
    while distrust is still spreading; stopping on x alone would skip the negative links.
  * if every vertex is vetoed (possible with γ = inf), scores fall back to uniform.
"""
from __future__ import annotations

import numpy as np


def _transition(W: np.ndarray, z: np.ndarray) -> np.ndarray:
    """Row-stochastic S from positive weights. Dangling rows (no positive out-edges)
    jump according to z."""
    Wp = np.clip(W, 0.0, None)
    np.fill_diagonal(Wp, 0.0)
    out = Wp.sum(axis=1, keepdims=True)
    S = np.where(out > 0, Wp / np.where(out > 0, out, 1.0), z[None, :])
    return S


def pagerank(W: np.ndarray, alpha: float = 0.85, eps: float = 1e-6, max_iter: int = 100,
             z: np.ndarray | None = None) -> np.ndarray:
    """Weighted PageRank on the positive part of W (negative edges are ignored)."""
    n = W.shape[0]
    if n == 0:
        return np.zeros(0)
    z = np.full(n, 1.0 / n) if z is None else z / z.sum()
    S = _transition(W, z)
    x = np.full(n, 1.0 / n)
    for _ in range(max_iter):
        x_new = alpha * (S.T @ x) + (1 - alpha) * z
        x_new /= x_new.sum()
        if np.abs(x_new - x).max() < eps:
            return x_new
        x = x_new
    return x


def pagetrust(W: np.ndarray, alpha: float = 0.85, gamma: float = 1.0, memory: float = 0.0,
              eps: float = 1e-6, max_iter: int = 100, z: np.ndarray | None = None,
              return_iters: bool = False):
    """PageTrust ranking. gamma may be np.inf. memory in [0, 1]: probability a surfer
    keeps its blacklist across a random jump (the paper uses 0 or 1)."""
    n = W.shape[0]
    if n == 0:
        return (np.zeros(0), 0) if return_iters else np.zeros(0)
    z = np.full(n, 1.0 / n) if z is None else z / z.sum()
    S = _transition(W, z)                      # S[j, i]: prob. j -> i along a link
    neg = W < 0
    np.fill_diagonal(neg, False)

    x = np.full(n, 1.0 / n)
    P = neg.astype(float)
    P_tilde = P.copy()
    it = 0
    for it in range(1, max_iter + 1):
        # 1. ranking update with the distrust of surfers arriving at each vertex
        d = np.diag(P_tilde)
        if np.isinf(gamma):
            keep = (d <= 1e-12).astype(float)
        else:
            keep = np.clip(1.0 - d, 0.0, 1.0) ** gamma
        Gx = alpha * (S.T @ x) + (1 - alpha) * z
        x_new = keep * Gx
        total = x_new.sum()
        x_new = x_new / total if total > 0 else np.full(n, 1.0 / n)

        # 2. arrival-mix matrix T[i, j] (computed with the current x, as in the paper)
        link_flow = alpha * S.T * x[None, :]                 # [i, j] = α S[j, i] x_j
        jump_flow = (1 - alpha) * z[:, None] * x[None, :]    # [i, j] = (1-α) z_i x_j
        arrivals = link_flow.sum(axis=1) + (1 - alpha) * z * x.sum()
        T = (link_flow + memory * jump_flow) / np.where(arrivals > 0, arrivals, 1.0)[:, None]

        # 3. blacklists travel with surfers, then each vertex adds its own negative links
        P_tilde_new = T @ P
        P = P_tilde_new.copy()
        P[neg] = 1.0
        np.fill_diagonal(P, 0.0)

        done = max(np.abs(x_new - x).max(),
                   np.abs(np.diag(P_tilde_new) - np.diag(P_tilde)).max()) < eps
        x, P_tilde = x_new, P_tilde_new
        if done:
            break
    return (x, it) if return_iters else x


def in_degree(W: np.ndarray) -> np.ndarray:
    """Signed sum of incoming edge weights (degree centrality)."""
    return W.sum(axis=0)

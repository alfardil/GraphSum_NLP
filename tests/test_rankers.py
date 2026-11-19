import sys, numpy as np
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__))))
from rankers import pagerank, pagetrust, in_degree
rng = np.random.default_rng(0)
W = rng.random((6, 6)); np.fill_diagonal(W, 0)
pr = pagerank(W)
assert np.isclose(pr.sum(), 1)
# no negative edges -> PageTrust == PageRank for any gamma / memory
for g in (0, 1, 2, np.inf):
    for m in (0, 1):
        assert np.allclose(pagetrust(W, gamma=g, memory=m), pr, atol=1e-5), (g, m)
# negative edges with gamma = 0 -> PageRank on the positive part
Wn = W.copy(); Wn[0, 3] = -1.0; Wn[1, 3] = -1.0; Wn[2, 3] = -0.5
assert np.allclose(pagetrust(Wn, gamma=0), pagerank(Wn), atol=1e-5)
# distrusted vertex 3 drops, more so with higher conviction, and is 0 at gamma = inf
s = {g: pagetrust(Wn, gamma=g, memory=1) for g in (0, 1, 2, np.inf)}
assert s[0][3] > s[1][3] > s[2][3] > s[np.inf][3], {g: v[3] for g, v in s.items()}
assert s[np.inf][3] < 1e-9 and all(np.isclose(v.sum(), 1) for v in s.values())
# memory keeps blacklists across jumps -> at least as much distrust
assert pagetrust(Wn, gamma=1, memory=1)[3] <= pagetrust(Wn, gamma=1, memory=0)[3] + 1e-9
# dangling vertex and empty graph
Wd = W.copy(); Wd[5, :] = 0
assert np.isclose(pagerank(Wd).sum(), 1) and np.isclose(pagetrust(Wd).sum(), 1)
assert pagetrust(np.zeros((0, 0))).shape == (0,)
x, it = pagetrust(Wn, gamma=1, return_iters=True); print("converged in", it, "iters")
print("rankers ok; vertex-3 score by gamma:", {g: round(float(v[3]), 4) for g, v in s.items()})

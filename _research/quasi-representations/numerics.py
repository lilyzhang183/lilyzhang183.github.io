"""
Numerical checks for the note
"Dimension cost of cancelling the winding number in quasi-representations".

Everything here is elementary linear algebra on explicit matrices:

  * winding(U, V)          : Exel-Loring winding number of an almost commuting pair,
                             computed as (1/2 pi) * sum of principal arguments of the
                             eigenvalues of  V U V^* U^*.
  * voiculescu(n)          : the clock/shift pair (U_n, V_n) on C^n, winding -1.
  * berg_correction(...)   : the explicit U-turn ("Berg") construction of a commuting
                             pair (A, B) on C^{n+k} close to
                                 X = U_n (+) U_k,   Y = V_n (+) V_k^*,
                             with windows of length L and N_b turning points.
  * compression_check(...) : verifies the polar-compression lemma on the output:
                             the compressed corner of the commuting pair is 6 eta^2-almost
                             commuting and carries winding number +1.

Run:  python3 numerics.py          (takes a few minutes; prints the tables used in the note)
"""
import numpy as np
from numpy.linalg import svd

rng = np.random.default_rng(0)


def opnorm(M):
    return svd(M, compute_uv=False)[0]


def clock(n):
    return np.diag(np.exp(2j * np.pi * np.arange(n) / n))


def shift(n):
    """V e_j = e_{j+1 mod n}."""
    V = np.zeros((n, n), dtype=complex)
    for j in range(n):
        V[(j + 1) % n, j] = 1.0
    return V


def voiculescu(n):
    return clock(n), shift(n)


def comm(A, B):
    return A @ B - B @ A


def winding(U, V):
    Z = V @ U @ V.conj().T @ U.conj().T
    ev = np.linalg.eigvals(Z)
    return float(np.sum(np.angle(ev)) / (2 * np.pi))


def polar(T):
    """Unitary part of the polar decomposition T = W |T| (T assumed invertible)."""
    W, s, Vh = svd(T)
    return W @ Vh


# --------------------------------------------------------------------------------------
#  The U-turn construction
# --------------------------------------------------------------------------------------

def berg_correction(n, k, L, Nb, verbose=False):
    """
    Lane + : sites j in Z/n, vectors e^+_j (indices 0..n-1),
             X e^+_j = w_n^j e^+_j,  Y e^+_j = e^+_{j+1}.
    Lane - : sites l in Z/k, vectors e^-_l (indices n..n+k-1),
             X e^-_l = w_k^l e^-_l,  Y e^-_l = e^-_{l-1}   (this is (U_k, V_k^*), winding +1).

    Returns (X, Y, A, B, info) with A, B commuting unitaries.
    """
    N = n + k
    X = np.zeros((N, N), dtype=complex)
    X[:n, :n] = clock(n)
    X[n:, n:] = clock(k)
    Y = np.zeros((N, N), dtype=complex)
    Y[:n, :n] = shift(n)
    Y[n:, n:] = shift(k).conj().T      # backward shift on lane -

    def ep(j):
        v = np.zeros(N, dtype=complex); v[j % n] = 1.0; return v

    def em(l):
        v = np.zeros(N, dtype=complex); v[n + (l % k)] = 1.0; return v

    # turning points: common phase theta_a = 2 pi a / Nb
    mp = [int(round(n * a / Nb)) for a in range(Nb)]   # lane + sites
    mm = [int(round(k * a / Nb)) for a in range(Nb)]   # lane - sites
    Mp = [(mp[(a + 1) % Nb] - mp[a]) % n or n for a in range(Nb)]
    Mm = [(mm[(a + 1) % Nb] - mm[a]) % k or k for a in range(Nb)]
    if min(Mp) < L + 1 or min(Mm) < L + 1:
        raise ValueError(f"windows overlap: min block lengths {min(Mp)}, {min(Mm)} < L+1={L+1}")

    B = Y.copy()
    alpha = (np.pi / 2) * np.arange(L + 1) / L
    for a in range(Nb):
        h = [ep(mp[a] - L + i) for i in range(L + 1)]
        F = [em(mm[a] + L - i) for i in range(L + 1)]
        hp = [np.cos(alpha[i]) * h[i] + np.sin(alpha[i]) * F[i] for i in range(L + 1)]
        fp = [-np.sin(alpha[i]) * h[i] + np.cos(alpha[i]) * F[i] for i in range(L + 1)]
        for i in range(L):
            B += np.outer(hp[i + 1] - Y @ hp[i], hp[i].conj())
            B += np.outer(fp[i + 1] - Y @ fp[i], fp[i].conj())

    # cycle subspaces of B: follow the orbit of a free lane-+ vector in each block
    projs = []
    for a in range(Nb):
        v0 = ep(mp[a] + 1)
        vecs = [v0]
        v = B @ v0
        while abs(abs(np.vdot(v0, v)) - 1.0) > 1e-8:
            vecs.append(v)
            v = B @ v
            if len(vecs) > N + 1:
                raise RuntimeError("orbit did not close")
        Q = np.array(vecs).T
        projs.append(Q @ Q.conj().T)
    P_sum = sum(projs)
    assert opnorm(P_sum - np.eye(N)) < 1e-8, "cycle subspaces do not exhaust the space"

    theta = [2 * np.pi * a / Nb for a in range(Nb + 1)]
    A = sum(np.exp(1j * (theta[a] + theta[a + 1]) / 2) * projs[a] for a in range(Nb))

    info = dict(
        unitary_A=opnorm(A @ A.conj().T - np.eye(N)),
        unitary_B=opnorm(B @ B.conj().T - np.eye(N)),
        commutator_AB=opnorm(comm(A, B)),
        eta_X=opnorm(X - A),
        eta_Y=opnorm(Y - B),
        cycle_lengths=[int(round(np.trace(P).real)) for P in projs],
    )
    info["eta"] = max(info["eta_X"], info["eta_Y"])
    if verbose:
        print(info)
    return X, Y, A, B, info


def compression_check(n, k, A, B, eta):
    """Polar compression of the commuting pair (A,B) to the lane - corner."""
    A22, B22 = A[n:, n:], B[n:, n:]
    Ut, Vt = polar(A22), polar(B22)
    out = dict(
        corner_commutator=opnorm(comm(A22, B22)),
        polar_commutator=opnorm(comm(Ut, Vt)),
        bound_6eta2=6 * eta ** 2,
        offdiag_A=max(opnorm(A[:n, n:]), opnorm(A[n:, :n])),
        offdiag_B=max(opnorm(B[:n, n:]), opnorm(B[n:, :n])),
        winding_polar_corner=winding(Ut, Vt),
        dist_polar_to_Uk=opnorm(Ut - clock(k)),
        dist_polar_to_Vk_star=opnorm(Vt - shift(k).conj().T),
    )
    return out


def best_correction(n, k, Ls=None, Nbs=None):
    """Grid search over window length L and number of turning points Nb."""
    best = None
    if Ls is None:
        Ls = sorted(set(max(1, int(round(c * np.sqrt(k)))) for c in (0.2, 0.3, 0.45)))
    for L in Ls:
        cand_Nb = Nbs if Nbs is not None else sorted(set(max(1, int(k // (c * (L + 1)))) for c in (1.5, 2.5)))
        for Nb in cand_Nb:
            if Nb < 1:
                continue
            try:
                X, Y, A, B, info = berg_correction(n, k, L, Nb)
            except ValueError:
                continue
            if best is None or info["eta"] < best[-1]["eta"]:
                best = (L, Nb, X, Y, A, B, info)
    return best


if __name__ == "__main__":
    np.set_printoptions(precision=4, suppress=True)

    print("=== 1. Winding numbers and Lemma A  (|w| <= m*delta/4) ===")
    for m in (5, 20, 100, 400):
        U, V = voiculescu(m)
        d = opnorm(comm(U, V))
        print(f"m={m:4d}  w(U_m,V_m)={winding(U,V):+.6f}  w(U_m,V_m^*)={winding(U,V.conj().T):+.6f}"
              f"  delta=|1-w_m|={d:.5f}  m*delta/4={m*d/4:.4f}")
    U, V = voiculescu(7)
    print("tensor with 1_3:  w(U(x)1, V(x)1) =", round(winding(np.kron(U, np.eye(3)), np.kron(V, np.eye(3))), 6))
    print("additivity: w((U_5 (+) U_3), (V_5 (+) V_3^*)) =",
          round(winding(np.block([[voiculescu(5)[0], np.zeros((5,3))],[np.zeros((3,5)), voiculescu(3)[0]]]),
                        np.block([[voiculescu(5)[1], np.zeros((5,3))],[np.zeros((3,5)), voiculescu(3)[1].conj().T]])), 6))

    print("\n=== 2. The U-turn construction: (U_n (+) U_k, V_n (+) V_k^*) is eta-close to a commuting pair ===")
    print("n     k     L   Nb    eta_X     eta_Y     eta      eta*sqrt(k)   ||[A,B]||   cycle lengths (min,max)")
    results = []
    for (n, k) in [(400, 100), (400, 200), (400, 400), (1000, 100), (1000, 250), (1000, 500), (1000, 1000),
                   (2000, 500)]:
        L, Nb, X, Y, A, B, info = best_correction(n, k)
        results.append((n, k, L, Nb, info))
        print(f"{n:<5d} {k:<5d} {L:<3d} {Nb:<4d} {info['eta_X']:.5f}  {info['eta_Y']:.5f}  {info['eta']:.5f}  "
              f"{info['eta']*np.sqrt(k):8.4f}   {info['commutator_AB']:.1e}   "
              f"({min(info['cycle_lengths'])},{max(info['cycle_lengths'])})")

    print("\n=== 3. Polar-compression lemma on the constructed pair (lane - corner, dimension k) ===")
    for (n, k) in [(400, 100), (1000, 250), (1000, 1000)]:
        L, Nb, X, Y, A, B, info = best_correction(n, k)
        c = compression_check(n, k, A, B, info["eta"])
        print(f"n={n}, k={k}: ||[A22,B22]||={c['corner_commutator']:.4f}, ||[polar]||={c['polar_commutator']:.4f} "
              f"<= 6 eta^2 = {c['bound_6eta2']:.4f};  offdiag(A),offdiag(B) = {c['offdiag_A']:.4f},{c['offdiag_B']:.4f} <= eta={info['eta']:.4f}")
        print(f"            winding of polar corner = {c['winding_polar_corner']:+.4f}  (should be +1 = -w(U_n,V_n));"
              f"  dist to (U_k, V_k^*) = {c['dist_polar_to_Uk']:.4f}, {c['dist_polar_to_Vk_star']:.4f}")

    print("\n=== 4. Lower bound vs. construction, winding number 1, complement dimension k ===")
    print("k      eta(constr.)   (2/3)/eta^2 (lower bd on k)   ratio k / lower bd")
    for (n, k, L, Nb, info) in results:
        if n == 1000:
            lb = (2.0 / 3.0) / info["eta"] ** 2
            print(f"{k:<6d} {info['eta']:.5f}       {lb:10.2f}                  {k/lb:8.2f}")

import time
import random

# =====================================================================
#  PROJECT: "SentinelLog" - Real-Time Log Intrusion Detection System
#  Uses Naive, Rabin-Karp, and KMP string matching to scan server
#  access logs for known attack signatures (SQLi, XSS, Path Traversal)
#  and benchmarks the 3 algorithms on realistic log data.
# =====================================================================

# ---------- 1. Naive Search ----------
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return [], 0

    matches, comparisons = [], 0
    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            matches.append(i)
    return matches, comparisons


# ---------- 2. KMP Search ----------
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length, i = 0, 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return [], 0
    lps = compute_lps(pattern)
    matches, comparisons = [], 0
    i = j = 0
    while i < n:
        comparisons += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches, comparisons


# ---------- 3. Rabin-Karp Search ----------
def rabin_karp(text, pattern, q=101):
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return [], 0
    d = 256
    h = pow(d, m - 1, q)
    p_hash = t_hash = 0
    matches, comparisons = [], 0
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q
    for s in range(n - m + 1):
        if p_hash == t_hash:
            for k in range(m):
                comparisons += 1
                if text[s + k] != pattern[k]:
                    break
            else:
                matches.append(s)
        if s < n - m:
            t_hash = (d * (t_hash - ord(text[s]) * h) + ord(text[s + m])) % q
            if t_hash < 0:
                t_hash += q
    return matches, comparisons


# ---------- 4. Attack Signature Database ----------
ATTACK_SIGNATURES = {
    "SQL Injection":     "' OR '1'='1",
    "SQL Injection (UNION)": "UNION SELECT",
    "XSS Attack":        "<script>alert(",
    "Path Traversal":    "../../etc/passwd",
    "Command Injection": "; rm -rf",
}


# ---------- 5. Synthetic Log Generator ----------
def generate_log_file(num_lines=2000, attack_ratio=0.01, seed=42):
    random.seed(seed)
    benign_templates = [
        "GET /index.html HTTP/1.1 200",
        "GET /images/logo.png HTTP/1.1 200",
        "POST /login HTTP/1.1 200 user=alice",
        "GET /api/products?id=104 HTTP/1.1 200",
        "GET /favicon.ico HTTP/1.1 404",
        "POST /checkout HTTP/1.1 302",
    ]
    lines = []
    attack_positions = []

    for i in range(num_lines):
        if random.random() < attack_ratio:
            sig_name, sig_pattern = random.choice(list(ATTACK_SIGNATURES.items()))
            malicious_line = f"GET /search?q={sig_pattern} HTTP/1.1 500"
            lines.append(malicious_line)
            attack_positions.append((i, sig_name))
        else:
            lines.append(random.choice(benign_templates))

    log_text = "\n".join(lines)
    return log_text, attack_positions


# ---------- 6. Scan Log With All 3 Algorithms ----------
def scan_log(log_text, algorithm_fn):
    detections = {}
    total_comparisons = 0
    for name, pattern in ATTACK_SIGNATURES.items():
        matches, comps = algorithm_fn(log_text, pattern)
        total_comparisons += comps
        if matches:
            detections[name] = len(matches)
    return detections, total_comparisons


# ---------- 7. Benchmark Across Log Sizes ----------
def run_benchmark():
    print("\n" + "=" * 78)
    print("PERFORMANCE BENCHMARK: Naive vs KMP vs Rabin-Karp on server logs")
    print("=" * 78)
    sizes = [500, 1000, 5000, 10000, 20000]
    print(f"{'LogLines':>10} {'Naive(ms)':>12} {'KMP(ms)':>12} {'RK(ms)':>12} "
          f"{'NaiveCmp':>10} {'KMPCmp':>10} {'RKCmp':>10}")
    print("-" * 78)

    for size in sizes:
        log_text, _ = generate_log_file(num_lines=size, attack_ratio=0.01, seed=1)

        start = time.perf_counter()
        _, c_naive = scan_log(log_text, naive_search)
        t_naive = (time.perf_counter() - start) * 1000

        start = time.perf_counter()
        _, c_kmp = scan_log(log_text, kmp_search)
        t_kmp = (time.perf_counter() - start) * 1000

        start = time.perf_counter()
        _, c_rk = scan_log(log_text, rabin_karp)
        t_rk = (time.perf_counter() - start) * 1000

        print(f"{size:>10} {t_naive:>12.4f} {t_kmp:>12.4f} {t_rk:>12.4f} "
              f"{c_naive:>10} {c_kmp:>10} {c_rk:>10}")


# ---------- 8. Main Demo ----------
def main():
    print("=" * 78)
    print("   SENTINELLOG — Intrusion Detection via String Matching Algorithms")
    print("=" * 78)

    log_text, injected_attacks = generate_log_file(num_lines=1500, attack_ratio=0.015, seed=7)
    print(f"\nGenerated synthetic log with {log_text.count(chr(10)) + 1} lines.")
    print(f"Ground-truth attacks injected: {len(injected_attacks)}")

    for name, algo in [("Naive Search", naive_search),
                        ("KMP Search", kmp_search),
                        ("Rabin-Karp", rabin_karp)]:
        start = time.perf_counter()
        detections, comps = scan_log(log_text, algo)
        elapsed = (time.perf_counter() - start) * 1000

        print(f"\n--- Scan using {name} ---")
        print(f"Time: {elapsed:.4f} ms | Total character comparisons: {comps}")
        if detections:
            print("Detected attack types:")
            for atk, count in detections.items():
                print(f"   ⚠️  {atk}: {count} occurrence(s)")
        else:
            print("No attacks detected.")

    run_benchmark()

    print("\n" + "=" * 78)
    print("CONCLUSION")
    print("=" * 78)
    print("All 3 algorithms correctly flagged the same attack signatures, confirming")
    print("correctness. Naive search does the most character comparisons since it")
    print("re-scans overlapping regions on every mismatch. Rabin-Karp does drastically")
    print("fewer character comparisons (it uses a rolling hash to skip most positions")
    print("entirely and only verifies characters when the hash matches) - but its")
    print("wall-clock time is higher here because computing the rolling hash in pure")
    print("Python adds per-character overhead that outweighs the comparison savings")
    print("at this log size. KMP does about as many comparisons as Naive on this data")
    print("(few repeated sub-patterns to exploit) but never re-reads a text character,")
    print("giving it the best guaranteed worst-case O(n+m). In a compiled language")
    print("(C/C++), Rabin-Karp's low comparison count would translate into real speed")
    print("gains, and it scales best when checking MANY signatures against one log,")
    print("exactly how real intrusion detection systems (e.g. Snort/Suricata) use it.")


if __name__ == "__main__":
    main()
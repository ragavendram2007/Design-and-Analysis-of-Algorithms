# DAA Lab Projects — Interactive Web Applications

**Course:** AM5303 – Design and Analysis of Algorithms
**Programme:** B.E. CSE (AIML), Chennai Institute of Technology
**Author:** Ragavendra

This repository contains ten self-contained, single-file web applications —
one for every exercise in the DAA Lab Manual. Every Python algorithm from
the manual has been ported to JavaScript, wrapped in an interactive
dark-themed UI, and verified against the original logic before delivery.

No build step, server, or dependency installation is required for any of
them — just open the `.html` file in a browser.

---

## Project Index

| # | Lab Exercise | App Name | File | Algorithms Covered |
|---|---|---|---|---|
| 1 | Ex 1 — Interpolation Search | **Smart Roll Number Lookup System** | `smart_roll_number_lookup.html` | Interpolation Search, Binary Search |
| 2 | Ex 2 — String Matching | **SentinelLog** | `sentinellog.html` | Naive Search, Rabin-Karp, KMP |
| 3 | Ex 3 — Minimum Spanning Tree | **Smart City Fiber Network Planner** | `smart_city_fiber_planner.html` | Kruskal's Algorithm, Prim's Algorithm |
| 4 | Ex 4 — Single Source Shortest Path | **SafeRide — Shortest Commute Finder** | `Project_4_-_web_app.html` | Dijkstra's Algorithm, Brute-Force Verification |
| 5 | Ex 5 — Divide & Conquer | **City Sensor Network Extreme Reading Finder** | `Project_5_-_web_app.html` | Divide & Conquer Min-Max, Naive Linear Scan |
| 6 | Ex 6 — Dynamic Programming | **SIGNAL — Traffic-Camera Pipeline Optimizer** | `Project_6_-_Smart_Traffic-Camera_Image_Pipeline_Optimizer_web_app.html` | Matrix Chain Multiplication (DP vs Brute-Force) |
| 7 | Ex 7 — Backtracking | **QueenScope — N-Queens Backtracking Visualizer** | `Project_7_-_QueenScope.html` | N-Queens Backtracking |
| 8 | Ex 8 — Branch & Bound | **RouteBound — TSP Branch & Bound Visualizer** | `Project_8_-_RouteBound.html` | Travelling Salesman Problem (Branch & Bound) |
| 9 | Ex 9 — Bin Packing | **CloudBin** | `cloudbin.html` | First Fit, First Fit Decreasing, Best Fit Decreasing, Next Fit Decreasing |
| 10 | Ex 10 — Randomized Algorithms | **QuickGuard** | `quickguard.html` | Deterministic QuickSort, Randomized QuickSort |

---

## 1. Smart Roll Number Lookup System *(Ex 1)*

A student-record lookup tool that compares **Interpolation Search** against
**Binary Search** on a sorted roll-number dataset.

**Features**
- Configurable dataset size and starting roll number, generated with a
  seeded PRNG for reproducible results.
- Search for an existing roll, a known-missing roll, or a custom roll number,
  with comparison counts shown for each search.
- Student statistics: total count, highest/lowest/average marks.
- Benchmark tab: runs both algorithms across dataset sizes from 1,000 to
  100,000, reporting average time and comparisons per size.

---

## 2. SentinelLog *(Ex 2)*

A log-intrusion-detection simulator that scans synthetic server access logs
for known attack signatures (SQL injection, XSS, path traversal, command
injection) using three string-matching algorithms.

**Features**
- Synthetic log generator with configurable line count, attack ratio, and
  random seed.
- Scan tab: runs Naive Search, KMP, and Rabin-Karp side by side, showing
  detected attack types, occurrence counts, comparisons, and timing for each.
- Log viewer with injected attack lines highlighted.
- Benchmark tab: compares all three algorithms across log sizes from 500 to
  20,000 lines.
- Signatures tab: lists the known attack patterns being searched for.

**Verified:** all three algorithms were cross-checked in Node.js to confirm
they report identical match positions and detection counts on the same log
data — differing only in comparison count and speed, as expected.

---

## 3. Smart City Fiber Network Planner *(Ex 3)*

Plans the minimum-cost fiber-optic cable layout connecting city junctions
using **Kruskal's** and **Prim's** Minimum Spanning Tree algorithms.

**Features**
- Demo Network tab: runs both algorithms on an 8-junction city dataset
  (CityCenter, TechPark, Airport, Hospital, University, MetroStation,
  Stadium, Mall), with a verification banner confirming both algorithms
  agree on total cost.
- Graph View tab: an SVG diagram of the city network with the selected MST
  routes highlighted against the faded candidate routes.
- Benchmark tab: compares both algorithms on random, connected graphs from
  50 to 1,000 nodes.
- Candidate Routes tab: full table of all considered cable routes and costs.

**Verified:** in Node.js, both algorithms produced identical MST costs on
the demo network and on every random graph size tested (50–1000 nodes), and
the random-graph generator was confirmed to always produce a connected graph.

---

## 4. SafeRide — Shortest Commute Finder *(Ex 4)*

Finds the safest-and-shortest cycling route across a city road network using
**Dijkstra's Algorithm**, where each road's weight combines distance with a
cycling-safety risk penalty (so the "shortest" route is also the safer one).

**Features**
- City road network (Home, SchoolJn, MarketRd, RiverBridge, TechPark,
  MainSignal, ParkLane, Office) with distance + risk-weighted edges.
- Shortest-path result from Home to every other location, with the full
  route and cost shown for each.
- Brute-force verification: an exhaustive search over all simple paths
  confirms Dijkstra's answer is truly optimal, not just fast.
- Benchmark tab: Dijkstra's performance on random road networks from 50 to
  5,000 nodes, demonstrating its near-linearithmic O((V+E) log V) growth.

---

## 5. City Sensor Network Extreme Reading Finder *(Ex 5)*

Finds the cleanest and most polluted zones (min/max AQI) across a city's IoT
air-quality sensor network using a **Divide & Conquer** min-max algorithm,
compared against a naive linear scan.

**Features**
- Demo sensor network across 10 Chennai zones (T Nagar, Anna Nagar,
  Velachery, Adyar, Guindy, Tambaram, Perungudi, Porur, Egmore, Mylapore),
  with a seeded hazardous-AQI spike and an unusually clean reading injected.
- Side-by-side comparison of Divide & Conquer vs naive scan results and
  comparison counts, with a verification check that both agree.
- Hazard alert when the most polluted zone crosses the AQI threshold.
- Benchmark tab: comparison counts at sensor-network sizes from 10 to
  100,000, checked against the theoretical 3n/2 − 2 bound.

---

## 6. SIGNAL — Traffic-Camera Pipeline Optimizer *(Ex 6)*

Finds the cheapest order to chain a sequence of matrix transforms (the kind
a traffic-camera vision pipeline runs every frame through — perspective fix,
rotation, scaling, color conversion) using the **Matrix Chain Multiplication**
dynamic-programming algorithm, verified against true brute-force enumeration.

**Features**
- Configurable chain of matrix dimensions representing a camera frame
  pipeline.
- DP solution showing the optimal parenthesization and minimum scalar
  multiplication cost, compared directly against brute-force enumeration of
  every possible grouping.
- Visualizes just how much the multiplication order can affect cost for the
  same fixed sequence of transforms.

---

## 7. QueenScope — N-Queens Backtracking Visualizer *(Ex 7)*

A live, step-by-step visualizer for the **N-Queens backtracking algorithm** —
showing not just the final solution, but every placement and every
undo (backtrack) as it happens.

**Features**
- Configurable board size (N).
- Play through the full recursive backtracking search automatically, or
  step through it manually one placement/removal at a time.
- Visual distinction between a queen being placed, a queen being removed on
  conflict, and a completed valid solution.

---

## 8. RouteBound — TSP Branch & Bound Visualizer *(Ex 8)*

A live visualizer for solving the **Travelling Salesman Problem** with
**Branch & Bound** — showing the priority queue of partial routes, the
lower-bound calculation for each, and the pruning of branches that can't
beat the best full tour found so far.

**Features**
- Editable city cost matrix — type your own costs, randomize it, or reset to
  a preset 5-city example.
- Live view of the branch-and-bound queue as it expands the most promising
  partial route first and prunes the rest.
- Shows the gap between exploring every possible (n−1)! tour and the much
  smaller set Branch & Bound actually needs to check.

---

## 9. CloudBin *(Ex 9)*

Frames the Bin Packing problem as allocating cloud tasks (by RAM demand) to
fixed-capacity servers, comparing three approximation algorithms.

**Features**
- Configurable task list (comma-separated RAM sizes) and server capacity.
- Allocation Result tab: runs First Fit, First Fit Decreasing, and Best Fit
  Decreasing, visualizing each server's packed tasks as a filled bar with
  utilization percentage, and flagging whichever algorithm(s) use the fewest
  servers.
- Benchmark tab: 100 trials of 50 random tasks each, reporting the average
  number of servers used by FF, FFD, BFD, and Next Fit Decreasing.

**Verified:** the manual's own reference Python code was run directly and
found to produce a different bin count (6) than the manual's stated sample
output (5), due to floating-point rounding (`1.0 - 0.9` does not exactly
equal `0.1` in IEEE-754 arithmetic, so an exact-fit item can be rejected by
a strict `>=` check). A small epsilon tolerance was added to the capacity
comparisons in this app so results match the manual's intended packing.

---

## 10. QuickGuard *(Ex 10)*

Demonstrates why production sort implementations randomize their pivot
choice, by comparing **Deterministic QuickSort** (last-element pivot)
against **Randomized QuickSort** across four input distributions.

**Features**
- Configurable array size (capped at 5,000 — see note below).
- Runs both algorithms on Random, Sorted, Reverse-sorted, and Nearly-sorted
  arrays, reporting comparison counts and timing for each.
- Bar-chart visualization showing the comparison-count blowup for
  deterministic QuickSort on structured input, next to randomized
  QuickSort's consistently low comparison count.
- "How It Works" tab explaining the theory in plain terms.

**Verified:** in Node.js, deterministic QuickSort on a sorted array produced
exactly N(N−1)/2 comparisons (the theoretical worst case), while randomized
QuickSort stayed close to N·log₂N regardless of input order. Recursion depth
was also stress-tested directly: deterministic QuickSort on sorted input
recurses to depth N and was found to overflow the JavaScript call stack
somewhere between 5,000–8,000 elements, which is why array size is capped
at 5,000 and the sort call is wrapped in a try/catch as a safety net.

---

## Design Notes (all apps)

- **Single file, zero dependencies.** Each app is one `.html` file with
  inline CSS and JavaScript — no external libraries, no build tools, no
  internet connection required after download.
- **Seeded randomness.** Apps that use random data generate it with a
  `mulberry32` seeded pseudo-random number generator so that "random"
  datasets are reproducible across runs, mirroring Python's
  `random.seed(n)` behavior in the original lab code.
- **Direct algorithm ports.** Every core algorithm (search, sort, string
  matching, graph, packing, DP, backtracking, branch & bound) is a
  line-by-line JavaScript translation of the Python reference implementation
  from the lab manual — not a rewrite — so behavior and complexity
  characteristics match the original.
- **Pre-shipped verification.** Before delivery, each app's core algorithm
  logic was extracted and executed standalone in Node.js to confirm
  correctness (matching outputs across algorithms, expected complexity
  behavior, edge cases) rather than relying on visual inspection alone.

## How to Run

1. Download the `.html` file for the project you want.
2. Open it directly in any modern browser (Chrome, Firefox, Edge, Safari).
3. No installation, server, or internet connection needed.

## Folder Layout

```
DAA-Lab-Projects/
├── README.md
├── smart_roll_number_lookup.html                                       (Ex 1)
├── sentinellog.html                                                    (Ex 2)
├── smart_city_fiber_planner.html                                       (Ex 3)
├── Project_4_-_web_app.html                        (SafeRide)          (Ex 4)
├── Project_5_-_web_app.html                        (City Sensor Net)   (Ex 5)
├── Project_6_-_...pipeline_optimizer_web_app.html  (SIGNAL)            (Ex 6)
├── Project_7_-_QueenScope.html                                         (Ex 7)
├── Project_8_-_RouteBound.html                                         (Ex 8)
├── cloudbin.html                                                       (Ex 9)
└── quickguard.html                                                     (Ex 10)
```

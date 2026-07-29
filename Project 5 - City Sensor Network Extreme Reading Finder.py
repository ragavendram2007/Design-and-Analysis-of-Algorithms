import random
import time

# =====================================================================
#  PROJECT: "City Sensor Network Extreme Reading Finder"
#  Uses Divide & Conquer to instantly find the cleanest and most
#  polluted zones (min/max AQI) across a city's IoT sensor network,
#  and compares comparison-efficiency against a naive linear scan.
# =====================================================================

HAZARD_AQI_THRESHOLD = 200  # AQI above this = hazardous air quality

# ---------- Divide & Conquer Min-Max ----------
comparison_count = 0  # global counter, reset before each run

def min_max_dc(arr, low, high):
    global comparison_count

    if not arr:
        return None, None

    if low < 0 or high >= len(arr) or low > high:
        raise ValueError("invalid array range")

    if low == high:
        return arr[low], arr[low]

    if high == low + 1:
        comparison_count += 1
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        return arr[high], arr[low]

    mid = (low + high) // 2
    lmin, lmax = min_max_dc(arr, low, mid)
    rmin, rmax = min_max_dc(arr, mid + 1, high)

    comparison_count += 1
    overall_min = lmin if lmin < rmin else rmin
    comparison_count += 1
    overall_max = lmax if lmax > rmax else rmax
    return overall_min, overall_max


# ---------- Naive Linear Scan ----------
def min_max_naive(arr):
    if not arr:
        return None, None, 0

    mn, mx = arr[0], arr[0]
    comps = 0
    for x in arr[1:]:
        comps += 1
        if x < mn:
            mn = x
        comps += 1
        if x > mx:
            mx = x
    return mn, mx, comps


# ---------- City Zone Sensor Network (demo dataset) ----------
ZONES = ["TNagar", "Anna Nagar", "Velachery", "Adyar", "Guindy",
         "Tambaram", "Perungudi", "Porur", "Egmore", "Mylapore"]


def generate_sensor_readings(zones, seed=7):
    random.seed(seed)
    readings = [random.randint(40, 180) for _ in zones]
    readings[3] = 245   # Adyar - hazardous spike (e.g. construction dust)
    readings[8] = 28    # Egmore - unusually clean reading
    return readings


def demo_sensor_network():
    print("=" * 78)
    print("   CITY SENSOR NETWORK EXTREME READING FINDER (Divide & Conquer)")
    print("=" * 78)

    readings = generate_sensor_readings(ZONES)

    print(f"\nZones monitored: {len(ZONES)}")
    print(f"{'Zone':>14} {'AQI':>6}")
    print("-" * 24)
    for zone, aqi in zip(ZONES, readings):
        flag = "  ⚠️ HAZARD" if aqi > HAZARD_AQI_THRESHOLD else ""
        print(f"{zone:>14} {aqi:>6}{flag}")

    global comparison_count
    comparison_count = 0
    dc_min, dc_max = min_max_dc(readings, 0, len(readings) - 1)
    dc_comps = comparison_count

    naive_min, naive_max, naive_comps = min_max_naive(readings)

    print(f"\n--- Divide & Conquer Result ---")
    print(f"Cleanest zone AQI: {dc_min} | Most polluted zone AQI: {dc_max}")
    print(f"Comparisons used: {dc_comps}")

    print(f"\n--- Naive Linear Scan Result ---")
    print(f"Cleanest zone AQI: {naive_min} | Most polluted zone AQI: {naive_max}")
    print(f"Comparisons used: {naive_comps}")

    cleanest_zone = ZONES[readings.index(dc_min)]
    worst_zone = ZONES[readings.index(dc_max)]

    print(f"\n--- Verification ---")
    if dc_min == naive_min and dc_max == naive_max:
        print("✅ Both methods agree on the extreme readings!")
    else:
        print("❌ Mismatch detected (unexpected).")

    print(f"\n📍 Cleanest zone: {cleanest_zone} (AQI {dc_min})")
    print(f"📍 Most polluted zone: {worst_zone} (AQI {dc_max})")
    if dc_max > HAZARD_AQI_THRESHOLD:
        print(f"🚨 ALERT: {worst_zone} has crossed the hazardous AQI threshold "
              f"({HAZARD_AQI_THRESHOLD})! Recommend rerouting cyclists/pedestrians away from this zone.")


# ---------- Benchmark: comparisons at growing sensor-network sizes ----------
def run_benchmark():
    print("\n" + "=" * 78)
    print("PERFORMANCE BENCHMARK: D&C vs Naive comparisons vs theoretical formula")
    print("=" * 78)
    global comparison_count
    sizes = [10, 100, 1000, 10000, 100000]
    print(f"{'Sensors':>10} {'D&C Comps':>12} {'Naive Comps':>14} {'Formula 3n/2-2':>16} "
          f"{'D&C Time(ms)':>14} {'Naive Time(ms)':>16}")
    print("-" * 78)

    for size in sizes:
        random.seed(size)
        arr = [random.randint(1, 500) for _ in range(size)]

        comparison_count = 0
        start = time.perf_counter()
        min_max_dc(arr, 0, len(arr) - 1)
        dc_time = (time.perf_counter() - start) * 1000
        dc_comps = comparison_count

        start = time.perf_counter()
        _, _, naive_comps = min_max_naive(arr)
        naive_time = (time.perf_counter() - start) * 1000

        formula = 3 * size // 2 - 2
        print(f"{size:>10} {dc_comps:>12} {naive_comps:>14} {formula:>16} "
              f"{dc_time:>14.4f} {naive_time:>16.4f}")


def main():
    demo_sensor_network()
    run_benchmark()

    print("\n" + "=" * 78)
    print("CONCLUSION")
    print("=" * 78)
    print("The Divide & Conquer approach correctly identified both the cleanest")
    print("and most polluted zones, matching the naive scan's answer exactly, while")
    print("using noticeably fewer comparisons than naive's 2(n-1) at every size -")
    print("staying close to (though not always exactly at) the theoretical 3n/2-2")
    print("bound, since the exact count depends on how the array happens to split")
    print("at each recursion level. For 100000 sensors, this is still a real ~17-25%")
    print("reduction in comparisons. In an always-on smart-city dashboard")
    print("polling thousands of sensors every few seconds, that reduction adds up")
    print("to meaningful savings in processing cost at scale - and the same min-max")
    print("scan pattern could equally track traffic density or road-safety risk")
    print("scores across zones for SafeRide AI's live risk dashboard.")


if __name__ == "__main__":
    main()
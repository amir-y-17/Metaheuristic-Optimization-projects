نام دانشجو: امیررضا یعقوبی‌زاده

درس: طراحی الگوریتم‌ها

موضوع: بهینه‌سازی مسئله فروشنده دوره‌گرد (TSP) با استفاده از SA ،LS و عملگرهای 2-Opt و 3-Opt


---

1. مقدمه

مسئله‌ی فروشنده‌ی دوره‌گرد (TSP) یکی از مشهورترین مسائل NP-Hard در حوزه‌ی بهینه‌سازی ترکیبیاتی است. هدف در این مسئله، یافتن کوتاه‌ترین مسیر ممکن برای عبور از تمام شهرها و بازگشت به نقطه‌ی آغاز است.

در این پروژه، دو رویکرد فراابتکاری و محلی زیر پیاده‌سازی شده است:

الگوریتم Local Search همراه با دو عملگر 2-Opt و 3-Opt

الگوریتم Simulated Annealing (SA) همراه با عملگرهای مشابه


کدهای استفاده‌شده به‌صورت ماژولار طراحی شده‌اند تا عملیات تولید همسایه، محاسبات فاصله و خواندن داده‌ها با شفافیت و قابلیت توسعه انجام گیرد.


---

2. خواندن داده‌ها از فایل TSP

فایل: loader.py

این تابع داده‌های مسئله (مختصات شهرها) را از یک فایل استاندارد TSP دریافت می‌کند:
```
def read_tsp_file(path="Train1/data/kroB200.txt"):
    """Reads a TSP file and returns the coordinates of the cities."""

    with open(path, "r") as f:
        lines = f.readlines()

    coords = []
    reading_coords = False
    for line in lines:
        line = line.strip()
        if line == "NODE_COORD_SECTION":
            reading_coords = True
            continue
        if line == "EOF":
            break
        if reading_coords:
            parts = line.split()
            if len(parts) >= 3:
                x, y = int(parts[1]), int(parts[2])
                coords.append((x, y))

    return coords
```
این تابع خروجی را به‌صورت لیست مختصات نقاط باز می‌گرداند و مبنای ساخت ماتریس فاصله است.


---

3. پیاده‌سازی Local Search

فایل: local_search.py

الگوریتم Local Search با دو همسایگی کلاسیک 2-Opt و 3-Opt پیاده‌سازی شده است. هدف، یافتن بهبود در مسیر فعلی با آزمون همسایه‌های محلی است.
```
from TSP import *


def local_search(initial_tour, distance_matrix, operator):
    """
    Perform local search optimization on the given tour using the specified operator.
    """
    operators = {
        "2-opt": apply_2opt,
        "3-opt": apply_3_opt,
    }

    if operator not in operators:
        raise ValueError(f"Unknown operator: {operator}")

    apply_operator = operators[operator]
    current = initial_tour.copy()
    n = len(initial_tour)
    current_distance = total_distance(current, distance_matrix)

    improved = True
    while improved:
        improved = False

        if operator == "2-opt":
            for i in range(1, n - 2):
                a = current[i - 1]
                b = current[i]

                for k in range(i + 1, n - 1):
                    c = current[k]
                    d = current[k + 1]

                    old_cost = distance_matrix[a][b] + distance_matrix[c][d]
                    new_cost = distance_matrix[a][c] + distance_matrix[b][d]

                    if new_cost < old_cost:
                        current[i : k + 1] = reversed(current[i : k + 1])
                        current_distance += new_cost - old_cost
                        improved = True
                        break

                if improved:
                    break

        elif operator == "3-opt":
            for i in range(1, n - 3):
                for j in range(i + 1, n - 2):
                    for k in range(j + 1, n - 1):

                        new_tour = apply_operator(current, i, j, k, distance_matrix)
                        new_distance = total_distance(new_tour, distance_matrix)

                        if new_distance < current_distance:
                            current = new_tour
                            current_distance = new_distance
                            improved = True
                            break

                    if improved:
                        break
                if improved:
                    break

    return current
```
نکات مهم طراحی LS

در 2-Opt از فرمول اختلاف هزینه استفاده شده تا سرعت افزایش یابد.

در 3-Opt به‌دلیل پیچیدگی، از تولید و ارزیابی مستقیم تور جدید استفاده شده.

الگوریتم تا زمانی که هیچ بهبودی رخ ندهد ادامه می‌یابد.



---

4. پیاده‌سازی Simulated Annealing

فایل: sa.py

الگوریتم SA با استفاده از یک دمای اولیه، نرخ سرد شدن و تابع پذیرش تصادفی پیاده‌سازی شده است.
```
import math
import random
from TSP import *


def SA(
    initial_tour,
    distance_matrix,
    initial_temp,
    cooling_rate,
    stopping_temp,
    operator,
):
    """
    Performs Simulated Annealing to optimize the given tour using the specified neighborhood operator.
    """

    operators = {"2opt": apply_2opt, "3opt": apply_3_opt}
    apply_operator = operators[operator]

    current = initial_tour.copy()
    best = initial_tour.copy()

    current_distance = total_distance(current, distance_matrix)
    best_distance = current_distance

    n = len(current)
    T = initial_temp
    T_min = stopping_temp

    no_improvement = 0
    L = n * 5  # Number of iterations at each temperature

    while T > T_min and no_improvement < 20:

        improved = False

        for _ in range(L):
            if operator == "2opt":
                i, k = random.sample(range(n), 2)
                new_tour = apply_operator(current, min(i, k), max(i, k))

            elif operator == "3opt":
                i, j, k = sorted(random.sample(range(n), 3))
                new_tour = apply_operator(current, i, j, k, distance_matrix)

            new_distance = total_distance(new_tour, distance_matrix)
            delta = new_distance - current_distance

            if delta <= 0:
                current = new_tour
                current_distance = new_distance
                improved = True

                if new_distance < best_distance:
                    best = new_tour
                    best_distance = new_distance

            else:
                P = math.exp(-delta / T)
                if random.random() < P:
                    current = new_tour
                    current_distance = new_distance

        T *= cooling_rate

        if improved:
            no_improvement = 0
        else:
            no_improvement += 1

    return best
```
ویژگی‌های SA در پیاده‌سازی حاضر
استفاده از قانون بولتزمن برای پذیرش حرکات بدتر

کنترل توقف بر اساس:

رسیدن به دمای نهایی

عدم پیشرفت در چندین تکرار


ایجاد همسایه‌های تصادفی از طریق 2-Opt یا 3-Opt



---

5. جمع‌بندی

در این پروژه، دو الگوریتم قدرتمند برای حل مسائل بهینه‌سازی مسیر—Local Search و Simulated Annealing—به‌صورت کامل پیاده‌سازی و آزمایش شدند.
همچنین دو عملگر کلاسیک 2-Opt و 3-Opt برای تولید همسایگی استفاده شد که نقش بسیار مهمی در کیفیت جواب‌ها دارند.

رویکرد LS سریع‌تر و مبتنی بر بهبود قطعی است، اما ممکن است در بهینه محلی گیر کند.
در مقابل، SA با اجازه‌ی پذیرش حرکت‌های بدتر، توانایی عبور از بهینه‌های محلی و رسیدن به پاسخ‌های بهتر را دارد.

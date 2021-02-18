# Лабораторна робота №1 на тему "Обчислення показників надійності за даними випробувань"
# Виконав студент групи ІО-71 Єрмоленко Віталій, варіант №6

# Вхідна вибірка наробітків до відмови (у годинах)

hour_table = [32, 314, 3, 755, 407, 439, 59, 1036, 142, 631, 317, 1175, 1991, 1329, 68, 126, 31, 420, 229, 173, 188, 938, 326, 1802, 424, 10, 668, 266, 1, 442, 459, 341, 293, 227, 104, 866, 110, 798, 70, 379, 355, 1232, 115, 230, 928, 2183, 387, 40, 903, 947, 169, 1733, 217, 628, 230, 871, 1360, 512, 19, 19, 359, 34, 575, 152, 741, 244, 379, 80, 401, 225, 334, 1301, 227, 335, 345, 2268, 1049, 354, 13, 441, 923, 995, 223, 350, 617, 2101, 174, 1852, 601, 335, 308, 1763, 273, 658, 499, 1027, 135, 8, 384, 3460]

# Завдання за варіантом:
# 1. Середній наробіток до відмови Tср,
# 2. γ-відсотковий наробіток на відмову Tγ при γ = 0.76,
# 3. ймовірність безвідмовної роботи на час 1914 годин,
# 4. інтенсивність відмов на час 489 годин

gamma = 0.76
faultless_time = 1914
intens_time = 489

sorted_hour = sorted(hour_table)
interval_length = 0
ten_intervals = []
stat_densities = []
P_list = []


def get_Tcp():
    return sum(hour_table) / len(hour_table)


def get_T(gamma):
    global interval_length, stat_densities, ten_intervals, P_list
    interval_length = (sorted_hour[-1] - sorted_hour[0]) / 10

    for i in range(0, 10):
        ten_intervals.append([a for a in sorted_hour if (i * interval_length <= a <= (i + 1) * interval_length)])

    stat_densities = [len(interval) / (len(sorted_hour) * interval_length) for interval in ten_intervals]
    area_sum = 1
    
    for i in range(10):
        P_list.append(area_sum)
        area_sum -= stat_densities[i] * interval_length

    p_less = max([p for p in P_list if p < gamma])
    p_more = min([p for p in P_list if p > gamma])

    index_less = P_list.index(p_less)
    index_more = P_list.index(p_more)

    d = (p_more - gamma) / (p_more - p_less)
    T = index_more + interval_length * d
    return T


def p_unfail(time):
    Sum = 1
    whole_intervals = int(time // interval_length)
    
    for i in range(whole_intervals):
        Sum -= stat_densities[i] * interval_length
    Sum -= stat_densities[whole_intervals] * (time % interval_length)
    return Sum


def fail_freq(time):
    f = stat_densities[int(time // interval_length)]
    p = p_unfail(time)
    return f / p


print("Середній наробіток до відмови Tср:", get_Tcp())
print("γ-відсотковий наробіток на відмову Tγ при γ = ", gamma, ":",  get_T(gamma))
print("ймовірність безвідмовної роботи на час", faultless_time, "годин:", p_unfail(faultless_time))
print("інтенсивність відмов на час", intens_time, "годин:", fail_freq(intens_time))

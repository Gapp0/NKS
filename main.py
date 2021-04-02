import math

P1 = 0.32
P2 = 0.82
P3 = 0.15
P4 = 0.24
P5 = 0.66
P6 = 0.99
P7 = 0.93


def var6(p1, p2, p3, p4, p5, p6, p7):
    r12 = 1 - (1 - p1) * (1 - p2)
    r13 = 1 - (1 - p1) * (1 - p3)
    r23 = 1 - (1 - p2) * (1 - p3)
    r134 = r13 * p4
    r56 = 1 - (1 - p5) * (1 - p6)
    r57 = 1 - (1 - p5) * (1 - p6)
    r67 = 1 - (1 - p6) * (1 - p7)
    s1 = r134 * r56
    s2 = r23 * r57
    ss = 1 - (1 - s1) * (1 - s2)
    t = r12 * ss * r67
    return t


print("Імовірність безвідмовної роботи системи:", var6(P1, P2, P3, P4, P5, P6, P7))

time = 1390
k1 = 3
k2 = 3

P_system = var6(P1, P2, P3, P4, P5, P6, P7)
Q_system = 1 - P_system
T_system = -time / math.log(P_system, math.e)

Q_reserved_system_1 = (1 - P_system) ** (k1 + 1)
P_reserved_system_1 = 1 - Q_reserved_system_1
T_reserved_system_1 = -time / math.log(P_reserved_system_1, math.e)
G_q_1 = Q_reserved_system_1 / Q_system
G_p_1 = P_reserved_system_1 / P_system
G_t_1 = T_reserved_system_1 / T_system

Q_reserved_system_2 = Q_system ** 4 / math.factorial(k1 + 1)
P_reserved_system_2 = 1 - Q_reserved_system_2
T_reserved_system_2 = -time / math.log(P_reserved_system_2, math.e)
G_q_2 = Q_reserved_system_2 / Q_system
G_p_2 = P_reserved_system_2 / P_system
G_t_2 = T_reserved_system_2 / T_system

print("Базова імовірність безвідмовної роботи = {}\n"
      "Базова імовірність відмови = {}\n"
      "Базовий середній наробіток на відмову = {}\n".format(P_system, Q_system, T_system))

print("Імовірність безвідмовної роботи системи з навантаженим загальним резервуванням = {}\n"
      "Імовірність відмови системи з навантаженим загальним резервуванням = {}\n"
      "Середній час роботи системи з навантаженим загальним резервуванням = {}".format(P_reserved_system_1,
                                                                                       Q_reserved_system_1,
                                                                                       T_reserved_system_1))
print("Виграш системи з навантаженим загальним резервуванням по імовірності безвідмовної роботи = {}\n"
      "Виграш системи з навантаженим загальним резервуванням по імовірності відмови = {}\n"
      "Виграш системи з навантаженим загальним резервуванням по середньому часу роботи = {}\n".format(G_p_1, G_q_1,
                                                                                                      G_t_1))

print("Імовірність безвідмовної роботи системи з ненавантаженим загальним резервуванням = {}\n"
      "Імовірність відмови системи з ненавантаженим загальним резервуванням = {}\n"
      "Середній час роботи системи з ненавантаженим загальним резервуванням = {}".format(P_reserved_system_2,
                                                                                         Q_reserved_system_2,
                                                                                         T_reserved_system_2))
print("Виграш системи з ненавантаженим загальним резервуванням по імовірності безвідмовної роботи = {}\n"
      "Виграш системи з ненавантаженим загальним резервуванням по імовірності відмови = {}\n"
      "Виграш системи з ненавантаженим загальним резервуванням по середньому часу роботи = {}\n".format(G_p_2, G_q_2,
                                                                                                        G_t_2))

from math import log10 as lg
from math import log as ln
from math import e, sinh, cosh, exp

#Дано:
T_п = 375
T_г = 0
T_0 = T_1 = 293
T_2 = 353
G_общ = 850
G_2 = 725
G_0 = 1000
G_1 = 100
G_шл = 76
G_з = 19
W_p = 0.05
M_H2O = 18
M_H2 = 2
M_N2 = 28
M_CO = 28
M_CO2 = 44
w_C_y_daf = 0.75
w_O2_y_daf = 0.2
w_H_y_daf = 0.04
w_N_y_daf = 0.01
w_O2 = 0.9824
w_N2 = 0.0176

#Решение:
for T_г in range(1673, 1990, 1):
    G_п = G_общ-G_2
    G_г = G_0+G_1+G_2+G_п-G_шл-G_з

    G_c = (G_0 * (1 - W_p) - G_шл - G_з) * w_C_y_daf
    G_O = (G_0 * (1 - W_p) - G_шл - G_з) * w_O2_y_daf + G_2 * w_O2 + ((16 * (G_0 * W_p + G_п)) / M_H2O)
    G_H = (G_0 * (1 - W_p) - G_шл - G_з) * w_H_y_daf + (2 * 1 * (G_0 * W_p + G_п)) / M_H2O
    G_N = (G_0 * (1 - W_p) - G_шл - G_з) * w_N_y_daf + G_2 * (1 - w_O2) + G_1
    
    #Задаёмся максимальной температурой в зоне газификации Tг=1973 K (из оптимального диапазона 1673 - 1973 K).

    lgK_p = round((2217.5/T_г)+0.297*lg(T_г)+0.3525*10**(-3)*T_г-0.0508*10**(-6)*(T_г**2)-3.26, 4)
    K_p = round(10**lgK_p, 5)
    
    a = (1-K_p)/M_CO2**2 
    #print (a)
    b = 1/M_CO2 * (G_H/(2*G_г)+G_c/(12*G_г)-G_O/(16*G_г)+(G_O*K_p)/(16*G_г))
    #print (b)
    c = K_p * (G_c/(12*G_г)-G_O/(16*G_г)) * G_c/(12*G_г)
    #print (c)
    D = (b**2)-4*a*c
    #print(D)
    w_CO2 = round((-b + (D**0.5)) / (2*a), 5) 
    #print(w_CO2)
    w_CO = round((M_CO*G_c)/(G_г*12) - (M_CO/M_CO2) * w_CO2, 4)
    w_H2O = round((M_H2O*G_O)/(G_г*16) - (M_H2O*G_c)/(G_г*12) - (M_H2O/M_CO2)*w_CO2, 4)
    w_H2 = round((2*G_H)/(2*G_г*1) - (2*G_O)/(G_г*16) + (2*G_c)/(G_г*12) + (2/M_CO2) * w_CO2, 4)
    w_N2 = round((M_N2*G_N)/(2*G_г*14), 4)
    #print(w_CO)
    #print(w_H2O)
    #print(w_H2)
    #print(w_N2)

    Cp1_T_1 = (29105 + 8614.9 * ((1701.6/293) / sinh(1701.6/293))**2 + 103.47 * ((909.79/293) / cosh(909.79/293))**2) / (G_0 * M_N2)
    #print(Cp1_T_1)
    Cp2_T_2 = round((33359 + 26798 * ((2609.3/T_п) / sinh(2609.3/T_п))**2 + 8888 * ((1167.6/T_п) / cosh(1167.6/T_п))**2) / (G_0 *M_H2O), 4)
    Cp3_T_2 = round((29103 + 10040 * ((2526.5/T_2) / sinh(2526.5/T_2))**2 + 9356 * ((1153.8/T_2) / cosh(1153.8/T_2))**2) / (G_0 * 32), 4)
    Cp4_T_2 = round((29105 + 8614.9 * ((1701.6/T_2) / sinh(1701.6/T_2))**2 + 103.47 * ((909.79/T_2) / cosh(909.79/T_2))**2) / (G_0 * M_N2), 4)
    Cp5_T_2 = round((29105 + 8614.9 * ((1701.6/T_г) / sinh(1701.6/T_г))**2 + 103.47 * ((909.79/T_г) / cosh(909.79/T_г))**2) / (G_0 * M_N2), 4)
    #print(Cp5_T_2)
    Cp6_T_2 = round((29108 + 8773 * ((3085.1/T_г) / sinh(3085.1/T_г))**2 + 8455.3 * ((1538.2/T_г) / cosh(1538.2/T_г))**2) / (G_0 * M_CO), 4)
    Cp7_T_2 = round((29370 + 34540 * ((-1428/T_г) / sinh(-1428/T_г))**2 + 8455.3 * ((588/T_г) / cosh(588/T_г))**2) / (G_0 * M_CO2), 4)
    Cp8_T_2 = round((27617 + 9560 * ((2466/T_г) / sinh(2466/T_г))**2 + 3760 * ((567.6/T_г) / cosh(567.6/T_г))**2) / (G_0 * 2), 4)
    Cp9_T_2 = round((33359 + 26798 * ((2609.3/T_г) / sinh(2609.3/T_г))**2 + 8888 * ((1167.6/T_г) / cosh(1167.6/T_г))**2) / (G_0 *M_H2O), 4)

    ΣСp_г = round(w_CO2 * Cp7_T_2 + w_CO * Cp6_T_2 + w_H2O * Cp9_T_2 + w_H2 * Cp8_T_2 + w_N2 * Cp5_T_2, 4)
    #print(ΣСp_г)
    Cp_шл_T_2 = round(0.276 + 0.001138 * (T_г - 273), 4)
    #print(Cp_шл_T_2)
    Cp_3 = 1.172
    Cp_2 = round(0.98*Cp3_T_2+0.02*1.2652, 4)
    #print(Cp_2)
    r_H2O_фп = round(((52053000 / M_H2O) * exp((0.3199 - 0.212 * (T_2 / 647.35) + 0.258 * ((T_2 / 647.35)**2)) * ln(1 - T_2 / 647.35)) / 1000), 4)
    #print(r_H2O_фп)
    Q_дисс_H2O = 241840
    Q_дисс_CO2 = 283100
    Q_в_p0 = 25422
    Q_p = round(G_0 * Q_в_p0  - ((M_H2O * r_H2O_фп) / 2) * (G_0 * (1 - W_p) - G_шл - G_з) * w_H_y_daf - (((G_г * w_H2) / 2) * Q_дисс_H2O + ((G_г * w_CO) / M_CO) * Q_дисс_CO2), 4)
    #print(Q_p)

    Cp0 = 1.6936
    left_side = round(G_0 * Cp0 * T_0 + G_1 * Cp1_T_1 * T_1 + G_2 * Cp3_T_2 * T_2 + G_п * Cp2_T_2 * T_п + Q_p, 4)
    #print(left_side)
    Q_п = 0
    Q_пот = 0
    right_side = round(G_г * ΣСp_г * T_г + G_шл * Cp_шл_T_2 * T_г + G_з * Cp_3 * T_г + G_0 * W_p *r_H2O_фп + Q_п + Q_пот, 4)
    #print(right_side)

    error_rate = round((abs(left_side-right_side)) / left_side * 100, 4)
    #print(error_rate)
    if error_rate < 1:
        break
print(f'Оптимальное значение T_г: {T_г} K, Погрешность расчетов составляет: {error_rate} %')

T_вх = round((G_0 * Cp0 * T_0 + G_1 * Cp1_T_1 * T_1 + G_2 * Cp3_T_2 * T_2 + G_п * Cp2_T_2 * T_п) / (G_0 * Cp0 + G_1 * Cp1_T_1 + G_2 * Cp3_T_2 + G_п * Cp2_T_2), 4)
print(T_вх)
T_вых = T_г
T_ср = round((T_вых - T_вх) / (ln(T_вых / T_вх)), 4)
error_rate_T_ср = round(abs(((T_ср - 900)) / 900) * 100, 4)
print (f"T_ср = {T_ср} K, Погрешность расчетов составляет {error_rate_T_ср}, %")
K = round(1/K_p,4)
K_nT = K / 1
print("Cтатистический вес процесса газификации равен:",K_nT)
print(f"T_п = {T_п} K, T_вых = {T_вых} K,G_2 = {G_2} Кг/ч, G_п = {G_п} Кг/ч, T_вх = {T_вх} K, K_nT = {K_nT}")
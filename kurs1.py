import Tochki as toch
import hs_diagram_helper as hs
import numpy as np
import matplotlib.pyplot as plt


MPa = 10 ** 6
kPa = 10 ** 3
MW = 10 ** 6
unit = 1 / MPa


a = toch.Parametry(N=400*MW,
                  P0=26 * MPa,
                  t0=555,
                  P_pp=3.5 * MPa,
                  t_pp=560,
                  t_pw=266,
                  Pk=3.4 * kPa,
                  internal_efficiency=0.85,
                  mechanical_efficiency=0.992,
                  generator_efficiency=0.99)
a.print_coeff()

G_golova, G_kond = a.get_mas_flow(a.get_input(0.84))
print("Расход в голову турбины равен = ", G_golova)
print("Расход в конденсатор равен = ", G_kond)


fig, ax = hs.plt.subplots(1, 1, figsize=(15, 15))
hs.plot_hs_diagram(
    ax,
    points=[a._point_0, a.point_0_true, a._point_1, a.point_1_true, a._point_pp, a.point_pp_true, a._point_k,
            a.point_k_true]
)
hs.plot_process(ax, points=[a._point_0, a.point_0_true, a.point_1_true], color='black')
hs.plot_process(ax, points=[a._point_pp, a.point_pp_true, a.point_k_true], color='black')
hs.plot_process(ax, points=[a._point_0, a._point_1], alpha=0.5, color='grey')
hs.plot_process(ax, points=[a._point_pp, a._point_k], alpha=0.5, color='grey')
plt.show()
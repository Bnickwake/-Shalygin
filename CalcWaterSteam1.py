from iapws import IAPWS97


class SteamCalc:
    def __init__(self, p=None, t=None, v=None, h=None, x=None, s=None, phase=None, *args, **kwargs):

        self.p = p
        self.t = t
        self.v = v
        self.h = h
        self.x = x
        self.s = s
        self.phase = phase

    def find_h(self):
        steam = IAPWS97(P=self.p, T=self.t, v=self.v, h=self.h, s=self.s, x=self.x, phase=self.phase)
        return steam.h

    def find_p(self):
        steam = IAPWS97(P=self.p, T=self.t, v=self.v, h=self.h, s=self.s, x=self.x, phase=self.phase)
        return steam.P

    def find_t(self):
        steam = IAPWS97(P=self.p, T=self.t, v=self.v, h=self.h, s=self.s, x=self.x, phase=self.phase)
        return steam.T

    def find_v(self):
        steam = IAPWS97(P=self.p, T=self.t, v=self.v, h=self.h, s=self.s, x=self.x, phase=self.phase)
        return steam.v

    def find_x(self):
        steam = IAPWS97(P=self.p, T=self.t, h=self.h, s=self.s, x=self.x, phase=self.phase)
        return steam.x

    def find_s(self):
        steam = IAPWS97(P=self.p, T=self.t, v=self.v, h=self.h, s=self.s, x=self.x, phase=self.phase)
        return steam.s

    def find_phase(self):
        steam = IAPWS97(P=self.p, T=self.t, h=self.h, s=self.s, x=self.x, phase=self.phase)
        return steam.phase

    def find_t_s_po_p(self):
        if self.p is not None:
            steam_s = IAPWS97(P=self.p, x=1)
            return steam_s.T
        else:
            raise KeyError("Введите давление")

    def find_h_s_po_p(self):
        if self.p is not None:
            steam_s = IAPWS97(P=self.p, x=1)
            return steam_s.h
        else:
            raise KeyError("Введите давление")

    def find_s_s_po_p(self):
        if self.p is not None:
            steam_s = IAPWS97(P=self.p, x=1)
            return steam_s.s
        else:
            raise KeyError("Введите давление")

    def find_h_s_po_t(self):
        if self.t is not None:
            steam_s = IAPWS97(T=self.t, x=1)
            return steam_s.h
        else:
            raise KeyError("Введите температуру")

    def find_p_s_po_t(self):
        if self.t is not None:
            steam_s = IAPWS97(T=self.t, x=1)
            return steam_s.P
        else:
            raise KeyError("Введите температуру")

    def find_s_s_po_t(self):
        if self.t is not None:
            steam_s = IAPWS97(T=self.t, x=1)
            return steam_s.s
        else:
            raise KeyError("Введите температуру")

    def calculation_isoentropic_process(self, p_1=None, t_1=None, h_1=None, s=None, p_2=None, t_2=None, h_2=None):
        start_point = IAPWS97(P=p_1, T=t_1, h=h_1, s=s)
        final_point = IAPWS97(P=p_2, T=t_2, h=h_2, s=start_point.s)

        t_2 = final_point.T
        p_2 = final_point.P
        v_2 = final_point.v

        return p_2, v_2, t_2

    def calculation_isothermal_process(self, p_1=None, t=None, h_1=None, s_1=None, p_2=None, s_2=None, h_2=None):
        start_point = IAPWS97(P=p_1, T=t, h=h_1, s=s_1)
        final_point = IAPWS97(P=p_2, T=start_point.T, h=h_2, s=s_2)

        t = final_point.T
        p_2 = final_point.P
        v_2 = final_point.v

        return p_2, v_2, t

    def calculation_isobaric_process(self, p=None, t_1=None, h_1=None, s_1=None, t_2=None, s_2=None, h_2=None):
        start_point = IAPWS97(P=p, T=t_1, h=h_1, s=s_1)
        final_point = IAPWS97(P=start_point.P, T=t_2, h=h_2, s=s_2)

        v_2 = final_point.v
        t_2 = final_point.T
        p = final_point.P

        return p, v_2, t_2

    def calculation_isochoric_process(self, p_1=None, t_1=None, h_1=None, s_1=None, p_2=None, t_2=None, s_2=None,
                                      h_2=None):
        start_point = IAPWS97(P=p_1, T=t_1, h=h_1, s=s_1)
        final_point = IAPWS97(P=p_2, T=t_2, h=h_2, s=s_2, v=start_point.v)

        v = final_point.v
        t_2 = final_point.T
        p = final_point.P

        return p_2, v, t_2
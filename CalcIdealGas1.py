class GasCalc:
    def __init__(self, p=None, t=None, v=None, h=None, c_v=None, gamma=None, c_p=None, r=None, *args, **kwargs):
        self.p = p
        self.t = t
        self.v = v
        self.h = h
        self.c_v = c_v
        self.gamma = gamma
        self.c_p = c_p
        self.r = r


    def calc_p(self, *args, **kwargs):
        count = 0
        if self.p is None:
            for value in [self.t, self.r, self.t]:
                if value is not None:
                    count += 1
            if count == 3:
                return self.r * self.t / self.v
            else:
                raise KeyError("Необходимы дополнительные параметры")
        return self.p

    def calc_t(self, *args, **kwargs):
        count = 0
        if self.t is None:
            for value in [self.p, self.v, self.r]:
                if value is not None:
                    count += 1
            if count == 2:
                return self.p * self.v / self.r
            else:
                raise KeyError("Необходимы дополнительные параметры")
        else:
            return self.t

    def calc_v(self, *args, **kwargs):
        count = 0
        if self.v is None:
            for value in [self.p, self.r, self.t]:
                if value is not None:
                    count += 1
            if count == 2:
                return self.r * self.t / self.p
            else:
                raise KeyError("Необходимы дополнительные параметры")
        else:
            return self.v

    def calc_h(self, *args, **kwargs):
        count = 0
        if self.h is None:
            for value in [self.c_p, self.t]:
                if value is not None:
                    count += 1
            if count == 2:
                return self.c_p * self.t
            else:
                raise KeyError("Необходимы дополнительные параметры")
        else:
            return self.h

    def calc_c_v(self, *args, **kwargs):
        count = 0
        if self.c_v is None:
            for value in [self.c_p, self.r]:
                if value is not None:
                    count += 1
            if count == 2:
                return self.c_p - self.r
            else:
                raise KeyError("Необходимы дополнительные параметры")
        else:
            return self.c_v

    def calc_gamma(self, *args, **kwargs):
        count = 0
        if self.gamma is None:
            for value in [self.c_p, self.r]:
                if value is not None:
                    count += 1
            if count == 2:
                return self.c_p / (self.c_p - self.r)
            else:
                raise KeyError("Необходимы дополнительные параметры")
        else:
            return self.gamma

    def calc_isothermal_process(self, v_1=None, p_1=None, v_2=None, p_2=None, *args, **kwargs):
        count = 0
        for value in [v_1, p_1, v_2, p_2]:
            if value is not None:
                count += 1
        if count > 2:
            t = p_1 * v_1 / self.r
            if v_2 is not None:
                p_2 = self.r * t / v_2
            else:
                v_2 = self.r * t / p_2
            return p_2, v_2, t
        else:
            raise KeyError("Необходимы дополнительные параметры")

    def calc_isobaric_process(self, v_1=None, t_1=None, v_2=None, t_2=None, *args, **kwargs):
        count = 0
        for value in [t_1, v_1, t_2, v_2]:
            if value is not None:
                count += 1
        if count > 2:
            p = self.r * t_1 / v_1
            if v_2 is not None:
                t_2 = p * v_2 / self.r
            else:
                v_2 = self.r * p / t_2
            return p, v_2, t_2
        else:
            raise KeyError("Необходимы дополнительные параметры")

    def calc_isochoric_process(self, t_1=None, p_1=None, t_2=None, p_2=None, *args, **kwargs):
        count = 0
        for value in [t_1, p_1, t_2, p_2]:
            if value is not None:
                count += 1
        if count > 2:
            v = self.r * t_1 / p_1
            if p_2 is not None:
                t_2 = p_2 * v / self.r
            else:
                p_2 = self.r * t_2 / v
            return p_2, v, t_2
        else:
            raise KeyError("Необходимы дополнительные параметры")

    def calc_isointropic_process_pv_(self, p_1=None, p_2=None, v_1=None, v_2=None, *args, **kwargs):
        count = 0
        gamma = self.c_p / (self.c_p - self.r)
        for value in [v_1, p_1, v_2, p_2]:
            if value is not None:
                count += 1
        if count > 2:
            if p_2 is not None:
                v_2 = ((p_1 * v_1 ** gamma) / p_2) ** (1 / gamma)
            else:
                p_2 = (p_1 * v_1 ** gamma) / (v_2 ** gamma)
            return p_2, v_2, gamma
        else:
            raise KeyError("Необходимы дополнительные параметры")

    def calc_isoinrtopic_process_tv_(self, t_1=None, t_2=None, v_1=None, v_2=None, *args, **kwargs):
        count = 0
        gamma = self.c_p / (self.c_p - self.r)
        for value in [v_1, t_1, v_2, t_2]:
            if value is not None:
                count += 1
        if count > 2:
            if t_2 is not None:
                v_2 = ((t_1 * v_1 ** (gamma - 1)) / t_2) ** (1 / (gamma - 1))
            else:
                t_2 = (t_1 * v_1 ** (gamma - 1)) / (v_2 ** (gamma - 1))
            return v_2, t_2, gamma
        else:
            raise KeyError("Необходимы дополнительные параметры")

    def opred_condition(self, p=None, v=None, t=None, *args, **kwargs):
        return "Gas"

    def calculation_x(self, p=None, v=None, t=None, *args, **kwargs):
        return 1




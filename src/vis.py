import src as fvs
import copy

class Vision():

    def __init__(self, rat, pxl, itr):
        self.rat = rat  # ratio
        self.pxl = pxl  # pixels
        self.itr = itr  # iterpolation
        self.chg = (self.pxl//2) * self.rat  # change
        self.frm = {'cur': None}  # frames
        self.mod = {}  # models
        self.fnc = []  # functions

    def __setitem__(self, key, val):
        self.frm[key] = val

    def __getitem__(self, key):
        return self.frm[key]

    def __iter__(self):
        return iter(self.frm.items())

    def function(self, pre, run):
        pre(self)
        self.fnc.append(run)

    def imread(self, img, fpt):
        h, w = img.shape[:2]

        crp = [[], []]
        crp[0] = [fpt[1] - self.chg, fpt[1] + self.chg]
        crp[1] = [fpt[0] - self.chg, fpt[0] + self.chg]

        if crp[1][0] <= 0:
            crp[1][0] = 0
        if crp[1][1] <= 1:
            crp[1][1] = 1

        if crp[1][0] >= w-1:
            crp[1][1] = w-1
        if crp[1][1] >= w:
            crp[1][1] = w

        if crp[0][0] <= 0:
            crp[0][0] = 0
        if crp[0][1] <= 1:
            crp[0][1] = 1

        if crp[0][0] >= h-1:
            crp[0][0] = h-1
        if crp[0][1] >= h:
            crp[0][1] = h

        tmp = img[crp[0][0]: crp[0][1], crp[1][0]: crp[1][1]]
        self.frm['cur'] = fvs.resize(tmp, (self.pxl, self.pxl), self.itr)

        msgs = [f(self, img, fpt) for f in self.fnc]

        for msg in msgs:
            if msg['key'] == 'face' and msg['offset'] != [0, 0]:
                return msg
            if msg['key'] == 'search' and msg['offset'] != [0, 0]:
                return msg

        return {'key': None, 'offset': None}

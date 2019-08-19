import cv2

class Device(cv2.VideoCapture):

    def __init__(self, src, *args, **kwargs):
        cv2.VideoCapture.__init__(self, src, *args, **kwargs)
        self.src = src  # source
        self.fpt = [0, 0]  # focal-point
        self.img = self.read()[1]  # image
        self.vis = {}  # visions

    def __setitem__(self, key, val):
        self.vis[key] = val

    def __getitem__(self, key):
        return self.vis[key]

    def __iter__(self):
        return iter(self.vis.items())

    def imread(self):
        ret, self.img = self.read()
        if ret:
            h, w = self.img.shape[:2]
            offset = [int((w//2) + self.fpt[0]), int((h//2) - self.fpt[1])]
            msgs = [v.imread(self.img, offset) for v in self.vis.values()]
            for msg in msgs:
                if msg['key'] == 'face':
                    self.fpt = [self.fpt[0] + msg['offset'][0], self.fpt[1] + msg['offset'][1]]
                    return ret, self.img, 1
            for msg in msgs:
                if msg['key'] == 'search' and msg['offset'] != [0, 0]:
                    self.fpt = [self.fpt[0] + msg['offset'][0], self.fpt[1] + msg['offset'][1]]
                    return ret, self.img, 0
        return ret, self.img, 0

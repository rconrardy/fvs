import cv2

def resize(frm, pxl, itr):
    if itr == "linear":
        frm = cv2.resize(frm, pxl, interpolation=cv2.INTER_LINEAR)
    elif itr == "nearest":
        frm = cv2.resize(frm, pxl, interpolation=cv2.INTER_NEAREST)
    elif itr == "area":
        frm = cv2.resize(frm, pxl, interpolation=cv2.INTER_AREA)
    elif itr == "cubic":
        frm = cv2.resize(frm, pxl, interpolation=cv2.INTER_CUBIC)
    elif itr == "lanczos":
        frm = cv2.resize(frm, pxl, interpolation=cv2.INTER_LANCZOS4)
    elif itr == "subsampling":
        frm = subsampling(frm, pxl)
    return frm

def subsampling(frm, pxl):
    h, w, c = frm.shape
    count = numpy.array([h / pxl[0], w / pxl[1]])
    ret_rows = numpy.array([0, count[0]])
    new_frm = numpy.zeros((pxl[0], pxl[1], 3), dtype=numpy.uint8)
    for row in range(pxl[0]):
        ret_cols = numpy.array([0, count[1]])
        for col in range(pxl[1]):
            x = numpy.random.randint(ret_cols[0], ret_cols[1])
            y = numpy.random.randint(ret_rows[0], ret_rows[1])
            ret_cols += count[1]
            new_frm[row, col] = frm[y, x, :]
        ret_rows += count[0]
    return new_frm

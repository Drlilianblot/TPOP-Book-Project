class Shape(object):
    ''' Docs for Shape

    '''

    def __init__(self, centre = None, orientation = 0):
        if centre is None:
            self._centre = Point(0,0)
        else:
            self._centre = centre

        self._orientation = orientation

    def get_centre(self):
        return self._centre

    def move_to(self, point):
        self._centre = point

    def rotate(self, centre = None, angle = 180):
        if centre is None:
            centre = self._centre

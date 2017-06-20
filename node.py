class Node:

    def __init__(self, color="white", passable=True, fscore=0, gscore=0, hscore=0, x=0, y=0, name=None, parent=None, neighbor=None):
        self._color = color
        self._passable = passable
        self._fscore = fscore
        self._gscore = gscore
        self._hscore = hscore
        self._x = x
        self._y = y
        self._name = name
        self._parent = parent
        if neighbor is None:
            self._neighbor = []
        else:
            self._neighbor = neighbor

    def clear_node():
        fscore = 0
        gscore = 0
        hscore = 0
        parent = None

################################
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
################################

    @property
    def passable(self):
        return self._passable

    @passable.setter
    def passable(self, value):
        self._passable = value
################################

    @property
    def fscore(self):
        return self._fscore

    @fscore.setter
    def fscore(self, value):
        self._fscore = value
################################

    @property
    def gscore(self):
        return self._gscore

    @gscore.setter
    def gscore(self, value):
        self._gscore = value
################################

    @property
    def hscore(self):
        return self._hscore

    @hscore.setter
    def hscore(self, value):
        self._hscore = value
################################

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
################################

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
################################

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
################################

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value
################################

    @property
    def neighbor(self):
        return self._neighbor

    @neighbor.setter
    def neighbor(self, value):
        self._neighbor.append(value)

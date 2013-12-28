
class Body:
    """Container class for 3d objects."""
    
    def p(self):
        """Returns the name of the type of body this is."""
        return 'Body'
    
    def get_color(self, point):
        """Returns color of body at given point."""
        pass
    
    def normal(self, point):
        """Returns normal vector of body at given point."""
        pass
    
    def reflectivity(self, point):
        """Returns percentage of brightness due to specular reflection."""
        pass
    
    def set_opacity(self, t = 1.0):
        """Sets percentage of light absorbed by body."""
        self._trans = t
        return self
    
    def opacity(self):
        """Returns body's transparency."""
        return self._trans
    
    def set_index(self, n = 1.0):
        """Sets body's index of refraction."""
        self._n = n
        return self
    
    def get_index(self):
        """Returns body's index of refraction."""
        return self._n
    
    def __init__(self):
        self.set_transparency()
        self.set_index()
    
    def intersection(self, ray):
        """Returns distance at which ray intersects body."""
        pass

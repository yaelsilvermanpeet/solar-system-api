from app import db

class Moon(db.Model):

    id = db.Column(
        db.Integer, 
        primary_key=True, 
        autoincrement=True)
    
    name = db.Column(
        db.String,
        nullable = False)
    
    description = db.Column(
        db.String,
        nullable = False) 
    
    size = db.Column(
        db.Numeric,
        nullable = False)
    
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"))
    planet = db.relationship("Planet", back_populates="moons")

    def to_dict(self):
        return dict(
            id = self.id,
            name = self.name,
            description = self.description,
            size = self.size
        )
    
    
    @classmethod
    def from_dict(cls, moon_data):
        return cls(
            name = moon_data["name"],
            description = moon_data["description"],
            size = moon_data["size"]
        )
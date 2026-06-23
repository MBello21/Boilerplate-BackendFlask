from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    freak: firstname[str] = mapped_column(String(120), nullable=False)
    
    def serialize(self): 
        return {
            "id": self.id,
            "firstname": self.firstname,
        }
        

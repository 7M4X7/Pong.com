from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the database
Base = declarative_base()
engine = create_engine("sqlite:///pingpong.db")
Session = sessionmaker(bind=engine)
session = Session()

# Define the Player table
class Player(Base):
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rating = Column(Integer, default=1000)

# Define the Match table
class Match(Base):
    __tablename__ = "matches"
    
    id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey("players.id"))
    player2_id = Column(Integer, ForeignKey("players.id"))
    winner_id = Column(Integer, ForeignKey("players.id"))
    played_at = Column(DateTime, default=func.now())

# Create tables
Base.metadata.create_all(engine)
print("Database and tables created successfully!")

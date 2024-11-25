from pydantic import BaseModel
from typing import List,Annotated,Optional
from database import engine, SessionLocal

class ChoiceBase(BaseModel):
    choice_text : str
    is_correct : bool
class QuestionBase(BaseModel):
    question_text : str
    choices : List[ChoiceBase]
class ChoiceUpdate(BaseModel):
    choice_text: Optional[str] = None
    is_correct: Optional[bool] = None
    
def get_db():
    db = SessionLocal()
    try: 
        yield db
    except Exception:
        db.rollback()
    finally:
        db.close()
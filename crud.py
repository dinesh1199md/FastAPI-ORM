from sqlalchemy.orm import Session
import models
from schema import QuestionBase,ChoiceUpdate

def get_all(db:Session,):
    try:
        return db.query(models.Choices).all()
    except Exception as e:
        print(f"Exception @get_all : {e}")

def get_question_by_id(question_id :int,db:Session):
     try:
        return db.query(models.Questions).filter(models.Questions.id  == question_id).first()
     except Exception as e:
        print(f"Exception @get_question_by_id : {e}")
  
def get_choice_by_id(question_id :int,db:Session):
     try:
        return db.query(models.Choices).filter(models.Choices.question_id == question_id).all()
     except Exception as e:
        print(f"Exception @get_choice_by_id : {e}")
        
def update_choices_by_id(question_id:int,str_choice : str,db: Session):
    try:
        result=db.query(models.Choices).filter(models.Choices.id == question_id).first()
        if result:
            result.choice_text=str_choice
            db.commit()
            db.refresh(result)
            return result
    except Exception as e:
        print(f"Exception @update_choices_by_id : {e}")

def add_question(question: QuestionBase,db: Session):
    try:
        db_question = models.Questions(question_text=question.question_text)
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        for choice in question.choices:
            db_choice = models.Choices(choice_text=choice.choice_text,is_correct=choice.is_correct
                                    ,question_id=db_question.id)
            db.add(db_choice)
        db.commit()    
        db.refresh(db_question)
    
        return db_question
    except Exception as e:
        print(f"Exception @add_question : {e}")
        
def patch_update_choices(choice_id:int,updates:ChoiceUpdate,db:Session):
    try:
        choice = db.query(models.Choices).filter(models.Choices.id == choice_id).first()
        
        if updates.choice_text:
            choice.choice_text = updates.choice_text
        if updates.is_correct:
            choice.is_correct = updates.is_correct
        db.commit()
        db.refresh(choice)
        return choice
    except Exception as e:
        print(f"Exception @patch_update_choices: {e}")
        
    
def delete_choices_by_id(question_id : int,db :Session):
    try:
        db.query(models.Choices).filter(models.Choices.question_id  == question_id).delete()
        result=db.query(models.Questions).filter(models.Questions.id  == question_id).first()
        if result:
            db.delete(result)
            db.commit()
            return {"Data Deleted":{question_id}}
    except Exception as e:
        print(f"Exception @delete_choices_by_id: {e}")
    
from fastapi import FastAPI, Depends, HTTPException,status
from pydantic import BaseModel
from typing import List,Annotated,Optional
import models 
from database import engine, SessionLocal
from sqlalchemy.orm import Session
# test
from schema import get_db,ChoiceUpdate,QuestionBase
from crud import get_all,get_question_by_id,get_choice_by_id,update_choices_by_id,add_question,patch_update_choices,delete_choices_by_id

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
        
db_dependency = Annotated[Session, Depends(get_db)]

#get all
@app.get("/get_all_choices",tags=["Get"])
async def get_choices(db :db_dependency):
    result=get_all(db)
    if not result:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Empty Table")
    return result 

#get with filter
@app.get("/questions/{question_id}",tags=["Get"])
async def get_question(question_id : int,db :db_dependency):
    result=get_question_by_id(question_id,db)
    if not result:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="question is not Found")
    return result

@app.get("/choices/{question_id}",tags=["Get"])
async def get_choices(question_id : int,db :db_dependency):
    result=get_choice_by_id(question_id,db)
    if not result:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="choice is not Found")
    return result  

#update
@app.put("/update_choices/{choise_id}",tags=["Put"])
async def update_choices(question_id : int,str_choice : str,db :db_dependency):
    result=update_choices_by_id(question_id,str_choice,db)
    if not result:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="choice is not Found")
    return result 
 
#create new entry
@app.post("/questions",tags=["Post"])
async def create_questions(question: QuestionBase,db: db_dependency):
    db_question =add_question(question,db)
    if not db_question:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Question is not Found")
    return f"message question  created successfully: {db_question.question_text}"
    
#patch 
@app.patch("/patch_choices/{choice_id}",tags=["Patch"])
async def update_choice(choice_id : int,updates : ChoiceUpdate,db :db_dependency):
    choice = patch_update_choices(choice_id,updates,db)
    if not choice:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Choice is not Found")
    return f"updated successfully: {choice.id}"
   
#delete
@app.delete("/delete_question/{question_id}",tags=["Delete"])
async def delete_choices(question_id : int,db :db_dependency):
    result=delete_choices_by_id(question_id,db)
    if not  result:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Choice is not Found")
    return f"updated successfully: {result}"
    
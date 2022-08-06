from multiprocessing import synchronize
from fastapi import FastAPI, Depends, APIRouter, Response, status, HTTPException
from sqlalchemy.orm import Session
from .. import database, schemas, models, oauth2

router = APIRouter(prefix="/vote", tags=["Vote"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post doesn't found")

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    vote_data = vote_query.first()

    if (vote.dir == 1):
        if vote_data:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="You were already voted this post")

        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Vote added succfully"}
    else:
        if not vote_data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="The requested post is not found")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Vote deleted successfully"}

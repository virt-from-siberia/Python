from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2


router = APIRouter(
    prefix='/vote',
    tags=['Votes']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(database.get_db),
         current_user=Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post not found")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id ==
                                              vote.post_id, models.Vote.user_id == current_user.id)

    found_vote = vote_query.first()

    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="User has already voted on this post")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()

        return {"message": "successfully added vote"}

    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Vote not found")

        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "successfully deleted vote"}

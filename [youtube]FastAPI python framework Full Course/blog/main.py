from fastapi import FastAPI, Depends, HTTPException, status, Response
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


models.Base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


@app.get('/blog')
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()

    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with {id} not found")

    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_200_OK)
def delete_blog(id: int,  db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with {id} not found")

    blog.delete(synchronize_session=False)
    db.commit()

    return {"details": f"blog with id {id} has been deleted"}


@app.put('/blog/{id}', status_code=status.HTTP_200_OK)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"blog with {id} not found")

    blog.update(request)
    db.commit()

    return blog


@app.post('/user')
def create_user(request: schemas.User,  db: Session = Depends(get_db)):
    print(request)
    new_user = models.User(
        firstname=request.firstname,
        lastname=request.lastname,
        email=request.email,
        password=request.password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

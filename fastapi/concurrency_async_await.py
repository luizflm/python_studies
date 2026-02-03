from fastapi import FastAPI
import httpx
import requests

app = FastAPI()


@app.get("/posts/async/{post}/comments")
async def get_post_comments(post: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jsonplaceholder.typicode.com/posts/{post}/comments")
        return response.json()


@app.get("/posts/sync/{post}/comments")
def get_post_comments(post: int):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post}/comments")
    return response.json()

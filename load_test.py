import asyncio
import aiohttp

# URL of your deployed Flask application
URL = "http://127.0.0.1:5000/predict"

# Path to the image you want to send
# Assuming the image is in the same directory as this script and has a .jpg extension
IMAGE_PATH = "tree-736885_1280.jpg"

async def send_request(session, url, image_path):
    with open(image_path, 'rb') as f:
        files = {'file': f}
        async with session.post(url, data=files) as response:
            return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, URL, IMAGE_PATH) for _ in range(1000)]  # Change 1000 to the desired number of requests
        results = await asyncio.gather(*tasks)
        for res in results:
            print(res)

if __name__ == "__main__":
    asyncio.run(main())

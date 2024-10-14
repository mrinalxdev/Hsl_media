import aiohttp
import asyncio

class HSLMediaPlayer:
    def __init__(self, url):
        self.url = url
        self.session = None

    async def fetch_manifest(self):
        if not self.session :
            self.session = aiohttp.ClientSession()
        
        async with self.session.get(self.url) as response:
            if response.status == 200:
                return await response.text()
            
            else : 
                raise Exception(f"Failed to fetch manifest : HTTP {response.status}")
        
    async def fetch_segment(self, segment_url):
        if not self.session:
            self.session = aiohttp.ClientSession()
        
        async with self.session.get(segment_url) as response:
            if response.status == 200:
                return await response.read()
            else :
                raise Exception(f"Failed to fetch segment : HTTP {response.status}")
    
    async def close(self):
        if self.session:
            await self.session.close()

async def main():
    player = HSLMediaPlayer("http://exampler.com/playlist.m3u8")
    try :
        manifest = await player.fetch_manifest
        print("Manifest : ", manifest)
    
    finally :
        await player.close()


if __name__ == "__main__":
    asyncio.run(main())
import unittest
from unittest.mock import patch, MagicMock
from src.player.hsl_client import HSLClient

class TestHSLClient(unittest.TestCase):
    def setUp(self):
        self.client = HSLClient("http://example.com/playlist.m3u8")

    @patch('aiohttp.ClientSession.get')
    async def test_fetch_manifest(self, mock_get):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.text.return_value = "#EXTM3U\n#EXT-X-VERSION:3\n"
        mock_get.return_value.__aenter__.return_value = mock_response

        manifest = await self.client.fetch_manifest()
        self.assertEqual(manifest, "#EXTM3U\n#EXT-X-VERSION:3\n")

    @patch('aiohttp.ClientSession.get')
    async def test_fetch_segment(self, mock_get):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b"segment data"
        mock_get.return_value.__aenter__.return_value = mock_response

        segment = await self.client.fetch_segment("http://example.com/segment1.ts")
        self.assertEqual(segment, b"segment data")

if __name__ == '__main__':
    unittest.main()
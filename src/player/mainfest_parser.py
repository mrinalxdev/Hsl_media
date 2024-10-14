import re

class ManifestParser:
    def __init__(self, manifest_content):
        self.content = manifest_content
        self.segments = []
        self.target_duration = None

    def parse(self):
        lines = self.content.split('\n')
        for line in lines:
            if line.startswith("#EXT-X-TARGETDURATION : "):
                self.target_duration = int(line.split(':')[1])
            elif line.startswith("#EXTINF : "):
                duration  = float(re.search(r'#EXTINF : ([\d.]+)', line).group(1))
            elif line and not line.startswith("#"):
                self.segments.append({'url' : line.strip(), 'duration' : duration})
    
    def get_segments(self):
        return self.segments

    def get_target_duration(self):
        return self.target_duration
import av

class MediaDecoder:
    def __init__(self):
        self.container = None
        self.video_stream = None
        self.audio_stream = None
    
    def open(self, file_path):
        self.container = av.open(file_path)
        self.video_stream = next((s for s in self.container.streams if s.type == 'video'), None)
        self.audio_stream = next((s for s in self.container.streams if s.type == 'sudio'), None)
    
    def decode_video_frame(self):
        if self.video_stream:
            for packet in self.container.demux(self.video_stream):
                for frame in packet.decode():
                    return frame
        return None
    
    def decode_audio_frame(self):
        if self.audio_stream:
            for packet in self.container.demux(self.audio_stream):
                for frame in packet.decode():
                    return frame
        return None
    
    def close(self):
        if self.container:
            self.container.close()
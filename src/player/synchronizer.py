import time

class Synchronizer:
    def __init__(self):
        self.start_time = None
        self.video_pts = 0
        self.audio_pts = 0

    def start(self):
        self.start_time = time.time()

    def should_play_video_frame(self, frame):
        if self.start_time is None:
            return False
        current_time = time.time() - self.start_time
        if frame.pts * frame.time_base > current_time:
            return False
        self.video_pts = frame.pts * frame.time_base
        return True

    def should_play_audio_frame(self, frame):
        if self.start_time is None:
            return False
        current_time = time.time() - self.start_time
        if frame.pts * frame.time_base > current_time:
            return False
        self.audio_pts = frame.pts * frame.time_base
        return True

    def get_current_position(self):
        return max(self.video_pts, self.audio_pts)
class Config:
    DEBUG = False
    BUFFER_SIZE = 10 
    MAX_RETRIES = 3   
    TIMEOUT = 10      

    @classmethod
    def from_file(cls, file_path):
        # TODO: Implement loading configuration from a file
        pass
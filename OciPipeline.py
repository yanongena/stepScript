prefix = "[OCI-PIPELINE] "
prefix_error = prefix + " [ERROR] "
prefix_status = prefix + " [STATUS] "
prefix_finished = prefix + " [FINISHED] "

class OciPipeline:
    def __init__(self):
        self.COMPLETED = 0
        self.WITH_ERROR = -1
        self.ABORTED = 1

    def start(self,message):
        print(prefix + message)

    def status(self,percentage):
        print(prefix_status + str(round(percentage)))

    def error(self,message):
        print(prefix_error + message)

    def finished(self,statusCode):
        print(prefix_finished + str(statusCode))
from MediatorBaseHandler import MediatorBaseHandler
from mediator.Mediator import Mediator


from MediatorBaseRequestModel import MediatorRequestModel

class TestRequest(MediatorRequestModel):
    email:str


@Mediator.handler("main")
class TestHandler(MediatorBaseHandler):

    def handle(req: TestRequest):
        print("main Çalıştı")
    


@Mediator.handler("fake")
class FakeHandler(MediatorBaseHandler):

    def handle(req: TestRequest):
        print("fake Çalıştı")


def endpoint(req:TestRequest):
    Mediator.handle("fake",req)
    
endpoint(TestRequest())
import inspect

from MediatorBaseRequestModel import MediatorRequestModel
from MediatorBaseHandler import MediatorBaseHandler




class Mediator:
    handlerMap = {}

    

    @staticmethod
    def registerHandler(containerName:str,reqModelType:type,handler:MediatorBaseHandler):
        Mediator.handlerMap[containerName] = Mediator.handlerMap[containerName] if containerName in Mediator.handlerMap else {}
        
        Mediator.handlerMap[containerName][reqModelType] = handler 


    @staticmethod
    def handle(containerName:str,req:MediatorRequestModel):
        Mediator.handlerMap.get(containerName).get(type(req)).handle(req)

    

    @staticmethod
    def handler(containerName:str):
        def decorator(handlercls):
            Mediator.registerHandler(containerName,inspect.signature(handlercls.handle).parameters.get(list(inspect.signature(handlercls.handle).parameters)[0]).annotation,handlercls)
        return decorator



    
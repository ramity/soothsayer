from flask import escape

class BaseRepository:
    model = None

    def __init__(self):
        self.model = None

    def find(self, id):
        return self.model.objects(id=id).first()

    def findBy(self, query):
        return self.model.objects(**query)

    def findOneBy(self, query):
        return self.model.objects(**query).first()

    def findAll(self):
        return self.model.objects()

    def insert(self, data):
        return self.model(**data).save()

    def update(self, id, updates):
        return self.model(id=id).update(**updates)

    def updateWhere(self, query, updates):
        return self.model(**query).update(**updates)

    def delete(self, id):
        return self.model(id=id).delete()

    def deleteWhere(self, query):
        return self.model(**query).delete()

    def handleRequest(self, request):
        response = {}
        json = request.get_json()
        response["model"] = self.populateModel(json)
        response["errors"] = self.populateErrors(response["model"])
        return response

    def populateModel(self, json):
        model = {}
        keys = self.model.getKeys()

        for key in keys:
            value = json[key] if key in json else None

            if value != None or value == (not False):
                model[key] = value

        return model

    def populateErrors(self, model):
        errors = {}
        requiredKeys = self.model.getRequiredKeys()

        for requiredKey in requiredKeys:
            if requiredKey not in model:
                errors[requiredKey] = []
                errors[requiredKey].append("{0} was not not found in the request and is a required key".format(requiredKey))
                # potentially add something in the future to validate data type of value being passed with type of attrib on model
                # errors[requiredKey].append("{0} type".format(type(getattr(self.model, requiredKey))))

        return errors

    def mergeUpdates(self, original={}, updates={}):
        for originalKey in original:
            if originalKey in updates:
                original[originalKey] = updates[originalKey]

        return original

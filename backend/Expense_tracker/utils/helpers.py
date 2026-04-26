from datetime import datetime

currentId = 0

def generateId():
    global currentId
    currentId += 1
    return currentId

def now():
  return datetime.now().isoformat()
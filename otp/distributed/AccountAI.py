from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class AccountAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("AccountAI")

class Order(object):

    # instance properties
    _orderItem = "None"
    _orderAmount = 0
    _orderFilled = -1

    # Constructor
    def __init__(self, argItem, argAmount):
        # print "Order:__init__"

        # set the order item
        if (isinstance(argItem, str)):
            if (len(argItem) > 0):
                self._orderItem = argItem

        # set the order amount
        if (argAmount > 0):
            self._orderAmount = argAmount

    # Magic methods
    def __repr__(self):
        # assemble the dictionary
        locOrder = {'item': self._orderItem, 'amount': self._orderAmount}
        return repr(locOrder)

    # Instance methods
    # attempt to fill the order
    def fill(self, argSrc):
        # print "Order:fill"

        try:
            # does the warehouse have the item in stock?
            if (argSrc is not None):
                if(argSrc.hasInventory(self._orderItem)):
                    # get the item
                    locCount = argSrc.getInventory(self._orderItem, self._orderAmount)

                    # update the following property
                    self._orderFilled = locCount
                else:
                    # print "Inventory item not available"
                    pass
            else:
                pass

        except TypeError:
            pass
            # print "Invalid warehouse"

    # check if the order has been filled
    def isFilled(self):
        # print "Order:isFilled_"
        return (self._orderAmount == self._orderFilled)


class Warehouse(object):
    # private properties
    _houseName = None
    _houseList = None

    # accessors
    def warehouseName(self):
        return (self._houseName)

    def inventory(self):
        return (self._houseList)

    #INVENTORY ACTIONS

    # set up the warehouse
    def setup(self, argName, argList):
        pass

    # check for an inventory item
    def hasInventory(self, argItem):
        pass

    # retrieve an inventory item
    def getInventory(self, argItem, argCount):
        pass

    # add an inventory item
    def addInventory(self, argItem, argCount):
        pass

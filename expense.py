class Category():
    def setCatId(self, catid):
        self.__catid = catid

    def setCatName(self, cname):
        self.__catname = cname

    def getCatId(self):
        return self.__catid

    def getCatName(self):
        return self.__catname


class Expense():
    def setAmount(self, amount):
        self.amount = amount

    def setRemark(self, remark):
        self.remark = remark

    def setDate(self, date):
        self.date = date

    def setCategoryId(self, cid):
        self.cid = cid

    def getAmount(self):
        return self.amount

    def getRemark(self):
        return self.remark

    def getDate(self):
        return self.date

    def getCategoryId(self):
        return self.cid

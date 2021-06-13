from expense import Category, Expense


class App():
    catList = []
    expList = []

    def startApp(self):
        while True:

            choice = self.printOptions()
            if choice == 1:
                self.addCategory()
            elif choice == 2:
                self.categoryListing()
            elif choice == 3:
                self.addExpense()
            elif choice == 4:
                self.reportCatWise()
            elif choice == 5:
                self.reportMonthWise()
            elif choice == 6:
                self.reportMonthRangeWise()
            elif choice == 7:
                self.amount()
            elif choice == 8:
                break

    def printOptions(self):
        print("1. Add Category")
        print("2. Category Listing")
        print("3. Expense Entry")
        print("4. Report: CategoryWise")
        print("5. Report: Month")
        print("6. Report: MonthRange")
        print("7. Report: Amount")
        print("8. Exit")
        ch = int(input("Enter your choice: "))
        return ch

    def addCategory(self):
        id = int(input("Enter Category ID: "))
        nm = input("Enter Category Name: ")

        c = Category()
        c.setCatId(id)
        c.setCatName(nm)

        App.catList.append(c)
        print("Category Added!")

    def categoryListing(self):
        print("================Available Categories================")
        for i in App.catList:
            print(i.getCatId(), i.getCatName())

    def addExpense(self):
        # amount, remark, date, cid
        self.categoryListing()
        catid = int(input("Select Category: "))

        amount = float(input("Enter Amount: "))
        remark = input("Enter Remark: ")
        date = input("Enter Date (dd/mm/yyyy): ")

        e = Expense()
        e.setAmount(amount)
        e.setRemark(remark)
        e.setDate(date)
        e.setCategoryId(catid)

        App.expList.append(e)
        print("Expenses Added!")

    def reportCatWise(self):
        self.categoryListing()
        cid = int(input("Select Category:"))

        for e in App.expList:
            if e.getCategoryId() == cid:
                print(e.getAmount(), e.getRemark(), e.getDate())

    def reportMonthWise(self):
        year = int(input("Enter Year: "))
        month = int(input("Enter Month: "))

        for i in App.expList:
            dt = i.getDate()  # "10/04/2021"
            dt2 = dt.split("/")  # ['10', '04', '2021']

            if year == int(dt2[2]) and month == int(dt2[1]):
                print(i.getAmount(), i.getRemark(), i.getDate())

    def reportMonthRangeWise(self):
        year = int(input("Enter year: "))
        smonth = int(input("Enter start month: "))
        emonth = int(input("Enter end month: "))

        for i in App.expList:
            dt1 = i.getDate()
            dt11 = dt1.split("/")

            if year == int(dt11[2]) and smonth <= int(dt11[1]) <= emonth:
                print(i.getAmount(), i.getRemark(), i.getDate())

    def amount(self):
        samount = int(input("Enter start limit: "))
        eamount = int(input("Enter end limit: "))

        for i in App.expList:
            dt1 = i.getAmount()

            if samount <= dt1 <= eamount:
                print(i.getAmount(), i.getRemark(), i.getDate())


App().startApp()

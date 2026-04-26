from utils.parser import parse_args

class ExpenseController:
    def __init__(self, service):
        self.service = service

    def handle(self, command, args):
        if command == "add":
            return self._add(args)

        elif command == "list":
            return self._list()

        elif command == "delete":
            return self._delete(args)

        elif command == "update":
            return self._update(args)

        elif command == "summary":
            return self._summary(args)

        else:
            return "Unknown command"


    def _add(self, args):
        data = parse_args(args)

        expense = self.service.add(
            data.get("description"),
            int(data.get("amount"))
        )

        return f"Expense added successfully (ID: {expense.id})"

    def _list(self):
        expenses = self.service.list()

        lines = ["ID  Date        Description  Amount"]

        for e in expenses:
            lines.append(f"{e.id}   {e.date}  {e.description}  ${e.amount}")

        return "\n".join(lines)

    def _delete(self, args):
        data = parse_args(args)

        self.service.delete(int(data.get("id")))

        return "Expense deleted successfully"

    def _update(self, args):
        data = parse_args(args)

        self.service.update(
            int(data.get("id")),
            data.get("description"),
            int(data["amount"]) if "amount" in data else None
        )

        return "Expense updated successfully"


    def _summary(self, args):
        data = parse_args(args)

        if "month" in data:
            total = self.service.get_month_total(int(data["month"]))
            return f"Total expenses for month {data['month']}: ${total}"
        else:
            total = self.service.get_total()
            return f"Total expenses: ${total}"
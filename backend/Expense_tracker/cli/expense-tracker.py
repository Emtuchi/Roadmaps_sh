#!/usr/bin/env python3

import sys
from repository.ExpenseRepo import ExpenseRepo
from services.ExpenseService import ExpenseService
from controllers.controller import ExpenseController
from factories.ExpenseFactory import ExpenseFactory

from utils import helpers

def main():
    if len(sys.argv) < 2:
        print("No command provided")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    # Dependency wiring (manual DI)
    repo = ExpenseRepo("data/expenses.json")
    factory = ExpenseFactory(helpers.generateId, helpers.now)
    service = ExpenseService(repo, factory, helpers)
    controller = ExpenseController(service)

    try:
        result = controller.handle(command, args)
        print(result)
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
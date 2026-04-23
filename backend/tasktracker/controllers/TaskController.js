class TaskController {
  constructor(service) {
    this.service = service;
  }

  handle(command, args) {
    try {
      switch (command) {
        case "add":
          return this.service.addTask(args.join(" "));

        case "update":
          return this.service.updateTask(
            args[0],
            args.slice(1).join(" ")
          );

        case "delete":
          return this.service.deleteTask(args[0]);

        case "mark-in-progress":
          return this.service.updateStatus(args[0], "in-progress");

        case "mark-done":
          return this.service.updateStatus(args[0], "done");

        case "list":
          return this.service.listTasks(args[0]);

        default:
          return "Unknown command";
      }
    } catch (err) {
      return err.message;
    }
  }
}

module.exports = TaskController;
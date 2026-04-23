class TaskService {
  constructor(repository, factory, helpers) {
    this.repository = repository;
    this.factory = factory;
    this.helpers = helpers;
  }

  addTask(description) {
    const tasks = this.repository.getAll();

    const task = this.factory.create(description);

    tasks.push(task);
    this.repository.saveAll(tasks);

    return `Task added successfully (ID: ${task.getId()})`;
  }

  updateTask(id, description) {
    const tasks = this.repository.getAll();
    const task = tasks.find(t => t.getId() === Number(id));

    if (!task) return "Task not found";

    task.updateDescription(description, this.helpers.now);

    this.repository.saveAll(tasks);
    return "Task updated";
  }

  deleteTask(id) {
    const task = this.repository.findById(id);
    if (!task) return "Task not found";

    this.repository.deleteById(id);
    return "Task deleted";
  }

  updateStatus(id, status) {
    const tasks = this.repository.getAll();
    const task = tasks.find(t => t.getId() === Number(id));

    if (!task) return "Task not found";

    task.updateStatus(status, this.helpers.now);

    this.repository.saveAll(tasks);
    return "Status updated";
  }

  listTasks(status = null) {
    let tasks = this.repository.getAll();

    if (status) {
      tasks = tasks.filter(t => t.getStatus() === status);
    }

    return tasks.map(t => t.toJSON());
  }
}

module.exports = TaskService;
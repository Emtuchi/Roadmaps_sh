const Task = require("../models/Task");

class TaskFactory {
  constructor(generateId, now) {
    this.generateId = generateId;
    this.now = now;
  }

  create(description) {
    if (!description) throw new Error("Description required");

    const id = this.generateId();
    const timestamp = this.now();

    return new Task(id, description, "todo", timestamp, timestamp);
  }
}

module.exports = TaskFactory;
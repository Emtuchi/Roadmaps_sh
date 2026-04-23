const { readFile, writeFile } = require("../utils/file");
const Task = require("../models/Task");

class TaskRepository {
  constructor(filePath) {
    this.filePath = filePath;
  }

  getAll() {
    const data = readFile(this.filePath);
    return data.map(Task.fromJSON);
  }

  saveAll(tasks) {
    writeFile(this.filePath, tasks.map(t => t.toJSON()));
  }

  findById(id) {
    return this.getAll().find(t => t.getId() === Number(id)) || null;
  }

  deleteById(id) {
    const tasks = this.getAll().filter(t => t.getId() !== Number(id));
    this.saveAll(tasks);
  }
}

module.exports = TaskRepository;
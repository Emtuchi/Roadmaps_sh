class CLI {
  constructor(controller) {
    this.controller = controller;
  }

  run() {
    const [, , command, ...args] = process.argv;

    const result = this.controller.handle(command, args);

    console.log(result);
  }
}

module.exports = CLI;
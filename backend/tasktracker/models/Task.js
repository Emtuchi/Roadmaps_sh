class Task {
    #id
    #status

    constructor (id, description, status, updatedAt, createdAt) {
        this.#id = id,
        this.#status = status,
        this.description = description,
        this.createdAt = createdAt,
        this.updatedAt = updatedAt
    }

    updateDesc(newDesccription, now) {
        if(!newDesccription) throw new Error("invalid desceription");
        
        this.description = newDesccription;
        this.updatedAt = now();
    }

    updatedStatus(newStatus, now) {
        const allowed = ["todo", "in-progress", "done"];

        if (!allowed.includes(newStatus)) {
            throw new Error("Invalid status");
        }

        this.#status = newStatus;
        this.updatedAt = now();
    }

    getId() {
        return this.#id;
    }

    getStatus() {
        return this.#status;
    }

    toJSON() {
       return {
         id: this.#id,
         description: this.description,
         status: this.#status,
         createdAt: this.createdAt,
         updatedAt: this.updatedAt,
       };
    }

    static fromJSON(json) {
        return new Task(
            json.id, 
            json.description, 
            json.status, 
            json.createdAt, 
            json.updatedAt
        );
    }
}

module.exports = Task;
class Building {
    constructor(sqft) {
        this.sqft = sqft;
    }

    // GETTER
    get sqft() {
        return this._sqft;
    }

    // SETTER
    set sqft(value) {
        if (typeof value !== "number") {
            throw new TypeError("sqft must be a number");
        }
        this._sqft = value;
    }

    // ABSTRACT METHOD SIMULÉE
    evacuationWarningMessage() {
        throw new Error("Class extending Building must override evacuationWarningMessage");
    }
}

export default Building;

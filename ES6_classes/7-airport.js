class Airport{
    constructor(name, code){
        this.name = name;
        this.code = code;
    }
        // GETTERS
    get code() {
        return this._code;
    }

    get name() {
        return this._name;
    }

    // SETTERS
    set code(value) {
        if (typeof value !== "string") {
            throw new TypeError("Code must be a string");
        }
        this._code = value;
    }

    set name(value) {
        if (typeof value !== "string") {
            throw new TypeError("Name must be a string");
        }
        this._name = value;
    }
    toString(){
    return this._code;
}
}
export default Airport;
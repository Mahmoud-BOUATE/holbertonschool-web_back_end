import Currency from "./3-currency.js";

export default class Pricing {
    constructor(amount, currency) {
        this.amount = amount;
        this.currency = currency;
    }

    // GETTERS
    get amount() {
        return this._amount;
    }

    get currency() {
        return this._currency;
    }

    // SETTERS
    set amount(value) {
        if (typeof value !== "number") {
            throw new TypeError("Amount must be a number");
        }
        this._amount = value;
    }

    set currency(value) {
        if (!(value instanceof Currency)) {
            throw new TypeError("Currency must be a Currency object");
        }
        this._currency = value;
    }

    // METHOD
    displayFullPrice() {
        return `${this._amount} ${this._currency.name} (${this._currency.code})`;
    }

    // STATIC METHOD
    static convertPrice(amount, conversionRate) {
        if (typeof amount !== "number" || typeof conversionRate !== "number") {
            throw new TypeError("Both arguments must be numbers");
        }
        return amount * conversionRate;
    }
}

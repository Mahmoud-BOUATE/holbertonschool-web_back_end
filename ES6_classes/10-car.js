class car{
    constructor(brand, motor, color){
        this._brand = brand;
        this._motor = motor;
        this._color = color;
    }
    get brand(){
        return this._brand
    }
    get motor(){
        return this._motor
    }
    get color(){
        return this._color
    }
    set brand(valeur){
        if (typeof valeur !== "string"){
            throw new TypeError("brand must be a string");
        }
        this._brand = valeur
    }
    set motor(valeur){
        if (typeof valeur !== "string"){
            throw new TypeError("motor must be a string");
        }
        this._motor = valeur
    }
    set color(valeur){
        if (typeof valeur !== "string"){
            throw new TypeError("color must be a string");
        }
        this._color = valeur
    }
    cloneCar(){
        return 
    }

}
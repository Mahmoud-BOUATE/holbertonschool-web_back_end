class Building{
    constructor(sqft){
        this.sqft = sqft;
    }
    get sqft(){
        return this._sqtf;
    }
    evacuationWarningMessage(){
        throw new Error("Class extending Building must override evacuationWarningMessage");
    }
}

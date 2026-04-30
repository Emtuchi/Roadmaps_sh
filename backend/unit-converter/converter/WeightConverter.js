import { conversionStrategy } from "./ConversionStrategy.js";

export class WeightConverter extends conversionStrategy {
    constructor () {
        super();
        this.units = {
            kg: 1,
            g: 0.001,
            lb: 0.453592,
        };
    }

    convert(value, from, to) {
        if (!this.units[from] || !this.units[to]) {
            throw new Error("invalid weight unit");
        }

        const base = value * this.units[from];
        return base / this.units[to];
    }
}
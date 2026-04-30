import { conversionStrategy } from "./ConversionStrategy.js";

export class LengthConverter extends conversionStrategy {
    constructor() {
        super();
        this.units = {
            m: 1,
            km: 1000,
            cm: 0.01,
            mm: 0.001,
        };
    }

    convert(value, from, to) {
        if (!this.units[from] || !this.units[to]) {
            throw new Error("invalid length unit");
        }

        const base = value * this.units[from];
        return base / this.units[to];
    }
}
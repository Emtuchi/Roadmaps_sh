import { conversionStrategy } from "./ConversionStrategy.js";

export class TemperatureConverter extends conversionStrategy {
  convert(value, from, to) {
    if (from === to) return value;

    let celsius;

    if (from === "C") celsius = value;
    else if (from === "F") celsius = (value - 32) * (5 / 9);
    else if (from === "K") celsius = value - 273.15;
    else throw new Error("Invalid temperature unit");

    if (to === "C") return celsius;
    if (to === "F") return (celsius * 9) / 5 + 32;
    if (to === "K") return celsius + 273.15;

    throw new Error("Invalid temperature unit");
  }
}
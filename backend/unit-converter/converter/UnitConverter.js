import { LengthConverter } from "./LengthConverter.js";
import { WeightConverter } from "./WeightConverter.js";
import { TemperatureConverter } from "./TemperatureConverter.js";

export class UnitConverter {
  constructor() {
    this.converters = {
      length: new LengthConverter(),
      weight: new WeightConverter(),
      temperature: new TemperatureConverter(),
    };
  }

  convert(type, value, from, to) {
    const converter = this.converters[type];

    if (!converter) {
      throw new Error("Invalid conversion type");
    }

    return converter.convert(value, from, to);
  }
}
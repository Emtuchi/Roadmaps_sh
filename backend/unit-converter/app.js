import { UnitConverter } from "./converter/UnitConverter.js";

const converter = new UnitConverter();

// DOM elements
const typeEl = document.getElementById("type");
const valueEl = document.getElementById("value");
const fromEl = document.getElementById("from");
const toEl = document.getElementById("to");
const resultEl = document.getElementById("result");
const btn = document.getElementById("convertBtn");

// Units for UI
const units = {
  length: ["m", "km", "cm", "mm"],
  weight: ["kg", "g", "lb"],
  temperature: ["C", "F", "K"],
};

// Populate dropdowns
function populateUnits(type) {
  fromEl.innerHTML = "";
  toEl.innerHTML = "";

  units[type].forEach(unit => {
    fromEl.add(new Option(unit, unit));
    toEl.add(new Option(unit, unit));
  });
}

// Initial load
populateUnits(typeEl.value);

// Change type
typeEl.addEventListener("change", () => {
  populateUnits(typeEl.value);
});

// Convert
btn.addEventListener("click", () => {
  const type = typeEl.value;
  const value = parseFloat(valueEl.value);
  const from = fromEl.value;
  const to = toEl.value;

  if (isNaN(value)) {
    resultEl.textContent = "Enter a valid number";
    return;
  }

  try {
    const result = converter.convert(type, value, from, to);
    resultEl.textContent = result;
  } catch (err) {
    resultEl.textContent = err.message;
  }
});
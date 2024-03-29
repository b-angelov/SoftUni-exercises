document.body.innerHTML = `
    <h1>Distance Converter</h1>
    <div>
        <label for="inputDistance">From:</label>
        <input type="text" id="inputDistance">
        <select id="inputUnits">
            <option value="km">Kilometers</option>
            <option value="m">Meters</option>
            <option value="cm">Centimeters</option>
            <option value="mm">Millimeters</option>
            <option value="mi">Miles</option>
            <option value="yrd">Yards</option>
            <option value="ft">Feet</option>
            <option value="in">Inches</option>
        </select>
        <input type="button" id="convert" value="Convert">
    </div>
    <div>
        <label for="outputDistance">To:</label>
        <input type="text" id="outputDistance" disabled="disabled">
        <select id="outputUnits">
            <option value="km">Kilometers</option>
            <option value="m">Meters</option>
            <option value="cm">Centimeters</option>
            <option value="mm">Millimeters</option>
            <option value="mi">Miles</option>
            <option value="yrd">Yards</option>
            <option value="ft">Feet</option>
            <option value="in">Inches</option>
        </select>
    </div>
`;

let names = ['Kilometers',
    'Meters',
    'Centimeters',
    'Millimeters',
    'Miles',
    'Yards',
    'Feet',
    'Inches'];

let rates = [
    1000,
    1,
    0.01,
    0.001,
    1609.34,
    0.9144,
    0.3048,
    0.0254
];

let input = 2;
let inputIndex = 0;

result();
let btn = $('#convert');
let output = $('#outputDistance');
document.getElementById('inputUnits').selectedIndex = inputIndex;
$('#inputDistance').val(input.toString());

for (let i = 0; i < 8; i++) {
    let expected = input * rates[inputIndex] / rates[i];
    checkConversion(i, expected);
}

function checkConversion(option, expected) {
    document.getElementById('outputUnits').selectedIndex = option;
    btn.trigger('click');
    let value = Number(output.val());
    while (value >= 10) {
        value /= 10;
    }
    while (expected >= 10) {
        expected /= 10;
    }
    expect(value).to.be.closeTo(expected, 0.002, "Error converting from " + names[inputIndex] + " to " + names[option]);
}
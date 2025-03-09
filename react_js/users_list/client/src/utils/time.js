import {capitalize} from "./strings.js";

function getDate(dateISOString) {
    if (!(dateISOString instanceof Date)){
        dateISOString = new Date(dateISOString)
    }
    const [month, day, year] = [
        dateISOString.toLocaleString("month", {month: "long"}),
        dateISOString.getDay(),
        dateISOString.getFullYear(),
    ]
    return `${capitalize(month)} ${day}, ${year}`
}

function fromDate(dateISOString) {

}

export {getDate}
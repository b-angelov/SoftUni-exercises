/*Creating function for task name: List of Names*/

function listOfNames(names) {
    names.sort((a,b) => a.localeCompare(b));
    names.forEach((name,idx) => console.log(`${idx + 1}.${name}`));
}

listOfNames(['df','fd','dsfds','sfsdf','fdsfsdfsdfs']);

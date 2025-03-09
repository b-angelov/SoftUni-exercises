
function clickButton(e,functionName,...args) {
    e.preventDefault()
    functionName(...args)
}

export {clickButton}
import {useContext, useEffect, useState} from "react";
import MainContext from "../contexts/MainContext.js";

export default function Pagination() {

    const {currentItem,setReload,setCurrentItem,itemsPerPage,setItemsPerPage,itemsCount,setItemsCount,currentPage,setCurrentPage,totalPages} = useContext(MainContext)
    const [activeButtons, setActiveButtons] = useState({
        previous: false,
        next: false,
        first: false,
        last: false,
    })

    const handleItemsChange = (e) => {
        setItemsPerPage(e.target.value)
        goToFirst()
        setReload(true)
    }

    useEffect(()=>{
        if(itemsCount > 0){
            // setItemsCount(itemsCount)
            // setTotalPages(Math.ceil(itemsCount / itemsPerPage))
            // setCurrentItem((currentPage - 1) * itemsPerPage)
            setActiveButtons({
                ...activeButtons,
                previous : currentPage !== 1,
                next : currentPage !== totalPages,
                first : currentPage !== 1,
                last : currentPage !== totalPages,
            })
        }
    },[itemsCount,itemsPerPage,currentPage,totalPages])



    const goToFirst = (e) =>{
        if(e){
            e.preventDefault()
        }
        if (currentPage > 1){
            setCurrentPage(1)
            setReload(true)
        }
    }



    const goToPrevious = (e) =>{
        e.preventDefault()
        if (currentPage > 1){
            setCurrentPage(currentPage-1)
            setReload(true)
        }
    }

    const goToNext = (e) =>{
        e.preventDefault()
        if (currentPage < totalPages){
            setCurrentPage(currentPage+1)
            setReload(true)
        }
    }

    const goToLast = (e) =>{
        e.preventDefault()
        if (currentPage < totalPages){
            setCurrentPage(totalPages)
            setReload(true)
        }
    }

    return (
        <>
            <div className="pagination position">
                <div className="limits">
                    <span>Items per page:</span>
                    <select name="limit" className="limit" value={itemsPerPage} onChange={handleItemsChange}>
                        <option value="5">5</option>
                        <option value="10">10</option>
                        <option value="15">15</option>
                        <option value="20">20</option>
                    </select>
                </div>
                <p className="pages">{currentItem + 1} - {((currentItem + parseInt(itemsPerPage)) < itemsCount)?(currentItem + parseInt(itemsPerPage)):itemsCount} of {itemsCount}</p>
                <div className="actions">
                    <button className="btn" title="First Page" disabled={!activeButtons.first} name={"first"} onClick={goToFirst}>
                        <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angles-left"
                             className="svg-inline--fa fa-angles-left" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                            <path fill="currentColor"
                                  d="M77.25 256l137.4-137.4c12.5-12.5 12.5-32.75 0-45.25s-32.75-12.5-45.25 0l-160 160c-12.5 12.5-12.5 32.75 0 45.25l160 160C175.6 444.9 183.8 448 192 448s16.38-3.125 22.62-9.375c12.5-12.5 12.5-32.75 0-45.25L77.25 256zM269.3 256l137.4-137.4c12.5-12.5 12.5-32.75 0-45.25s-32.75-12.5-45.25 0l-160 160c-12.5 12.5-12.5 32.75 0 45.25l160 160C367.6 444.9 375.8 448 384 448s16.38-3.125 22.62-9.375c12.5-12.5 12.5-32.75 0-45.25L269.3 256z">
                            </path>
                        </svg>
                    </button>

                    <button className="btn" title="Previous Page" disabled={!activeButtons.previous} name={"previous"} onClick={goToPrevious}>
                        <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angle-left"
                             className="svg-inline--fa fa-angle-left" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512">
                            <path fill="currentColor"
                                  d="M192 448c-8.188 0-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25l160-160c12.5-12.5 32.75-12.5 45.25 0s12.5 32.75 0 45.25L77.25 256l137.4 137.4c12.5 12.5 12.5 32.75 0 45.25C208.4 444.9 200.2 448 192 448z">
                            </path>
                        </svg>
                    </button>
                    <button className="btn" title="Next Page" disabled={!activeButtons.next} name={"next"} onClick={goToNext}>
                        <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angle-right"
                             className="svg-inline--fa fa-angle-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 512">
                            <path fill="currentColor"
                                  d="M64 448c-8.188 0-16.38-3.125-22.62-9.375c-12.5-12.5-12.5-32.75 0-45.25L178.8 256L41.38 118.6c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0l160 160c12.5 12.5 12.5 32.75 0 45.25l-160 160C80.38 444.9 72.19 448 64 448z">
                            </path>
                        </svg>
                    </button>

                    <button className="btn" title="Last Page" disabled={!activeButtons.last} name={"last"} onClick={goToLast}>
                        <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="angles-right"
                             className="svg-inline--fa fa-angles-right" role="img" xmlns="http://www.w3.org/2000/svg"
                             viewBox="0 0 448 512">
                            <path fill="currentColor"
                                  d="M246.6 233.4l-160-160c-12.5-12.5-32.75-12.5-45.25 0s-12.5 32.75 0 45.25L178.8 256l-137.4 137.4c-12.5 12.5-12.5 32.75 0 45.25C47.63 444.9 55.81 448 64 448s16.38-3.125 22.62-9.375l160-160C259.1 266.1 259.1 245.9 246.6 233.4zM438.6 233.4l-160-160c-12.5-12.5-32.75-12.5-45.25 0s-12.5 32.75 0 45.25L370.8 256l-137.4 137.4c-12.5 12.5-12.5 32.75 0 45.25C239.6 444.9 247.8 448 256 448s16.38-3.125 22.62-9.375l160-160C451.1 266.1 451.1 245.9 438.6 233.4z">
                            </path>
                        </svg>
                    </button>
                </div>
            </div>
        </>
    )
}
import NoContentOverlap from "./NoContentOverlap.jsx";
import NoUserOverlap from "./NoUserOverlap.jsx";
import OnErrorOverlap from "./OnErrorOverlap.jsx";
import TableRow from "./TableRow.jsx";
import {fetchItems} from "../API/fetch.js";
import {useContext, useEffect, useState} from "react";
import {getDate} from "../utils/time.js";
import mainContext from "../contexts/MainContext.js";
import {paginationFilter, sortFilter} from "../utils/filters.js";

export default function Table() {

    const [users, setUsers] = useState([])
    const [activeSort, setActiveSort] = useState({
        field: 'createdAt',
        order: 'asc'
    })

    const [isWaiting, setIsWaiting] = useState(false)
    const [failedToFetch, setFailedToFetch] = useState(false)
    const [noContent, setNoContent] = useState(false)
    const [noUsers, setNoUsers] = useState(false)
    const [arrowStyle, setArrowStyle] = useState("rotate(0deg)")

    const {
        reloadTrigger,
        setReload,
        activeSearchFilter,
        activeSortFilter,
        setActiveSortFilter,
        itemsPerPage,
        setCurrentItem,
        currentItem,
        setItemsCount,
        setCurrentPage,
        currentPage,
        setTotalPages,
        resetOrder,
        setResetOrder,
        searchCommitted,
        setSearchCommitted,
    } = useContext(mainContext)

    const sortClasses = {
        icon: "icon",
        active: "active-icon",
        svg: "svg-inline--fa",
        fa: "fa-arrow-down",
        table: "Table_icon__+HHgn",
    }

    let activeFields = {
        firstName: false,
        lastName: false,
        email: false,
        phoneNumber: false,
        createdAt: true,
    }

    const handleSorting = (name) => {
        setActiveSort({field: name, order: activeSort.order === 'asc' ? 'desc' : 'asc'})
        setArrowStyle(activeSort.order === 'asc' ? "rotate(0deg)" : "rotate(180deg)")
        Object.keys(activeFields).forEach((key) => {
            activeFields[key] = name === key
        })
        setActiveSortFilter(() => (input) => {
            return sortFilter(input, name, activeSort.order)
        })
        setCurrentPage(1)
        setReload(true)
    }

    const addClasses = (name) => {
        let classes = []
        if (activeSort.field === name) {
            classes.push(sortClasses.active)
        }
        classes.push(sortClasses.icon)
        classes.push(sortClasses.svg)
        classes.push(sortClasses.fa)
        classes.push(sortClasses.table)
        return classes.join(" ")
    }

    // useEffect(()=>{
    //
    // },[activeSort])

    useEffect(() => {
        setReload(false)
        setIsWaiting(true)
        setNoUsers(false)
        setNoContent(false)
            fetchItems("http://localhost:3030/jsonstore/users",()=>{setFailedToFetch(true); setReload(true); setIsWaiting(false)})
                .then(res => {
                    res = Object.values(res)
                    res = activeSearchFilter(res)
                    res = activeSortFilter(res)
                    res = paginationFilter(res, currentPage, itemsPerPage, setCurrentItem, setItemsCount, setTotalPages)
                    res = res.map((user) => {
                        /* user.createdAt = getDate(user.createdAt)*/
                        /* user.updatedAt = getDate(user.updatedAt)*/
                        user.setReload = setReload
                        return <TableRow key={user._id} {...user}/>
                    })
                    if (!res.length) {
                        if (searchCommitted) {
                            setNoContent(true)
                        } else {
                            setNoUsers(true)
                        }
                    }
                    setIsWaiting(false)
                    setSearchCommitted(false)
                    setUsers(res)
                })
    }, [reloadTrigger])

    useEffect(() => {
        if (resetOrder) {
            setActiveSort({field: 'createdAt', order: 'asc'})
            setActiveSortFilter(() => (input) => input)
            setResetOrder(false)
        }
    },[resetOrder])

    const loadingSpinnerOverlap = (
        <>
            <div className="loading-shade">
                {/*Loading spinner*/}
                <div className="spinner"></div>
            </div>
        </>
    )

    return (
        <>


            <div className="table-wrapper">
                {isWaiting && loadingSpinnerOverlap}
                {/*Overlap components*/}

                {/*<div className="loading-shade">*/}
                {/*Loading spinner*/}
                {/*<div className="spinner"></div>*/}

                {/*        No users added yet*/}

                {noUsers && (<div className="loading-shade"><NoUserOverlap/></div>)}
                {noContent && (<div className="loading-shade"><NoContentOverlap/></div>)}
                {failedToFetch && (<div className="loading-shade"><OnErrorOverlap/></div>)}
                {/*</div>*/}

                <table className="table">
                    <thead>
                    <tr>
                        <th>
                            Image
                        </th>
                        <th name="firstName" onClick={(e) => handleSorting('firstName')}>
                            First name
                            <svg aria-hidden="true" focusable="false" data-prefix="fas"
                                 data-icon="arrow-down" className={addClasses("firstName")}
                                 role="img"
                                 xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" style={{transform:arrowStyle}}>
                                <path fill="currentColor"
                                      d="M374.6 310.6l-160 160C208.4 476.9 200.2 480 192 480s-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 370.8V64c0-17.69 14.33-31.1 31.1-31.1S224 46.31 224 64v306.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0S387.1 298.1 374.6 310.6z">
                                </path>
                            </svg>
                        </th>
                        <th name="lastName" onClick={(e) => handleSorting('lastName')}>
                            Last name
                            <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-down"
                                 className={addClasses("lastName")} role="img"
                                 xmlns="http://www.w3.org/2000/svg"
                                 viewBox="0 0 384 512" style={{transform:arrowStyle}}>
                                <path fill="currentColor"
                                      d="M374.6 310.6l-160 160C208.4 476.9 200.2 480 192 480s-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 370.8V64c0-17.69 14.33-31.1 31.1-31.1S224 46.31 224 64v306.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0S387.1 298.1 374.6 310.6z">
                                </path>
                            </svg>
                        </th>
                        <th name="email" onClick={(e) => handleSorting('email')}>
                            Email
                            <svg aria-hidden="true" focusable="false" data-prefix="fas"
                                 data-icon="arrow-down"
                                 className={addClasses("email")} role="img"
                                 xmlns="http://www.w3.org/2000/svg"
                                 viewBox="0 0 384 512" style={{transform:arrowStyle}}>
                                <path fill="currentColor"
                                      d="M374.6 310.6l-160 160C208.4 476.9 200.2 480 192 480s-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 370.8V64c0-17.69 14.33-31.1 31.1-31.1S224 46.31 224 64v306.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0S387.1 298.1 374.6 310.6z">
                                </path>
                            </svg>
                        </th>
                        <th name="phoneNumber" onClick={(e) => handleSorting('phoneNumber')}>
                            Phone
                            <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-down"
                                 className={addClasses("phoneNumber")} role="img"
                                 xmlns="http://www.w3.org/2000/svg"
                                 viewBox="0 0 384 512" style={{transform:arrowStyle}}>
                                <path fill="currentColor"
                                      d="M374.6 310.6l-160 160C208.4 476.9 200.2 480 192 480s-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 370.8V64c0-17.69 14.33-31.1 31.1-31.1S224 46.31 224 64v306.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0S387.1 298.1 374.6 310.6z">
                                </path>
                            </svg>
                        </th>
                        <th name="createdAt" onClick={(e) => handleSorting('createdAt')}>
                            Created
                            <svg aria-hidden="true" focusable="false" data-prefix="fas"
                                 data-icon="arrow-down"
                                 className={addClasses("createdAt")} role="img"
                                 xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512" style={{transform:arrowStyle}}>
                                <path fill="currentColor"
                                      d="M374.6 310.6l-160 160C208.4 476.9 200.2 480 192 480s-16.38-3.125-22.62-9.375l-160-160c-12.5-12.5-12.5-32.75 0-45.25s32.75-12.5 45.25 0L160 370.8V64c0-17.69 14.33-31.1 31.1-31.1S224 46.31 224 64v306.8l105.4-105.4c12.5-12.5 32.75-12.5 45.25 0S387.1 298.1 374.6 310.6z">
                                </path>
                            </svg>
                        </th>
                        <th>Actions</th>
                    </tr>
                    </thead>
                    <tbody>
                    {/*Table row component*/}
                    {users}
                    </tbody>
                </table>


            </div>
        </>)
}
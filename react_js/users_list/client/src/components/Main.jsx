import Section from "./Section.jsx";
import UserDetails from "./UserDetails.jsx";
import CreateEditForm from "./CreateEditForm.jsx";
import DeleteUserComponent from "./DeleteUserComponent.jsx";
import MainContext from "../contexts/MainContext.js";
import {useState} from "react";

export default function Main() {

    const [activeMode, setActiveMode] = useState('')
    const [toggledDialog, setToggledDialog] = useState(false)
    const [reloadTrigger, setReload] = useState(false)
    const [activeSearchFilter, setActiveSearchFilter] = useState(() => input => input)
    const [activeSortFilter, setActiveSortFilter] = useState(() => input => input)
    const [currentItem, setCurrentItem] = useState(1)
    const [currentPage, setCurrentPage] = useState(1)
    const [itemsPerPage, setItemsPerPage] = useState(5)
    const [itemsCount, setItemsCount] = useState(1)
    const [totalPages, setTotalPages] = useState(1)
    const [resetOrder, setResetOrder] = useState(false)
    const [searchCommitted, setSearchCommitted] = useState(false)

    const sections = {
        section: (props) => <Section {...props}/>,
        userDetails: (props) => <UserDetails {...props}/>,
        createEditForm: (props) => <CreateEditForm {...props}/>,
        deleteUser: (props) => <DeleteUserComponent {...props}/>,
    }

    const toggleDialog = (dialogName, props = {}) => {
        if (toggledDialog) {
            setActiveMode('')
            setToggledDialog(false)
            return
        }
        setToggledDialog(true)
        setActiveMode(sections[dialogName](props))
    }

    return (
        <MainContext.Provider value={{
            toggleDialog,
            reloadTrigger,
            setReload,
            activeSearchFilter,
            setActiveSearchFilter,
            activeSortFilter,
            setActiveSortFilter,
            currentItem,
            setCurrentItem,
            itemsPerPage,
            setItemsPerPage,
            itemsCount,
            setItemsCount,
            currentPage,
            setCurrentPage,
            totalPages,
            setTotalPages,
            resetOrder,
            setResetOrder,
            searchCommitted,
            setSearchCommitted
        }}>
            <main className="main">
                <Section/>
                {activeMode}
            </main>
        </MainContext.Provider>
    )
}
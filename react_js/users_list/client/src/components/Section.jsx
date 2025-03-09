import SearchBar from "./SearchBar.jsx";
import Pagination from "./Pagination.jsx";
import Table from "./Table.jsx";
import {useContext} from "react";
import MainContext from "../contexts/MainContext.js";

export default function Section() {

    const {toggleDialog,setReload} = useContext(MainContext)

    function toggleAddUser(e){
        e.preventDefault()
        toggleDialog("createEditForm",{setReload})
    }

    return (
        <>
            <section className="card users-container">
                <SearchBar/>
                <Table/>


                {/*New user button*/}
                <button className="btn-add btn" onClick={toggleAddUser}>Add new user</button>

                <Pagination/>
            </section>
        </>
    )
}
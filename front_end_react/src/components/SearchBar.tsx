import { useState, useEffect } from "react"
import search_bar_icon from "../../public/search-outline-svgrepo-com.svg"


export const SearchBar = () => {

    const[search, setSearch] = useState("");

    return (<>
    
        <form action="/search" method="post" style={{"minWidth": "43vw"}}>
            <div className="input-group">
                <input
                type="search"
                className="form-control fs-5"
                placeholder="Search"
                aria-label="Search"
                style={{"borderTopLeftRadius": "100px", "borderBottomLeftRadius": "100px", "minHeight":"70px", "paddingLeft": "30px"}}
                />
                <button 
                type="submit" 
                style={{"background": "white", "borderTopRightRadius": "100px", "borderBottomRightRadius": "100px",
                     "color": "rgba(106, 106, 106, 1)", "borderColor": "rgb(222, 226, 230)", "borderLeft": "none", "paddingRight": "30px"}} 
                className="btn btn-primary fw-bold fs-5">
                    <img src={search_bar_icon} alt="magnifyer icon" style={{"width": "40px"}}/>
                </button>
            </div>
        </form>

    </>)
}
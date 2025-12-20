import { useState, useEffect } from "react"
import search_bar_icon from "../../public/search-outline-svgrepo-com.svg"


export const SearchBar = () => {

    const[searchString, setSearchString] = useState("");


    const submitSearch = async (e: React.FormEvent<HTMLFormElement>): Promise<void> => {
        e.preventDefault();
        const response = await fetch("http://127.0.0.1/search", {
            method: 'POST',
            body: JSON.stringify({
                'searchString': searchString 
            })
        })
        .then(response => { return response })
        .catch(err => console.log(err))

        console.log(response)
    }

    return (<>
    
        <form style={{"minWidth": "43vw"}} onSubmit={submitSearch} >
            <div className="input-group">
                <input
                type="search"
                className="form-control fs-5"
                placeholder="Search"
                aria-label="Search"
                style={{"borderTopLeftRadius": "100px", "borderBottomLeftRadius": "100px", "minHeight":"60px", "paddingLeft": "30px"}}
                onChange={e => setSearchString(e.target.value)}
                />
                <button 
                type="submit" 
                style={{"background": "white", "borderTopRightRadius": "100px", "borderBottomRightRadius": "100px",
                     "color": "rgba(106, 106, 106, 1)", "borderColor": "rgb(222, 226, 230)", "borderLeft": "none", "paddingRight": "30px"}} 
                className="btn btn-primary fw-bold fs-5">
                    <img src={search_bar_icon} alt="magnifyer icon" style={{"width": "45px"}}/>
                </button>
            </div>
        </form>

    </>)
}
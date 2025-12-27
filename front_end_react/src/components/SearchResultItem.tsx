import type { SearchResultType } from "../Interfaces"


export const SearchResultItem: React.FC<SearchResultType> = ({url, title, description}) => {
    return (
        <>
            <div className="card border-0 shadow-none main-container-object">
                <div className="card-body">
                    <div className="title-container">
                        <a href={url}
                        className="card-title" 
                        style={{"fontSize": "25px", "color": "rgb(74, 47, 156)"}}>
                            {title}
                        </a>
                    </div>
                    <div className="description-container">
                        <p className="card-text">
                            {description}
                        </p>
                    </div>
                </div>
            </div>
        </>
    )
}
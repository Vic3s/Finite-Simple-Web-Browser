import imageSearch from "../../public/image-search-svgrepo-com.svg"
import speachSearch from "../../public/microphone-alt-1-svgrepo-com.svg"

export const MoreSeacthOptions = () => {

    return (<>
        <div className="more-options-container d-flex flex-row align-items-center justify-content-center gap-3">
            <img style={{"width": "70px"}} src={imageSearch} alt="image search icon" />
            <img style={{"width": "70px"}} src={speachSearch} alt="speach to text search icon" />
        </div>
    </>)
}
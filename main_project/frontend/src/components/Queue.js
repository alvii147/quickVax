import React, { useEffect } from 'react'
import "./Queue.css"
import { MapContainer, TileLayer, Marker, useMap } from "react-leaflet";
import { SearchControl , OpenStreetMapProvider } from "leaflet-geosearch";
import '../../node_modules/leaflet-geosearch/dist/geosearch.css';
import girl from "../images/girl.svg";
const Search = (props) => {
    const map = useMap()
    const { provider } = props
    
    useEffect(() => {
        const searchControl = new SearchControl({
            style: 'bar',
            provider: provider,
        })

        map.addControl(searchControl)
        return () => map.removeControl(searchControl)
    },  [props])

    return null
}

export default function Queue() {

    return (
        <div id="queue-outer" className="outer-box-font">
            <h1>Join the Queue</h1>
            <div id="queue-inner">
                <h2 className="inner-box-font">FIND YOUR LOCATION</h2>
                <div id="inner-inner-box">
                    <MapContainer className="item map-container" center={[51.505, -0.09]} zoom={13} scrollWheelZoom={false}>
                        <TileLayer
                            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors' url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
                        <Search provider={new OpenStreetMapProvider()}>
                            {(info) => (
                                <Marker position={info?.latLng}>
                                </Marker>
                            )}
                        </Search>
                    </MapContainer>
                    <div></div>
                    <div id="item right-wrapper">
                        <img src={girl} alt="girl" />
                        <button>Continue</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

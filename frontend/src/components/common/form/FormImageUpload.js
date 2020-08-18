import React, { useState } from 'react'
import axios from 'axios'

const uploadUrl = process.env.REACT_APP_IMAGE_UPLOAD_URL
const uploadPreset = process.env.REACT_APP_IMAGE_UPLOAD_PRESET

function FormImageUpload({ label }) {
  const [image, setImage] = useState(null)

  const handleUpload = async event => {
    const data = new FormData()
    data.append('file', event.target.files[0])
    data.append('upload_preset', uploadPreset)
    const res = await axios.post(uploadUrl, data)
    setImage({
      image: res.data.url
    }, () => {
      this.props.onChange({ target: { name: this.props.name, value: this.state.image } })
    })
  }

  return (
    <div>
      {image ?
      
        <div>
          <img className="image is-64x64" src={image} alt="selected"/>
        </div>
          
        :
        <>
          <label className="label">{label}</label>
          <input
            className="input"
            type="file"
            onChange={handleUpload}
          />
        </>
      }
    </div>
  )
}

export default FormImageUpload
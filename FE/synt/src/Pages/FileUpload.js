import React from 'react'
import Header from '../components/Header/Header'
import NavBar from '../components/Navbar/Navbar'
import Upload from '../components/Upload/Upload'
import './fileUpload.css'

const FileUpload = () => {
  return (
    <div>
      <div class="main">
        <div class="top">
            <Header/>
        </div>
        <div class="content">
            <div class="navigation">
                <NavBar/>
            </div>
            <div class="upload-content">
                <Upload/>
            </div>

        </div>
      </div>
    </div>
  )
}

export default FileUpload

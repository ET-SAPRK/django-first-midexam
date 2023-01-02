import React, {useState, useEffect} from 'react'
import axios from 'axios'
import './fetch.css'

const Fetch = () => {
  const [data, setData] = useState([])

  const fetch =() => {
    axios.get("http://127.0.0.1:8000/core/student-list/")
    .then((res) => setData(res.data))
    .then(err => console.log(err))
  }
  useEffect(()=>{
    fetch();
  },[])
  return (
    <div>
      {data.map((res) => 
        <div className='cont'>
          Name: <input value={res.studentName}/>
          grade: <input value={res.grade}/>
        </div>
      )}
    </div>
  )
}

export default Fetch
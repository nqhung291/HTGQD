import axios from 'axios'

export function uploadInfo(data) {
  return axios({
    method: 'post',
    url: 'http://127.0.0.1:5000/upload',
    data
  })
}

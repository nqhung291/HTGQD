import axios from 'axios'

export function fetchUniverisy() {
  return axios({
    method: 'get',
    url: 'http://127.0.0.1:5000/university'
  })
}

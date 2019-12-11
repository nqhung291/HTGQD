import axios from 'axios'

export function fetchRank(data) {
  return axios({
    method: 'post',
    url: 'http://127.0.0.1:5000/ranking',
    data
  })
}

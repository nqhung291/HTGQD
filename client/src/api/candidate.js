import axios from 'axios'

export function fetchCandidateList(query) {
  return axios({
    method: 'get',
    url: 'http://127.0.0.1:5000/candidate',
    params: query
  })
}

export function updateCandidate(id, data) {
  return axios({
    method: 'put',
    url: `http://127.0.0.1:5000/candidate/${id}`,
    data
  })
}

export function createCandidate(data) {
  return axios({
    method: 'post',
    url: 'http://127.0.0.1:5000/candidate',
    data
  })
}

import request from '@/utils/request'

// post
export const postAction = (url, parameter) => {
  return request({
    url: url,
    method: 'post',
    data: parameter
  })
}

// post
export const postActionPa = (url, parameter) => {
  return request({
    url: url,
    method: 'post',
    params: parameter
  })
}

// post method= {post | put}
export const httpAction = (url, parameter, method) => {
  return request({
    url: url,
    method: method,
    data: parameter
  })
}

// put
export const putAction = (url, parameter) => {
  return request({
    url: url,
    method: 'put',
    data: parameter
  })
}

// put
export const putActionPa = (url, parameter) => {
  return request({
    url: url,
    method: 'put',
    params: parameter
  })
}

// get
export const getAction = (url, params) => {
  return request({
    url,
    method: 'get',
    params
  })
}
export const deleteAction = (url, params) => {
  return request({
    url,
    method: 'delete',
    data: params
  })
}

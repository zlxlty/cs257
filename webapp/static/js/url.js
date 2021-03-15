/*
 * @Author: Tianyi Lu
 * @Description: 
 * @Date: 2021-03-16 00:54:43
 * @LastEditors: Tianyi Lu
 * @LastEditTime: 2021-03-16 00:55:23
 */

export function getBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port
    return baseURL
}

export function getAPIBaseURL() {
    return getBaseURL() + '/api';
}

export function getStaticURL() {
    return getBaseURL() + '/static';
}

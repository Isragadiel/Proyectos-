import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
    http.get('https://jsonplaceholder.typicode.com/posts');
    sleep(1);
}
export const options = {
    stages: [
        { duration : '10s',target:5},//sube a 5 usuarios 
        {duration : '20s',target:10},//sube a 10 usuarios
        {duration:'10s',target:0},//baja a 0
    ],
    thresholds: {
        http_req_duration:['p(95)<200'],
        http_req_failed: ['rate<0.01'],

    }
};
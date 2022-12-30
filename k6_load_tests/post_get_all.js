import { check } from 'k6';
import http from 'k6/http';


export const options = {
  vus: 12,
  duration: '30s',
};

export default function() {
    const url = 'http://0.0.0.0:8000/api/posts/';

    const res = http.get(url);

    check(res, {
        'is status 200': (r) => r.status == 200,
    });
}
import { check } from 'k6';
import http from 'k6/http';


export const options = {
  vus: 12,
  duration: '30s',
};

http.setResponseCallback(
  http.expectedStatuses(201)
);

export default function() {
    const url = 'http://0.0.0.0:8000/api/post/';

    // Please, insert here a manually generated JWT token
    const token = '';

    const payload = JSON.stringify(
        {
            content: 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Morbi quis gravida ex. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed sed hendrerit mauris, ac ultrices nisi. Sed blandit ipsum sed mauris pellentesque blandit id sit amet dui. Interdum et malesuada fames ac ante ipsum primis in faucibus. Quisque fermentum posuere nibh, suscipit tempor ante ornare sit amet. Vivamus dictum dolor tempor mi semper sollicitudin. In fringilla tincidunt urna, nec feugiat magna commodo sed. Suspendisse convallis, tellus nec suscipit gravida, leo orci dignissim libero, non interdum odio metus at elit. Donec egestas suscipit varius. Praesent vitae tristique urna, sit amet pretium orci.',
        }
    );

    const params = {
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
        },
    };

    const res = http.post(url, payload, params);

    check(res, {
        'is status 201': (r) => r.status == 201,
    });
}
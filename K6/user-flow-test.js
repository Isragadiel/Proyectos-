import http from 'k6/http';
import { check, sleep } from 'k6';

/*
  CONFIGURACIÓN DE LA PRUEBA
  - stages: define cómo crece y disminuye la carga
  - thresholds: reglas que deben cumplirse o el test falla
*/
export const options = {
    stages: [
        { duration: '10s', target: 5 },   // Ramp-up: subir progresivamente hasta 5 usuarios
        { duration: '20s', target: 10 },  // Carga estable: mantener hasta 10 usuarios
        { duration: '10s', target: 0 },   // Ramp-down: bajar progresivamente a 0
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'], // 95% de las requests deben responder en menos de 500ms
        http_req_failed: ['rate<0.05'],   // Menos del 5% de las requests pueden fallar
    },
};

/*
  SETUP()
  Se ejecuta UNA sola vez antes de comenzar la prueba.
  Ideal para login y obtención de token.
*/
export function setup() {

    // Payload de autenticación
    const loginPayload = JSON.stringify({
        username: 'kminchelle',
        password: '0lelplR',
    });

    // Request POST para login
    const loginRes = http.post(
        'https://dummyjson.com/auth/login',
        loginPayload,
        {
            headers: { 'Content-Type': 'application/json' },
        }
    );

    // Validamos que el login sea exitoso
    check(loginRes, {
        'login status 200': (r) => r.status === 200,
    });

    // Extraemos el token del response JSON
    const token = loginRes.json('token');

    // Devolvemos el token para usarlo en el test principal
    return { token };
}

/*
  FUNCIÓN PRINCIPAL
  Se ejecuta por cada usuario virtual (VU).
  Recibe los datos retornados por setup().
*/
export default function (data) {

    /*
    Obtener listado de productos
    Se envía el token en el header Authorization
    */
    const productsRes = http.get(
        'https://dummyjson.com/products',
        {
            headers: {
                Authorization: `Bearer ${data.token}`,
            },
        }
    );

    check(productsRes, {
        'products status 200': (r) => r.status === 200,
    });

    sleep(1); // Simula tiempo de lectura del usuario


    /*
    Consultar detalle de un producto específico
    */
    const detailRes = http.get(
        'https://dummyjson.com/products/1'
    );

    check(detailRes, {
        'product detail status 200': (r) => r.status === 200,
    });

    sleep(1); // Simula tiempo entre acciones
}
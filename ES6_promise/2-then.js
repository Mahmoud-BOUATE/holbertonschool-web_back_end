export default function handleResponseFromAPI(promise) {
    return Promise.resolve(promise)
        .then(() => ({
            status: 200,
            body: 'Success',
        }))
        .then((response) => {
            console.log('Got a response from the API');
            return response;
        })
        .catch(() => new Error());
}

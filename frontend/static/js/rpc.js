/**
 * Ayudante simple de JSON-RPC que imita a web.rpc de Odoo.
 */
export async function rpc(url, params = {}) {
    const id = Math.round(Math.random() * 1000000);
    const body = {
        jsonrpc: "2.0",
        id: id,
        method: "call",
        params: params
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        });

        const data = await response.json();
        if (data.error) {
            throw new Error(data.error.message || 'Error de RPC');
        }
        return data.result;
    } catch (error) {
        console.error("RPC Fallido:", error);
        throw error;
    }
}

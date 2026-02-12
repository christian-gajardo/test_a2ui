/**
 * Clase de Componente Base ligera que imita al Owl Component de Odoo.
 * Maneja un estado reactivo básico (proxied) y renderizado manual para simplificar.
 */
export class Component {
    constructor(parent, props = {}) {
        this.parent = parent;
        this.props = props;
        this.state = this._makeReactive({});
        this.template = this.setup(); // setup() debe devolver la plantilla HTML
    }

    setup() {
        // Para ser sobrescrito por componentes
        return `<div>Componente Base</div>`;
    }

    _makeReactive(obj) {
        const component = this;
        return new Proxy(obj, {
            set(target, key, value) {
                target[key] = value;
                component.render(); // Re-renderizar al cambiar el estado
                return true;
            }
        });
    }

    render() {
        if (!this.parent) return;
        this.parent.innerHTML = this.setup();
        this.mounted();
    }

    mounted() {
        // Para ser sobrescrito para listeners de eventos, etc.
    }
}

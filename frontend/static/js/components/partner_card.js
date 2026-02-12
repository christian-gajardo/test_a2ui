import { Component } from '../component.js';

export class PartnerCard extends Component {
    setup() {
        const { partner } = this.props;
        return `
            <div style="border: 1px solid #ddd; padding: 10px; margin: 5px; border-radius: 4px;">
                <strong>${partner.name}</strong><br/>
                <small>${partner.email}</small>
            </div>
        `;
    }
}

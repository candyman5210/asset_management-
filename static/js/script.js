// Sample asset data
const assets = [
    {
        name: "Laptop",
        description: "High-performance laptop for work and gaming.",
        imageUrl: "https://via.placeholder.com/300x150"
    },
    {
        name: "Projector",
        description: "Portable projector for presentations.",
        imageUrl: "https://via.placeholder.com/300x150"
    },
    {
        name: "Camera",
        description: "DSLR camera for high-quality photos.",
        imageUrl: "https://via.placeholder.com/300x150"
    }
];

// Function to load assets into the dashboard
function loadAssets() {
    const assetContainer = document.getElementById('asset-container');
    const assetTemplate = document.getElementById('asset-template');

    assets.forEach(asset => {
        const assetCard = assetTemplate.cloneNode(true);
        assetCard.style.display = 'block';
        assetCard.querySelector('.asset-name').textContent = asset.name;
        assetCard.querySelector('.asset-description').textContent = asset.description;
        assetCard.querySelector('.asset-image').src = asset.imageUrl;
        
        assetContainer.appendChild(assetCard);
    });
}

// Initialize the dashboard
document.addEventListener('DOMContentLoaded', loadAssets);

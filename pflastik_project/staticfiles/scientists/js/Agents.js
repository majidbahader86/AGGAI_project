document.addEventListener('DOMContentLoaded', (event) => {
    const diseaseCards = document.querySelector('.disease-cards');
    
    // Add smooth scrolling with mouse wheel
    diseaseCards.addEventListener('wheel', (e) => {
        e.preventDefault();
        diseaseCards.scrollLeft += e.deltaY;
    });

    // Add touch scrolling for mobile devices
    let isDown = false;
    let startX;
    let scrollLeft;

    diseaseCards.addEventListener('mousedown', (e) => {
        isDown = true;
        startX = e.pageX - diseaseCards.offsetLeft;
        scrollLeft = diseaseCards.scrollLeft;
    });

    diseaseCards.addEventListener('mouseleave', () => {
        isDown = false;
    });

    diseaseCards.addEventListener('mouseup', () => {
        isDown = false;
    });

    diseaseCards.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - diseaseCards.offsetLeft;
        const walk = (x - startX) * 2;
        diseaseCards.scrollLeft = scrollLeft - walk;
    });
});
document.addEventListener('DOMContentLoaded', (event) => {
    // Add floating particles
    for (let i = 0; i < 50; i++) {
        let particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + 'vw';
        particle.style.animationDuration = (Math.random() * 3 + 2) + 's';
        particle.style.animationDelay = Math.random() * 2 + 's';
        document.body.appendChild(particle);
    }

    // Add diagnosis functionality
    const diagnoseBtn = document.getElementById('diagnose-btn');
    const fileInput = document.getElementById('plant-image');

    diagnoseBtn.addEventListener('click', () => {
        if (fileInput.files.length > 0) {
            // Simulate diagnosis
            setTimeout(() => {
                alert('Diagnosis complete! Your plant appears to have leaf spot disease. Recommended treatment: Apply a fungicide and improve air circulation around the plant.');
            }, 2000);
        } else {
            alert('Please upload an image first.');
        }
    });

    // Add a day-night cycle to the background
    function dayNightCycle() {
        const time = (Date.now() % 60000) / 60000; // 1 minute cycle
        const hue = Math.floor(time * 360);
        const lightness = 50 - Math.sin(time * Math.PI * 2) * 30;
        document.body.style.background = `radial-gradient(circle at center,
            hsl(${hue}, 70%, ${lightness + 20}%),
            hsl(${hue}, 70%, ${lightness}%),
            hsl(${hue}, 70%, ${lightness - 20}%))`;
        requestAnimationFrame(dayNightCycle);
    }
    dayNightCycle();
});
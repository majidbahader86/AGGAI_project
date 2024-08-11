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
    // for (let i = 0; i < 50; i++) {
    //     let particle = document.createElement('div');
    //     particle.className = 'particle';
    //     particle.style.left = Math.random() * 100 + 'vw';
    //     particle.style.animationDuration = (Math.random() * 3 + 2) + 's';
    //     particle.style.animationDelay = Math.random() * 2 + 's';
    //     document.body.appendChild(particle);
    // }

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

   

    // Simulate drone activities
    const activities = [
        "Drone 1 scanning Field A for pest activity",
        "Drone 2 monitoring irrigation levels in Field B",
        "Drone 3 collecting multispectral data from Field C",
        "Drone 4 inspecting crop health in Field D",
        "Drone 5 mapping Field E for precision agriculture",
        "Drone 6 assessing nitrogen levels in Field A",
        "Drone 7 detecting early signs of disease in Field B",
        "Drone 8 analyzing soil moisture content in Field C",
        "Drone 9 evaluating weed pressure in Field D",
        "Drone 10 monitoring crop growth stages in Field E",
        "Drone 11 conducting thermal imaging for stress detection in Field A",
        "Drone 12 assessing pollination efficiency in Field B"
    ];

    function addActivity() {
        const list = document.getElementById('drone-activity-list');
        const activity = activities[Math.floor(Math.random() * activities.length)];
        const li = document.createElement('li');
        li.textContent = activity;
        li.style.padding = '10px';
        li.style.borderBottom = '1px solid #ecf0f1';
        li.style.transition = 'background-color 0.3s ease';
        li.style.cursor = 'pointer';
        li.addEventListener('mouseover', () => {
            li.style.backgroundColor = '#f0f3f6';
        });
        li.addEventListener('mouseout', () => {
            li.style.backgroundColor = 'transparent';
        });
        list.insertBefore(li, list.firstChild);
        if (list.children.length > 5) {
            list.removeChild(list.lastChild);
        }
    }

    setInterval(addActivity, 5000);

    // Animate drone markers
    const droneMarkers = document.querySelectorAll('.drone-marker');
    droneMarkers.forEach(marker => {
        setInterval(() => {
            const newX = Math.random() * 780 + 10;
            const newY = Math.random() * 580 + 10;
            marker.setAttribute('cx', newX);
            marker.setAttribute('cy', newY);
        }, 10000);
    });
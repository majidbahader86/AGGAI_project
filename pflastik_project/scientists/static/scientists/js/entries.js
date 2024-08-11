document.addEventListener('DOMContentLoaded', function() {
    const openCardBtn = document.getElementById('openCardBtn');
    const magicCard = document.getElementById('magicCard');

    openCardBtn.addEventListener('click', function() {
        if (magicCard.classList.contains('hidden')) {
            magicCard.classList.remove('hidden');
            openCardBtn.textContent = 'Close Data Card';
            openCardBtn.classList.remove('pulse');
        } else {
            magicCard.classList.add('hidden');
            openCardBtn.textContent = 'Open Data Card';
            openCardBtn.classList.add('pulse');
        }
    });
});

function linkBitcoinToPlant() {
    const plantName = document.getElementById('plant-name').value;
    const bitcoinAddress = document.getElementById('bitcoin-address').value;

    if (!plantName || !bitcoinAddress) {
        alert('Please select a plant and enter a Bitcoin address.');
        return;
    }

    // Here we would typically send this data to a server
    // For now, we'll just display a success message
    const infoDiv = document.getElementById('bitcoin-plant-info');
    infoDiv.innerHTML = `our ${plantName} is now linked to Bitcoin address: ${bitcoinAddress}`;
    infoDiv.style.color = '#4CAF50';
    
    // Add a fun animation to celebrate the linking
    const card = document.getElementById('bitcoin-plant-card');
    card.style.animation = 'pulse 0.5s';
    setTimeout(() => {
        card.style.animation = '';
    }, 500);
}

// Add custom context menu
document.body.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    const ctxMenu = document.querySelector('.ctxmenu');
    if (ctxMenu) {
        ctxMenu.style.left = `${e.clientX}px`;
        ctxMenu.style.top = `${e.clientY}px`;
        ctxMenu.style.display = 'block';
    }
});

document.body.addEventListener('click', function() {
    const ctxMenu = document.querySelector('.ctxmenu');
    if (ctxMenu) {
        ctxMenu.style.display = 'none';
    }
});

function linkBitcoinToPlant() {
    const plantName = document.getElementById('plant-name').value;
    const bitcoinAddress = document.getElementById('bitcoin-address').value;
    if (plantName && bitcoinAddress) {
        document.getElementById('bitcoin-plant-info').innerHTML = `Your ${plantName} is now linked to Bitcoin address: ${bitcoinAddress}`;
        
        // Simulating transactions and balance updates
        updateTransactions();
        updateBalance();
    } else {
        alert('Please enter both plant name and Bitcoin address.');
    }
}

function updateTransactions() {
    const transactions = document.getElementById('transactions');
    const newTransactions = [
        'Received 0.001 BTC for plant care',
        'Spent 0.0005 BTC on fertilizer',
        'Received 0.002 BTC from plant sponsor'
    ];
    
    transactions.innerHTML = newTransactions.map(tx => `<li>${tx}</li>`).join('');
}

function updateBalance() {
    const balance = document.getElementById('current-balance');
    balance.textContent = '0.0025 BTC';
}

// Add event listeners to checkboxes
const checkboxes = document.querySelectorAll('#plant-checklist input[type="checkbox"]');
checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        if (this.checked) {
            alert(`Task completed: ${this.parentElement.textContent.trim()}`);
        }
    });
});
function submitForm(endpoint, formId) {
    const formData = new FormData(document.getElementById(formId));
    const data = Object.fromEntries(formData.entries());
    if (data.latitude) data.latitude = parseFloat(data.latitude);
    if (data.longitude) data.longitude = parseFloat(data.longitude);
    if (data.record_count) data.record_count = parseInt(data.record_count);
    if (data.environmental_conditions) data.environmental_conditions = JSON.parse(data.environmental_conditions || '{}');
    if (data.authors) data.authors = data.authors.split(',').map(author => author.trim());
    if (data.keywords) data.keywords = data.keywords.split(',').map(keyword => keyword.trim());
    if (data.fields) data.fields = data.fields.split(',').map(field => field.trim());

    fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert("Information submitted to the blockchain!");
        document.getElementById(formId).reset();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function submitDiseaseInfo() {
    submitForm("{% url 'submit_disease_info' %}", 'diseaseForm');
}

function submitPaperInfo() {
    submitForm("{% url 'submit_paper_info' %}", 'paperForm');
}

function submitDatasetInfo() {
    submitForm("{% url 'submit_dataset_info' %}", 'datasetForm');
}
console.log("Dataset Information:", datasetInfo);
// Here we would typically send this data to our blockchain or backend
alert("Dataset signed to the blockchain!");


// if ('WebSocket' in window) {
//     (function () {
//         function refreshCSS() {
//             var sheets = [].slice.call(document.getElementsByTagName("link"));
//             var head = document.getElementsByTagName("head")[0];
//             for (var i = 0; i < sheets.length; ++i) {
//                 var elem = sheets[i];
//                 var parent = elem.parentElement || head;
//                 parent.removeChild(elem);
//                 var rel = elem.rel;
//                 if (elem.href && typeof rel != "string" || rel.length == 0 || rel.toLowerCase() == "stylesheet") {
//                     var url = elem.href.replace(/(&|\?)_cacheOverride=\d+/, '');
//                     elem.href = url + (url.indexOf('?') >= 0 ? '&' : '?') + '_cacheOverride=' + (new Date().valueOf());
//                 }
//                 parent.appendChild(elem);
//             }
//         }
//         var protocol = window.location.protocol === 'http:' ? 'ws://' : 'wss://';
//         var address = protocol + window.location.host + window.location.pathname + '/ws';
//         var socket = new WebSocket(address);
//         socket.onmessage = function (msg) {
//             if (msg.data == 'reload') window.location.reload();
//             else if (msg.data == 'refreshcss') refreshCSS();
//         };
//         if (sessionStorage && !sessionStorage.getItem('IsThisFirstTime_Log_From_LiveServer')) {
//             console.log('Live reload enabled.');
//             sessionStorage.setItem('IsThisFirstTime_Log_From_LiveServer', true);
//         }
//     })();
// }
// else {
//     console.error('Upgrade your browser. This Browser is NOT supported WebSocket for Live-Reloading.');
// }

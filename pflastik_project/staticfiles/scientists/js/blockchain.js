   // Disease Chart
   const diseaseCtx = document.getElementById('diseaseChart').getContext('2d');
   new Chart(diseaseCtx, {
       type: 'bar',
       data: {
           labels: ['Fungal', 'Bacterial', 'Viral', 'Nematode', 'Parasitic Plants'],
           datasets: [{
               label: 'Number of Disease Records',
               data: [45000, 35000, 25000, 15000, 5000],
               backgroundColor: [
                   'rgba(255, 99, 132, 0.7)',
                   'rgba(54, 162, 235, 0.7)',
                   'rgba(255, 206, 86, 0.7)',
                   'rgba(75, 192, 192, 0.7)',
                   'rgba(153, 102, 255, 0.7)'
               ],
               borderColor: [
                   'rgba(255, 99, 132, 1)',
                   'rgba(54, 162, 235, 1)',
                   'rgba(255, 206, 86, 1)',
                   'rgba(75, 192, 192, 1)',
                   'rgba(153, 102, 255, 1)'
               ],
               borderWidth: 1
           }]
       },
       options: {
           responsive: true,
           maintainAspectRatio: false,
           plugins: {
               title: {
                   display: true,
                   text: 'Plant Disease Records by Type'
               }
           },
           scales: {
               y: {
                   beginAtZero: true
               }
           }
       }
   });

   // Paper Chart
   const paperCtx = document.getElementById('paperChart').getContext('2d');
   new Chart(paperCtx, {
       type: 'line',
       data: {
           labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
           datasets: [{
               label: 'Scientific Papers Published',
               data: [65, 59, 80, 81, 56, 55, 87],
               fill: false,
               borderColor: 'rgb(75, 192, 192)',
               tension: 0.1
           }]
       },
       options: {
           responsive: true,
           maintainAspectRatio: false,
           plugins: {
               title: {
                   display: true,
                   text: 'Scientific Paper Publications (Last 7 Months)'
               }
           }
       }
   });

   // Dataset Chart
   const datasetCtx = document.getElementById('datasetChart').getContext('2d');
   new Chart(datasetCtx, {
       type: 'pie',
       data: {
           labels: ['Genomic Data', 'Field Trials', 'Climate Data', 'Soil Analysis', 'Imaging Data'],
           datasets: [{
               label: 'Dataset Distribution',
               data: [4.7, 3.2, 2.8, 2.5, 2.5],
               backgroundColor: [
                   'rgba(255, 99, 132, 0.7)',
                   'rgba(54, 162, 235, 0.7)',
                   'rgba(255, 206, 86, 0.7)',
                   'rgba(75, 192, 192, 0.7)',
                   'rgba(153, 102, 255, 0.7)'
               ],
               hoverOffset: 4
           }]
       },
       options: {
           responsive: true,
           maintainAspectRatio: false,
           plugins: {
               title: {
                   display: true,
                   text: 'Dataset Distribution by Type (in TB)'
               }
           }
       }
   });

   // New Chart (Radar Chart)
   const newChartCtx = document.getElementById('newChart').getContext('2d');
   new Chart(newChartCtx, {
       type: 'radar',
       data: {
           labels: ['Yield', 'Disease Resistance', 'Drought Tolerance', 'Nutrient Efficiency', 'Growth Rate'],
           datasets: [{
               label: 'Variety A',
               data: [80, 90, 70, 85, 75],
               fill: true,
               backgroundColor: 'rgba(255, 99, 132, 0.2)',
               borderColor: 'rgb(255, 99, 132)',
               pointBackgroundColor: 'rgb(255, 99, 132)',
               pointBorderColor: '#fff',
               pointHoverBackgroundColor: '#fff',
               pointHoverBorderColor: 'rgb(255, 99, 132)'
           }, {
               label: 'Variety B',
               data: [70, 85, 80, 75, 90],
               fill: true,
               backgroundColor: 'rgba(54, 162, 235, 0.2)',
               borderColor: 'rgb(54, 162, 235)',
               pointBackgroundColor: 'rgb(54, 162, 235)',
               pointBorderColor: '#fff',
               pointHoverBackgroundColor: '#fff',
               pointHoverBorderColor: 'rgb(54, 162, 235)'
           }]
       },
       options: {
           responsive: true,
           maintainAspectRatio: false,
           plugins: {
               title: {
                   display: true,
                   text: 'Plant Variety Comparison'
               }
           },
           scales: {
               r: {
                   angleLines: {
                       display: false
                   },
                   suggestedMin: 0,
                   suggestedMax: 100
               }
           }
       }
   });
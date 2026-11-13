let monthlyChart, reportCategoryChart;

const month = new Date().toISOString().slice(0, 7);

document.getElementById('reportMonth').value = month;


// Load Reports
async function loadReports() {

    try {
        const selectedMonth =
            document.getElementById('reportMonth').value;

        const category =
            document.getElementById('reportCategory').value;

        const d = await api(
            `/reports?month=${encodeURIComponent(selectedMonth)}&category=${encodeURIComponent(category)}`
        );


        // Monthly Expense Overview
        if (monthlyChart) {
            monthlyChart.destroy();
        }

        monthlyChart = new Chart(
            document.getElementById('monthlyChart'),
            {
                type: 'bar',

                data: {
                    labels: d.monthly.labels,

                    datasets: [{
                        label: 'Monthly Expenses',
                        data: d.monthly.values,
                        backgroundColor: '#1268f3',
                        borderRadius: 6,
                        maxBarThickness: 55
                    }]
                },

                options: {
                    responsive: true,
                    maintainAspectRatio: false,

                    plugins: {
                        legend: {
                            display: false
                        },

                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return 'Expenses: ₹' +
                                        Number(context.raw).toLocaleString('en-IN');
                                }
                            }
                        }
                    },

                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            }
        );


        // Category Doughnut Chart
        if (reportCategoryChart) {
            reportCategoryChart.destroy();
        }

        const labels = d.categories.map(x => x.category);
        const values = d.categories.map(x => Number(x.total));

        const colors = d.categories.map((x, i) =>
            `hsl(${i * 65}, 70%, 55%)`
        );

        reportCategoryChart = new Chart(
            document.getElementById('reportCategoryChart'),
            {
                type: 'doughnut',

                data: {
                    labels: labels,

                    datasets: [{
                        data: values,
                        backgroundColor: colors,
                        borderColor: '#ffffff',
                        borderWidth: 2,
                        hoverOffset: 5
                    }]
                },

                options: {
                    responsive: true,

                    plugins: {
                        legend: {
                            display: true,
                            position: 'bottom'
                        }
                    },

                    cutout: '60%'
                }
            }
        );

    } catch (error) {
        console.error('Reports loading error:', error);
    }
}


// Month Filter
document.getElementById('reportMonth').onchange = loadReports;


// Category Filter
document.getElementById('reportCategory').onchange = loadReports;


// Initial Load
loadReports();
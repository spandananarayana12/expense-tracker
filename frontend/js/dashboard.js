let categoryChart;

// Load Dashboard Data
async function loadDashboard() {
    try {
        const d = await api('/dashboard');

        document.getElementById('balance').textContent =
            money(d.summary.balance);

        document.getElementById('income').textContent =
            money(d.summary.income);

        document.getElementById('expenses').textContent =
            money(d.summary.expenses);

        document.getElementById('userName').textContent =
            d.user.name.split(' ')[0];
        // Display selected profile avatar
const savedUser = JSON.parse(
    localStorage.getItem('expense_user') || '{}'
);

const avatar = d.user.avatar || savedUser.avatar || 'girl';

const profileAvatar = document.getElementById('profileAvatar');

if (profileAvatar) {
    profileAvatar.src = avatar === 'boy'
        ? 'assets/images/boy-avatar.png'
        : 'assets/images/girl-avatar.png';
}
        renderCategory(d.categories);
        renderRecent(d.recent);

    } catch (e) {
        console.error('Dashboard loading error:', e);
    }
}


// Display Expenses by Category
function renderCategory(items) {

    const labels = items.map(x => x.category);
    const values = items.map(x => Number(x.total));

    // Generate one color for each category
    const colors = items.map((x, i) =>
        `hsl(${i * 65}, 70%, 55%)`
    );

    // Display Category Legend
    document.getElementById('categoryLegend').innerHTML =
        items.map((x, i) => `
            <span>
                <i class="dot" style="background:${colors[i]}"></i>
                ${x.category}
                <b>${x.percent}%</b>
            </span>
        `).join('');


    // Destroy Previous Chart
    if (categoryChart) {
        categoryChart.destroy();
    }


    // Create Doughnut Chart
    categoryChart = new Chart(
        document.getElementById('categoryChart'),
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
                maintainAspectRatio: true,

                plugins: {
                    legend: {
                        display: false
                    }
                },

                cutout: '62%'
            }
        }
    );
}


// Display Recent Transactions
function renderRecent(items) {

    const box = document.getElementById('recentTransactions');

    box.innerHTML = items.length
        ? items.map(t => `
            <div class="transaction-row">

                <div>
                    <b>${t.category}</b>
                    <small>
                        ${t.date} · ${t.description || t.type}
                    </small>
                </div>

                <span class="amount ${t.type}">
                    ${t.type === 'income' ? '+' : '-'}${money(t.amount)}
                </span>

                <small>${t.type}</small>

            </div>
        `).join('')

        : '<p class="muted">No transactions yet.</p>';
}


// Initialize Dashboard
loadDashboard();
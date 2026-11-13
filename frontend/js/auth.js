const registerForm = document.getElementById('registerForm');
const loginForm = document.getElementById('loginForm');

// Registration
if (registerForm) {
    registerForm.addEventListener('submit', async e => {
        e.preventDefault();

        const m = document.getElementById('authMessage');

        const selectedAvatar = document.querySelector(
            'input[name="avatar"]:checked'
        );

        if (!selectedAvatar) {
            setMessage(m, 'Please select a profile avatar.', 'error');
            return;
        }

        try {
            const data = await api('/auth/register', {
                method: 'POST',
                body: JSON.stringify({
                    name: document.getElementById('name').value,
                    email: document.getElementById('email').value,
                    password: document.getElementById('password').value,
                    avatar: selectedAvatar.value
                })
            });

            localStorage.setItem(
                'expense_user',
                JSON.stringify(data.user)
            );

            location.href = 'dashboard.html';

        } catch (err) {
            setMessage(m, err.message, 'error');
        }
    });
}


// Login
if (loginForm) {
    loginForm.addEventListener('submit', async e => {
        e.preventDefault();

        const m = document.getElementById('authMessage');

        try {
            const data = await api('/auth/login', {
                method: 'POST',
                body: JSON.stringify({
                    email: document.getElementById('email').value,
                    password: document.getElementById('password').value
                })
            });

            localStorage.setItem(
                'expense_user',
                JSON.stringify(data.user)
            );

            location.href = 'dashboard.html';

        } catch (err) {
            setMessage(m, err.message, 'error');
        }
    });
}


// Forgot Password
const forgot = document.getElementById('forgot');

if (forgot) {
    forgot.onclick = e => {
        e.preventDefault();
        alert('Please contact support to reset your password.');
    };
}
let employees = [];
let editingEmployeeId = null;

function fetchEmployees() {
    fetch('/employees/')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Received data:", data);
            if (Array.isArray(data)) {
                employees = data;
                renderEmployeeList();
            } else {
                console.error("Received data is not an array:", data);
            }
        })
        .catch(error => {
            console.error("Error fetching employees:", error);
        });
}

function renderEmployeeList() {
    const employeeList = document.getElementById('employee-list');
    if (Array.isArray(employees) && employees.length > 0) {
        employeeList.innerHTML = `
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    ${employees.map(employee => `
                        <tr>
                            <td>${employee.name}</td>
                            <td>${employee.email}</td>
                            <td>${employee.phone}</td>
                            <td>
                                <div class="actions">
                                    <button class="edit-btn" onclick="editEmployee(${employee.id})">Edit</button>
                                    <button class="delete-btn" onclick="deleteEmployee(${employee.id})">Delete</button>
                                </div>
                            </td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;
    } else {
        employeeList.innerHTML = '<p>No employees found.</p>';
    }
}

function submitForm(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const employee = Object.fromEntries(formData.entries());

    const url = editingEmployeeId ? `/employees/${editingEmployeeId}` : '/employees/';
    const method = editingEmployeeId ? 'PUT' : 'POST';

    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(employee),
    })
    .then(response => response.json())
    .then(data => {
        if (editingEmployeeId) {
            const index = employees.findIndex(emp => emp.id === editingEmployeeId);
            employees[index] = data;
        } else {
            employees.push(data);
        }
        renderEmployeeList();
        form.reset();
        resetForm();
    });
}

function editEmployee(id) {
    const employee = employees.find(emp => emp.id === id);
    if (employee) {
        document.getElementById('name').value = employee.name;
        document.getElementById('email').value = employee.email;
        document.getElementById('phone').value = employee.phone;
        document.getElementById('form-title').textContent = 'Edit Employee';
        document.getElementById('submit-btn').textContent = 'Update Employee';
        document.getElementById('cancel-btn').style.display = 'block';
        editingEmployeeId = id;
    }
}

function deleteEmployee(id) {
    if (confirm('Are you sure you want to delete this employee?')) {
        fetch(`/employees/${id}`, { method: 'DELETE' })
            .then(() => {
                employees = employees.filter(emp => emp.id !== id);
                renderEmployeeList();
            });
    }
}

function resetForm() {
    document.getElementById('employee-form').reset();
    document.getElementById('form-title').textContent = 'Add Employee';
    document.getElementById('submit-btn').textContent = 'Add Employee';
    document.getElementById('cancel-btn').style.display = 'none';
    editingEmployeeId = null;
}

document.addEventListener('DOMContentLoaded', () => {
    fetchEmployees();
    document.getElementById('employee-form').addEventListener('submit', submitForm);
    document.getElementById('cancel-btn').addEventListener('click', resetForm);
});
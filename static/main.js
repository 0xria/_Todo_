// Optional: highlight tasks when clicked
document.addEventListener('DOMContentLoaded', () => {
    const tasks = document.querySelectorAll('li');
    tasks.forEach(task => {
        task.addEventListener('click', () => {
            task.style.backgroundColor = '#d1ffd6';
        });
    });
});

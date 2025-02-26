// Load files when page loads
document.addEventListener('DOMContentLoaded', loadFiles);

// Add search functionality
document.querySelector('.search-box').addEventListener('input', filterFiles);

function loadFiles() {
    const filesList = document.getElementById('files-list');
    filesList.innerHTML = '<div class="loading">טוען קבצים...</div>';

    fetch('/logs')
        .then(response => response.json())
        .then(data => {
            if (data.files.length === 0) {
                filesList.innerHTML = '<div class="no-files">אין קבצי Log להצגה</div>';
                return;
            }

            filesList.innerHTML = '';

            // Sort files by date (newest first)
            data.files.sort((a, b) => {
                return new Date(b.date) - new Date(a.date);
            });

            data.files.forEach(file => {
                const fileDate = new Date(file.date);
                const formattedDate = fileDate.toLocaleString('he-IL');

                const fileCard = document.createElement('div');
                fileCard.className = 'file-card';
                fileCard.setAttribute('data-filename', file.name);
                fileCard.innerHTML = `
                    <h3>${file.name}</h3>
                    <div class="file-date">${formattedDate}</div>
                `;

                fileCard.addEventListener('click', () => {
                    viewLogFile(file.name);
                });

                filesList.appendChild(fileCard);
            });
        })
        .catch(error => {
            console.error('שגיאה בטעינת קבצים:', error);
            filesList.innerHTML = '<div class="no-files">שגיאה בטעינת קבצים</div>';
        });
}

function viewLogFile(filename) {
    fetch(`/logs/${filename}`)
        .then(response => response.json())
        .then(data => {
            const logContent = document.getElementById('log-content');
            const filesList = document.getElementById('files-list');
            const backButton = document.querySelector('.back-button');

            // Format and display the log content
            let formattedContent = '';

            if (Array.isArray(data)) {
                data.forEach((keyPressGroup, groupIndex) => {
                    formattedContent += `קבוצת הקלדות ${groupIndex + 1}:\n`;

                    if (Array.isArray(keyPressGroup)) {
                        keyPressGroup.forEach(keyPress => {
                            let displayKey = keyPress;

                            // Clean up pynput key format if needed
                            if (displayKey.includes("'")) {
                                displayKey = displayKey.replace(/Key.|'/g, '');
                            }

                            formattedContent += `  • ${displayKey}\n`;
                        });
                    }

                    formattedContent += '\n';
                });
            } else {
                formattedContent = JSON.stringify(data, null, 2);
            }

            logContent.querySelector('pre').textContent = formattedContent;

            // Show log content, hide file list
            logContent.style.display = 'block';
            filesList.style.display = 'none';
            backButton.style.display = 'block';
        })
        .catch(error => {
            console.error('שגיאה בטעינת קובץ:', error);
            alert('שגיאה בטעינת תוכן הקובץ');
        });
}

function showFilesList() {
    const logContent = document.getElementById('log-content');
    const filesList = document.getElementById('files-list');
    const backButton = document.querySelector('.back-button');

    logContent.style.display = 'none';
    filesList.style.display = 'grid';
    backButton.style.display = 'none';
}

function filterFiles() {
    const searchTerm = document.querySelector('.search-box').value.toLowerCase();
    const fileCards = document.querySelectorAll('.file-card');

    fileCards.forEach(card => {
        const fileName = card.getAttribute('data-filename').toLowerCase();
        if (fileName.includes(searchTerm)) {
            card.style.display = 'block';
        } else {
            card.style.display = 'none';
        }
    });
}
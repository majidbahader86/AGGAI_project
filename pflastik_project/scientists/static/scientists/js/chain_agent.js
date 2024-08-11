// Check if the script is already loaded
if (typeof window.__CHAIN_AGENT_SCRIPT_LOADED === 'undefined') {
    window.__CHAIN_AGENT_SCRIPT_LOADED = true;

    document.addEventListener('DOMContentLoaded', () => {
        console.log('DOM fully loaded and parsed');

        // Select elements
        const toggleButton = document.getElementById('toggle-door');
        const door = document.querySelector('.door');
        const mainContent = document.querySelector('.main-content');
        const terminalText = document.getElementById('terminal-text');
        const commandInput = document.getElementById('command-input');
        const accuracy = document.getElementById('accuracy');
        const tasks = document.getElementById('tasks');
        const uptime = document.getElementById('uptime');

        if (toggleButton) {
            console.log('Toggle button found');
            toggleButton.addEventListener('click', () => {
                console.log('Toggle button clicked');
                if (door) {
                    door.classList.toggle('open');
                    if (door.classList.contains('open')) {
                        console.log('Door is now open');
                        mainContent.style.perspective = '2000px';
                        typeText("Welcome to the AI Agent Terminal!\n\nAn AI agent operates on a specialized blockchain dedicated to registering plant diseases,.\n\nInitializing AI cores...\nConnecting to PlantChain...\nSyncing with GeneticChain...\nAccessing global plant and genetic databases...\nLaunching predictive models for plant disease analysis...\n\nAI Agent ready for deep analysis and real-time insights on plant genetics and disease prevention.\n\nType 'help' for a list of available commands.");
                        commandInput.focus();
                    } else {
                        console.log('Door is now closed');
                        mainContent.style.perspective = '1500px';
                        terminalText.textContent = '';
                    }
                } else {
                    console.log('Door element not found');
                }
            });
        } else {
            console.log('Toggle button not found');
        }

        function typeText(text) {
            console.log('Typing text:', text);
            let i = 0;
            terminalText.textContent = '';
            function typing() {
                if (i < text.length) {
                    terminalText.textContent += text.charAt(i);
                    i++;
                    setTimeout(typing, 25);
                }
            }
            typing();
        }

        if (commandInput) {
            commandInput.addEventListener('keydown', function(event) {
                if (event.key === 'Enter') {
                    const command = this.value.trim().toLowerCase();
                    console.log('Command entered:', command);
                    let response = '';

                    switch(command) {
                        case 'help':
                            response = "Available commands:\n- status: Check AI Agent status\n- analyze [plant name]: Analyze a plant for diseases\n- sequence [species]: Perform genetic sequencing\n- stats: View current statistics\n- plantchain: View latest PlantChain blocks\n- genechain: View latest GeneChain blocks";
                            break;
                        case 'status':
                            response = "AI Agent Status:\n- PlantChain: Connected and actively processing\n- GeneticChain: Synced and ready for sequencing\n- Plant Disease Analysis: Operational\n- Genetic Sequencing: Standing by";
                            break;
                        case 'stats':
                            response = `Current Statistics:\n- Plant Analysis Accuracy: ${accuracy ? accuracy.textContent : 'N/A'}\n- Genetic Sequences Processed: ${tasks ? tasks.textContent : 'N/A'}\n- AI System Uptime: ${uptime ? uptime.textContent : 'N/A'}`;
                            break;
                        case 'plantchain':
                            response = "Latest PlantChain Blocks:\n" + getLatestBlocks('plantchain-blocks', 3);
                            break;
                        case 'genechain':
                            response = "Latest GeneChain Blocks:\n" + getLatestBlocks('genechain-blocks', 3);
                            break;
                        default:
                            if (command.startsWith('analyze')) {
                                const plant = command.split(' ')[1];
                                response = `Analyzing ${plant || 'unknown plant'} for diseases...\nAccessing PlantChain...\nRetrieving latest research data...\nRunning AI models...\nAnalysis complete. Check PlantChain for detailed results.`;
                            } else if (command.startsWith('sequence')) {
                                const species = command.split(' ')[1];
                                response = `Initiating genetic sequencing for ${species || 'unknown species'}...\nAccessing GeneticChain...\nPreparing sequencing algorithms...\nProcessing genetic data...\nSequencing complete. Results stored in GeneticChain.`;
                            } else {
                                response = "Unknown command. Type 'help' for a list of available commands.";
                            }
                    }

                    terminalText.textContent += `\n\n> ${command}\n${response}`;
                    this.value = '';
                    terminalText.scrollTop = terminalText.scrollHeight;
                }
            });
        } else {
            console.log('Command input element not found');
        }

        function getLatestBlocks(tableId, count) {
            console.log(`Getting latest blocks for table: ${tableId}`);
            const table = document.getElementById(tableId);
            if (!table) {
                console.log(`Table with id ${tableId} not found`);
                return '';
            }
            const rows = table.getElementsByTagName('tr');
            let result = '';
            for (let i = 0; i < count && i < rows.length; i++) {
                const cells = rows[i].getElementsByTagName('td');
                result += `Block ${cells[0].textContent}: ${cells[1].textContent}\n`;
            }
            return result;
        }

        const button = document.querySelector('.button');
        if (button) {
            button.addEventListener('click', function() {
                alert('AI Agent Details:\n\nRunning on: PlantChain and GeneticChain\nSpecialization: Plant disease analysis and genetic sequencing\nCurrent Focus: Improving crop resilience and yield through AI-driven genetic analysis');
            });
        } else {
            console.log('Button element not found');
        }

        function updateStats() {
            console.log('Updating stats');
            if (accuracy) {
                accuracy.textContent = (Math.random() * (99 - 90) + 90).toFixed(1) + '%';
            }
            if (tasks) {
                tasks.textContent = Math.floor(Math.random() * (2000 - 1000) + 1000).toLocaleString();
            }
            if (uptime) {
                uptime.textContent = (99 + Math.random() * 0.9).toFixed(2) + '%';
            }
        }

        function updateBlockchain(chainId, blockCount) {
            console.log(`Updating blockchain: ${chainId} with ${blockCount} blocks`);
            const blockList = document.getElementById(chainId + '-blocks');
            if (!blockList) {
                console.log(`Block list with id ${chainId + '-blocks'} not found`);
                return;
            }
            blockList.innerHTML = '';
            for (let i = 0; i < blockCount; i++) {
                const row = document.createElement('tr');
                if (chainId === 'plantchain') {
                    row.innerHTML = `
                        <td>${blockCount - i}</td>
                        <td>${generateRandomHash()}</td>
                        <td>${Math.floor(Math.random() * 10) + 1}</td>
                        <td>${Math.floor(Math.random() * 10) + 1}</td>
                        <td>${Math.floor(Math.random() * 10) + 1}</td>
                    `;
                } else {
                    row.innerHTML = `
                        <td>${blockCount - i}</td>
                        <td>${generateRandomHash()}</td>
                        <td>${Math.floor(Math.random() * 100) + 1}</td>
                        <td>${['Arabidopsis', 'Rice', 'Wheat', 'Maize', 'Soybean'][Math.floor(Math.random() * 5)]}</td>
                    `;
                }
                blockList.appendChild(row);
            }
        }

        function generateRandomHash() {
            return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
        }

        setInterval(updateStats, 5000);
        setInterval(() => updateBlockchain('plantchain', 5), 10000);
        setInterval(() => updateBlockchain('genechain', 10), 15000);

        updateBlockchain('plantchain', 5);
        updateBlockchain('genechain', 10);

        // Enhanced user experience
        document.querySelectorAll('.dashboard-card, .table-container').forEach(element => {
            element.addEventListener('mousemove', function(e) {
                const bbox = this.getBoundingClientRect();
                const x = e.clientX - bbox.left;
                const y = e.clientY - bbox.top;
                const centerX = bbox.width / 2;
                const centerY = bbox.height / 2;
                const deltaX = (x - centerX) / centerX;
                const deltaY = (y - centerY) / centerY;

                this.style.transform = `perspective(1000px) rotateX(${deltaY * 5}deg) rotateY(${-deltaX * 5}deg) scale3d(1.02, 1.02, 1.02)`;
            });

            element.addEventListener('mouseleave', function() {
                this.style.transform = '';
            });
        });

        // Add a subtle parallax effect to the background
        document.addEventListener('mousemove', function(e) {
            const moveX = (e.clientX * -0.05) / 8;
            const moveY = (e.clientY * -0.05) / 8;
            console.log(`Background mouse move: moveX=${moveX}, moveY=${moveY}`);
            document.body.style.backgroundPosition = `${moveX}px ${moveY}px`;
        });

    });
} else {
    console.log('Chain agent script is already loaded');
}

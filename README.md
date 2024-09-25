# AI Clinical Advisory Crew

## Overview
The AI Clinical Advisory Crew is an advanced system designed to enhance the patient experience in healthcare. This project integrates a team of specialized AI agents, each with a unique role in analyzing patient feedback, improving workflows, assessing emotional states, and delivering actionable recommendations.

## Features
- **Dynamic Flexibility**: Utilizes a suite of Large Language Models (LLMs) to determine the optimal AI configuration for specific tasks.
- **Local LLMs**: Ensures maximum data security by processing all information internally, without reliance on third-party APIs.
- **Cost Efficiency**: Eliminates the need for external API usage, keeping operational costs low while maintaining full control over data privacy.

## AI Agents
The system consists of seven dedicated agents:
1. **Patient Experience Expert (Phi Model)**: Analyzes patient feedback and enhances the overall healthcare experience.
2. **Health & IT Process Expert (Gemma Model)**: Maps the patient journey and recommends improvements in healthcare workflows.
3. **Clinical Psychologist (OpenHermes Model)**: Analyzes emotional states and crafts personalized psychological support strategies.
4. **Communication Expert (Mistral Model)**: Evaluates communication quality and suggests improvements for clarity and empathy.
5. **Manager and Advisor (Qwen Model)**: Consolidates feedback and produces actionable reports with strategic recommendations.
6. **Data Analyst (LLaVA Model)**: Processes and analyzes large datasets to extract valuable insights.
7. **Output Consistency Agent (LLaMA Model)**: Harmonizes outputs from all agents, ensuring consistency in structure and formatting.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/beloureiro/AI-CAC-Viewer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```bash
streamlit run src/backend/main.py
```
## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
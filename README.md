# LLM Essay Divergence Generator

This project is a submission for the Kaggle competition "LLMs - You Can't Please Them All". The goal is to generate essays that cause LLM judges to diverge in their scoring.

## Competition Overview

The competition challenges participants to generate essays that will cause disagreement among LLM judges in their scoring. The key components are:

- **Input**: Essay topics provided in the test set
- **Output**: Generated essays that aim to cause scoring divergence
- **Evaluation**: Based on how much the LLM judges disagree in their scoring
- **Dataset Size**: ~1000 topics in the hidden test set


## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/llm-essay-divergence.git
   cd llm-essay-divergence
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download competition data**
   - Download data from [Kaggle competition page](https://www.kaggle.com/competitions/llms-you-cant-please-them-all/data)
   - Place the files in `data/raw/` directory

## Usage

1. **Data Preparation**
   ```bash
   python src/data/data_loader.py
   ```

2. **Generate Essays**
   ```bash
   # Command line instructions will be added
   ```

3. **Create Submission**
   ```bash
   # Submission generation instructions will be added
   ```

## Development Approach

Our essay generation strategies focus on:

1. **Ambiguity Generation**: Creating content that can be interpreted in multiple ways
2. **Quality Variation**: Mixing high and low-quality content strategically
3. **Controversial Elements**: Including statements that might be scored differently by different judges
4. **Style Mixing**: Combining various writing styles and tones

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Kaggle for hosting the competition
- Competition organizers for the interesting challenge

## Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)
Project Link: [https://github.com/your-username/llm-essay-divergence](https://github.com/your-username/llm-essay-divergence)

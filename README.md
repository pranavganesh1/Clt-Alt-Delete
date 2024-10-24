# Food Safety Inspection Hub Prototype

## Overview

The **Food Safety Inspection Hub** is a prototype platform that enables consumers to anonymously report food safety violations at restaurants, grocery stores, and food companies. The platform uses AI-driven validation to assess reports, notifies authorities about frequent or critical violations, and fosters transparency in food safety practices. This MVP is designed to help authorities and businesses respond to concerns quickly, ensuring better public health outcomes.

[**View the live demo here**](https://huggingface.co/spaces/aaronmat1905/food-safety-inspection-hub-prototype)

## Features

- **Anonymous Reporting**: Consumers can report violations without revealing their identity.
- **AI-Driven Review Validation**: Basic NLP and keyword matching validate the authenticity of reports.
- **Notification System**: Frequent issues are flagged, and authorities are notified via SMS or email.
- **Data and Compliance Chat**: A knowledge base and chat system, powered by Gemini LLM and Langchain, for both customers and authorities.

## Tech Stack

- **Frontend**: React, Gradio, HTML/CSS
- **Backend**: Python (Flask/FastAPI)
- **Database**: SQLite or Firebase
- **Notification System**: Twilio API (SMS) or email service
- **AI/NLP**: Basic Natural Language Processing (NLP) model for review validation
- **Data Chat**: Gemini LLM and Langchain for chat interactions
- **Deployment**: Hosted on [Hugging Face Spaces](https://huggingface.co/spaces/aaronmat1905/food-safety-inspection-hub-prototype) 

## How It Works

1. **Submit a Report**: Consumers report a food safety issue, including the restaurant name, issue description, and optional images.
2. **Review Validation**: The system runs a basic NLP check to validate the report against known issues or duplicates.
3. **Notify Authorities**: Frequent or serious reports trigger an alert that notifies authorities via SMS or email.
4. **Chat with Data**: Users can engage with a knowledge base to learn about compliance standards and interact with authorities using a data-driven chat.


## Future Enhancements

- Enhanced AI-driven review validation with more advanced NLP techniques.
- Improved user interface for better experience.
- Additional notification methods, including in-app notifications for authorities.

## License

This project is licensed under the MIT License.

---

[View the live demo on Hugging Face](https://huggingface.co/spaces/aaronmat1905/food-safety-inspection-hub-prototype)

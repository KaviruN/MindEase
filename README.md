# MINDEASE Chat Application

This is a Django-based web application designed to provide mental health support through an AI-powered chat assistant. The application allows users to interact with the AI, save chat history, and retrieve past conversations.

## Features

### User Authentication
- **Sign Up**: New users can create an account.
- **Sign In**: Existing users can log in to access their chat history.
- **Sign Out**: Users can securely log out of their account.

### AI Chat Assistant
- **Interactive Chat**: Users can send prompts to the AI assistant and receive responses in real-time.
- **Mental Health Support**: The AI is trained to provide support on various mental health topics such as anxiety, depression, stress, and more.

### Chat History
- **Save Conversations**: All user interactions with the AI are saved to the database.
- **Retrieve Past Conversations**: Users can view their chat history, which is displayed in a user-friendly format.

### Prompt Filtering
- **Keyword Filtering**: The application filters prompts based on a predefined list of keywords to ensure appropriate content.

## How It Works

1. **User Authentication**: Users must sign up or log in to access the chat feature.
2. **Chat Interface**: Once logged in, users can navigate to the chat page.
3. **Sending Prompts**: Users can type their prompts into the input field and submit them.
4. **AI Response**: The AI processes the prompt and returns a response, which is displayed on the chat page.
5. **Saving Data**: Both the prompt and the response are saved to the database for future reference.
6. **Viewing History**: Users can scroll through their chat history to review past conversations.


## Technologies Used

- **Django**: Web framework for building the application.
- **OpenAI**: API for the AI chat assistant.
- **HTML/CSS**: Front-end technologies for building the user interface.
- **JavaScript**: Enhances interactivity on the chat page.

## Future Enhancements

- **Real-time Chat**: Implement WebSocket for real-time communication.
- **Advanced Filtering**: Improve the keyword filtering mechanism.
- **User Profiles**: Allow users to update their profiles and preferences(coming soon).
- **Analytics**: Provide insights and analytics on user interactions.

## Contributing

Contributions are welcome! If you have any ideas or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.All rights reserved.

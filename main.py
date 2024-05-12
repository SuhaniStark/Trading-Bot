# Code start here
import openai

# Set up your OpenAI API key
openai.api_key = 'your-api-key'

def generate_trade_ideas(prompt):
    # Use ChatGPT to generate trade ideas based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    
    # Extract the generated text from the response
    trade_idea = response.choices[0].text.strip()
    
    return trade_idea

def main():
    # Example prompt
    prompt = "Generate a trade idea for AAPL stock based on recent news and technical analysis."
    
    # Generate trade ideas using ChatGPT
    trade_idea = generate_trade_ideas(prompt)
    
    # Print the generated trade idea
    print("Generated Trade Idea:")
    print(trade_idea)

if __name__ == "__main__":
    main()
    
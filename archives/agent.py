from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
import os

load_dotenv()

llm = GoogleGenerativeAI(model='gemini-2.0-flash', google_api_key=os.getenv("GOOGLE_API_KEY"))

print("Aight tight tigth, Working...")

functionality = '''
This card component is designed for a blood donation camp website to collect crucial information about a potential donor's blood group and smoking habits. It focuses on a simple, efficient user experience with clear data input mechanisms and validation. The component should be easily integrated into the main page and responsive across different devices.\n\n**Detailed Functionality Breakdown:**\n\n*   **Blood Group Selection:**\n    *   A dropdown menu or radio button group allows the user to select their blood group from a predefined list (O+, O-, A+, A-, B+, B-, AB+, AB-).  The list should be comprehensive and cover all possible blood groups.\n    *   The selected blood group should be stored and easily accessible for data processing (e.g., saving to a database).\n    *   Implement basic validation to ensure a blood group is selected before proceeding.\n\n*   **Last Smoked Date/Time Input:**\n    *   Utilize a date and time picker component for users to accurately specify when they last smoked a cigarette.\n    *   The date and time picker should be user-friendly and intuitive, providing a clear calendar view and time selection options.\n    *   Implement validation to ensure a valid date and time are selected (e.g., not a future date).\n    *   Store the date and time in a standardized format (e.g., ISO 8601) for consistent data handling.\n\n*   **Data Handling and Submission (Implicit):**\n    *   While the card itself doesn't directly handle submission, it should be designed to easily integrate with a form or data submission mechanism on the main page.\n    *   Ensure the component provides access to the collected data (blood group, last smoked date/time) so it can be submitted as part of a larger form.\n\n*   **Accessibility Considerations:**\n    *   Ensure the component is accessible to users with disabilities by providing appropriate ARIA attributes and keyboard navigation support.\n    *   Use semantic HTML elements to improve accessibility and SEO.\n\n*   **Error Handling:**\n    *   Provide clear and concise error messages if the user fails to provide the required information or enters invalid data.  These errors should be displayed inline, near the relevant input field.\n\n*   **Responsiveness:**\n    *   The component should be responsive and adapt to different screen sizes, ensuring a consistent user experience across all devices (desktops, tablets, and smartphones)
'''


print(
    llm.invoke(f'''
    You are an expert frontend react and javascript developer who is well versed with latest trends in react, based on this 
    these details
    {functionality}
     you need to code a react component, code it wihtout any styling but ensure all mentioned functionalities are there and working 
    as mentioned in the given description.
    Only return me .jsx code
''')
)
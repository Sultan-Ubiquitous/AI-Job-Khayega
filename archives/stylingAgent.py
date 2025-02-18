from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
import os

load_dotenv()

llm = GoogleGenerativeAI(model='gemini-2.0-flash', google_api_key=os.getenv("GOOGLE_API_KEY"))

print("Aight tight tigth, Working...")

description = '''
"The card component's styling should convey an ominous yet informative feel, reflecting the seriousness of blood donation criteria, particularly regarding smoking. The color palette and typography should work together to create a visually striking and easily readable component.\n\n**Detailed Styling Breakdown:**\n\n*   **Color Palette:**\n    *   **Primary Colors:** Red (#8B0000 - Dark Blood Red) and Black (#000000).\n    *   **Secondary Color:**  A muted grey (#696969) can be used for subtle details and text that doesn't need to be emphasized.\n    *   **Accent Color:** A slightly lighter shade of red (#A52A2A - Brownish Red) can be used for interactive elements or subtle highlights.\n    *   **Rationale:** The combination of red and black evokes a sense of urgency and seriousness, aligning with the critical nature of blood donation and health considerations.\n\n*   **Typography:**\n    *   **Font Family:** Use a clear and readable sans-serif font like 'Roboto' or 'Open Sans' for body text.  For headings, consider a slightly bolder and more impactful font like 'Montserrat' or 'Lato'.\n    *   **Font Sizes:**\n        *   Headings: 18-24px\n        *   Body Text: 14-16px\n        *   Labels: 12-14px\n    *   **Font Weight:** Use appropriate font weights (400, 500, 700) to create visual hierarchy and emphasize important information.\n    *   **Color:**  Use white or a very light grey (#f0f0f0) for text on the dark backgrounds to ensure readability. Dark grey or black for text on lighter backgrounds.\n\n*   **Layout and Spacing:**\n    *   Use generous padding and margins to create visual breathing room and prevent overcrowding.  A padding of 16px to 24px is recommended.\n    *   Maintain consistent spacing between elements to create a sense of order and professionalism.\n    *   Use a card-like structure with rounded corners (e.g., 8px radius) to visually separate the component from the rest of the page.\n\n*   **Visual Elements:**\n    *   **Icons:**  Consider using subtle icons to visually represent blood groups or smoking information. Use simple, minimalist icons that complement the overall design.\n    *   **Border:** A thin, dark grey (#444444) border can be added to the card to provide a subtle visual separation.\n\n*   **State Styling:**\n    *   **Hover/Focus States:** Provide clear visual feedback (e.g., a subtle background color change or border highlight) when the user hovers over or focuses on interactive elements (dropdown, date picker).\n    *   **Error States:**  Use a brighter shade of red (#FF0000) to highlight input fields that contain errors.  Provide a clear error message near the field.\n\n*   **Overall Impression:** The card should look professional, informative, and slightly serious. Avoid overly playful or distracting design elements. Focus on clarity, readability, and a consistent visual language that aligns with the blood donation camp's branding."
'''
code = '''
import React, { useState } from 'react';

const BloodDonationCard = () => {
  const [bloodGroup, setBloodGroup] = useState('');
  const [lastSmoked, setLastSmoked] = useState('');
  const [bloodGroupError, setBloodGroupError] = useState('');
  const [lastSmokedError, setLastSmokedError] = useState('');

  const bloodGroups = ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-'];

  const handleBloodGroupChange = (event) => {
    setBloodGroup(event.target.value);
    setBloodGroupError('');
  };

  const handleLastSmokedChange = (event) => {
    setLastSmoked(event.target.value);
    setLastSmokedError('');
  };

  const validateForm = () => {
    let isValid = true;

    if (!bloodGroup) {
      setBloodGroupError('Please select your blood group.');
      isValid = false;
    }

    if (!lastSmoked) {
      setLastSmokedError('Please select the date and time you last smoked.');
      isValid = false;
    } else {
      const selectedDate = new Date(lastSmoked);
      const currentDate = new Date();

      if (selectedDate > currentDate) {
        setLastSmokedError('Date cannot be in the future.');
        isValid = false;
      }
    }

    return isValid;
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    if (validateForm()) {
      // In a real application, you would handle the data submission here.
      console.log('Blood Group:', bloodGroup);
      console.log('Last Smoked:', lastSmoked);
      alert('Form submitted successfully! (Check console for data)');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="bloodGroup">Blood Group:</label>
        <select id="bloodGroup" value={bloodGroup} onChange={handleBloodGroupChange} aria-required="true">
          <option value="">Select Blood Group</option>
          {bloodGroups.map((group) => (
            <option key={group} value={group}>
              {group}
            </option>
          ))}
        </select>
        {bloodGroupError && <p role="alert">{bloodGroupError}</p>}
      </div>

      <div>
        <label htmlFor="lastSmoked">Last Smoked:</label>
        <input
          type="datetime-local"
          id="lastSmoked"
          value={lastSmoked}
          onChange={handleLastSmokedChange}
          aria-required="true"
        />
        {lastSmokedError && <p role="alert">{lastSmokedError}</p>}
      </div>

      <button type="submit">Submit</button>
    </form>
  );
};

export default BloodDonationCard;
'''

print(llm.invoke(f'''
   You are an expert tailwind CSS and UI/UX designer. your job is to style this code 
   {code}
   with this given description
   {description}
   analyze the description properly and 
   only return a .jsx component styled with tailwind css
    '''
))

# Make another agent to generate Mock Data
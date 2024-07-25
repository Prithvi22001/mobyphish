// Get references to the elements
const enableButton = document.getElementById('enableButton');
const disableLink = document.getElementsByClassName('locked');

// Function to enable the links and update their appearance
const enableLinks = () => {
  // Enable the disabled links
  for (let i = 0; i < disableLink.length; i++) {
    disableLink[i].classList.add('enabled');
    disableLink[i].setAttribute('href', disableLink[i].dataset.href);
  }

  // Store the enabled state in local storage
  localStorage.setItem('linksEnabled', 'true');
};

// Function to check the enabled state from local storage and enable the links if necessary
const checkLinksEnabled = () => {
  const linksEnabled = localStorage.getItem('linksEnabled');
  if (linksEnabled === 'true') {
    enableLinks();
  }
};

// Call the function to check the enabled state when the page loads
checkLinksEnabled();

// Define the click event handler for the enable button
enableButton.addEventListener('click', enableLinks);
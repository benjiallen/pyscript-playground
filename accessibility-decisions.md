# Accessibility decisions

## Context

* Help a friend
* Learn more about a technology I was interested in

## Design decisions

Things I had to think about while trying to make the UI accessible:

* Who is my audience and what assistive technology (AT) do they use?
* What are the main tasks that a user wants to complete?
* Semantics
* Accessible names - brevity vs. clarity
* Focus management
* Notifications for big content changes
* Breaking the browser. Back button 😭
* Usability testing and feedback

## Known issues

* pyscript loading overlay
  * It would be nice to update the screen reader on the loading status
  * Make sure focus is in the right place after the overlay closes
* Getting searches into browser history so the back button works again
* Validation and error prevention

## Drawbacks of this approach

* No quick way to get to the CEO (root of the tree)
* No way to visualize depth in the tree
  * How many levels deep is benjiallen within the org chart?
* No way to describe profile pictures?
  * Would that be a good idea?

## Testing techniques

### Accessibility testing tools

* W3C HTML validator
* axe DevTools Pro
* VMware Fusion running Windows 10, Chrome, NVDA

### End-to-end testing

* pytest and playwright

### Backlog

* Get axe scans working with playwright

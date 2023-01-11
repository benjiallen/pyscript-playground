# Accessibility decisions

## Context

* Help a friend
* Learn more about a technology I was interested in
* It's a side project - time influenced my decision making

## Design decisions

Things I had to think about while trying to make the UI accessible:

* Who is my audience and what assistive technology (AT) do they use?
* What are the main tasks that a user wants to complete?
* How regularly would the user use the tool?
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
* No quick way to get to the CEO (root of the tree)
* No "type ahead" search - a user doesn't get search suggestions as they type their search

## Drawbacks of this approach

Is there information a tree like visualization can give you that this UI cannot?

* No way to visualize depth in the tree
  * How many levels deep is benjiallen within the org chart?
  * Who is at the same level as benjiallen?
* No way to describe profile pictures?
  * Would that be a good idea?

## Testing techniques

### Accessibility testing tools

* [W3C HTML validator](https://validator.w3.org/)
* [axe DevTools Pro](https://www.deque.com/axe/devtools/)
* [VMware Fusion](https://www.vmware.com/products/fusion.html) running Windows 10, Chrome, [NVDA](https://www.nvaccess.org/download/)

### End-to-end testing

* [pytest](https://docs.pytest.org/en/7.2.x/) and [playwright](https://playwright.dev/python/)

### Backlog

* Get axe scans working with playwright

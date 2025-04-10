#   Budget Scheduling System

This HTML-based Budget Scheduling System helps users manage their finances by scheduling transfers, viewing transaction history, tracking unredeemed cash, and uploading spending history for analysis and suggestions.

##   Features

###   1.  New Transfer

Allows users to set up new transfers between accounts, specifying the source account, destination account, amount, frequency, date, and time.

* **Step 1:** Initial setup with a "Next" button.

    ```html
    <div id="step1" class="step active">
        <h2>Step 1: Transfer Setup</h2>
        <p>Welcome to the Budget Scheduling System. Click 'Next' to set up a new transfer.</p>
        <button onclick="nextStep()">Next</button>
    </div>
    ```

* **Step 2:** Schedule the transfer by selecting accounts, amount, frequency, date, and time. Input validation ensures a future date and time are selected.

    ```html
    <div id="step2" class="step">
        <h2>Schedule Transfer</h2>
        <p>From Account: <select id="fromAccount" onchange="updateBalance()">
            <option value="savings">Savings Account (Balance: R5000)</option>
            <option value="current">Current Account (Balance: R2000)</option>
        </select></p>
        <p>To Account: <select id="toAccount">
            <option>Savings Goal</option>
            <option>Credit Card Payment</option>
        </select></p>
        <p>Amount: R<input type="number" id="amount" min="0" step="0.01" onchange="updateBalance()"></p>
        <p>Frequency: <select id="frequency">
            <option>Once-off</option>
            <option>Weekly</option>
            <option>Monthly</option>
        </select></p>
        <p>Date: <input type="date" id="transferDate"></p>
        <p>Time: <input type="time" id="transferTime"></p>
        <p id="currentBalance">Current Balance: R5000</p>
        <p id="newBalance">New Balance after transfer: R5000</p>
        <button onclick="nextStep()">Next</button>
    </div>
    ```

    * The `validateDateTime()` function is used for date and time validation:

        ```javascript
        function validateDateTime() {
            const selectedDate = new Date(document.getElementById('transferDate').value + 'T' + document.getElementById('transferTime').value);
            const now = new Date();
            return selectedDate > now;
        }
        ```

* **Step 3:** Confirmation of transfer details.

    ```html
    <div id="step3" class="step">
        <h2>Confirmation</h2>
        <p>Please confirm your transfer details:</p>
        <div id="confirmationDetails"></div>
        <button onclick="confirmTransfer()">Confirm Transfer</button>
    </div>
    ```

    * The transfer details are displayed in the `confirmationDetails` div using JavaScript:

        ```javascript
        document.getElementById('confirmationDetails').innerHTML = `
            <p>From: ${fromAccount}</p>
            <p>To: ${toAccount}</p>
            <p>Amount: R${amount}</p>
            <p>Frequency: ${frequency}</p>
            <p>Date: ${date}</p>
            <p>Time: ${time}</p>
            <p>Current Balance: R${accountBalances[fromAccount]}</p>
            <p>New Balance: R${accountBalances[fromAccount] - amount}</p>
        `;
        ```

* **Step 4:** Transfer scheduled confirmation with an option to schedule another transfer.

    ```html
    <div id="step4" class="step">
        <h2>Transfer Scheduled</h2>
        <p>Your transfer has been successfully scheduled!</p>
        <button onclick="resetSimulation()">Schedule Another Transfer</button>
    </div>
    ```

###   2.  Transaction History

Displays a table of transaction history, showing the date & time, source account, destination account, amount, and status of each transaction.

```html
<div id="History" class="tab-content">
    <h2>Transaction History</h2>
    <table id="historyTable">
        <tr>
            <th>Date & Time</th>
            <th>From</th>
            <th>To</th>
            <th>Amount</th>
            <th>Status</th>
        </tr>
    </table>
</div>

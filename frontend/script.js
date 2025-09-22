// This is a conceptual script.
// In a real application, these functions would make API calls to your Python backend.
// For this example, we'll simulate the backend logic directly in JS.

// --- 1. Observer Pattern Simulation ---
const observerOutput = document.getElementById('observer-output');
const productPriceEl = document.getElementById('product-price');
const subscribeBtn = document.getElementById('subscribe-btn');

const observers = [];
const subject = {
    price: 999.00,
    notify: function() {
        observers.forEach(observer => observer.update(this.price));
    }
};

class UserObserver {
    constructor(name) {
        this.name = name;
    }
    update(newPrice) {
        observerOutput.innerHTML += `<p>✅ Notification for ${this.name}: Price of iPhone 15 has dropped to $${newPrice}.</p>`;
    }
}

subscribeBtn.addEventListener('click', () => {
    const newUser = new UserObserver('User ' + (observers.length + 1));
    observers.push(newUser);
    observerOutput.innerHTML += `<p>🔔 ${newUser.name} is now subscribed to price drop notifications.</p>`;
    
    // Simulate a price change after a delay
    setTimeout(() => {
        subject.price = 899.00;
        productPriceEl.textContent = `Current Price: $${subject.price}`;
        subject.notify();
    }, 2000);
});

// --- 2. Strategy Pattern Simulation ---
const strategyOutput = document.getElementById('strategy-output');
const paymentMethodSelect = document.getElementById('payment-method');
const payBtn = document.getElementById('pay-btn');

const paymentStrategies = {
    card: {
        pay: (amount) => `💳 Paying $${amount} using Credit/Debit Card.`
    },
    upi: {
        pay: (amount) => `📲 Paying $${amount} using UPI.`
    },
    wallet: {
        pay: (amount) => `💰 Paying $${amount} using Wallet.`
    }
};

payBtn.addEventListener('click', () => {
    const selectedStrategy = paymentMethodSelect.value;
    const strategy = paymentStrategies[selectedStrategy];
    strategyOutput.innerHTML = `<p>${strategy.pay(150.00)}</p>`;
});

// --- 3. Command Pattern Simulation ---
const commandOutput = document.getElementById('command-output');
const cartList = document.getElementById('cart-list');
const itemInput = document.getElementById('item-name');
const couponInput = document.getElementById('coupon-code');
const addItemBtn = document.getElementById('add-item-btn');
const removeItemBtn = document.getElementById('remove-item-btn');
const applyCouponBtn = document.getElementById('apply-coupon-btn');
const undoBtn = document.getElementById('undo-btn');

const cart = {
    items: [],
    addItem: (item) => {
        cart.items.push(item);
        commandOutput.innerHTML += `<p>🛒 Added '${item}' to cart.</p>`;
        updateCartList();
    },
    removeItem: (item) => {
        const index = cart.items.indexOf(item);
        if (index > -1) {
            cart.items.splice(index, 1);
            commandOutput.innerHTML += `<p>❌ Removed '${item}' from cart.</p>`;
            updateCartList();
        }
    },
    applyCoupon: (coupon) => {
        commandOutput.innerHTML += `<p>🎁 Applied coupon '${coupon}'.</p>`;
    }
};

const invoker = {
    history: [],
    execute: (command) => {
        invoker.history.push(command);
        command.execute();
    },
    undo: () => {
        if (invoker.history.length > 0) {
            const command = invoker.history.pop();
            command.undo();
            commandOutput.innerHTML += `<p>↩️ Undoing last action.</p>`;
        } else {
            commandOutput.innerHTML += `<p>Nothing to undo.</p>`;
        }
    }
};

// Command Classes (simulated)
class AddItemCommand {
    constructor(receiver, item) {
        this.receiver = receiver;
        this.item = item;
    }
    execute() { this.receiver.addItem(this.item); }
    undo() { this.receiver.removeItem(this.item); }
}

class RemoveItemCommand {
    constructor(receiver, item) {
        this.receiver = receiver;
        this.item = item;
    }
    execute() { this.receiver.removeItem(this.item); }
    undo() { this.receiver.addItem(this.item); }
}

class ApplyCouponCommand {
    constructor(receiver, coupon) {
        this.receiver = receiver;
        this.coupon = coupon;
    }
    execute() { this.receiver.applyCoupon(this.coupon); }
    undo() {
        // Simple undo for demonstration
        commandOutput.innerHTML += `<p>↪️ Undid coupon '${this.coupon}'.</p>`;
    }
}

// Event Listeners for Command section
addItemBtn.addEventListener('click', () => {
    const item = itemInput.value;
    if (item) {
        invoker.execute(new AddItemCommand(cart, item));
        itemInput.value = '';
    }
});

removeItemBtn.addEventListener('click', () => {
    const item = itemInput.value;
    if (item) {
        invoker.execute(new RemoveItemCommand(cart, item));
        itemInput.value = '';
    }
});

applyCouponBtn.addEventListener('click', () => {
    const coupon = couponInput.value;
    if (coupon) {
        invoker.execute(new ApplyCouponCommand(cart, coupon));
        couponInput.value = '';
    }
});

undoBtn.addEventListener('click', () => {
    invoker.undo();
});

function updateCartList() {
    cartList.innerHTML = '';
    cart.items.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        cartList.appendChild(li);
    });
}
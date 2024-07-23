// Description: Sleep-Tite Motel Customer Booking --> JavaScript
// Author: Harini Manohar
// Dates: 15 July to 26 July, 2024

// Define the customer object
const customer = {
    title: "Mr.",
    Fname: "Misha",
    Lname: "Collins",
    birthDate: new Date("1990-01-15"),
    gender: "Male",
    roomPreferences: ["non-smoking", "sea-facing", "pet-friendly", "king-size bed"],
    paymentMethod: "Credit Card",
    mailingAddress: {
        street: "123 Main St",
        city: "Brookfield",
        provinvce: "NL",
        postalCode: "A1A1A1",
        country: "Canada"
    },
    phoneNumber: "709-123-4567",
    stayDates: {
        checkIn: new Date("2024-07-20"),
        checkOut: new Date("2024-07-25")
    },
    
    // Method to calculate age
    calculateAge: function() {
        const today = new Date();
        let age = today.getFullYear() - this.birthDate.getFullYear();
        const monthDiff = today.getMonth() - this.birthDate.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < this.birthDate.getDate())) {
            age--;
        }
        return age;
    },
    
    // Method to calculate duration of stay
    calculateStayDuration: function() {
        const timeDiff = this.stayDates.checkOut - this.stayDates.checkIn;
        const days = Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
        return days;
    },

    // Method to format room preferences array
    formatRoomPreferences: function() {
        const prefs = this.roomPreferences;
        if (prefs.length === 0) return '';
        if (prefs.length === 1) return prefs[0];
        const lastPref = prefs.pop();
        return prefs.join(', ') + ' room with a ' + lastPref;
    },

    
    // Method to generate customer details
    getDetailsList: function() {
        return `
            <center><h2 style="color: slateblue">SLEEP-TITE MOTEL</h2></center>
            <p style="border: 2px solid dodgerblue; background-color:aliceblue; color: dodgerblue"><br/><b><u>Online Customer Booking Details:</b></u><br/>
            <br/>
            <b>Name:</b> ${this.Fname} ${this.Lname} <br/>
            <b>Age:</b> ${this.calculateAge()}<br/>
            <b>Gender:</b> ${this.gender}<br/>
            <b>Room Preferences:</b> ${this.roomPreferences.join(", ")}<br/>
            <b>Payment Method:</b> ${this.paymentMethod}<br/>
            <b>Mailing Address:</b> ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.provinvce}, ${this.mailingAddress.postalCode}, ${this.mailingAddress.country}<br/>
            <b>Phone Number:</b> ${this.phoneNumber}<br/>
            <b>Check-In Date:</b> ${this.stayDates.checkIn.toDateString()}<br/>
            <b>Check-Out Date:</b> ${this.stayDates.checkOut.toDateString()}<br/>
            <b>Duration of Stay:</b> ${this.calculateStayDuration()} days<br/>
            <br/>
            </p>
        `;
    },

    // Method to generate a descriptive paragraph
    getDescription: function() {
        return `
            <center><h3 style="color:#d65c85"><strong><em><u>Attention! Public Announcement!</u></em></strong><br/></h3></center>
            <p style="border:2px solid #d65c85;background-color:lavenderblush; color:#d65c85">
            <br/>    
            It is with great pleasure that we welcome our distinguished guest, ${this.title} ${this.Fname} ${this.Lname}, aged ${this.calculateAge()}. ${this.title} ${this.Lname} graces us with his presence, preferring the luxuries of a ${this.formatRoomPreferences()}. Residing at ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.provinvce}, ${this.mailingAddress.postalCode}, ${this.mailingAddress.country}, ${this.title} ${this.Lname} has chosen our establishment for a delightful stay from ${this.stayDates.checkIn.toDateString()} to ${this.stayDates.checkOut.toDateString()}, favoring the convenience and security of payment via his ${this.paymentMethod}.
            <br/><br/>
            ${this.title} ${this.Lname} can be contacted by phone at ${this.phoneNumber}, and we are honored to host him for a period of ${this.calculateStayDuration()} days. His discerning taste and preference for comfort and elegance are well noted, and we are committed to ensuring that his stay is nothing short of extraordinary. 
            <br/><br/>
            With every comfort meticulously attended to, and every detail thoughtfully considered, we extend our warmest welcome to ${this.title} ${this.Fname} ${this.Lname}. We are confident that his time with us will be memorable, and it is our sincere hope that he will carry fond memories of his stay at our esteemed establishment.<br/>
            <br/>
            </p>
        `;
    }
};

// Display the customer details and description in the HTML
document.getElementById('customer-info').innerHTML = customer.getDetailsList() + customer.getDescription();

// Output the customer description to the console or webpage
console.log(customer.getDescription());
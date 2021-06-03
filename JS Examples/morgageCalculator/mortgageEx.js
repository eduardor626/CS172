

function validNumber(fieldinput){
var unicode=fieldinput.charCode? fieldinput.charCode : fieldinput.keyCode;
if ((unicode!=8) && (unicode!=46)) { //if the key isn't the backspace key (which we should allow)
if (unicode<48||unicode>57) //if not a number
return false; //disable key press
}
}

function myPayment()
{
// Reset error messages to blank
document.getElementById('loanError').innerHTML = '';
document.getElementById('yearsError').innerHTML = '';
document.getElementById('rateError').innerHTML = '';

// Form validation checking
if ((document.mortgagecalc.loan.value === null) || (document.mortgagecalc.loan.value.length === 0) || (isNaN(document.mortgagecalc.loan.value) === true))
{
document.getElementById('monthlyPayment').innerHTML = 'Please enter the missing information.';
document.getElementById('loanError').innerHTML = 'Numeric value required. Example: 165000';
} else if ((document.mortgagecalc.years.value === null) || (document.mortgagecalc.years.value.length === 0) || (isNaN(document.mortgagecalc.years.value) === true))
{
document.getElementById('monthlyPayment').innerHTML = 'Please enter the missing information.';
document.getElementById('yearsError').innerHTML = 'Numeric value required. Example: 30';
} else if ((document.mortgagecalc.rate.value === null) || (document.mortgagecalc.rate.value.length === 0) || (isNaN(document.mortgagecalc.rate.value) === true))
{
document.getElementById('monthlyPayment').innerHTML = 'Please enter the missing information.';
document.getElementById('rateError').innerHTML = 'Numeric value required. Example: 5.25';
} else
{
// Set variables from form data
var loanprincipal = document.mortgagecalc.loan.value;
var months = document.mortgagecalc.years.value * 12;
var interest = document.mortgagecalc.rate.value / 1200;

// Calculate mortgage payment and display result
document.getElementById('monthlyPayment').innerHTML = 'Your monthly mortgage payment will be ' + '$' + (loanprincipal * interest / (1 - (Math.pow(1/(1 + interest), months)))).toFixed(2)+'.';
document.getElementById('friendlyReminder').style.display = 'block';
}

// payment = principle * monthly interest/(1 - (1/(1+MonthlyInterest)*Months))

}

function myPaymentReset()
{
// Reset everything to default/null/blank
document.getElementById('monthlyPayment').innerHTML = 'Values reset';
document.getElementById('friendlyReminder').style.display = 'none';
document.getElementById('loanError').innerHTML = '';
document.getElementById('yearsError').innerHTML = '';
document.getElementById('rateError').innerHTML = '';
document.mortgagecalc.loan.value = null;
document.mortgagecalc.years.value = null;
document.mortgagecalc.rate.value = null;
}
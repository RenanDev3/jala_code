### Date Helpers
<br>
<p>This application has two functions that makes usual rotines when manipulating dates information.</p>

<p>The first function 'get_date_interval(start_date, end_date)' receives two dates in the format 'mm/dd/yyyy' as strings and returns a list with all dates between the initial and final date, day by day.</p>

<p>The second function 'get_default_date_data(start_date, end_date, default_value)' can be explained in two parts. The first one, this functions takes the start_date and end_date as inputed arguments, calls the previous function 'get_date_interval()' to generate a list with all days between the inputed arguments. The second part, this functions returns a dict with the following (key, value) pair: {'date' : date, 'value' : default_value} for each generated day received in the list from the called function</p>
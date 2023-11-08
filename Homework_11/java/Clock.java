public class Clock {

	private int hours;
	private int minutes;
	private int seconds;

	public Clock(int hours, int minutes, int seconds) {
		this.hours = hours;
		this.minutes = minutes;
		this.seconds = seconds;
	}

	public int addHour() {
		if (hours >= 23) { // Corrected the condition from 24 to 23
			hours = 0;
		} else {
			hours++;
		}
		return hours;
	}

	public int addMinute() {
		if (minutes >= 59) { // Changed the condition to check 'minutes'
			minutes = 0;
			addHour(); // Call addHour() instead of addMinute()
		} else {
			minutes++;
		}
		return minutes;
	}

	public int addSecond() {
		if (seconds >= 59) { // Corrected the condition from 60 to 59
			seconds = 0;
			addMinute(); // Call addMinute() instead of addSecond()
		} else {
			seconds++;
		}
		return seconds;
	}

	public String get24HourFormat() {
		String format24;

		format24 = pad(hours) + ":" + pad(minutes) + ":" + pad(seconds);

		return format24;
	}

	private String getSuffix() {
		String suffix;

		if (hours < 12) {
			suffix = "AM";
		} else {
			suffix = "PM";
		}

		return suffix;
	}

	public String get12HourFormat() {
		int displayHours = (hours == 0 || hours == 12) ? 12 : hours % 12; // Modified the display hours calculation
		String format12 = displayHours + ":" + pad(minutes) + ":" + pad(seconds) + " " + getSuffix();

		return format12;
	}

	private String pad(int value) {
		String paddedValue;

		if (value <= 9) { // Modified the condition to check values less than or equal to 9
			paddedValue = "0" + value;
		} else {
			paddedValue = String.valueOf(value);
		}

		return paddedValue;
	}
}

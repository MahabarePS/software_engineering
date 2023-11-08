import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class ClockTest {

    @Test
    public void testAddHour() {
        Clock clock = new Clock(10, 30, 45);
        assertEquals(11, clock.addHour());
    }

    @Test
    public void testAddMinute() {
        Clock clock = new Clock(10, 30, 45);
        clock.addMinute();
        assertEquals(32, clock.addMinute());
    }

    @Test
    public void testAddSecond() {
        Clock clock = new Clock(10, 30, 45);
        clock.addSecond();
        assertEquals(47, clock.addSecond());
    }

    @Test
    public void testGet24HourFormat() {
        Clock clock = new Clock(10, 30, 45);
        assertEquals("10:30:45", clock.get24HourFormat());
    }

    @Test
    public void testGet12HourFormat() {
        Clock clock = new Clock(10, 30, 45);
        assertEquals("10:30:45 AM", clock.get12HourFormat());
    }
}

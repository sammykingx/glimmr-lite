# Glimmr Todo's

## Client Display Page
- A searchable, sortable/Filterable table with
    - Searchable:  email, phone
    - Filterable: Status [guest, active, inactive], Total bookings, Total spent
    - deactivate client account
- Chart: pie chart of active, guest, and inactive clients
- Graph: top locations from clients.
- Quick Actions: email/SMS client directly, reset password, assign to an agent.
- lient Profile Modal → Clicking a client row shows a modal with deeper info (address, booking history, payment history, notes).
- Create clients

## Staffs
- Overview Stats
    - Total Staff (all roles combined)
    - Active Staff (not suspended/deactivated)
    - Total Cleaning Agents
    - Agents Online
- Suspended Staff badge
- Add New Staff (floating button / top-right CTA, opens modal form with role select + contact details).
- Data Table
    - Name & Role (with avatar/initials icon, role badge: Manager/Agent)
    - Email & Phone
    - City / Province
    - Bookings Assigned (count)
    - Status (Active / Suspended / Deactivated — with colored pill badges)
    - Last Active (last login or last assignment date)
    - Actions (dropdown: Assign to Booking, Edit, Suspend, Deactivate, Delete)
- Staf Modal
    - Profile header: Name, role, contact info, location.
    - If agents: Booking info (Completed, pending, cancelled)
    - Actions: Assign to new booking, Suspend, Deactivate, Delete.

## Bookings
- Graph: clients bookings, guest bookings, returning booking,
## Payments
- prevent double payments within the same session

## Tests
- write tests for both FE and BE
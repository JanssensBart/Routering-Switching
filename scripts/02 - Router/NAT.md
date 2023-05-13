# NAT OVERLOADING

```ini
conf t
access-list *list-number* permit *source + wildcard-mask*
ip nat inside source list *list-number* interface *int-number* overload
interface *int-number*
ip nat inside
interface *int-number*
ip nat oustide 
```

# NAT verificatie & troubleshooting

```ini
show ip nat statistics
```
```ini
show ip nat translations
```
```ini
clear ip nat statistics
```
```ini
show ip nat statistics *
```
```ini
debug ip nat detailed
```
```ini
show access-lists
```
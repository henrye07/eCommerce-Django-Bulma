const d = document,
    w=window;

    document.addEventListener('DOMContentLoaded', () => {

        // Get all "navbar-burger" elements
        const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
      
        // Check if there are any navbar burgers
        if ($navbarBurgers.length > 0) {
      
          // Add a click event on each of them
          $navbarBurgers.forEach( el => {
            el.addEventListener('click', () => {
      
              // Get the target from the "data-target" attribute
              const target = el.dataset.target;
              const $target = document.getElementById(target);
      
              // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
              el.classList.toggle('is-active');
              $target.classList.toggle('is-active');
      
            });
          });
        }
      
      });

const $DrowDownBtn = d.getElementById("dropdownbtn"),
    $DrowDownCtn = d.getElementsByClassName("dropdown");

    $DrowDownBtn.addEventListener("click", (e) => {
        e.preventDefault();
        $DrowDownCtn.classList.add("is-active")
})


const $Tabs = d.querySelectorAll(".tabs li");
const $TabsContent = d.querySelectorAll("#tab-content > div")

$Tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        $Tabs.forEach(item => item.classList.remove("is-active"))
        tab.classList.toggle("is-active")
        const target = tab.dataset.target;
        $TabsContent.forEach(box => {
            if (box.getAttribute('id') === target) {
                box.classList.remove("is-hidden")
            } else {
                box.classList.add("is-hidden")
            }
                
        })
    })
})

d.addEventListener('DOMContentLoaded', () => {
    (d.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
      const $notification = $delete.parentNode;
  
      $delete.addEventListener('click', () => {
        $notification.parentNode.removeChild($notification);
      });
    });
  });





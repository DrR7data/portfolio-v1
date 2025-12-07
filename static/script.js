console.log("Hello Everyone, All right. If you can see this is bacause you are looking for in the place correct.");
console.log("Si estás leyendo esto desde la consola, significa que eres de esos desarrolladores que van más allá de lo evidente. Gracias por dedicar tu tiempo a revisar, analizar y entender cada detalle del código. Cada variable que inspeccionas, cada error que corriges y cada mejora que propones construye un producto más sólido, más claro y más elegante. Tu curiosidad es tu mayor herramienta, tu habilidad es tu mejor lenguaje y tu dedicación es lo que realmente transforma líneas en soluciones. ¡Sigue adelante, porque el mundo necesita más desarrolladores como tú! - DevSpirit");

console.log("If you're reading this from the console, it means you're one of those developers who go beyond the obvious. Thank you for taking the time to review, analyze, and understand every detail of the code. Every variable you inspect, every bug you fix, and every improvement you suggest helps build a product that is stronger, cleaner, and more elegant. Your curiosity is your greatest tool, your skill is your best language, and your dedication is what truly turns lines of code into real solutions. Keep going—the world needs more developers like you! - DevSpirit");


        // Mobile Menu Toggle
        const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
        const navLinks = document.querySelector('.nav-links');
        const navItems = document.querySelectorAll('.nav-links a');

        mobileMenuBtn.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            mobileMenuBtn.innerHTML = navLinks.classList.contains('active') 
                ? '<i class="fas fa-times"></i>' 
                : '<i class="fas fa-bars"></i>';
        });

        // Close mobile menu when clicking on a link
        navItems.forEach(item => {
            item.addEventListener('click', () => {
                navLinks.classList.remove('active');
                mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
            });
        });

        // Smooth scroll for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Header background on scroll
        const header = document.querySelector('header');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.style.backgroundColor = 'rgba(10, 25, 47, 0.95)';
                header.style.backdropFilter = 'blur(10px)';
            } else {
                header.style.backgroundColor = 'var(--header-bg)';
            }
        });

        // Project cards animation on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe project cards
        document.querySelectorAll('.project-card').forEach(card => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(20px)';
            card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            observer.observe(card);
        });

        // Typewriter effect for hero section
        const typewriterText = "Combino medicina con tecnología.";
        let i = 0;
        const speed = 50;
        
        function typeWriter() {
            if (i < typewriterText.length) {
                document.querySelector(".hero-content h3").innerHTML = 
                    typewriterText.substring(0, i+1) + '<span style="color: var(--accent-color)">|</span>';
                i++;
                setTimeout(typeWriter, speed);
            } else {
                document.querySelector(".hero-content h3").innerHTML = 
                    typewriterText + '<span style="color: var(--accent-color)">|</span>';
                // Blinking cursor effect
                setInterval(() => {
                    const cursor = document.querySelector(".hero-content h3 span");
                    cursor.style.opacity = cursor.style.opacity === '0' ? '1' : '0';
                }, 500);
            }
        }
        
        // Start typewriter effect after a short delay
        setTimeout(typeWriter, 1000);
import re

with open('c:/Users/User/Downloads/themed/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. State initialization script
init_script = '''<body>
    <script>
        (function() {
            if (localStorage.getItem('theme') === 'light') {
                document.body.classList.add('light-theme');
            }
        })();
    </script>'''
content = content.replace('<body>', init_script)

# 2. Add CSS Variables
root_vars = '''        :root {
            --background: #0a0a0a;
            --background-alt: #0f0f0f;
            --foreground: #ffffff;
            --accent: #00FFB2; 
            --accent-secondary: #FF0066; 
            --accent-tertiary: #7B61FF; 
            --gray: #888888;
            --gray-light: #a0a0a0;
            
            /* UI Component specifics */
            --card-bg: rgba(15, 15, 15, 0.4);
            --card-border: rgba(255, 255, 255, 0.05);
            --card-shadow: rgba(0, 0, 0, 0.5);
            --card-hover-border: var(--accent);
            --card-glow: rgba(0, 255, 178, 0.2);
            
            --nav-bg: rgba(10, 10, 10, 0.8);
            --nav-border: rgba(255, 255, 255, 0.05);
            
            --shape-opacity: 0.03;
            --glass-blur: 12px;
            
            /* Education Card Overlays */
            --edu-overlay: rgba(0, 0, 0, 0.7);
            --edu-hover-overlay: rgba(0, 0, 0, 0.5);

            --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            --transition-slow: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }

        body.light-theme {
            --background: #F4F7FB;
            --background-alt: #EBF1F8;
            --foreground: #111827;
            --accent: #34C8FF;
            --accent-secondary: #5A8DFF;
            --accent-tertiary: #FF6DA8;
            --gray: #475467;
            --gray-light: #667085;
            
            /* UI Component specifics - Crystal refraction physics */
            --card-bg: rgba(255, 255, 255, 0.25);
            --card-border: rgba(255, 255, 255, 0.45);
            --card-shadow: rgba(31, 41, 55, 0.04);
            --card-hover-border: rgba(52, 200, 255, 0.6);
            --card-glow: rgba(52, 200, 255, 0.12);
            
            --nav-bg: rgba(244, 247, 251, 0.4);
            --nav-border: rgba(255, 255, 255, 0.5);
            
            --shape-opacity: 0.08;
            --glass-blur: 20px;
            
            /* Education Card Overlays - Adapts dark images to light readable backgrounds */
            --edu-overlay: rgba(255, 255, 255, 0.75);
            --edu-hover-overlay: rgba(255, 255, 255, 0.6);
        }

        body, nav, .skill-card, .project-card, .timeline-content, .education-card, footer, .loader, .menu-overlay, a, p, h1, h2, h3, span {
            transition: background 0.8s cubic-bezier(0.25, 1, 0.5, 1),
                        background-color 0.8s cubic-bezier(0.25, 1, 0.5, 1),
                        border-color 0.8s cubic-bezier(0.25, 1, 0.5, 1),
                        color 0.8s cubic-bezier(0.25, 1, 0.5, 1),
                        box-shadow 0.8s cubic-bezier(0.25, 1, 0.5, 1),
                        opacity 0.8s cubic-bezier(0.25, 1, 0.5, 1),
                        transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }
        
        /* Cursor Light Mode adjustments */
        body.light-theme .cursor {
            mix-blend-mode: normal;
            background: rgba(255, 255, 255, 0.3);
            backdrop-filter: blur(4px);
            border-color: var(--accent);
        }
        
        body.light-theme .cursor-dot {
            background: var(--foreground);
            box-shadow: 0 0 10px var(--foreground);
        }
        
        /* Shape opacity */
        .shape {
            opacity: var(--shape-opacity);
        }
        
        /* Skill Card Light Mode */
        body.light-theme .skill-card {
            border-top: 1px solid rgba(255, 255, 255, 0.8);
            box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.6), 0 10px 30px var(--card-shadow);
        }
        body.light-theme .skill-card:hover {
            box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.6), 0 30px 60px var(--card-shadow), 0 0 20px var(--card-glow);
        }
        
        /* Theme Toggle styles */
        #theme-toggle {
            background: transparent;
            border: none;
            cursor: none;
            position: relative;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: var(--transition);
        }
        
        #theme-toggle svg {
            position: absolute;
            width: 22px;
            height: 22px;
            transition: all 0.6s cubic-bezier(0.25, 1, 0.5, 1);
        }
        
        .moon-icon {
            opacity: 1;
            transform: rotate(0deg) scale(1);
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5));
            fill: var(--foreground);
        }
        .sun-icon {
            opacity: 0;
            transform: rotate(90deg) scale(0);
            fill: var(--foreground);
        }
        
        body.light-theme .moon-icon {
            opacity: 0;
            transform: rotate(-90deg) scale(0);
        }
        
        body.light-theme .sun-icon {
            opacity: 1;
            transform: rotate(0deg) scale(1);
            filter: drop-shadow(0 1px 1px rgba(255,255,255,0.8));
        }
        '''
content = re.sub(r':root\s*\{[^}]+\}', root_vars, content, count=1)

# Replace specific hardcoded values with variables
replacements = [
    (r'background: rgba\(10,\s*10,\s*10,\s*0\.8\);', 'background: var(--nav-bg);'),
    (r'backdrop-filter: blur\(10px\);', 'backdrop-filter: blur(var(--glass-blur));'),
    (r'-webkit-backdrop-filter: blur\(10px\);', '-webkit-backdrop-filter: blur(var(--glass-blur));'),
    (r'border-bottom: 1px solid rgba\(255,\s*255,\s*255,\s*0\.05\);', 'border-bottom: 1px solid var(--nav-border);'),
    
    (r'background: rgba\(15,\s*15,\s*15,\s*0\.4\);', 'background: var(--card-bg);'),
    (r'backdrop-filter: blur\(12px\);', 'backdrop-filter: blur(var(--glass-blur));'),
    (r'-webkit-backdrop-filter: blur\(12px\);', '-webkit-backdrop-filter: blur(var(--glass-blur));'),
    (r'border: 1px solid rgba\(255,\s*255,\s*255,\s*0\.05\);', 'border: 1px solid var(--card-border);'),
    
    (r'background: rgba\(15,\s*15,\s*15,\s*0\.6\);', 'background: var(--card-bg);'),
    (r'backdrop-filter: blur\(15px\);', 'backdrop-filter: blur(var(--glass-blur));'),
    (r'-webkit-backdrop-filter: blur\(15px\);', '-webkit-backdrop-filter: blur(var(--glass-blur));'),
    (r'border: 1px solid rgba\(255,\s*255,\s*255,\s*0\.1\);', 'border: 1px solid var(--card-border);'),
    
    (r'box-shadow: 0 -10px 30px rgba\(0,0,0,0\.5\);', 'box-shadow: 0 -10px 30px var(--card-shadow);'),
    (r'box-shadow: 0 30px 60px rgba\(0,\s*255,\s*178,\s*0\.3\);', 'box-shadow: 0 30px 60px var(--card-glow);'),
    (r'box-shadow: 0 20px 40px rgba\(0,\s*255,\s*178,\s*0\.2\),\s*0 0 20px rgba\(0,\s*255,\s*178,\s*0\.1\);', 'box-shadow: 0 20px 40px var(--card-glow), 0 0 20px var(--card-glow);'),
    
    (r'color: white;', 'color: var(--foreground);'),
    (r'background: rgba\(0,\s*0,\s*0,\s*0\.7\);', 'background: var(--edu-overlay);'),
    (r'background: rgba\(0,\s*0,\s*0,\s*0\.5\);', 'background: var(--edu-hover-overlay);'),
    
    (r'background: linear-gradient\(to bottom,\s*transparent 0%,\s*rgba\(10,\s*10,\s*10,\s*0\.9\) 70%\);', 'background: linear-gradient(to bottom, transparent 0%, var(--background) 70%);'),
    (r'opacity:\s*0\.03;\s*z-index:\s*-1;\s*pointer-events:\s*none;\s*animation:\s*floatShape\s*30s\s*ease-in-out\s*infinite;', 'z-index: -1;\n            pointer-events: none;\n            animation: floatShape 30s ease-in-out infinite;')
]
for old, new in replacements:
    content = re.sub(old, new, content)

# STUDENT underline animation
underline_old = r'background: linear-gradient\(90deg,\s*var\(--accent\)\s*0%,\s*var\(--accent-secondary\)\s*100%\);\s*transform:\s*scaleX\(0\);\s*transform-origin:\s*left;\s*animation:\s*expandLine\s*1\.5s\s*ease\s*forwards\s*2\.8s;'
underline_new = '''background: linear-gradient(90deg, var(--accent) 0%, var(--accent-secondary) 50%, var(--accent-tertiary) 100%);
            background-size: 200% 100%;
            transform: scaleX(0);
            transform-origin: left;
            animation: expandLine 1.5s ease forwards 2.8s, liquidFlow 4s linear infinite 2.8s;'''
content = re.sub(underline_old, underline_new, content)

liquid_kf = '''@keyframes expandLine {
            to { transform: scaleX(1); }
        }

        @keyframes liquidFlow {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }'''
content = content.replace('@keyframes expandLine {\n            to { transform: scaleX(1); }\n        }', liquid_kf)

# Insert Toggle Button in Navbar
nav_old = '''<div class="menu-btn">'''
nav_new = '''<div style="display: flex; align-items: center; gap: 1.5rem;">
            <button id="theme-toggle" aria-label="Toggle Theme">
                <svg class="sun-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 3V4M12 20V21M4 12H3M21 12H20M6.31412 6.31412L5.60702 5.60702M17.6859 17.6859L18.393 18.393M6.31412 17.6859L5.60702 18.393M17.6859 6.31412L18.393 5.60702M16 12C16 14.2091 14.2091 16 12 16C9.79086 16 8 14.2091 8 12C8 9.79086 9.79086 8 12 8C14.2091 8 16 9.79086 16 12Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <svg class="moon-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
            </button>
            <div class="menu-btn">'''
content = content.replace(nav_old, nav_new)
content = content.replace('</div>\n    </nav>', '</div>\n        </div>\n    </nav>')

# Theme Toggle Logic
toggle_js = '''// --- THEME TOGGLE ---
            const themeToggleBtn = document.getElementById('theme-toggle');
            themeToggleBtn.addEventListener('click', () => {
                document.body.classList.toggle('light-theme');
                const newTheme = document.body.classList.contains('light-theme') ? 'light' : 'dark';
                localStorage.setItem('theme', newTheme);
            });
            
            // --- REVEAL ON SCROLL'''
content = content.replace('// --- REVEAL ON SCROLL', toggle_js)

# Add elements to custom cursor hover list
content = content.replace("'a, button, .menu-btn, .project-card, .cta-button, .contact-link, .skill-card, .social-links a'", "'a, button, .menu-btn, .project-card, .cta-button, .contact-link, .skill-card, .social-links a, #theme-toggle'")

with open('c:/Users/User/Downloads/themed/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

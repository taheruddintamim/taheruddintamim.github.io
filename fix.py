import re

with open('c:/Users/User/Downloads/themed/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update variables in :root and body.light-theme
root_vars_new = '''        :root {
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
            
            /* New variables for layout */
            --footer-end: #050505;
            --menu-bg: rgba(10, 10, 10, 0.9);

            --transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
            --transition-slow: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }'''

content = re.sub(r'\s*:\s*root\s*\{.*?(?=body\.light-theme)', root_vars_new + '\n\n', content, flags=re.DOTALL)

light_theme_new = '''        body.light-theme {
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
            --edu-overlay: rgba(255, 255, 255, 0.2);
            --edu-hover-overlay: rgba(255, 255, 255, 0.1);
            
            --footer-end: #E2E8F0;
            --menu-bg: rgba(244, 247, 251, 0.95);
        }'''
content = re.sub(r'body\.light-theme\s*\{.*?(?=body, nav, \.skill-card)', light_theme_new + '\n\n        ', content, flags=re.DOTALL)

# 2. Add extra CSS logic for Nav, Menu Texture, Titles, and Education text shadows
extra_css = '''
        /* Extra Refinements */
        body.light-theme nav {
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.04), inset 0 -1px 0 rgba(255, 255, 255, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.8);
            border-bottom: 1px solid rgba(255,255,255,0.6);
            background: rgba(255, 255, 255, 0.4);
        }
        
        body.light-theme .section-title {
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.06);
            letter-spacing: 0.02em;
        }

        .menu-overlay {
            background: var(--menu-bg) !important;
        }
        
        .menu-overlay::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: linear-gradient(45deg, var(--card-border) 25%, transparent 25%, transparent 50%, var(--card-border) 50%, var(--card-border) 75%, transparent 75%, transparent);
            background-size: 60px 60px;
            opacity: 0.06;
            pointer-events: none;
            z-index: -1;
            animation: moveTexture 20s linear infinite;
        }
        
        @keyframes moveTexture {
            0% { background-position: 0 0; }
            100% { background-position: 60px 60px; }
        }

        body.light-theme .education-level, 
        body.light-theme .education-details, 
        body.light-theme .education-year {
            text-shadow: 0 1px 4px rgba(255, 255, 255, 0.95), 0 0 15px rgba(255, 255, 255, 0.9);
            font-weight: 600;
        }
        
        body.light-theme .education-card.ssc-card,
        body.light-theme .education-card.designer-card {
            border: 1px solid rgba(255,255,255,0.8);
            box-shadow: inset 0 0 20px rgba(255,255,255,0.5), 0 15px 30px rgba(0,0,0,0.05);
        }

        .logo svg {
            width: 45px !important;
            height: 45px !important;
            transition: transform 0.4s ease;
        }
        .logo-t-path {
            fill: var(--foreground);
            transition: var(--transition);
        }
        .logo-dot-path {
            stroke: var(--accent);
            transition: var(--transition);
        }
        
        footer {
            background: linear-gradient(to bottom, var(--background) 0%, var(--footer-end) 100%) !important;
        }
        
        '''

content = content.replace('/* Shape opacity */', extra_css + '\n        /* Shape opacity */')

# 3. Logo HTML Update
logo_old = '''<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M25 20H75V35H60V80H40V35H25V20Z" fill="white"/>
                <path d="M78 55C83.5228 55 88 59.4772 88 65C88 70.5228 83.5228 75 78 75C72.4772 75 68 70.5228 68 65C68 59.4772 72.4772 55 78 55Z" stroke="#00FFB2" stroke-width="4"/>
            </svg>'''
            
logo_new = '''<svg viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M25 20H75V35H60V80H40V35H25V20Z" class="logo-t-path"/>
                <path d="M78 55C83.5228 55 88 59.4772 88 65C88 70.5228 83.5228 75 78 75C72.4772 75 68 70.5228 68 65C68 59.4772 72.4772 55 78 55Z" class="logo-dot-path" stroke-width="4"/>
            </svg>'''

content = content.replace(logo_old, logo_new)

# 4. Remove old menu-overlay background and footer background if present to avoid conflicts
content = re.sub(r'\.menu-overlay\s*\{[^}]*background:\s*rgba\(10,\s*10,\s*10,\s*0\.6\);', lambda m: m.group(0).replace('background: rgba(10, 10, 10, 0.6);', '/* background dynamically set */'), content)
content = re.sub(r'footer\s*\{[^}]*background:\s*linear-gradient\(to bottom,\s*var\(--background\)\s*0%,\s*#050505\s*100%\);', lambda m: m.group(0).replace('background: linear-gradient(to bottom, var(--background) 0%, #050505 100%);', '/* background dynamically set */'), content)

with open('c:/Users/User/Downloads/themed/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")

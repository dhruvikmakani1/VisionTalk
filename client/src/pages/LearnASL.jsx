import { useState, useMemo } from 'react'
import { FaMagnifyingGlass, FaHandBackFist } from 'react-icons/fa6'
import './LearnASL.css'

// ASL sign data
const ASL_SIGNS = [
  ...Array.from({ length: 26 }, (_, i) => ({
    char: String.fromCharCode(65 + i),
    type: 'letter',
    tip: `Form the ASL letter ${String.fromCharCode(65 + i)}`,
  })),
  ...Array.from({ length: 10 }, (_, i) => ({
    char: String(i),
    type: 'number',
    tip: `Show the number ${i} in ASL`,
  })),
]

// ASL hand descriptions for learning
const ASL_DESCRIPTIONS = {
  'A': 'Make a fist with thumb resting on the side',
  'B': 'Hold fingers straight up, thumb tucked across palm',
  'C': 'Curve hand into a C shape',
  'D': 'Touch thumb to middle/ring/pinky fingertips, index points up',
  'E': 'Curl all fingers down, thumb tucked under',
  'F': 'Touch index to thumb forming a circle, other fingers up',
  'G': 'Point index finger sideways, thumb parallel above',
  'H': 'Point index and middle finger sideways together',
  'I': 'Make a fist, extend only the pinky finger up',
  'J': 'Like I, but trace a J motion with pinky',
  'K': 'Index and middle fingers up in a V, thumb between them',
  'L': 'L-shape with thumb and index finger',
  'M': 'Tuck thumb under first three fingers',
  'N': 'Tuck thumb under first two fingers',
  'O': 'All fingertips touch thumb forming an O',
  'P': 'Like K but pointing downward',
  'Q': 'Like G but pointing downward',
  'R': 'Cross index over middle finger, both pointing up',
  'S': 'Make a fist with thumb over fingers',
  'T': 'Thumb tucked between index and middle finger',
  'U': 'Hold index and middle fingers up together',
  'V': 'Peace sign — index and middle fingers in a V',
  'W': 'Index, middle, and ring fingers up and spread',
  'X': 'Hook the index finger, other fingers in fist',
  'Y': 'Extend thumb and pinky, other fingers curled',
  'Z': 'Draw a Z in the air with index finger',
  '0': 'Form an O shape with all fingers touching thumb',
  '1': 'Point index finger up, other fingers curled',
  '2': 'Peace sign — index and middle fingers up',
  '3': 'Thumb, index, and middle fingers extended',
  '4': 'Four fingers up, thumb tucked into palm',
  '5': 'All five fingers spread open',
  '6': 'Touch thumb to pinky, other three fingers up',
  '7': 'Touch thumb to ring finger, other fingers up',
  '8': 'Touch thumb to middle finger, other fingers up',
  '9': 'Touch thumb to index finger, other fingers up',
}

// Hand emoji representations (Fallback for numbers)
const HAND_EMOJIS = {
  '0': '👌', '1': '☝️', '2': '✌️', '3': '🤟', '4': '🖐',
  '5': '🖐', '6': '🤙', '7': '🤟', '8': '🤞', '9': '👌',
}

// Map characters to their actual sign images in /public/sign
const getSignImage = (char) => {
  if (char === 'J') return '/sign/J.jpg';
  const digits = '0123456789';
  if (digits.includes(char)) {
    if (char === '0') return '/sign/0.webp';
    return `/sign/${char}.png`;
  }
  if (char >= 'A' && char <= 'Z') return `/sign/${char}.webp`;
  return null;
}

export default function LearnASL() {
  const [filter, setFilter] = useState('all')
  const [search, setSearch] = useState('')
  const [selectedSign, setSelectedSign] = useState(null)

  const filteredSigns = useMemo(() => {
    return ASL_SIGNS.filter(sign => {
      const matchesFilter = filter === 'all' || sign.type === filter
      const matchesSearch = sign.char.toLowerCase().includes(search.toLowerCase())
      return matchesFilter && matchesSearch
    })
  }, [filter, search])

  return (
    <div className="learn-page page-enter">
      <div className="container">
        {/* ── Header ── */}
        <div className="learn-header">
          <h1>Learn <span className="gradient-text">ASL Signs</span></h1>
          <p>Explore all 36 supported American Sign Language signs. Click any card to learn more.</p>
        </div>

        {/* ── Controls ── */}
        <div className="learn-controls">
          <div className="filter-tabs">
            {['all', 'letter', 'number'].map(f => (
              <button
                key={f}
                className={`filter-tab ${filter === f ? 'active' : ''}`}
                onClick={() => setFilter(f)}
              >
                {f === 'all' ? 'All (36)' : f === 'letter' ? 'Alphabet (A-Z)' : 'Numbers (0-9)'}
              </button>
            ))}
          </div>

          <div className="search-box glass-card">
            <FaMagnifyingGlass className="search-icon" />
            <input
              type="text"
              placeholder="Search signs..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              id="search-signs"
            />
          </div>
        </div>

        {/* ── Grid ── */}
        <div className="signs-grid">
          {filteredSigns.map((sign, index) => (
            <button
              key={sign.char}
              className={`sign-card glass-card ${selectedSign?.char === sign.char ? 'selected' : ''}`}
              onClick={() => setSelectedSign(selectedSign?.char === sign.char ? null : sign)}
              style={{ animationDelay: `${index * 0.03}s` }}
              id={`sign-${sign.char}`}
            >
              <div className="sign-visual">
                {getSignImage(sign.char) ? (
                  <img src={getSignImage(sign.char)} alt={`ASL ${sign.char}`} className="sign-img" />
                ) : (
                  <span className="sign-emoji">{HAND_EMOJIS[sign.char] || '✋'}</span>
                )}
              </div>
              <div className="sign-char">{sign.char}</div>
              <div className="sign-type">{sign.type}</div>
            </button>
          ))}
        </div>

        {/* ── Detail Modal ── */}
        {selectedSign && (
          <div className="sign-detail-overlay" onClick={() => setSelectedSign(null)}>
            <div className="sign-detail glass" onClick={(e) => e.stopPropagation()}>
              <button className="detail-close" onClick={() => setSelectedSign(null)}>×</button>
              <div className="detail-visual">
                {getSignImage(selectedSign.char) ? (
                  <img src={getSignImage(selectedSign.char)} alt={`ASL ${selectedSign.char}`} className="detail-img" />
                ) : (
                  <span className="detail-emoji">{HAND_EMOJIS[selectedSign.char] || '✋'}</span>
                )}
              </div>
              <h2 className="detail-char gradient-text">{selectedSign.char}</h2>
              <span className="detail-type">{selectedSign.type === 'letter' ? 'Alphabet Letter' : 'Number'}</span>
              <div className="detail-divider" />
              <div className="detail-section">
                <h4><FaHandBackFist /> How to Sign</h4>
                <p>{ASL_DESCRIPTIONS[selectedSign.char]}</p>
              </div>
              <div className="detail-tip">
                💡 Practice this sign in the <a href="/practice">Practice Mode</a> to get real-time AI feedback!
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

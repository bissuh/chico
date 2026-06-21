import {AbsoluteFill, useCurrentFrame, Img, staticFile} from 'remotion';
import {loadFont as loadInter} from '@remotion/google-fonts/Inter';

const {fontFamily: INTER} = loadInter();

const C = {
  bg: '#2A7A6D',
  ink: '#FFFFFF',
  sub: 'rgba(255,255,255,0.85)',
  accent: '#CFEFE7',
  line: 'rgba(255,255,255,0.24)',
  card: 'rgba(255,255,255,0.10)',
};

const Texture: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill
      style={{
        opacity: 0.06,
        mixBlendMode: 'soft-light',
        backgroundImage: `radial-gradient(circle at 15% 25%, #fff 0.5px, transparent 1.5px)`,
        backgroundSize: '6px 6px',
        pointerEvents: 'none',
      }}
    />
  );
};

// concentric "moat" rings around the business core. A rival has to cross all three.
const Bullseye: React.FC = () => {
  const cx = 340;
  const cy = 340;
  const rings = [
    {r: 300, fill: 'rgba(255,255,255,0.05)'},
    {r: 215, fill: 'rgba(255,255,255,0.08)'},
    {r: 130, fill: 'rgba(255,255,255,0.12)'},
  ];
  return (
    <svg width="640" height="680" viewBox="0 0 680 680" style={{flexShrink: 0}}>
      {rings.map((ring, i) => (
        <circle key={i} cx={cx} cy={cy} r={ring.r} fill={ring.fill} stroke={C.line} strokeWidth={2.5} />
      ))}
      {/* core: you */}
      <circle cx={cx} cy={cy} r={70} fill={C.accent} />
      <text x={cx} y={cy + 12} textAnchor="middle" style={{fontFamily: INTER, fontWeight: 800, fontSize: 40, fill: C.bg}}>
        YOU
      </text>
      {/* number badges at 12 o'clock of each ring, outer = 1 */}
      {[
        {y: 340 - 300, n: '1'},
        {y: 340 - 215, n: '2'},
        {y: 340 - 130, n: '3'},
      ].map((b, i) => (
        <g key={i}>
          <circle cx={cx} cy={b.y} r={26} fill={C.bg} stroke={C.accent} strokeWidth={3} />
          <text x={cx} y={b.y + 11} textAnchor="middle" style={{fontFamily: INTER, fontWeight: 800, fontSize: 32, fill: C.accent}}>
            {b.n}
          </text>
        </g>
      ))}
    </svg>
  );
};

const Legend: React.FC<{n: string; name: string; hook: string}> = ({n, name, hook}) => (
  <div style={{display: 'flex', gap: 26, alignItems: 'center'}}>
    <div
      style={{
        width: 62,
        height: 62,
        borderRadius: 31,
        flexShrink: 0,
        background: C.card,
        border: `3px solid ${C.accent}`,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontFamily: INTER,
        fontWeight: 800,
        fontSize: 32,
        color: C.accent,
      }}
    >
      {n}
    </div>
    <div>
      <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 48, color: C.ink, lineHeight: 1.0, letterSpacing: '-0.01em'}}>{name}</div>
      <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 30, color: C.sub, marginTop: 8}}>{hook}</div>
    </div>
  </div>
);

export const MoatsDiagram: React.FC = () => {
  return (
    <AbsoluteFill style={{backgroundColor: C.bg, fontFamily: INTER}}>
      <Texture />
      <AbsoluteFill style={{padding: 96, display: 'flex', flexDirection: 'column'}}>
        {/* header */}
        <div>
          <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 26, letterSpacing: '0.18em', textTransform: 'uppercase', color: C.accent}}>Will it last?</div>
          <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 86, color: C.ink, lineHeight: 1.0, letterSpacing: '-0.02em', marginTop: 12}}>
            Stack your moats
          </div>
          <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 34, color: C.sub, marginTop: 16}}>
            A rival has to cross all three to reach your customers.
          </div>
        </div>

        {/* diagram + legend */}
        <div style={{flex: 1, display: 'flex', alignItems: 'center', gap: 70}}>
          <Bullseye />
          <div style={{flex: 1, display: 'flex', flexDirection: 'column', gap: 44}}>
            <Legend n="1" name="Counter-positioning" hook="They can't copy it without killing their model." />
            <Legend n="2" name="Switching costs" hook="Leaving you is painful. The habit holds." />
            <Legend n="3" name="Data + learning loop" hook="It compounds. Every month you pull further ahead." />
          </div>
        </div>

        {/* footer */}
        <div style={{paddingTop: 28, borderTop: `2px solid ${C.line}`, display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
          <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 32, color: C.ink}}>
            Value comes from the test. Potential comes from the moat.
          </div>
          <div style={{display: 'flex', alignItems: 'center', gap: 14, opacity: 0.9}}>
            <Img src={staticFile('logo-b.png')} style={{height: 42, width: 'auto'}} />
            <div style={{fontFamily: INTER, fontWeight: 600, fontSize: 26, color: C.sub}}>@thebillionperson</div>
          </div>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

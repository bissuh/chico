import {AbsoluteFill, useCurrentFrame, Img, staticFile} from 'remotion';
import {loadFont as loadInter} from '@remotion/google-fonts/Inter';

const {fontFamily: INTER} = loadInter();

const C = {
  bg: '#2A7A6D',
  ink: '#FFFFFF',
  sub: 'rgba(255,255,255,0.85)',
  accent: '#CFEFE7',
  line: 'rgba(255,255,255,0.22)',
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

const Pips: React.FC = () => (
  <div style={{display: 'flex', gap: 13, marginTop: 26}}>
    {[0, 1, 2, 3, 4].map((i) => (
      <div key={i} style={{width: 28, height: 28, borderRadius: 14, border: `3px solid ${C.accent}`, background: 'transparent'}} />
    ))}
  </div>
);

const Column: React.FC<{tag: string; name: string; desc: string; showDivider: boolean}> = ({tag, name, desc, showDivider}) => (
  <div style={{flex: 1, display: 'flex'}}>
    {showDivider ? <div style={{width: 2, background: C.line, marginRight: 56}} /> : null}
    <div style={{flex: 1, display: 'flex', flexDirection: 'column'}}>
      <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 24, letterSpacing: '0.16em', textTransform: 'uppercase', color: C.accent}}>{tag}</div>
      <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 58, color: C.ink, letterSpacing: '-0.01em', marginTop: 16, lineHeight: 1.0}}>{name}</div>
      <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 31, color: C.sub, marginTop: 18, lineHeight: 1.3, minHeight: 84}}>{desc}</div>
      <Pips />
    </div>
  </div>
);

export const TriangleScorecard: React.FC = () => {
  return (
    <AbsoluteFill style={{backgroundColor: C.bg, fontFamily: INTER}}>
      <Texture />
      <AbsoluteFill style={{padding: 96, display: 'flex', flexDirection: 'column'}}>
        {/* header */}
        <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start'}}>
          <div style={{maxWidth: 1250}}>
            <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 26, letterSpacing: '0.18em', textTransform: 'uppercase', color: C.accent}}>The Test</div>
            <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 92, color: C.ink, lineHeight: 1.0, letterSpacing: '-0.02em', marginTop: 14}}>
              The Founder&rsquo;s Triangle
            </div>
            <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 34, color: C.sub, marginTop: 18}}>
              Score each corner 1 to 5. One green and you start.
            </div>
          </div>
          {/* triangle motif (decorative, away from text) */}
          <svg width="200" height="172" viewBox="0 0 200 172" style={{flexShrink: 0, marginTop: 6}}>
            <polygon points="100,12 12,160 188,160" fill="none" stroke={C.line} strokeWidth={3} />
            <circle cx="100" cy="12" r="9" fill={C.accent} />
            <circle cx="12" cy="160" r="9" fill={C.accent} />
            <circle cx="188" cy="160" r="9" fill={C.accent} />
          </svg>
        </div>

        {/* three columns */}
        <div style={{flex: 1, display: 'flex', alignItems: 'center', gap: 56, marginTop: 20}}>
          <Column tag="Corner 1" name="DOMAIN" desc="Years inside an industry. You start at year five while they start at zero." showDivider={false} />
          <Column tag="Corner 2" name="DEPTH" desc="The craft that feels like play to you and like work to everyone else." showDivider />
          <Column tag="Corner 3" name="DISTRIBUTION" desc="Your unfair way to reach customers: an audience, a network, a partner." showDivider />
        </div>

        {/* footer */}
        <div style={{paddingTop: 30, borderTop: `2px solid ${C.line}`, display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
          <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 34, color: C.ink}}>
            One corner at 4-5: start. All three green: floor it.
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

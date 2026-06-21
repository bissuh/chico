import {AbsoluteFill, Img, staticFile} from 'remotion';
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

const Texture: React.FC = () => (
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

const Card: React.FC<{name: string; money: string; stack: string; dist: string}> = ({name, money, stack, dist}) => (
  <div
    style={{
      flex: 1,
      background: C.card,
      border: `2px solid ${C.line}`,
      borderRadius: 28,
      padding: 56,
      display: 'flex',
      flexDirection: 'column',
    }}
  >
    <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 54, color: C.ink, letterSpacing: '-0.01em'}}>{name}</div>
    <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 132, color: C.accent, lineHeight: 0.95, letterSpacing: '-0.03em', marginTop: 14}}>{money}</div>
    <div style={{fontFamily: INTER, fontWeight: 600, fontSize: 26, color: C.sub, marginTop: 4, textTransform: 'uppercase', letterSpacing: 2}}>per month</div>
    <div style={{fontFamily: INTER, fontWeight: 600, fontSize: 32, color: C.ink, marginTop: 28}}>{stack}</div>
    <div style={{marginTop: 'auto', paddingTop: 24, borderTop: `2px solid ${C.line}`, fontFamily: INTER, fontWeight: 500, fontSize: 30, color: C.sub}}>
      <span style={{color: C.accent, fontWeight: 700}}>Distribution: </span>
      {dist}
    </div>
  </div>
);

export const ProofStrip: React.FC = () => (
  <AbsoluteFill style={{backgroundColor: C.bg, fontFamily: INTER}}>
    <Texture />
    <AbsoluteFill style={{padding: 96, display: 'flex', flexDirection: 'column'}}>
      <div>
        <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 26, letterSpacing: '0.18em', textTransform: 'uppercase', color: C.accent}}>Proof it's a pattern</div>
        <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 86, color: C.ink, lineHeight: 1.0, letterSpacing: '-0.02em', marginTop: 12}}>
          Same shape. Different speed.
        </div>
      </div>

      <div style={{flex: 1, display: 'flex', alignItems: 'stretch', gap: 48, marginTop: 52}}>
        <Card name="AudioPen" money="$15K" stack="Bubble + OpenAI · 12-hour build" dist="months building in public" />
        <Card name="Formula Bot" money="$226K" stack="Bubble · weekend build" dist="one Reddit post" />
      </div>

      <div style={{paddingTop: 28, borderTop: `2px solid ${C.line}`, display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
        <div style={{fontFamily: INTER, fontWeight: 700, fontSize: 32, color: C.ink}}>
          Boring problem. Thin wrapper. Cheap AI. Real distribution.
        </div>
        <div style={{display: 'flex', alignItems: 'center', gap: 14, opacity: 0.9}}>
          <Img src={staticFile('logo-b.png')} style={{height: 42, width: 'auto'}} />
          <div style={{fontFamily: INTER, fontWeight: 600, fontSize: 26, color: C.sub}}>@thebillionperson</div>
        </div>
      </div>
    </AbsoluteFill>
  </AbsoluteFill>
);

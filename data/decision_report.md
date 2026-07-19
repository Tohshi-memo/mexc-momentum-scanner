# Decision Report

- generated_at: 2026-07-19T10:31:11.005137+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9023**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9023, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.17% | **-2.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/19 | 21.1% | +4.03% | **+0.85%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.75% | **+0.60%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.17% | **+2.17%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.84% | **+1.99%** |
| LIMIT_3PCT_LONG | 7/20 | 35.0% | +2.63% | **+0.92%** |
| LIMIT_2PCT_LONG | 8/20 | 40.0% | +1.30% | **+0.52%** |
| LIMIT_ATR_LONG | 6/20 | 30.0% | +0.95% | **+0.29%** |

## 2. $100 Live Portfolio

- 残高: **$110.80** / 初期 $100.00 (+10.80%)
- 確定トレード: 117件 (TP 43 / SL 69 / EXP 5)
- 最新: SKYAI/USDT:USDT EXPIRED PnL +0.79% 残高後 $110.80
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$398.31** / 初期 $100.00 (+298.31%)
- 確定: 3085件 (Win 966 / Loss 981 / Flat 1138) / skip 2499件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $398.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.84** / 初期 $100.00 (+26.84%)
- 確定: 984件 (Win 252 / Loss 201 / Flat 531) / skip 1450件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1624 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $126.84

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.40** / 初期 $100.00 (+0.40%)
- 確定: 225件 (Win 72 / Loss 113 / Flat 40) / pending 4件 / skip 265件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000481 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.40

## 6. Latest Market Context

- 更新: 2026-07-19T10:31:04.895176+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=64606.5
- Funnel: target 885 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +93.33% | $48,681,693.53 |
| BANK/USDT:USDT | +82.05% | $22,636,134.87 |
| TLM/USDT:USDT | +44.33% | $6,064,752.87 |
| B/USDT:USDT | +43.32% | $42,247,804.13 |
| TAG/USDT:USDT | +28.52% | $4,015,456.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +2.13% | +1.96% |
| BANK/USDT:USDT | below_1h_threshold | +1.70% | +1.53% |
| JASMY/USDT:USDT | below_1h_threshold | +1.42% | +1.25% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.30% | +1.13% |
| PI/USDT:USDT | below_1h_threshold | +1.22% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

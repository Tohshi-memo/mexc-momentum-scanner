# Decision Report

- generated_at: 2026-07-02T06:54:32.905416+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8053**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.20% / filled 20/20。**
- 全期間 MARKET基準: n=8053, expectancy=-0.03%
- 直近20件 MARKET基準: n=20, expectancy=+3.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.20% | **+3.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.20% | **+3.20%** |
| ASK | 20/20 | 100.0% | +3.19% | **+3.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +0.72% | **+0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 8/20 | 40.0% | +2.89% | **+1.16%** |
| LIMIT_9PCT_LONG | 10/20 | 50.0% | +0.77% | **+0.38%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -1.72% | **-0.17%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | -0.33% | **-0.20%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | -0.80% | **-0.68%** |

## 2. $100 Live Portfolio

- 残高: **$102.64** / 初期 $100.00 (+2.64%)
- 確定トレード: 47件 (TP 17 / SL 29 / EXP 1)
- 最新: AGLD/USDT:USDT TP_HIT PnL +8.00% 残高後 $102.64
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2170件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 545件 (Win 136 / Loss 131 / Flat 278) / skip 919件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0561 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T06:54:26.059208+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=60287.0
- Funnel: target 830 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +132.38% | $87,286,228.57 |
| BIRB/USDT:USDT | +66.06% | $4,348,947.57 |
| RIF/USDT:USDT | +38.24% | $5,591,659.65 |
| TLM/USDT:USDT | +31.22% | $8,116,604.52 |
| SLX/USDT:USDT | +18.33% | $9,219,456.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| M/USDT:USDT | below_1h_threshold | +3.85% | +4.17% |
| SYN/USDT:USDT | below_1h_threshold | +3.70% | +4.02% |
| SLX/USDT:USDT | below_1h_threshold | +2.31% | +2.62% |
| RIF/USDT:USDT | below_1h_threshold | +1.29% | +1.61% |
| PYTH/USDT:USDT | below_1h_threshold | +1.11% | +1.43% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

# Decision Report

- generated_at: 2026-06-23T16:36:40.954972+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7431**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.60% / filled 20/20。**
- 全期間 MARKET基準: n=7431, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/19 | 26.3% | +2.87% | **+0.75%** |
| MARKET | 20/20 | 100.0% | +0.60% | **+0.60%** |
| ASK | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.64% | **+0.32%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.36% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +3.18% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.34% | **+0.24%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$228.71** / 初期 $100.00 (+128.71%)
- 確定: 2081件 (Win 617 / Loss 690 / Flat 774) / skip 1911件
- 成長率目線: 平均log +0.000398 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $228.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.73** / 初期 $100.00 (+6.73%)
- 確定: 321件 (Win 92 / Loss 87 / Flat 142) / skip 521件
- 成長率目線: 平均log +0.000203 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0222 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.73

## 5. Latest Market Context

- 更新: 2026-06-23T16:36:36.418088+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=62587.7
- Funnel: target 802 → liquid 171 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MMT/USDT:USDT | +3.41% | $1,969,670.03 |
| ESPORTS/USDT:USDT | +3.27% | $6,450,408.14 |
| CLO/USDT:USDT | +3.10% | $4,579,347.96 |
| ARX/USDT:USDT | +2.77% | $18,023,209.30 |
| MVLL/USDT:USDT | +2.65% | $1,694,703.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.42% | +3.21% |
| MMT/USDT:USDT | below_1h_threshold | +3.41% | +3.20% |
| CLO/USDT:USDT | below_1h_threshold | +3.10% | +2.89% |
| ARX/USDT:USDT | below_1h_threshold | +2.75% | +2.54% |
| MVLL/USDT:USDT | below_1h_threshold | +2.66% | +2.45% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

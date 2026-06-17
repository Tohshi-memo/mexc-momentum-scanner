# Decision Report

- generated_at: 2026-06-17T23:03:24.891525+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6974**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.73% / filled 20/20。**
- 全期間 MARKET基準: n=6974, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.77% | **+0.77%** |
| MARKET | 20/20 | 100.0% | +0.73% | **+0.73%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.36% | **+0.28%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.56% | **+0.20%** |
| LIMIT_ATR | 14/20 | 70.0% | -0.13% | **-0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.32% | **+1.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$101.48** / 初期 $100.00 (+1.48%)
- 確定トレード: 12件 (TP 5 / SL 7 / EXP 0)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.48
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$200.70** / 初期 $100.00 (+100.70%)
- 確定: 1821件 (Win 497 / Loss 573 / Flat 751) / skip 1714件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $200.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$103.24** / 初期 $100.00 (+3.24%)
- 確定: 247件 (Win 65 / Loss 62 / Flat 120) / skip 138件
- 成長率目線: 平均log +0.000129 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0829 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $103.24

## 5. Latest Market Context

- 更新: 2026-06-17T23:03:19.583874+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=64334.0
- Funnel: target 790 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| O/USDT:USDT | +88.17% | $1,406,538.96 |
| ESPORTS/USDT:USDT | +84.67% | $17,762,787.62 |
| SYN/USDT:USDT | +40.93% | $4,057,364.24 |
| RE/USDT:USDT | +17.25% | $1,814,602.78 |
| MITO/USDT:USDT | +13.26% | $1,631,476.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BRETT/USDT:USDT | below_1h_threshold | +0.55% | +0.44% |
| AGT/USDT:USDT | below_1h_threshold | +0.49% | +0.38% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.48% | +0.38% |
| RE/USDT:USDT | below_1h_threshold | +0.46% | +0.35% |
| WLD/USDT:USDT | below_1h_threshold | +0.46% | +0.35% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

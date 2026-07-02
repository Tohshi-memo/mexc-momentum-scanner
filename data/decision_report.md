# Decision Report

- generated_at: 2026-07-02T08:50:19.006791+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8055**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.20% / filled 20/20。**
- 全期間 MARKET基準: n=8055, expectancy=-0.02%
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
| LIMIT_1PCT | 12/20 | 60.0% | +0.26% | **+0.15%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 7/20 | 35.0% | +2.16% | **+0.76%** |
| LIMIT_9PCT_LONG | 10/20 | 50.0% | +0.26% | **+0.13%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | -0.75% | **-0.15%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | -0.33% | **-0.20%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | -0.80% | **-0.68%** |

## 2. $100 Live Portfolio

- 残高: **$103.66** / 初期 $100.00 (+3.66%)
- 確定トレード: 48件 (TP 18 / SL 29 / EXP 1)
- 最新: TLM/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.66
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$284.67** / 初期 $100.00 (+184.67%)
- 確定: 2444件 (Win 754 / Loss 816 / Flat 874) / skip 2172件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $284.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.14** / 初期 $100.00 (+5.14%)
- 確定: 546件 (Win 136 / Loss 131 / Flat 279) / skip 920件
- 成長率目線: 平均log +0.000092 / 幾何平均 +0.009% per trade / maxDD +3.53%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0466 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $105.14

## 5. Latest Market Context

- 更新: 2026-07-02T08:50:12.670069+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.58% price=60472.3
- Funnel: target 829 → liquid 167 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.8 >= 65=1, 4h RSI 72.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TAIKO/USDT:USDT | +85.47% | $96,921,132.62 |
| BREV/USDT:USDT | +51.95% | $2,163,748.00 |
| BIRB/USDT:USDT | +50.71% | $5,228,336.47 |
| RIF/USDT:USDT | +28.14% | $5,976,583.54 |
| TLM/USDT:USDT | +25.80% | $8,621,687.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.87% | +1.29% |
| PENDLE/USDT:USDT | below_1h_threshold | +1.73% | +1.15% |
| GRAM/USDT:USDT | below_1h_threshold | +1.61% | +1.03% |
| ENA/USDT:USDT | below_1h_threshold | +1.28% | +0.70% |
| ADA/USDT:USDT | below_1h_threshold | +0.97% | +0.39% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

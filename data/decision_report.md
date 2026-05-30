# Decision Report

- generated_at: 2026-05-30T00:39:53.458284+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5082**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.47% / filled 20/20。**
- 全期間 MARKET基準: n=5082, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+1.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.55% | **+1.55%** |
| MARKET | 20/20 | 100.0% | +1.47% | **+1.47%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.90% | **+0.72%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.72% | **+0.32%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.70% | **+0.51%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.22% | **-0.12%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 743件 (Win 175 / Loss 226 / Flat 342) / skip 900件
- 成長率目線: 平均log +0.000308 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-30T00:39:50.271365+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=73477.3
- Funnel: target 773 → liquid 147 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.3 >= 65=1, 4h RSI 81.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XLM/USDT:USDT | +22.34% | $409,284,307.17 |
| OL/USDT:USDT | +17.11% | $1,467,194.72 |
| BASED/USDT:USDT | +16.63% | $2,480,072.42 |
| LAB/USDT:USDT | +15.43% | $131,204,952.93 |
| HBAR/USDT:USDT | +13.70% | $33,352,910.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +4.84% | +4.78% |
| BSB/USDT:USDT | below_1h_threshold | +4.63% | +4.56% |
| SEI/USDT:USDT | below_1h_threshold | +3.15% | +3.08% |
| VET/USDT:USDT | below_1h_threshold | +1.79% | +1.73% |
| BAT/USDT:USDT | below_1h_threshold | +1.59% | +1.52% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

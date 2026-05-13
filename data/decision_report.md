# Decision Report

- generated_at: 2026-05-13T16:11:46.253785+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4235**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.32% / filled 20/20。**
- 全期間 MARKET基準: n=4235, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.43% | **+1.35%** |
| MARKET | 20/20 | 100.0% | +1.32% | **+1.32%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.62% | **+1.21%** |
| ASK | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_BB3S | 7/18 | 38.9% | +1.97% | **+0.76%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.98% | **+0.69%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.71% | **+0.60%** |
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.27% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 342件 (Win 94 / Loss 125 / Flat 123) / skip 454件
- 成長率目線: 平均log +0.000513 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-13T16:11:39.942396+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=78790.0
- Funnel: target 765 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UP/USDT:USDT | +6.24% | $5,253,430.97 |
| BILL/USDT:USDT | +5.51% | $26,429,981.23 |
| LAB/USDT:USDT | +3.44% | $155,847,895.06 |
| COS/USDT:USDT | +3.29% | $2,341,750.77 |
| VELO/USDT:USDT | +3.18% | $1,965,088.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COS/USDT:USDT | below_1h_threshold | +4.57% | +4.57% |
| LAB/USDT:USDT | below_1h_threshold | +3.46% | +3.47% |
| VELO/USDT:USDT | below_1h_threshold | +3.18% | +3.19% |
| UB/USDT:USDT | below_1h_threshold | +3.15% | +3.16% |
| PLAY/USDT:USDT | below_1h_threshold | +2.24% | +2.25% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

# Decision Report

- generated_at: 2026-05-08T04:37:35.719404+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3734**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.86% / filled 20/20。**
- 全期間 MARKET基準: n=3734, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=+2.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.86% | **+2.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.86% | **+2.86%** |
| LIMIT_1PCT | 16/20 | 80.0% | +3.00% | **+2.40%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.58% | **+1.81%** |
| ASK | 20/20 | 100.0% | +1.65% | **+1.65%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.58% | **+1.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.87% | **+0.48%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.51% | **+0.31%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | +0.96% | **+0.29%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$98.83** / 初期 $100.00 (-1.17%)
- 確定トレード: 24件 (TP 6 / SL 16 / EXP 2)
- 最新: PENGUIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 190件 (Win 48 / Loss 64 / Flat 78) / skip 105件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +3.48%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-08T04:37:29.994590+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=79592.4
- Funnel: target 771 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +36.80% | $2,521,204.46 |
| LAB/USDT:USDT | +21.91% | $212,929,851.55 |
| DYDX/USDT:USDT | +21.65% | $12,691,793.19 |
| NOT/USDT:USDT | +19.55% | $10,980,292.31 |
| TST/USDT:USDT | +19.42% | $6,370,057.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PLAY/USDT:USDT | below_1h_threshold | +4.92% | +4.85% |
| LUNC/USDT:USDT | below_1h_threshold | +4.22% | +4.16% |
| DYDX/USDT:USDT | below_1h_threshold | +3.68% | +3.62% |
| AGT/USDT:USDT | below_1h_threshold | +3.34% | +3.27% |
| TST/USDT:USDT | below_1h_threshold | +2.67% | +2.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

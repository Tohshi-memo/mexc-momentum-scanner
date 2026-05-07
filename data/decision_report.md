# Decision Report

- generated_at: 2026-05-07T07:48:02.724951+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3591**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3591, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.02% | **+0.76%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.75% | **+0.71%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_BB3S | 7/20 | 35.0% | +1.64% | **+0.57%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +3.17% | **+1.58%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.76% | **+1.52%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +2.56% | **+1.28%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +3.86% | **+0.96%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.53% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$106.18** / 初期 $100.00 (+6.18%)
- 確定: 85件 (Win 30 / Loss 35 / Flat 20) / skip 67件
- 成長率目線: 平均log +0.000705 / 幾何平均 +0.071% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.18

## 4. Latest Market Context

- 更新: 2026-05-07T07:47:58.893371+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=81553.0
- Funnel: target 771 → liquid 190 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.8 >= 65=1, 4h RSI 82.9 >= 65=1, 4h RSI 78.8 >= 65=1, 4h RSI 72.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +210.22% | $1,943,376.25 |
| PENGUIN/USDT:USDT | +91.77% | $1,679,634.01 |
| B3/USDT:USDT | +73.28% | $10,041,207.85 |
| D/USDT:USDT | +70.79% | $1,028,599.28 |
| DOGS/USDT:USDT | +68.98% | $13,065,129.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDO/USDT:USDT | below_1h_threshold | +2.56% | +2.37% |
| FET/USDT:USDT | below_1h_threshold | +1.85% | +1.66% |
| XPL/USDT:USDT | below_1h_threshold | +1.79% | +1.60% |
| NIL/USDT:USDT | below_1h_threshold | +1.67% | +1.48% |
| FLOKI/USDT:USDT | below_1h_threshold | +1.64% | +1.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

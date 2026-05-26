# Decision Report

- generated_at: 2026-05-26T02:59:44.151438+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4883**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.28% / filled 20/20。**
- 全期間 MARKET基準: n=4883, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+2.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.28% | **+2.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.81% | **+2.81%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.54% | **+2.29%** |
| MARKET | 20/20 | 100.0% | +2.28% | **+2.28%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.71% | **+0.42%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.40% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$97.64** / 初期 $100.00 (-2.36%)
- 確定トレード: 64件 (TP 18 / SL 43 / EXP 3)
- 最新: ESPORTS/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.64
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$127.31** / 初期 $100.00 (+27.31%)
- 確定: 673件 (Win 169 / Loss 214 / Flat 290) / skip 771件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IN/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $127.31

## 4. Latest Market Context

- 更新: 2026-05-26T02:59:41.860205+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=76591.1
- Funnel: target 768 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| POND/USDT:USDT | +95.00% | $2,052,227.60 |
| GRASS/USDT:USDT | +12.53% | $8,611,139.94 |
| WLD/USDT:USDT | +8.46% | $52,357,641.37 |
| AKT/USDT:USDT | +4.93% | $1,455,361.71 |
| TIA/USDT:USDT | +3.01% | $22,116,304.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +2.97% | +3.13% |
| H/USDT:USDT | below_1h_threshold | +2.89% | +3.06% |
| XAN/USDT:USDT | below_1h_threshold | +2.52% | +2.68% |
| AKT/USDT:USDT | below_1h_threshold | +1.55% | +1.71% |
| NEAR/USDT:USDT | below_1h_threshold | +1.49% | +1.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

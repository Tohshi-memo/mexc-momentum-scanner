# Decision Report

- generated_at: 2026-05-29T17:42:55.623780+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5063**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=5063, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/14 | 57.1% | +2.97% | **+1.70%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.90% | **+0.81%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.96% | **+1.33%** |
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +2.00% | **+0.67%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +2.42% | **+0.48%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$98.60** / 初期 $100.00 (-1.40%)
- 確定トレード: 74件 (TP 22 / SL 49 / EXP 3)
- 最新: LIT/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.60
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.68** / 初期 $100.00 (+25.68%)
- 確定: 740件 (Win 175 / Loss 226 / Flat 339) / skip 884件
- 成長率目線: 平均log +0.000309 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CTR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $125.68

## 4. Latest Market Context

- 更新: 2026-05-29T17:42:48.131608+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=74244.8
- Funnel: target 774 → liquid 152 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.8 >= 65=1, 4h RSI 67.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +20.66% | $6,929,254.22 |
| GUA/USDT:USDT | +12.55% | $6,320,557.67 |
| GRASS/USDT:USDT | +11.88% | $2,354,441.11 |
| US/USDT:USDT | +10.24% | $1,066,917.28 |
| FET/USDT:USDT | +5.52% | $26,257,699.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QNTSTOCK/USDT:USDT | below_1h_threshold | +3.27% | +2.96% |
| EIGEN/USDT:USDT | below_1h_threshold | +3.19% | +2.88% |
| TIA/USDT:USDT | below_1h_threshold | +2.98% | +2.68% |
| WLD/USDT:USDT | below_1h_threshold | +2.38% | +2.08% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.05% | +1.75% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

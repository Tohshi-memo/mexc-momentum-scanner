# Decision Report

- generated_at: 2026-05-10T21:33:18.010665+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3991**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.36% / filled 20/20。**
- 全期間 MARKET基準: n=3991, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +2.79% | **+1.25%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.39% | **+0.37%** |
| ASK | 20/20 | 100.0% | +0.37% | **+0.37%** |
| MARKET | 20/20 | 100.0% | +0.36% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 16/20 | 80.0% | +2.27% | **+1.82%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.27% | **+1.21%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.30% | **+0.71%** |
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +0.81% | **+0.71%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.66% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$109.34** / 初期 $100.00 (+9.34%)
- 確定: 201件 (Win 50 / Loss 67 / Flat 84) / skip 351件
- 成長率目線: 平均log +0.000444 / 幾何平均 +0.044% per trade / maxDD +4.09%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $109.34

## 4. Latest Market Context

- 更新: 2026-05-10T21:33:14.323500+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=80872.4
- Funnel: target 769 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.7 >= 65=1, 4h RSI 79.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +38.63% | $3,443,683.86 |
| ALCH/USDT:USDT | +20.53% | $3,153,922.39 |
| B/USDT:USDT | +15.00% | $2,323,915.28 |
| TROLLSOL/USDT:USDT | +13.41% | $4,424,014.91 |
| SUI/USDT:USDT | +9.79% | $719,624,473.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FARTCOIN/USDT:USDT | below_1h_threshold | +2.63% | +2.41% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.29% | +2.07% |
| OG/USDT:USDT | below_1h_threshold | +2.23% | +2.01% |
| OPG/USDT:USDT | below_1h_threshold | +1.84% | +1.61% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.83% | +1.61% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

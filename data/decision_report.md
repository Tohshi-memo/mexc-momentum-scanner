# Decision Report

- generated_at: 2026-05-29T04:34:40.593183+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5004**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.15% / filled 20/20。**
- 全期間 MARKET基準: n=5004, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+2.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.15% | **+2.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.18% | **+2.18%** |
| MARKET | 20/20 | 100.0% | +2.15% | **+2.15%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.08% | **+1.77%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.36% | **+0.95%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.80% | **+0.52%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +1.27% | **+0.70%** |
| LIMIT_FIB1618_LONG | 7/20 | 35.0% | +1.46% | **+0.51%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | +0.73% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.23** / 初期 $100.00 (+28.23%)
- 確定: 729件 (Win 175 / Loss 222 / Flat 332) / skip 836件
- 成長率目線: 平均log +0.000341 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.23

## 4. Latest Market Context

- 更新: 2026-05-29T04:34:36.089046+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=73361.5
- Funnel: target 777 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +71.00% | $32,387,958.47 |
| CTR/USDT:USDT | +39.72% | $1,061,309.69 |
| DELLSTOCK/USDT:USDT | +36.34% | $7,735,488.69 |
| CLO/USDT:USDT | +21.00% | $1,463,514.25 |
| AR/USDT:USDT | +13.66% | $1,789,117.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.98% | +1.86% |
| CTR/USDT:USDT | below_1h_threshold | +1.93% | +1.80% |
| INJ/USDT:USDT | below_1h_threshold | +1.23% | +1.11% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.23% | +1.10% |
| GUA/USDT:USDT | below_1h_threshold | +1.17% | +1.05% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

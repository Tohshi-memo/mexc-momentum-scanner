# Decision Report

- generated_at: 2026-06-01T04:42:16.261987+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5272**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.33% / filled 20/20。**
- 全期間 MARKET基準: n=5272, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+2.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.33% | **+2.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.59% | **+2.59%** |
| MARKET | 20/20 | 100.0% | +2.33% | **+2.33%** |
| LIMIT_2PCT | 14/20 | 70.0% | +2.16% | **+1.51%** |
| LIMIT_ATR | 14/20 | 70.0% | +2.16% | **+1.51%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.36% | **+1.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +3.10% | **+1.55%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.19% | **+0.33%** |
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +0.25% | **+0.21%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +0.23% | **+0.14%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.25% | **+0.07%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 939件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T04:42:13.107220+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=73450.0
- Funnel: target 777 → liquid 133 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 70.3 >= 65=1, 4h RSI 80.8 >= 65=1, 4h RSI 86.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +164.42% | $28,967,899.01 |
| H/USDT:USDT | +66.40% | $22,202,018.47 |
| FHE/USDT:USDT | +34.10% | $1,176,079.63 |
| STG/USDT:USDT | +31.04% | $23,025,815.84 |
| WLD/USDT:USDT | +22.88% | $66,282,802.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +1.87% | +2.25% |
| CTR/USDT:USDT | below_1h_threshold | +1.72% | +2.10% |
| OFC/USDT:USDT | below_1h_threshold | +1.54% | +1.92% |
| HOME/USDT:USDT | below_1h_threshold | +1.49% | +1.87% |
| WLD/USDT:USDT | below_1h_threshold | +1.07% | +1.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

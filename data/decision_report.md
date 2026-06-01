# Decision Report

- generated_at: 2026-06-01T04:52:29.784990+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5274**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.55% / filled 20/20。**
- 全期間 MARKET基準: n=5274, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+2.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.55% | **+2.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +2.87% | **+2.87%** |
| MARKET | 20/20 | 100.0% | +2.55% | **+2.55%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.55% | **+1.91%** |
| LIMIT_ATR | 13/20 | 65.0% | +2.11% | **+1.37%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.70% | **+1.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 13/20 | 65.0% | +0.82% | **+0.54%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.19% | **+0.33%** |
| LIMIT_9PCT_LONG | 7/20 | 35.0% | +0.37% | **+0.13%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_6PCT_LONG | 13/20 | 65.0% | -0.14% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 941件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T04:52:27.011165+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=73468.5
- Funnel: target 777 → liquid 133 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +172.88% | $29,428,507.25 |
| H/USDT:USDT | +69.03% | $22,466,240.47 |
| STG/USDT:USDT | +27.86% | $23,124,669.71 |
| FHE/USDT:USDT | +26.79% | $1,206,361.30 |
| HOME/USDT:USDT | +21.17% | $3,993,759.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +3.79% | +4.15% |
| CTR/USDT:USDT | below_1h_threshold | +3.19% | +3.55% |
| PLAY/USDT:USDT | below_1h_threshold | +3.16% | +3.51% |
| BEAT/USDT:USDT | below_1h_threshold | +2.94% | +3.29% |
| FHE/USDT:USDT | below_1h_threshold | +1.75% | +2.11% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

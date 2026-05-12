# Decision Report

- generated_at: 2026-05-12T00:38:00.619864+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4080**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4080, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.84% | **+0.71%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.82% | **+0.61%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.34% | **+0.31%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.30% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| ASK_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 423件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-12T00:37:57.091834+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.24% price=81505.1
- Funnel: target 758 → liquid 189 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.0 >= 65=1, 4h RSI 85.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PENGUIN/USDT:USDT | +28.36% | $3,167,034.06 |
| GIGA/USDT:USDT | +27.18% | $1,077,756.30 |
| USELESS/USDT:USDT | +16.46% | $3,740,851.33 |
| SKYAI/USDT:USDT | +15.25% | $37,227,053.48 |
| H/USDT:USDT | +15.02% | $14,334,270.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +4.56% | +4.80% |
| DOGS/USDT:USDT | below_1h_threshold | +4.21% | +4.45% |
| H/USDT:USDT | below_1h_threshold | +3.35% | +3.59% |
| TRUTH/USDT:USDT | below_1h_threshold | +2.85% | +3.09% |
| NAORIS/USDT:USDT | below_1h_threshold | +2.19% | +2.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

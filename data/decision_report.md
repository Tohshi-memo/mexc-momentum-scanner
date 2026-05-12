# Decision Report

- generated_at: 2026-05-12T01:13:02.189677+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4081**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=4081, expectancy=-0.12%
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
| LIMIT_ATR | 15/20 | 75.0% | +0.35% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.60% | **+0.80%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| ASK_LONG | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 424件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-12T01:12:56.483475+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.18% price=81361.2
- Funnel: target 758 → liquid 185 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +26.60% | $1,126,180.46 |
| PENGUIN/USDT:USDT | +18.28% | $3,194,094.23 |
| USELESS/USDT:USDT | +16.41% | $3,797,147.05 |
| SAGA/USDT:USDT | +15.30% | $6,824,732.75 |
| SKYAI/USDT:USDT | +14.31% | $37,349,875.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MONAD/USDT:USDT | below_1h_threshold | +2.77% | +2.95% |
| SAGA/USDT:USDT | below_1h_threshold | +2.66% | +2.84% |
| SILVER/USDT:USDT | below_1h_threshold | +0.80% | +0.98% |
| OG/USDT:USDT | below_1h_threshold | +0.55% | +0.73% |
| VVV/USDT:USDT | below_1h_threshold | +0.48% | +0.66% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

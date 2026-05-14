# Decision Report

- generated_at: 2026-05-14T10:58:01.424511+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4283**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=4283, expectancy=-0.11%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/13 | 38.5% | +4.85% | **+1.87%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.30% | **+1.17%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.27% | **+1.02%** |
| ASK | 20/20 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +3.24% | **+2.70%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.92% | **+0.77%** |
| MARKET_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.32% | **+0.53%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.57% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$96.73** / 初期 $100.00 (-3.27%)
- 確定トレード: 42件 (TP 10 / SL 29 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.73
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.18** / 初期 $100.00 (+19.18%)
- 確定: 344件 (Win 94 / Loss 125 / Flat 125) / skip 500件
- 成長率目線: 平均log +0.000510 / 幾何平均 +0.051% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account +0.00% 残高後 $119.18

## 4. Latest Market Context

- 更新: 2026-05-14T10:57:55.742645+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=79557.3
- Funnel: target 763 → liquid 163 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIGENSYN/USDT:USDT | +56.79% | $4,588,784.57 |
| TROLLSOL/USDT:USDT | +29.39% | $2,222,774.00 |
| UP/USDT:USDT | +28.55% | $1,945,291.68 |
| CSCOSTOCK/USDT:USDT | +19.50% | $5,452,081.92 |
| PIEVERSE/USDT:USDT | +16.63% | $2,518,001.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UP/USDT:USDT | below_1h_threshold | +3.98% | +4.03% |
| GRT/USDT:USDT | below_1h_threshold | +3.41% | +3.46% |
| NIL/USDT:USDT | below_1h_threshold | +2.54% | +2.59% |
| UB/USDT:USDT | below_1h_threshold | +2.27% | +2.31% |
| SAGA/USDT:USDT | below_1h_threshold | +2.15% | +2.20% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

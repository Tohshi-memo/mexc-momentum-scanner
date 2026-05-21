# Decision Report

- generated_at: 2026-05-21T10:58:55.619200+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4618**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.55% / filled 20/20。**
- 全期間 MARKET基準: n=4618, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+1.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.55% | **+1.55%** |
| ASK | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |
| LIMIT_BB3S | 7/19 | 36.8% | +2.03% | **+0.75%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.94% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.01% | **+0.80%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.26% | **+0.57%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.08% | **+0.54%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.98% | **+0.49%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.21% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 58件 (TP 15 / SL 40 / EXP 3)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 633件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_6PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T10:58:52.859010+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.51% price=77202.4
- Funnel: target 766 → liquid 141 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1, 4h RSI 82.3 >= 65=1, 4h RSI 68.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROVE/USDT:USDT | +50.67% | $3,902,387.96 |
| EDEN/USDT:USDT | +38.53% | $30,801,452.96 |
| MITO/USDT:USDT | +37.08% | $1,010,524.23 |
| ROAM/USDT:USDT | +36.06% | $2,227,805.76 |
| USELESS/USDT:USDT | +18.22% | $2,000,644.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USOIL/USDT:USDT | below_1h_threshold | +3.45% | +3.96% |
| PROVE/USDT:USDT | below_1h_threshold | +3.24% | +3.74% |
| UKOIL/USDT:USDT | below_1h_threshold | +2.82% | +3.33% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.18% | +2.69% |
| EDEN/USDT:USDT | below_1h_threshold | +1.86% | +2.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

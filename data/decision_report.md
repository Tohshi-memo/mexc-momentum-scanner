# Decision Report

- generated_at: 2026-06-12T19:30:28.274309+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6540**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.62% / filled 20/20。**
- 全期間 MARKET基準: n=6540, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+3.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.62% | **+3.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.62% | **+3.62%** |
| ASK | 20/20 | 100.0% | +2.75% | **+2.75%** |
| LIMIT_2PCT | 13/20 | 65.0% | +3.25% | **+2.11%** |
| LIMIT_1PCT | 15/20 | 75.0% | +2.47% | **+1.85%** |
| LIMIT_ATR | 9/20 | 45.0% | +3.68% | **+1.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.71% | **+0.56%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_8PCT_LONG | 12/20 | 60.0% | -0.33% | **-0.20%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -1.56% | **-0.86%** |

## 2. $100 Live Portfolio

- 残高: **$96.11** / 初期 $100.00 (-3.89%)
- 確定トレード: 24件 (TP 5 / SL 18 / EXP 1)
- 最新: H/USDT:USDT TP_HIT PnL +8.00% 残高後 $96.11
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$164.64** / 初期 $100.00 (+64.64%)
- 確定: 1413件 (Win 388 / Loss 461 / Flat 564) / skip 1688件
- 成長率目線: 平均log +0.000353 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $164.64

## 4. Latest Market Context

- 更新: 2026-06-12T19:30:24.954973+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63700.7
- Funnel: target 774 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +22.16% | $9,564,987.48 |
| ESPORTS/USDT:USDT | +15.28% | $66,331,325.32 |
| AIN/USDT:USDT | +8.19% | $1,789,890.26 |
| HOME/USDT:USDT | +5.83% | $3,025,264.48 |
| H/USDT:USDT | +5.57% | $29,704,230.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIN/USDT:USDT | below_1h_threshold | +2.27% | +2.21% |
| COAI/USDT:USDT | below_1h_threshold | +1.97% | +1.91% |
| PLSTOCK/USDT:USDT | below_1h_threshold | +1.67% | +1.61% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +1.38% | +1.32% |
| RAVE/USDT:USDT | below_1h_threshold | +1.28% | +1.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

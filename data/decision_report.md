# Decision Report

- generated_at: 2026-05-12T20:28:16.454334+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4157**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4157, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.23% | **-0.06%** |
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +3.36% | **+2.02%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.78% | **+1.33%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.00% | **+1.30%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.95% | **+0.85%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.92% | **+0.64%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.64** / 初期 $100.00 (+19.64%)
- 確定: 293件 (Win 84 / Loss 101 / Flat 108) / skip 425件
- 成長率目線: 平均log +0.000612 / 幾何平均 +0.061% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VIC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $119.64

## 4. Latest Market Context

- 更新: 2026-05-12T20:28:13.234998+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=80745.7
- Funnel: target 758 → liquid 191 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VIC/USDT:USDT | +15.43% | $5,656,081.41 |
| LAB/USDT:USDT | +12.16% | $134,977,683.97 |
| SAGA/USDT:USDT | +11.03% | $51,236,816.05 |
| EDU/USDT:USDT | +9.91% | $3,966,888.01 |
| DYM/USDT:USDT | +9.62% | $2,032,659.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_1h_threshold | +3.94% | +4.00% |
| BILL/USDT:USDT | below_1h_threshold | +2.58% | +2.64% |
| DYM/USDT:USDT | below_1h_threshold | +2.52% | +2.59% |
| GRT/USDT:USDT | below_1h_threshold | +1.75% | +1.81% |
| ATOM/USDT:USDT | below_1h_threshold | +1.35% | +1.42% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

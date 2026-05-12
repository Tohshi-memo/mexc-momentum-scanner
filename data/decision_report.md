# Decision Report

- generated_at: 2026-05-12T20:14:11.880156+00:00
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

- 更新: 2026-05-12T20:14:08.694690+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=80734.8
- Funnel: target 758 → liquid 190 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VIC/USDT:USDT | +17.65% | $5,572,175.22 |
| LAB/USDT:USDT | +10.87% | $133,391,544.13 |
| SATO/USDT:USDT | +9.33% | $1,090,283.34 |
| PEAQ/USDT:USDT | +9.22% | $1,982,619.79 |
| SAGA/USDT:USDT | +8.69% | $49,819,180.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +3.83% | +3.91% |
| GIGA/USDT:USDT | below_1h_threshold | +1.38% | +1.46% |
| VIC/USDT:USDT | below_1h_threshold | +1.19% | +1.26% |
| KITE/USDT:USDT | below_1h_threshold | +0.85% | +0.93% |
| DYM/USDT:USDT | below_1h_threshold | +0.61% | +0.68% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

# Decision Report

- generated_at: 2026-05-09T04:42:38.097509+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3852**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3852, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-1.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.46% | **-1.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +0.53% | **+0.42%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.46% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.61% | **+1.62%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.09% | **+1.25%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.51% | **+1.25%** |
| MARKET_LONG | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +4.37% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 220件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T04:42:34.922589+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=80392.9
- Funnel: target 767 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYM/USDT:USDT | +33.03% | $1,082,048.90 |
| SATO/USDT:USDT | +32.59% | $4,177,389.49 |
| VVV/USDT:USDT | +21.11% | $9,847,203.19 |
| CORE/USDT:USDT | +19.58% | $2,098,836.64 |
| COLLECT/USDT:USDT | +17.59% | $7,732,496.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| REZ/USDT:USDT | below_1h_threshold | +4.46% | +4.39% |
| SATO/USDT:USDT | below_1h_threshold | +4.09% | +4.03% |
| SIREN/USDT:USDT | below_1h_threshold | +3.54% | +3.48% |
| ASTER/USDT:USDT | below_1h_threshold | +2.88% | +2.81% |
| GALA/USDT:USDT | below_1h_threshold | +2.57% | +2.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

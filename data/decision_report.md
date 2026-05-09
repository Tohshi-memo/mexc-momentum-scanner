# Decision Report

- generated_at: 2026-05-09T04:17:31.183633+00:00
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

- 更新: 2026-05-09T04:17:27.960450+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=80461.5
- Funnel: target 767 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +31.44% | $4,118,609.02 |
| CORE/USDT:USDT | +21.75% | $2,030,712.19 |
| COLLECT/USDT:USDT | +20.87% | $7,511,038.49 |
| VVV/USDT:USDT | +19.94% | $9,338,588.63 |
| ICP/USDT:USDT | +18.66% | $231,598,756.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GALA/USDT:USDT | below_1h_threshold | +3.42% | +3.27% |
| SATO/USDT:USDT | below_1h_threshold | +2.93% | +2.78% |
| DEEP/USDT:USDT | below_1h_threshold | +2.15% | +2.00% |
| TIA/USDT:USDT | below_1h_threshold | +1.81% | +1.66% |
| ENA/USDT:USDT | below_1h_threshold | +1.75% | +1.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

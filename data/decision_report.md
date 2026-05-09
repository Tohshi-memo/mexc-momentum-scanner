# Decision Report

- generated_at: 2026-05-09T02:12:36.741457+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3837**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3837, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-2.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.24% | **-2.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.70% | **+0.42%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_BB3S | 5/14 | 35.7% | +0.27% | **+0.10%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.02% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +2.61% | **+1.57%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +3.83% | **+1.34%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.04% | **+1.22%** |
| ASK_LONG | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +3.25% | **+1.14%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 205件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_BB3S` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T02:12:33.707068+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.15% price=80399.0
- Funnel: target 767 → liquid 174 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +25.55% | $6,607,719.95 |
| COLLECT/USDT:USDT | +25.11% | $6,807,046.28 |
| ICP/USDT:USDT | +23.08% | $232,575,091.53 |
| DEEP/USDT:USDT | +22.78% | $1,231,465.74 |
| CORE/USDT:USDT | +16.12% | $1,822,561.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +3.50% | +3.35% |
| IO/USDT:USDT | below_1h_threshold | +2.83% | +2.68% |
| COLLECT/USDT:USDT | below_1h_threshold | +2.58% | +2.44% |
| DYDX/USDT:USDT | below_1h_threshold | +1.79% | +1.64% |
| DEEP/USDT:USDT | below_1h_threshold | +1.58% | +1.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

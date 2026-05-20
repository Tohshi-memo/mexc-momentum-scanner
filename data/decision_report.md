# Decision Report

- generated_at: 2026-05-20T05:08:37.513390+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4524**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4524, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +2.97% | **+1.04%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.97% | **+0.49%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.39% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.39% | **+1.44%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.28% | **+0.83%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.50% | **+0.75%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.64% | **+0.74%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.53% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$124.41** / 初期 $100.00 (+24.41%)
- 確定: 486件 (Win 128 / Loss 167 / Flat 191) / skip 599件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $124.41

## 4. Latest Market Context

- 更新: 2026-05-20T05:08:35.481959+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=76867.5
- Funnel: target 764 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +37.26% | $19,555,524.87 |
| PROMPT/USDT:USDT | +32.15% | $12,673,673.13 |
| LIT/USDT:USDT | +25.42% | $7,114,477.98 |
| FIDA/USDT:USDT | +23.38% | $1,400,869.42 |
| ZEST/USDT:USDT | +14.78% | $1,914,775.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PROMPT/USDT:USDT | below_1h_threshold | +1.60% | +1.45% |
| ONDO/USDT:USDT | below_1h_threshold | +0.77% | +0.61% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +0.73% | +0.58% |
| ALGO/USDT:USDT | below_1h_threshold | +0.52% | +0.36% |
| XAN/USDT:USDT | below_1h_threshold | +0.49% | +0.33% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

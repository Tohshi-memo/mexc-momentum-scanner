# Decision Report

- generated_at: 2026-05-20T05:43:40.330214+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4528**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4528, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +3.30% | **+0.99%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.79% | **+0.44%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.42% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.79% | **+0.44%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.45% | **+0.29%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.30% | **+0.15%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +0.22% | **+0.14%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.17** / 初期 $100.00 (+23.17%)
- 確定: 490件 (Win 128 / Loss 169 / Flat 193) / skip 599件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $123.17

## 4. Latest Market Context

- 更新: 2026-05-20T05:43:35.491261+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.58% price=77196.9
- Funnel: target 764 → liquid 135 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROMPT/USDT:USDT | +32.47% | $12,373,208.29 |
| FIDA/USDT:USDT | +28.80% | $1,551,672.84 |
| SKYAI/USDT:USDT | +24.90% | $6,231,138.39 |
| EDEN/USDT:USDT | +24.74% | $20,107,193.80 |
| LIT/USDT:USDT | +22.81% | $7,342,357.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEST/USDT:USDT | below_1h_threshold | +4.93% | +4.35% |
| FIDA/USDT:USDT | below_1h_threshold | +4.24% | +3.66% |
| ONDO/USDT:USDT | below_1h_threshold | +2.82% | +2.23% |
| VVV/USDT:USDT | below_1h_threshold | +2.56% | +1.98% |
| XAN/USDT:USDT | below_1h_threshold | +2.15% | +1.57% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

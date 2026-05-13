# Decision Report

- generated_at: 2026-05-13T14:28:05.147625+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4228**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4228, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.48% | **-0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | -0.11% | **-0.09%** |
| LIMIT_5PCT | 5/20 | 25.0% | -1.03% | **-0.26%** |
| ASK | 20/20 | 100.0% | -0.29% | **-0.29%** |
| LIMIT_BB3S | 10/18 | 55.6% | -0.52% | **-0.29%** |
| LIMIT_FIB1618 | 4/20 | 20.0% | -1.99% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.31% | **+1.31%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.74% | **+1.13%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.72% | **+0.95%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.07% | **+0.70%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +3.46% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.78** / 初期 $100.00 (+19.78%)
- 確定: 341件 (Win 94 / Loss 124 / Flat 123) / skip 448件
- 成長率目線: 平均log +0.000529 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.01% 残高後 $119.78

## 4. Latest Market Context

- 更新: 2026-05-13T14:27:59.506584+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.29% price=79847.4
- Funnel: target 765 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +43.16% | $138,598,390.02 |
| COS/USDT:USDT | +34.36% | $1,874,641.08 |
| TRUTH/USDT:USDT | +31.09% | $3,922,565.43 |
| JCT/USDT:USDT | +28.04% | $1,128,278.79 |
| UB/USDT:USDT | +26.40% | $10,924,317.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FF/USDT:USDT | below_1h_threshold | +3.72% | +3.43% |
| UP/USDT:USDT | below_1h_threshold | +3.21% | +2.92% |
| TRUTH/USDT:USDT | below_1h_threshold | +3.19% | +2.90% |
| LAB/USDT:USDT | below_1h_threshold | +2.72% | +2.43% |
| VELO/USDT:USDT | below_1h_threshold | +2.35% | +2.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

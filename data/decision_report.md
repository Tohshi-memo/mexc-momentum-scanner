# Decision Report

- generated_at: 2026-05-20T09:09:16.700469+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4532**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4532, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| ASK | 20/20 | 100.0% | -0.07% | **-0.07%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |
| ASK_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.29% | **+0.20%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.14% | **+0.04%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.78** / 初期 $100.00 (+23.78%)
- 確定: 494件 (Win 129 / Loss 170 / Flat 195) / skip 599件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $123.78

## 4. Latest Market Context

- 更新: 2026-05-20T09:09:11.152354+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77406.9
- Funnel: target 762 → liquid 132 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +99.76% | $1,133,668.74 |
| FIDA/USDT:USDT | +30.15% | $2,544,043.21 |
| PROMPT/USDT:USDT | +28.36% | $12,434,632.90 |
| LIT/USDT:USDT | +26.15% | $8,194,162.22 |
| PLAY/USDT:USDT | +22.46% | $10,101,773.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +3.23% | +3.26% |
| LIT/USDT:USDT | below_1h_threshold | +1.37% | +1.40% |
| FIGHT/USDT:USDT | below_1h_threshold | +0.94% | +0.97% |
| UP/USDT:USDT | below_1h_threshold | +0.83% | +0.86% |
| CHIP/USDT:USDT | below_1h_threshold | +0.62% | +0.65% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

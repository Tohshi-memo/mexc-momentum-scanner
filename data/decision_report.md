# Decision Report

- generated_at: 2026-05-20T09:24:17.012094+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4533**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4533, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.63% | **-0.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 13/20 | 65.0% | +0.32% | **+0.21%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.46% | **-0.16%** |
| LIMIT_6PCT | 4/20 | 20.0% | -1.06% | **-0.21%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.73% | **-0.26%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.61% | **-0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.51% | **+1.51%** |
| ASK_LONG | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.15% | **+0.80%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +0.53% | **+0.24%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +0.38% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.02** / 初期 $100.00 (+25.02%)
- 確定: 495件 (Win 130 / Loss 170 / Flat 195) / skip 599件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $125.02

## 4. Latest Market Context

- 更新: 2026-05-20T09:24:09.945969+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77409.3
- Funnel: target 762 → liquid 132 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +103.37% | $1,326,989.59 |
| FIDA/USDT:USDT | +34.57% | $2,637,475.24 |
| PROMPT/USDT:USDT | +28.99% | $12,445,219.28 |
| LIT/USDT:USDT | +25.88% | $8,426,391.46 |
| PLAY/USDT:USDT | +21.80% | $10,193,887.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FIGHT/USDT:USDT | below_1h_threshold | +2.01% | +2.04% |
| DASH/USDT:USDT | below_1h_threshold | +1.63% | +1.66% |
| HOME/USDT:USDT | below_1h_threshold | +1.60% | +1.63% |
| FIDA/USDT:USDT | below_1h_threshold | +1.59% | +1.62% |
| ZEN/USDT:USDT | below_1h_threshold | +1.21% | +1.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

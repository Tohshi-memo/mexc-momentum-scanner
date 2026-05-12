# Decision Report

- generated_at: 2026-05-12T05:37:46.015012+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4096**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4096, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.18% | **-1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.04% | **+0.61%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.22% | **-0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.79% | **+2.51%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.55% | **+2.31%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +2.14% | **+1.72%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.64% | **+1.32%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.42% | **+0.97%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$111.47** / 初期 $100.00 (+11.47%)
- 確定: 232件 (Win 61 / Loss 81 / Flat 90) / skip 425件
- 成長率目線: 平均log +0.000468 / 幾何平均 +0.047% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $111.47

## 4. Latest Market Context

- 更新: 2026-05-12T05:37:42.757250+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=81194.3
- Funnel: target 762 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +51.46% | $2,740,657.65 |
| SKYAI/USDT:USDT | +38.03% | $42,517,292.19 |
| SAGA/USDT:USDT | +30.85% | $8,351,798.74 |
| GUA/USDT:USDT | +28.09% | $1,635,137.12 |
| USELESS/USDT:USDT | +26.24% | $5,094,010.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +4.39% | +4.39% |
| SAHARA/USDT:USDT | below_1h_threshold | +3.36% | +3.36% |
| USELESS/USDT:USDT | below_1h_threshold | +3.01% | +3.01% |
| GUA/USDT:USDT | below_1h_threshold | +2.98% | +2.98% |
| RIF/USDT:USDT | below_1h_threshold | +2.78% | +2.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
